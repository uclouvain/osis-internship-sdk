# coding: utf-8

"""
    Internship API

    This API delivers data for the Internship project.  # noqa: E501

    OpenAPI spec version: 1.0.10
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class StudentGet(object):
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
        'person': 'Person',
        'location': 'str',
        'postal_code': 'str',
        'city': 'str',
        'country': 'str',
        'email': 'str',
        'phone_mobile': 'str',
        'contest': 'str',
        'cohort': 'CohortGet',
        'evolution_score': 'float',
        'evolution_score_reason': 'str'
    }

    attribute_map = {
        'url': 'url',
        'person': 'person',
        'location': 'location',
        'postal_code': 'postal_code',
        'city': 'city',
        'country': 'country',
        'email': 'email',
        'phone_mobile': 'phone_mobile',
        'contest': 'contest',
        'cohort': 'cohort',
        'evolution_score': 'evolution_score',
        'evolution_score_reason': 'evolution_score_reason'
    }

    def __init__(self, url=None, person=None, location=None, postal_code=None, city=None, country=None, email=None, phone_mobile=None, contest=None, cohort=None, evolution_score=None, evolution_score_reason=None):  # noqa: E501
        """StudentGet - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._person = None
        self._location = None
        self._postal_code = None
        self._city = None
        self._country = None
        self._email = None
        self._phone_mobile = None
        self._contest = None
        self._cohort = None
        self._evolution_score = None
        self._evolution_score_reason = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if person is not None:
            self.person = person
        if location is not None:
            self.location = location
        if postal_code is not None:
            self.postal_code = postal_code
        if city is not None:
            self.city = city
        if country is not None:
            self.country = country
        if email is not None:
            self.email = email
        if phone_mobile is not None:
            self.phone_mobile = phone_mobile
        if contest is not None:
            self.contest = contest
        if cohort is not None:
            self.cohort = cohort
        if evolution_score is not None:
            self.evolution_score = evolution_score
        if evolution_score_reason is not None:
            self.evolution_score_reason = evolution_score_reason

    @property
    def url(self):
        """Gets the url of this StudentGet.  # noqa: E501


        :return: The url of this StudentGet.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this StudentGet.


        :param url: The url of this StudentGet.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def person(self):
        """Gets the person of this StudentGet.  # noqa: E501


        :return: The person of this StudentGet.  # noqa: E501
        :rtype: Person
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this StudentGet.


        :param person: The person of this StudentGet.  # noqa: E501
        :type: Person
        """

        self._person = person

    @property
    def location(self):
        """Gets the location of this StudentGet.  # noqa: E501


        :return: The location of this StudentGet.  # noqa: E501
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this StudentGet.


        :param location: The location of this StudentGet.  # noqa: E501
        :type: str
        """

        self._location = location

    @property
    def postal_code(self):
        """Gets the postal_code of this StudentGet.  # noqa: E501


        :return: The postal_code of this StudentGet.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this StudentGet.


        :param postal_code: The postal_code of this StudentGet.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def city(self):
        """Gets the city of this StudentGet.  # noqa: E501


        :return: The city of this StudentGet.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this StudentGet.


        :param city: The city of this StudentGet.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def country(self):
        """Gets the country of this StudentGet.  # noqa: E501


        :return: The country of this StudentGet.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this StudentGet.


        :param country: The country of this StudentGet.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def email(self):
        """Gets the email of this StudentGet.  # noqa: E501


        :return: The email of this StudentGet.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this StudentGet.


        :param email: The email of this StudentGet.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone_mobile(self):
        """Gets the phone_mobile of this StudentGet.  # noqa: E501


        :return: The phone_mobile of this StudentGet.  # noqa: E501
        :rtype: str
        """
        return self._phone_mobile

    @phone_mobile.setter
    def phone_mobile(self, phone_mobile):
        """Sets the phone_mobile of this StudentGet.


        :param phone_mobile: The phone_mobile of this StudentGet.  # noqa: E501
        :type: str
        """

        self._phone_mobile = phone_mobile

    @property
    def contest(self):
        """Gets the contest of this StudentGet.  # noqa: E501


        :return: The contest of this StudentGet.  # noqa: E501
        :rtype: str
        """
        return self._contest

    @contest.setter
    def contest(self, contest):
        """Sets the contest of this StudentGet.


        :param contest: The contest of this StudentGet.  # noqa: E501
        :type: str
        """

        self._contest = contest

    @property
    def cohort(self):
        """Gets the cohort of this StudentGet.  # noqa: E501


        :return: The cohort of this StudentGet.  # noqa: E501
        :rtype: CohortGet
        """
        return self._cohort

    @cohort.setter
    def cohort(self, cohort):
        """Sets the cohort of this StudentGet.


        :param cohort: The cohort of this StudentGet.  # noqa: E501
        :type: CohortGet
        """

        self._cohort = cohort

    @property
    def evolution_score(self):
        """Gets the evolution_score of this StudentGet.  # noqa: E501


        :return: The evolution_score of this StudentGet.  # noqa: E501
        :rtype: float
        """
        return self._evolution_score

    @evolution_score.setter
    def evolution_score(self, evolution_score):
        """Sets the evolution_score of this StudentGet.


        :param evolution_score: The evolution_score of this StudentGet.  # noqa: E501
        :type: float
        """

        self._evolution_score = evolution_score

    @property
    def evolution_score_reason(self):
        """Gets the evolution_score_reason of this StudentGet.  # noqa: E501


        :return: The evolution_score_reason of this StudentGet.  # noqa: E501
        :rtype: str
        """
        return self._evolution_score_reason

    @evolution_score_reason.setter
    def evolution_score_reason(self, evolution_score_reason):
        """Sets the evolution_score_reason of this StudentGet.


        :param evolution_score_reason: The evolution_score_reason of this StudentGet.  # noqa: E501
        :type: str
        """

        self._evolution_score_reason = evolution_score_reason

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
        if not isinstance(other, StudentGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
