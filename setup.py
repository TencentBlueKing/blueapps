# -*- coding: utf-8 -*-
"""
Tencent is pleased to support the open source community by making 蓝鲸智云PaaS平台社区版 (BlueKing PaaS Community
Edition) available.
Copyright (C) 2017-2021 THL A29 Limited, a Tencent company. All rights reserved.
Licensed under the MIT License (the "License"); you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://opensource.org/licenses/MIT
Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
specific language governing permissions and limitations under the License.
"""

# To use a consistent encoding
from codecs import open
from os import path

# Always prefer setuptools over distutils
from setuptools import find_packages, setup

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, "README.md"), encoding="utf-8") as f:
    long_description = f.read()
version = __import__("blueapps").__version__

setup(
    name="blueapps-open",
    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version=version,
    description="development framework for blueking",
    long_description=long_description,
    long_description_content_type='text/markdown',
    # The project's main homepage.
    url="https://github.com/TencentBlueKing/blueapps",
    # Author details
    author="blueking",
    author_email="blueking@tencent.com",
    include_package_data=True,
    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(),
    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    #   py_modules=["my_module"],
    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        "Django==2.2.6",
        "mysqlclient==1.4.4",
        #"bkoauth>=0.0.12",
        "MarkupSafe==1.1.1",
        "Mako>=1.0.6,<2.0",
        "requests==2.22.0",
        "python-json-logger==0.1.7",
        "whitenoise==3.3.0",

        # jwt
        "pycrypto==2.6.1",
        "PyJWT==1.7.1",
        "cryptography==2.7",
    ],
    zip_safe=False,
    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    entry_points={
        "console_scripts": ["bk-admin=blueapps.contrib.bk_commands:bk_admin"],
    },
)
