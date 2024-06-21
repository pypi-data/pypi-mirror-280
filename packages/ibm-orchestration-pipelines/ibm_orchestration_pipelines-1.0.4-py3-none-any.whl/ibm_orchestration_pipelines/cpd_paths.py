# IBM Confidential
# OCO Source Materials
# 5737-B37, 5737-C49, 5737-H76
# (C) Copyright IBM Corp. 2021, 2022  All Rights Reserved.
# The source code for this program is not published or
# otherwise divested of its trade secrets, irrespective of
# what has been deposited with the U.S. Copyright Office.

import itertools
import re
from enum import Enum
from typing import Optional, Set, Type, TypeVar, Mapping, Sequence, Union, \
    ClassVar, Tuple, Generic, overload

import attr
import urllib.parse


# according to: https://www.ietf.org/rfc/rfc1738.txt
# > Thus, only alphanumerics, the special characters "$-_.+!*'(),", and
# >    reserved characters used for their reserved purposes may be used
# >    unencoded within a URL.
# Additionally, tilde (~) is allowed due to it being used for the default COS bucket.
from ibm_orchestration_pipelines.client_errors import NoSuchOverloadError

_segment_regex: re.Pattern = re.compile(r'(([a-zA-Z0-9$\-_.+!*\')(~])|(%[0-9a-fA-F]{2}))*')
_escape_regex: re.Pattern = re.compile(r'%[0-9a-fA-F]{2}')

Self = TypeVar('Self')

def _validate_segment(segment: str) -> None:
    if _segment_regex.fullmatch(segment):
        return

    forbidden_chars = set()
    i = -1
    while i != len(segment):
        ch = segment[i]
        i += 1
        if ch == '%':
            # maybe take the next two?
            if i+2 < len(segment) and _escape_regex.fullmatch(segment[i:i+2]):
                # it's an escape
                i += 2
                continue

        if ch in forbidden_chars:
            continue
        if not _segment_regex.fullmatch(ch):
            forbidden_chars.add(ch)

    forbidden_chars_str = ', '.join([f"'{ch}'" for ch in forbidden_chars])
    raise TypeError(f"segment '{segment}' contains forbidden characters: {forbidden_chars_str}")


@attr.attrs(auto_attribs=True, frozen=True, kw_only=True)
class Query:
    """Represents a query inside of CPD Path."""
    name: str = None
    asset_type: str = None
    deployment_type: str = None
    revision: str = None
    tags: Sequence[str] = None

    query_labels: ClassVar[Mapping[str, str]] = {
        "name": "name",
        "asset_type": "asset_type",
        "deployment_type": "deployment_type",
        "rev": "revision",
        "tag": "tags",
        "tags": "tags",
    }

    def __str__(self) -> str:
        def quote(v: Union[str, Sequence[str]]) -> str:
            if isinstance(v, str):
                return urllib.parse.quote(v)
            else:
                return ",".join([urllib.parse.quote(el) for el in v])

        name_to_label = {v: k for k,v in self.query_labels.items()}

        fields = attr.asdict(self)
        fields_seq = {
            quote(name_to_label[k]): quote(v)
            for k, v in fields.items()
            if v is not None
        }
        return "&".join([f'{k}={v}' for k,v in fields_seq.items()])

    @classmethod
    def from_path(cls: Type[Self], path: Union[str, urllib.parse.ParseResult]) -> Self:
        if isinstance(path, str):
            path = urllib.parse.urlparse(path)
        params = urllib.parse.parse_qs(path.query)
        return cls.from_mapping(params)

    @classmethod
    def from_mapping(
        cls: Type[Self],
        params: Mapping[str, Union[str, Sequence[str]]],
    ) -> Self:
        fields = attr.fields_dict(cls)
        values = {}
        extra_params = {}

        for param_name, param_value in params.items():
            if param_name not in cls.query_labels:
                # gather extra parameters to throw one error
                extra_params[param_name] = param_value
                continue
            param_name = cls.query_labels[param_name]
            # is it the right type?
            if fields[param_name].type is str:
                # if passing 1-element list, it's fine
                if isinstance(param_value, list):
                    if len(param_value) != 1:
                        raise TypeError(f"Query field '{param_name}' expects a string, but got list: {param_value}")
                    param_value = param_value[0]
            else: # Sequence[str]
                if isinstance(param_value, str):
                    # wrap into a list
                    param_value = [param_value]
                # from csv
                param_value = list(itertools.chain(*[
                    el.split(",") for el in param_value
                ]))
            values[param_name] = param_value

        if len(extra_params) > 0:
            raise TypeError(f"Query got unexpected params: {extra_params}")

        # special handling of "tags":
        if 'tags' in values:
            tags = values['tags']
            tags = [tag.strip() for tag in tags]
            values['tags'] = tags

        return cls(**values)

