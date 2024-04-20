import io
import os
import re

from pathlib import Path
from setuptools import find_packages, setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type("")
    with io.open(filename, mode="r", encoding="utf-8") as fd:
        return re.sub(text_type(r":[a-z]+:`~?(.*?)`"), text_type(r"``\1``"), fd.read())


def version():
    """Get the local package version."""
    namespace = {}
    path = Path("maze/__version__.py")
    exec(path.read_text(), namespace)
    return namespace["__version__"]


setup(
    name="mazeai",
    version=version(),
    url="https://github.com/zhaisilong/mazeai",
    license="MIT",
    author="Zhai Silong",
    author_email="zhaisilong@outlook.com",
    description="A General Tool Set for Science Researches",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    packages=find_packages(where=".", exclude=("tests",), include=("*")),
    package_data={"maze": ["resource/*"]},
    entry_points={
        "console_scripts": [
            "maze = maze.__main__:main",
        ],
    },
    install_requires=[
        "rich",
        "ipykernel",
        "tqdm",
        "loguru",
        "hydra-core",
    ],
    extras_require={
        'chem': ['jpype1'],  # 可选的绘图支持
    },
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.7",
    ],
    python_requires=">=3.6",  # The recommended least version of python
)
