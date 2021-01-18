# coding: utf-8

"""
    Internship API

    This API delivers data for the Internship project.  # noqa: E501

    OpenAPI spec version: 1
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "osis_internship_sdk"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Internship API",
    author_email="",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Internship API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    include_package_data=True,
    long_description="""\
    This API delivers data for the Internship project.  # noqa: E501
    """
)