class RichEnum(Enum):
    @classmethod
    def member_mapping(cls: Type[Self]) -> Self:
        return {
            el.value: el for el in cls
        }

    @classmethod
    def from_string(cls: Type[Self], s: str) -> Self:
        return cls.member_mapping()[s]

    @classmethod
    def is_member(cls: Type[Self], s: str) -> Self:
        return s in cls.member_mapping()

class ScopeType(RichEnum):
    PROJECTS = "projects"
    SPACES   = "spaces"
    CATALOGS = "catalogs"

class ResourceType(RichEnum):
    ASSETS      = "assets"
    DEPLOYMENTS = "deployments"

class SpecialAssetsType(RichEnum):
    JOBS                    = "jobs"
    JOB_RUNS                = "job_runs"
    NOTEBOOKS               = "notebooks"
    CONNECTIONS             = "connections"
    ENVIRONMENTS            = "environments"
    HARDWARE_SPECIFICATIONS = "hardware_specifications"
    SOFTWARE_SPECIFICATIONS = "software_Specifications"

    def to_asset_type(self) -> str:
        return {
            type(self).JOBS: "job",
            type(self).JOB_RUNS: "job_run",
            type(self).NOTEBOOKS: "notebook",
            type(self).CONNECTIONS: "connection",
            type(self).ENVIRONMENTS: "environment",
            type(self).HARDWARE_SPECIFICATIONS: "hardware_specification",
            type(self).SOFTWARE_SPECIFICATIONS: "software_Specification",
        }[self]

    @classmethod
    def from_asset_type(cls: Type[Self], asset_type: str) -> Self:
        return {
            m.to_asset_type: m for m in cls.__member__
        }[asset_type]

class SpecialSegmentsType(Enum):
    FILES = "files"
    MNTS = "mnts"

_ST = TypeVar('_ST', ScopeType, Union[ResourceType, SpecialAssetsType])

@attr.attrs(auto_attribs=True, frozen=True, kw_only=True)
class Segment(Generic[_ST]):
    type: _ST
    id: Optional[str] = None

    def __str__(self) -> str:
        result = self.type.value
        if self.id:
            result += "/" + self.id
        return result

@attr.attrs(auto_attribs=True, frozen=True, kw_only=True)
class File:
    path: str

