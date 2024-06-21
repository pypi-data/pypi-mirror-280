# IBM Confidential
# OCO Source Materials
# 5737-B37, 5737-C49, 5737-H76
# (C) Copyright IBM Corp. 2021, 2022  All Rights Reserved.
# The source code for this program is not published or
# otherwise divested of its trade secrets, irrespective of
# what has been deposited with the U.S. Copyright Office.

import pytest

from ibm_orchestration_pipelines import CpdPath
from ibm_orchestration_pipelines.cpd_paths import CpdResource, CpdScopeFile, \
    CpdConnectionFile, CpdScope


def test_00_to_string_is_equiv():
    paths = [
        "cpd://dev-dallas/projects/6e351231-e734-4437-83e5-257fcfbb0a0a/assets/0d12adac-c073-4038-ba19-9c57017a5b57",
        "cpd:///projects/6e351231-e734-4437-83e5-257fcfbb0a0a/assets/0d12adac-c073-4038-ba19-9c57017a5b57",
        "/projects/6e351231-e734-4437-83e5-257fcfbb0a0a/assets/0d12adac-c073-4038-ba19-9c57017a5b57",
        "assets/0d12adac-c073-4038-ba19-9c57017a5b57",
        "cpd:///projects/4b4946f4-242e-4ed0-9c80-24ae9b48db19/files/abc/def",
        "/projects/4b4946f4-242e-4ed0-9c80-24ae9b48db19/files/abc/def",
        "cpd:///projects/4b4946f4-242e-4ed0-9c80-24ae9b48db19/connections/90985f12-2ae6-49bc-9872-4b94e1b47ef5/files/~/abc/def",
        "/projects/4b4946f4-242e-4ed0-9c80-24ae9b48db19/connections/90985f12-2ae6-49bc-9872-4b94e1b47ef5/files/~/abc/def",
    ]
    for path in paths:
        cpd_path = CpdPath.from_string(path)
        assert str(cpd_path) == path

def test_01_scope_and_resource_retrieved_correctly():
    scopes = [
        "cpd://dev-dallas/projects/6e351231-e734-4437-83e5-257fcfbb0a0a",
        "cpd:///projects/6e351231-e734-4437-83e5-257fcfbb0a0a",
        "/projects/6e351231-e734-4437-83e5-257fcfbb0a0a",
    ]
    resources = [
        "/projects/6e351231-e734-4437-83e5-257fcfbb0a0a/assets/0d12adac-c073-4038-ba19-9c57017a5b57",
        "cpd://dev-dallas/projects/6e351231-e734-4437-83e5-257fcfbb0a0a/assets/0d12adac-c073-4038-ba19-9c57017a5b57",
        "cpd:///projects/6e351231-e734-4437-83e5-257fcfbb0a0a/assets/0d12adac-c073-4038-ba19-9c57017a5b57",
        "/projects/6e351231-e734-4437-83e5-257fcfbb0a0a/assets/0d12adac-c073-4038-ba19-9c57017a5b57",
    ]
    for path in scopes + resources:
        cpd_path = CpdPath.from_string(path)
        assert cpd_path.scope_type() == "projects"
        assert cpd_path.scope_id() == "6e351231-e734-4437-83e5-257fcfbb0a0a"
    for path in resources:
        cpd_path = CpdResource.from_string(path)
        assert cpd_path.resource_type() == "assets"
        assert cpd_path.resource_id() == "0d12adac-c073-4038-ba19-9c57017a5b57"

def test_02a_scope_query_name():
    scopes = [
        "cpd://dev-dallas/projects?name=foo",
        "cpd:///projects?name=foo",
        "/projects?name=foo",
    ]
    for path in scopes:
        cpd_path = CpdPath.from_string(path)
        assert cpd_path.scope_type() == "projects"
        assert cpd_path.scope_id() is None
        assert cpd_path.query() == "name=foo"

