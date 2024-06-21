# Copyright IBM Corp. 2020. All Rights Reserved.

import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ibm-orchestration-pipelines",
    version="1.0.4",
    author="Rafał Bigaj, Maksymilian Erazmus",
    author_email="rafal.bigaj@pl.ibm.com, maksymilian.erazmus1@pl.ibm.com",
    description="Python utilities for IBM Orchestration Pipelines",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.ibm.com/docs/en/cloud-paks/cp-data/4.8.x?topic=assets-orchestrating-tasks-pipelines",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.9',
    install_requires = [
        'ibm_cloud_sdk_core>=3.11.3',
        'ibm-cos-sdk>=2.10.0',
        'attrs>=21.2.0',
        'kfp>=1.8.22,<2.0.0',
        'requests>=2.25.1',
        'responses>=0.13.4',
        'pytest>=6.2.5',
        'typing-extensions>=3.7.4',
        'urllib3==1.26.18'
    ],
    include_package_data=True,
)