@attr.attrs(auto_attribs=True, frozen=True, kw_only=True)
class Path:
    scope: Optional[Segment[ScopeType]]
    resource: Optional[Segment[Union[ResourceType, SpecialAssetsType]]]
    file: Optional[File]

    def __str__(self) -> str:
        result = ""
        if self.scope:
            result += "/" + str(self.scope)
        if self.resource:
            # Note: leading slash is only for absolute paths
            if result != "":
                result += "/"
            result += str(self.resource)
        if self.file:
            if result != "":
                result += "/files/"
            result += self.file.path
        return result

    @staticmethod
    def _maybe_parse_scope(
        segments: Sequence[str]
    ) -> Tuple[Optional[Segment], Sequence[str]]:
        assert len(segments) > 0

        scope: Optional[Segment] = None

        # absolute paths start from "/", so the first segment is empty
        res_idx = 0
        if segments[0] == "" and (len(segments) > 1 and segments[1] != SpecialSegmentsType.MNTS.value):
            assert len(segments) > 1
            el = segments[1]
            if ScopeType.is_member(el):
                scope = Segment(type=ScopeType.from_string(el))
            else:
                raise TypeError(f"Invalid CPD scope type: {segments[1]}")

            if len(segments) > 2:
                scope = attr.evolve(scope, id=segments[2])
                res_idx = 3
            else:
                res_idx = None

        # if no absolute path found, relative path is the whole
        remaining_segments = []
        if res_idx is not None:
            remaining_segments = segments[res_idx:]

        return scope, remaining_segments

    @staticmethod
    def _parse_resource_and_file(
        segments: Sequence[str],
        has_scope: bool,
        has_query: bool,
    ) -> Tuple[Optional[Segment], Optional[File]]:
        ns = len(segments)

        resource: Optional[Segment] = None
        file: Optional[File] = None

        # files/...
        if ns > 1 and segments[0] == SpecialSegmentsType.FILES.value:
            file = File(path="/".join(segments[1:]))
        elif ns > 1 and segments[1] == SpecialSegmentsType.MNTS.value:
            file = File(path="/".join(segments[0:]))
        # asset-123
        else:
            if ns == 1 and not has_query:
                el = segments[0]
                if has_scope:
                    # cannot: /spaces/abc/asset-123
                    if ResourceType.is_member(el) or SpecialAssetsType.is_member(el):
                        # /spaces/abc/deployments
                        # lacks query?
                        raise TypeError(f"CPD resource path to '{el}' lacks either id or query.")
                    else:
                        # /spaces/abc/asset-123
                        # lacks `assets` mid-path?
                        raise TypeError(f"CPD path is absolute but looks like relative. Maybe lacking 'assets' before id.")

                # note: this is one of the few cases in which the path will look different
                # asset-123 --> assets/asset-123
                resource = Segment(type=ResourceType.ASSETS, id=el)
            else: # ns > 1 or has_query
                el = segments[0]
                # deployments/abc, deployments?name=abc
                if ResourceType.is_member(el):
                    resource = Segment(type=ResourceType.from_string(el))
                # notebooks/abc, notebooks?name=abc
                elif SpecialAssetsType.is_member(el):
                    resource = Segment(type=SpecialAssetsType.from_string(el))
                # files/...
                elif el == SpecialSegmentsType.FILES.value:
                    file = File(path="/".join(segments[1:]))
                    # rest of the path is file path, do not consider
                    ns = 1
                else:
                    raise TypeError(f"Invalid CPD resource type: {segments[0]}")

                # deployments/abc
                if ns > 1:
                    assert resource is not None # as seen above
                    resource = attr.evolve(resource, id=segments[1])

            if ns > 2:
                # connections/_/files/~/...
                if segments[2] == SpecialSegmentsType.FILES.value:
                    if resource is None or resource.type != SpecialAssetsType.CONNECTIONS:
                        if resource is not None:
                            typ = resource.type
                            raise TypeError(f"File path only allowed for connection asset, but used on: {typ}")
                        else:
                            raise TypeError(f"File path only allowed for connection asset")
                    file = File(path="/".join(segments[3:]))
                else:
                    raise TypeError(f"Unexpected path segments: {'/'.join(segments[2:])}")
        return resource, file

    @classmethod
    def from_segments(
        cls: Type[Self],
        segments: Sequence[str],
        has_query: bool,
    ) -> Self:
        ns = len(segments)
        if ns == 0 or (ns == 1 and segments[0] == ""):
            raise TypeError("At least one path segment expected")

        scope, remaining_segments = cls._maybe_parse_scope(segments)

        # if no remaining segments, finish
        if not remaining_segments:
            return Path(
                scope=scope,
                resource=None,
                file=None,
            )

        has_scope = scope is not None
        resource, file = cls._parse_resource_and_file(
            remaining_segments,
            has_scope,
            has_query,
        )

        return Path(
            scope=scope,
            resource=resource,
            file=file,
        )


