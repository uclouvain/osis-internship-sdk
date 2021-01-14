# coding: utf-8

"""
    Internship API

    This API delivers data for the Internship project.  # noqa: E501

    OpenAPI spec version: 1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class OrganizationGet(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'url': 'str',
        'name': 'str',
        'acronym': 'str',
        'website': 'str',
        'reference': 'str',
        'phone': 'str',
        'location': 'str',
        'postal_code': 'str',
        'city': 'str',
        'country': 'Country',
        'cohort': 'CohortGet'
    }

    attribute_map = {
        'url': 'url',
        'name': 'name',
        'acronym': 'acronym',
        'website': 'website',
        'reference': 'reference',
        'phone': 'phone',
        'location': 'location',
        'postal_code': 'postal_code',
        'city': 'city',
        'country': 'country',
        'cohort': 'cohort'
    }

    def __init__(self, url=None, name=None, acronym=None, website=None, reference=None, phone=None, location=None, postal_code=None, city=None, country=None, cohort=None):  # noqa: E501
        """OrganizationGet - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._name = None
        self._acronym = None
        self._website = None
        self._reference = None
        self._phone = None
        self._location = None
        self._postal_code = None
        self._city = None
        self._country = None
        self._cohort = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if name is not None:
            self.name = name
        if acronym is not None:
            self.acronym = acronym
        if website is not None:
            self.website = website
        if reference is not None:
            self.reference = reference
        if phone is not None:
            self.phone = phone
        if location is not None:
            self.location = location
        if postal_code is not None:
            self.postal_code = postal_code
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if cohort is not None:
            self.cohort = cohort

    @property
    def url(self):
        """Gets the url of this OrganizationGet.  # noqa: E501


        :return: The url of this OrganizationGet.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this OrganizationGet.


        :param url: The url of this OrganizationGet.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def name(self):
        """Gets the name of this OrganizationGet.  # noqa: E501


        :return: The name of this OrganizationGet.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OrganizationGet.


        :param name: The name of this OrganizationGet.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def acronym(self):
        """Gets the acronym of this OrganizationGet.  # noqa: E501


        :return: The acronym of this OrganizationGet.  # noqa: E501
        :rtype: str
        """
        return self._acronym

    @acronym.setter
    def acronym(self, acronym):
        """Sets the acronym of this OrganizationGet.


        :param acronym: The acronym of this OrganizationGet.  # noqa: E501
        :type: str
        """

        self._acronym = acronym

    @property
    def website(self):
        """Gets the website of this OrganizationGet.  # noqa: E501


        :return: The website of this OrganizationGet.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this OrganizationGet.


        :param website: The website of this OrganizationGet.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def reference(self):
        """Gets the reference of this OrganizationGet.  # noqa: E501


        :return: The reference of this OrganizationGet.  # noqa: E501
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this OrganizationGet.


        :param reference: The reference of this OrganizationGet.  # noqa: E501
        :type: str
        """

        self._reference = reference

    @property
    def phone(self):
        """Gets the phone of this OrganizationGet.  # noqa: E501


        :return: The phone of this OrganizationGet.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this OrganizationGet.


        :param phone: The phone of this OrganizationGet.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def location(self):
        """Gets the location of this OrganizationGet.  # noqa: E501


        :return: The location of this OrganizationGet.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this OrganizationGet.


        :param location: The location of this OrganizationGet.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def postal_code(self):
        """Gets the postal_code of this OrganizationGet.  # noqa: E501


        :return: The postal_code of this OrganizationGet.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this OrganizationGet.


        :param postal_code: The postal_code of this OrganizationGet.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def city(self):
        """Gets the city of this OrganizationGet.  # noqa: E501


        :return: The city of this OrganizationGet.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this OrganizationGet.


        :param city: The city of this OrganizationGet.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this OrganizationGet.  # noqa: E501


        :return: The country of this OrganizationGet.  # noqa: E501
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this OrganizationGet.


        :param country: The country of this OrganizationGet.  # noqa: E501
        :type: Country
        """

        self._country = country

    @property
    def cohort(self):
        """Gets the cohort of this OrganizationGet.  # noqa: E501


        :return: The cohort of this OrganizationGet.  # noqa: E501
        :rtype: CohortGet
        """
        return self._cohort

    @cohort.setter
    def cohort(self, cohort):
        """Sets the cohort of this OrganizationGet.


        :param cohort: The cohort of this OrganizationGet.  # noqa: E501
        :type: CohortGet
        """

        self._cohort = cohort

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OrganizationGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