def test_02b_scope_query_tags():
    scopes = [
        "cpd://dev-dallas/projects?tags=abc,def",
        "cpd:///projects?tags=abc,def",
        "/projects?tags=abc,def",
    ]
    for path in scopes:
        cpd_path = CpdPath.from_string(path)
        assert cpd_path.scope_type() == "projects"
        assert cpd_path.scope_id() is None
        assert cpd_path.query() == "tags=abc,def"

def test_02c_scope_query_name():
    scopes = [
        "cpd://dev-dallas/projects?name=foo&tags=abc,def",
        "cpd:///projects?name=foo&tags=abc,def",
        "/projects?name=foo&tags=abc,def",
    ]
    for path in scopes:
        cpd_path = CpdPath.from_string(path)
        assert cpd_path.scope_type() == "projects"
        assert cpd_path.scope_id() is None
        assert cpd_path.query() == "name=foo&tags=abc,def"

def test_03a_resource_query_name():
    resources = [
        "cpd://dev-dallas/projects/6e351231-e734-4437-83e5-257fcfbb0a0a/assets?name=foo",
        "cpd:///projects/6e351231-e734-4437-83e5-257fcfbb0a0a/assets?name=foo",
        "/projects/6e351231-e734-4437-83e5-257fcfbb0a0a/assets?name=foo",
    ]
    for path in resources:
        cpd_path = CpdPath.from_string(path)
        assert cpd_path.scope_type() == "projects"
        assert cpd_path.scope_id() == "6e351231-e734-4437-83e5-257fcfbb0a0a"
        assert cpd_path.query() == "name=foo"

    relative_resources = [
        "assets?name=foo",
    ]
    for path in relative_resources:
        cpd_path = CpdPath.from_string(path)
        assert cpd_path.scope_type() is None
        assert cpd_path.scope_id() is None
        assert cpd_path.query() == "name=foo"

def test_03b_resource_query_tags():
    resources = [
        "cpd://dev-dallas/projects/6e351231-e734-4437-83e5-257fcfbb0a0a/assets?tags=abc,def",
        "cpd:///projects/6e351231-e734-4437-83e5-257fcfbb0a0a/assets?tags=abc,def",
        "/projects/6e351231-e734-4437-83e5-257fcfbb0a0a/assets?tags=abc,def",
    ]
    for path in resources:
        cpd_path = CpdPath.from_string(path)
        assert cpd_path.scope_type() == "projects"
        assert cpd_path.scope_id() == "6e351231-e734-4437-83e5-257fcfbb0a0a"
        assert cpd_path.query() == "tags=abc,def"

    relative_resources = [
        "assets?tags=abc,def",
    ]
    for path in relative_resources:
        cpd_path = CpdPath.from_string(path)
        assert cpd_path.scope_type() is None
        assert cpd_path.scope_id() is None
        assert cpd_path.query() == "tags=abc,def"

def test_03c_resource_query_names_and_tags():
    resources = [
        "cpd://dev-dallas/projects/6e351231-e734-4437-83e5-257fcfbb0a0a/assets?name=foo&tags=abc,def",
        "cpd:///projects/6e351231-e734-4437-83e5-257fcfbb0a0a/assets?name=foo&tags=abc,def",
        "/projects/6e351231-e734-4437-83e5-257fcfbb0a0a/assets?name=foo&tags=abc,def",
    ]
    for path in resources:
        cpd_path = CpdPath.from_string(path)
        assert cpd_path.scope_type() == "projects"
        assert cpd_path.scope_id() == "6e351231-e734-4437-83e5-257fcfbb0a0a"
        assert cpd_path.query() == "name=foo&tags=abc,def"

    relative_resources = [
        "assets?name=foo&tags=abc,def",
    ]
    for path in relative_resources:
        cpd_path = CpdPath.from_string(path)
        assert cpd_path.scope_type() is None
        assert cpd_path.scope_id() is None
        assert cpd_path.query() == "name=foo&tags=abc,def"