@attr.attrs(auto_attribs=True, frozen=True, kw_only=True)
class CpdPathData:
    has_prefix: bool
    ctx: Optional[str]
    path: Path
    query: Optional[Query]

    @classmethod
    def from_string(cls: Type[Self], path: str) -> Self:
        if not isinstance(path, str):
            typ = type(path).__name__
            raise TypeError(f"Path expected to be a string, but is of type {typ}")

        if path == "":
            raise TypeError("Provided path is empty")

        uri = urllib.parse.urlparse(path)

        if uri.scheme == "":
            has_prefix = False
        elif uri.scheme == "cpd":
            has_prefix = True
        else:
            raise TypeError(f"Unexpected schema: {uri.scheme}")

        ctx = uri.hostname
        if ctx == "":
            ctx = None

        query = None
        if uri.query != "":
            query = Query.from_path(uri)

        segments = uri.path.split("/")
        for segment in segments:
            _validate_segment(segment)

        has_query = query is not None
        path = Path.from_segments(segments, has_query)

        return cls(
            has_prefix=has_prefix,
            ctx=ctx,
            path=path,
            query=query,
        )

    def __str__(self) -> str:
        result = ""
        if self.has_prefix:
            result += "cpd://"
        if self.ctx:
            result += self.ctx
        result += str(self.path)
        if self.query:
            result += "?"
            result += str(self.query)
        return result

def _validate_scope_query(data: CpdPathData) -> None:
    if data.query is None:
        return
    params = {
        k for k,v in attr.asdict(data.query).items()
        if v is not None
    }
    allowed_params = {'name', 'tags'}
    not_allowed_params = params - allowed_params
    if not_allowed_params:
        s = ','.join([
            f'"{val}"' for val in not_allowed_params
        ])
        raise TypeError(f"Scope path used with not allowed query params: {s}")

@attr.attrs(auto_attribs=True, frozen=True)
class CpdPath:
    """
    Path to CPD scope or some resource within one.

    Scopes:

    * ``[cpd://[<context>]]/(projects|spaces|catalogs)/<scope-id>``
    * ``[cpd://[<context>]]/(projects|spaces|catalogs)?<query-string>]``

      * `name` - a scope name
      * `tags` - a list of resource tags (comma separated)

    Resources:

    * ``[cpd://[<context>]]/(projects|spaces|catalogs)/<scope-id>/<resource-type>/<resource-ID>``
    * ``[cpd://[<context>]]/(projects|spaces|catalogs)/<scope-id>/<resource-type>?<query-string>``

      * `name` - a resource name
      * `tags` - a list of resource tags (comma separated)
      * `rev` - a resource revision (if supported by a given resource type)
      * `asset_type` - an asset type (only for assets)
      * `datasource_type` - a datasource name (only for connection assets, eg. "bluemixcloudobjectstorage", "db2", "redshift")

    Files:

    * ``[cpd://[<context>]]/(projects|spaces|catalogs)/<scope-id>/files/<file-path>``
    * ``[cpd://[<context>]]/(projects|spaces|catalogs)/<scope-id>/connections/<connection-id>/files/<bucket-name>/<file-path>``
    """

    data: CpdPathData

    def __str__(self) -> str:
        return str(self.data)

    @classmethod
    def from_string(cls: Type[Self], path: str) -> Self:
        """
        Parse the path from some string. This is the preferred method of creating CPD-Paths.

        Note that different subclasses will be created from different kinds of paths.
        """
        # creates different kinds of CpdPath depending on path
        data = CpdPathData.from_string(path)

        if data.path.file is not None:
            if data.path.resource is not None:
                # connection file
                return CpdConnectionFile(data)
            else:
                # scope file
                return CpdScopeFile(data)
        elif data.path.resource is not None:
            # resource
            return CpdResource(data)
        elif data.path.scope is not None:
            # scope
            return CpdScope(data)
        else:
            raise TypeError(f"Uknown kind of CpdPath: {str(data)}")

    def context(self) -> Optional[str]:
        """
        Return the ``context`` part of the CPD-Path, if any.

        Example::

            path = CpdPath.from_string("cpd://dev/projects/123456789")
            assert path.context() == "dev"

            path = CpdPath.from_string("cpd:///projects/123456789")
            assert path.context() is None
        """
        return self.data.ctx

    def scope_type(self) -> Optional[str]:
        """
        Return the scope type, if any.

        Example::

            path = CpdPath.from_string("cpd://dev/projects/123456789")
            assert path.scope_type() == "projects"

            path = CpdPath.from_string("assets/3141592")
            assert path.scope_type() is None
        """
        if self.data.path.scope is None:
            return None
        return self.data.path.scope.type.value

    def scope_id(self) -> Optional[str]:
        """
        Return the scope ID, if any.

        Example::

            path = CpdPath.from_string("cpd://dev/projects/123456789")
            assert path.scope_id() == "123456789"

            path = CpdPath.from_string("cpd://dev/projects?name=foobar")
            assert path.scope_id() is None

            path = CpdPath.from_string("assets/3141592")
            assert path.scope_id() is None
        """
        if self.data.path.scope is None:
            return None
        return self.data.path.scope.id

    def query(self) -> Optional[str]:
        """
        Return the query party, if any.

        Example::

            path = CpdPath.from_string("cpd://dev/projects/123456789")
            assert path.query() is None

            path = CpdPath.from_string("cpd://dev/projects?name=foobar")
            assert path.query() == "name=foobar"
        """
        query_obj = self.data.query
        query_str = ""
        if query_obj:
            query_str = str(query_obj)
        if query_str == "":
            query_str = None
        return query_str

