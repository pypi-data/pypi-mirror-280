import os
from setuptools import setup

VERSION = "0.0.2"

if os.environ.get("CI_COMMIT_TAG"):
    version = os.environ["CI_COMMIT_TAG"]
else:
    version = VERSION

setup(
    name="data_tools_moton",
    version=version,
    description="Standalone tools package for ETL development",
    author="Rick Moton",
    license="MIT",
    packages=[
        "data_tools",
        "data_tools.io",
        "data_tools.utils",
    ],
    include_package_data=True,
    zip_safe=False,
)