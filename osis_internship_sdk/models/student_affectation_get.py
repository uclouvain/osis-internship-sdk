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


class StudentAffectationGet(object):
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
        'student': 'Student',
        'organization': 'OrganizationGet',
        'specialty': 'SpecialtyGet',
        'period': 'PeriodGet',
        'internship': 'InternshipGet'
    }

    attribute_map = {
        'url': 'url',
        'student': 'student',
        'organization': 'organization',
        'specialty': 'specialty',
        'period': 'period',
        'internship': 'internship'
    }

    def __init__(self, url=None, student=None, organization=None, specialty=None, period=None, internship=None):  # noqa: E501
        """StudentAffectationGet - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._student = None
        self._organization = None
        self._specialty = None
        self._period = None
        self._internship = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if student is not None:
            self.student = student
        if organization is not None:
            self.organization = organization
        if specialty is not None:
            self.specialty = specialty
        if period is not None:
            self.period = period
        if internship is not None:
            self.internship = internship

    @property
    def url(self):
        """Gets the url of this StudentAffectationGet.  # noqa: E501


        :return: The url of this StudentAffectationGet.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this StudentAffectationGet.


        :param url: The url of this StudentAffectationGet.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def student(self):
        """Gets the student of this StudentAffectationGet.  # noqa: E501


        :return: The student of this StudentAffectationGet.  # noqa: E501
        :rtype: Student
        """
        return self._student

    @student.setter
    def student(self, student):
        """Sets the student of this StudentAffectationGet.


        :param student: The student of this StudentAffectationGet.  # noqa: E501
        :type: Student
        """

        self._student = student

    @property
    def organization(self):
        """Gets the organization of this StudentAffectationGet.  # noqa: E501


        :return: The organization of this StudentAffectationGet.  # noqa: E501
        :rtype: OrganizationGet
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this StudentAffectationGet.


        :param organization: The organization of this StudentAffectationGet.  # noqa: E501
        :type: OrganizationGet
        """

        self._organization = organization

    @property
    def specialty(self):
        """Gets the specialty of this StudentAffectationGet.  # noqa: E501


        :return: The specialty of this StudentAffectationGet.  # noqa: E501
        :rtype: SpecialtyGet
        """
        return self._specialty

    @specialty.setter
    def specialty(self, specialty):
        """Sets the specialty of this StudentAffectationGet.


        :param specialty: The specialty of this StudentAffectationGet.  # noqa: E501
        :type: SpecialtyGet
        """

        self._specialty = specialty

    @property
    def period(self):
        """Gets the period of this StudentAffectationGet.  # noqa: E501


        :return: The period of this StudentAffectationGet.  # noqa: E501
        :rtype: PeriodGet
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this StudentAffectationGet.


        :param period: The period of this StudentAffectationGet.  # noqa: E501
        :type: PeriodGet
        """

        self._period = period

    @property
    def internship(self):
        """Gets the internship of this StudentAffectationGet.  # noqa: E501


        :return: The internship of this StudentAffectationGet.  # noqa: E501
        :rtype: InternshipGet
        """
        return self._internship

    @internship.setter
    def internship(self, internship):
        """Sets the internship of this StudentAffectationGet.


        :param internship: The internship of this StudentAffectationGet.  # noqa: E501
        :type: InternshipGet
        """

        self._internship = internship

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
        if not isinstance(other, StudentAffectationGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other