class CpdPathImpl(CpdPath):
    @classmethod
    def from_string(cls: Type[Self], path: str) -> Self:
        # overwriting to simplify inheritance
        result = super().from_string(path)
        if not isinstance(result, cls):
            expected = cls.__name__
            got = type(result).__name__
            raise TypeError(f"Expected to parse type {expected} but got {got}")
        return result

class CpdScope(CpdPathImpl):
    # always present
    def scope_type(self) -> str:
        return self.data.path.scope.type.value

    def file(self, path: str) -> 'CpdScopeFile':
        """
        Creates a path to a file in the given scope.

        The leading slash is optional.

        Example::

            scope = CpdScope.from_string("cpd://dev/projects/123456789")
            file_path_0 = scope.file("/files/abc/def")
            file_path_1 = scope.file("files/abc/def")
            assert file_path_0 == file_path_1
            assert file_path_0.file() == "/files/abc/def"
        """
        if self.query() is not None:
            raise RuntimeError(f".file(...) is only available for non-query paths")

        new_file_path = path.lstrip('/')
        new_file = File(path=new_file_path)
        new_path = attr.evolve(self.data.path, file=new_file)
        new_data = attr.evolve(self.data, path=new_path)
        new_cpd_path = CpdScopeFile(data=new_data)
        return new_cpd_path

class CpdScopeFile(CpdPathImpl):
    def file_path(self) -> str:
        """
        Extract the file path.

        Example::

            file_path = CpdPath.from_string("cpd://dev/projects/123456789/files/abc/def")
            assert file_path.file_path() == "/abc/def"

            file_path = CpdPath.from_string("cpd://dev/projects/123456789/connections/3141592/files/~/abc/def")
            assert file_path.file_path() == "/abc/def"
        """

        return  "/" + self.data.path.file.path

