# coding: utf-8

"""
    Internship API

    This API delivers data for the Internship project.  # noqa: E501

    OpenAPI spec version: 1.0.9
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Student(object):
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
        'uuid': 'str',
        'registration_id': 'str',
        'person': 'Person'
    }

    attribute_map = {
        'uuid': 'uuid',
        'registration_id': 'registration_id',
        'person': 'person'
    }

    def __init__(self, uuid=None, registration_id=None, person=None):  # noqa: E501
        """Student - a model defined in OpenAPI"""  # noqa: E501

        self._uuid = None
        self._registration_id = None
        self._person = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if registration_id is not None:
            self.registration_id = registration_id
        if person is not None:
            self.person = person

    @property
    def uuid(self):
        """Gets the uuid of this Student.  # noqa: E501


        :return: The uuid of this Student.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this Student.


        :param uuid: The uuid of this Student.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def registration_id(self):
        """Gets the registration_id of this Student.  # noqa: E501


        :return: The registration_id of this Student.  # noqa: E501
        :rtype: str
        """
        return self._registration_id

    @registration_id.setter
    def registration_id(self, registration_id):
        """Sets the registration_id of this Student.


        :param registration_id: The registration_id of this Student.  # noqa: E501
        :type: str
        """

        self._registration_id = registration_id

    @property
    def person(self):
        """Gets the person of this Student.  # noqa: E501


        :return: The person of this Student.  # noqa: E501
        :rtype: Person
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this Student.


        :param person: The person of this Student.  # noqa: E501
        :type: Person
        """

        self._person = person

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
        if not isinstance(other, Student):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
