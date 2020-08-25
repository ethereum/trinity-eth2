#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

TRINITY_DEP = "57bee06c9ad350ddfba1ae4b2081025aa454880d"

deps = {
    "trinity-eth2": [
        f"trinity @ git+https://github.com/ethereum/trinity.git@{TRINITY_DEP}"
    ],
    "test": [
        "async-timeout>=3.0.1,<4",
        "hypothesis>=4.45.1,<5",
        "pexpect>=4.6, <5",
        "factory-boy==2.12.0",
        "pytest>=5.3.0,<5.4",
        "pytest-cov>=2.8.1,<2.9",
        "pytest-mock>=1.12.1,<1.13",
        "pytest-randomly>=3.1.0,<3.2",
        "pytest-timeout>=1.4.2,<2",
        "pytest-watch>=4.2.0,<4.3",
        # xdist pinned at <1.29 due to: https://github.com/pytest-dev/pytest-xdist/issues/472
        "pytest-xdist>=1.29.0,<1.30",
        # only for eth2
        "ruamel.yaml==0.16.10",
        "eth-tester==0.4.0b2",
    ],
    # We have to keep some separation between trio and asyncio based tests
    # because `pytest-asyncio` is greedy and tries to run all asyncio fixtures.
    # See: https://github.com/ethereum/trinity/pull/790
    # NOTE: In order to properly run any asyncio tests you need to manually install the
    # test-asyncio deps, otherwise pytest will run them but never await for them to finish and
    # you'll get warnings saying that a coroutine was never awaited.
    "test-asyncio": ["pytest-asyncio>=0.10.0,<0.11", "pytest-aiohttp>=0.3.0,<0.4"],
    "test-trio": ["pytest-trio>=0.5.2,<0.6"],
    "lint": [
        "flake8==3.7.9",
        "flake8-bugbear==19.8.0",
        "mypy==0.782",
        "sqlalchemy-stubs==0.3",
        "black==19.3b0",
        "isort==4.3.21",
    ],
    "dev": [
        "bumpversion>=0.5.3,<1",
        "wheel",
        "setuptools>=36.2.0",
        "tox==2.7.0",
        "twine",
    ],
    "eth2": [
        "cytoolz>=0.9.0,<1.0.0",
        "eth-typing>=2.1.0,<3.0.0",
        "lru-dict>=1.1.6",
        "py-ecc==4.0.0",
        "rlp>=1.1.0,<2.0.0",
        "ssz==0.2.4",
        "asks>=2.3.6,<3",  # validator client
        "anyio>1.3,<1.4",
        "eth-keyfile",  # validator client
        "milagro-bls-binding==1.3.0",
    ],
}

deps["dev"] = (
    deps["dev"] + deps["trinity-eth2"] + deps["test"] + deps["lint"] + deps["eth2"]
)


install_requires = deps["trinity-eth2"] + deps["eth2"]


with open("./README.md") as readme:
    long_description = readme.read()


setup(
    name="trinity-eth2",
    # *IMPORTANT*: Don't manually change the version here. Use the 'bumpversion' utility.
    version="0.1.0-alpha.0",
    description="The Trinity client for the Ethereum 2.0 network",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Ethereum Foundation",
    author_email="piper@pipermerriam.com",
    url="https://github.com/ethereum/trinity",
    include_package_data=True,
    py_modules=["trinity-eth2", "eth2"],
    python_requires=">=3.7,<4",
    install_requires=install_requires,
    extras_require=deps,
    license="MIT",
    zip_safe=False,
    keywords="ethereum 2.0 blockchain evm trinity",
    packages=find_packages(exclude=["tests", "tests.*"]),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    # trinity
    entry_points={
        "console_scripts": [
            "trinity-beacon=trinity:main_beacon_trio",
            "trinity-validator=trinity:main_validator",
        ]
    },
)