def test_04a_scope_file_path():
    paths = [
        "cpd:///projects/4b4946f4-242e-4ed0-9c80-24ae9b48db19/files/abc/def",
        "/projects/4b4946f4-242e-4ed0-9c80-24ae9b48db19/files/abc/def",
    ]
    for path in paths:
        cpd_path = CpdPath.from_string(path)
        assert isinstance(cpd_path, CpdScopeFile)
        assert cpd_path.scope_type() == "projects"
        assert cpd_path.scope_id() == "4b4946f4-242e-4ed0-9c80-24ae9b48db19"
        assert cpd_path.file_path() == "/abc/def"

def test_04b_connection_file_path():
    paths = [
        "cpd:///projects/4b4946f4-242e-4ed0-9c80-24ae9b48db19/connections/90985f12-2ae6-49bc-9872-4b94e1b47ef5/files/~/abc/def",
        "/projects/4b4946f4-242e-4ed0-9c80-24ae9b48db19/connections/90985f12-2ae6-49bc-9872-4b94e1b47ef5/files/~/abc/def",
    ]
    for path in paths:
        cpd_path = CpdPath.from_string(path)
        assert isinstance(cpd_path, CpdConnectionFile)
        assert cpd_path.scope_type() == "projects"
        assert cpd_path.scope_id() == "4b4946f4-242e-4ed0-9c80-24ae9b48db19"
        assert cpd_path.resource_type() == "connections"
        assert cpd_path.resource_id() == "90985f12-2ae6-49bc-9872-4b94e1b47ef5"
        assert cpd_path.bucket_name() == "~"
        assert cpd_path.file_path() == "/abc/def"

def test_05a_file_in_scope():
    scope = CpdScope.from_string("cpd:///projects/4b4946f4-242e-4ed0-9c80-24ae9b48db19")
    file_path_0 = scope.file("/abc/def")
    file_path_1 = scope.file("/abc/def")
    assert file_path_0.file_path() == "/abc/def"
    assert file_path_0 == file_path_1

def test_05aa_no_file_in_scope_query():
    scope = CpdScope.from_string("cpd:///projects?name=abc")
    with pytest.raises(RuntimeError):
        scope.file('/abc/def')

def test_05b_file_in_connection():
    conn = CpdResource.from_string("cpd:///projects/4b4946f4-242e-4ed0-9c80-24ae9b48db19/connections/90985f12-2ae6-49bc-9872-4b94e1b47ef5")

    file_path_0 = conn.file("/abc/def")
    file_path_1 = conn.file("abc/def")
    file_path_2 = conn.file("~", "/abc/def")
    file_path_3 = conn.file("~", "abc/def")

    assert file_path_0.bucket_name() == "~"
    assert file_path_0.file_path() == "/abc/def"

    assert file_path_0 == file_path_1
    assert file_path_2 == file_path_3
    assert file_path_0 == file_path_2

    file_path_4 = conn.file("other", "/abc/def")
    assert file_path_4.bucket_name() == "other"
    assert file_path_4.file_path() == "/abc/def"

def test_05bb_no_file_in_connection_query():
    conn = CpdResource.from_string("cpd:///projects/4b4946f4-242e-4ed0-9c80-24ae9b48db19/connections?name=abc")
    with pytest.raises(RuntimeError):
        conn.file('/abc/def')

def test_05c_no_file_in_other_assets():
    assets = [
        "notebooks/90985f12-2ae6-49bc-9872-4b94e1b47ef5",
        "jobs/90985f12-2ae6-49bc-9872-4b94e1b47ef5",
        "job_runs/90985f12-2ae6-49bc-9872-4b94e1b47ef5",
        "environments/90985f12-2ae6-49bc-9872-4b94e1b47ef5",
        "deployments/90985f12-2ae6-49bc-9872-4b94e1b47ef5",
        "assets/90985f12-2ae6-49bc-9872-4b94e1b47ef5",
    ]
    for asset_str in assets:
        asset_path = CpdResource.from_string(asset_str)
        with pytest.raises(RuntimeError):
            asset_path.file('/abc/def')