class CpdResource(CpdPathImpl):
    def scope(self) -> Optional[CpdScope]:
        """
        Extract the scope path, if any.

        Example::

            scope_path = CpdPath.from_string("cpd://dev/projects/123456789")
            resource_path = CpdPath.from_string("cpd://dev/projects/123456789/connections/3141592")
            assert resource_path.scope() == scope_path
        """

        if self.data.path.scope is None:
            return None
        return CpdScope(
            data=CpdPathData(
                has_prefix=self.data.has_prefix,
                ctx=self.data.ctx,
                path=Path(
                    scope=self.data.path.scope,
                    resource=None,
                    file=None,
                ),
                query=None,
            )
        )

    def resource_type(self) -> str:
        """
        Return the resource type.

        Example::

            path = CpdPath.from_string("cpd://dev/projects/123456789/connections/3141592")
            assert path.resource_type() == "connections"
        """
        return self.data.path.resource.type.value

    def resource_id(self) -> Optional[str]:
        """
        Return the resource ID, if any.

        Example::

            path = CpdPath.from_string("cpd://dev/projects/123456789/connections/3141592")
            assert path.resource_id() == "3141592"

            path = CpdPath.from_string("cpd://dev/projects/123456789/connections?name=foobar")
            assert path.resource_id() is None
        """
        return self.data.path.resource.id

    @overload
    def file(self, path: str) -> 'CpdConnectionFile': ...
    @overload
    def file(self, bucket_name: str, path: str) -> 'CpdConnectionFile': ...

    def file(self, *args, **kwargs) -> 'CpdConnectionFile':
        """
        Creates a path to a file in the given connection.

        The leading slash is optional.

        Will fail if the resource is not a connection.

        Example::

            scope = CpdResource.from_string("cpd://dev/projects/123456789/connections/3141592")
            file_path_0 = scope.file("/files/abc/def")
            file_path_1 = scope.file("~", "/files/abc/def")
            assert file_path_0 == file_path_1
            assert file_path_0.bucket_name() == "~"
            assert file_path_0.file() == "/files/abc/def"
        """
        if len(args) == 2:
            bucket_name = args[0]
            path = args[1]
        elif len(args) == 1:
            if 'path' in kwargs:
                bucket_name = args[0]
                path = kwargs['path']
            else:
                bucket_name = '~'
                path = args[0]
        elif 'path' in kwargs and 'bucket_name' in kwargs:
            bucket_name = kwargs['bucket_name']
            path = kwargs['path']
        elif 'path' in kwargs:
            bucket_name = '~'
            path = kwargs['path']
        else:
            raise NoSuchOverloadError(f'{type(self).__name__}.file(...)', args, kwargs)

        if self.query() is not None:
            raise RuntimeError(f".file(...) is only available for non-query paths")

        if self.resource_type() != "connections":
            raise RuntimeError(f".file(...) is only available for connection resource, but used on '{self.resource_type()}'")

        bucket_name = bucket_name.strip('/')
        path = path.lstrip('/')
        new_file_path = f'{bucket_name}/{path}'

        new_file = File(path=new_file_path)
        new_path = attr.evolve(self.data.path, file=new_file)
        new_data = attr.evolve(self.data, path=new_path)
        new_cpd_path = CpdConnectionFile(data=new_data)
        return new_cpd_path

class CpdConnectionFile(CpdPathImpl):
    def scope(self) -> Optional[CpdScope]:
        """
        Extract the scope path, if any.

        Example::

            scope_path = CpdPath.from_string("cpd://dev/projects/123456789")
            resource_path = CpdPath.from_string("cpd://dev/projects/123456789/connections/3141592")
            assert resource_path.scope() == scope_path
        """

        if self.data.path.scope is None:
            return None
        return CpdScope(
            data=CpdPathData(
                has_prefix=self.data.has_prefix,
                ctx=self.data.ctx,
                path=Path(
                    scope=self.data.path.scope,
                    resource=None,
                    file=None,
                ),
                query=None,
            )
        )

    def resource_type(self) -> str:
        """
        Return the resource type.

        Example::

            path = CpdPath.from_string("cpd://dev/projects/123456789/connections/3141592")
            assert path.resource_type() == "connections"
        """
        return self.data.path.resource.type.value

    def resource_id(self) -> str:
        """
        Return the resource ID, if any.

        Example::

            path = CpdPath.from_string("cpd://dev/projects/123456789/connections/3141592")
            assert path.resource_id() == "3141592"

            path = CpdPath.from_string("cpd://dev/projects/123456789/connections?name=foobar")
            assert path.resource_id() is None
        """
        return self.data.path.resource.id

    def bucket_name(self) -> str:
        """
        Extract the bucket name.

        Example::

            file_path = CpdPath.from_string("cpd://dev/projects/123456789/connections/3141592/files/~/abc/def")
            assert file_path.bucket_name() == "~"
        """
        path = self.data.path.file.path
        parts = path.split("/")
        return parts[0]

    def file_path(self) -> str:
        path = self.data.path.file.path
        parts = path.split("/")
        if len(parts) < 1:
            return "/"
        else:
            return "/" + "/".join(parts[1:])
