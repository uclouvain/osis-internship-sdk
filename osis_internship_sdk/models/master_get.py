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


class MasterGet(object):
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
        'uuid': 'str',
        'person': 'Person',
        'civility': 'str',
        'role': 'str'
    }

    attribute_map = {
        'url': 'url',
        'uuid': 'uuid',
        'person': 'person',
        'civility': 'civility',
        'role': 'role'
    }

    def __init__(self, url=None, uuid=None, person=None, civility=None, role=None):  # noqa: E501
        """MasterGet - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._uuid = None
        self._person = None
        self._civility = None
        self._role = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if uuid is not None:
            self.uuid = uuid
        if person is not None:
            self.person = person
        if civility is not None:
            self.civility = civility
        if role is not None:
            self.role = role

    @property
    def url(self):
        """Gets the url of this MasterGet.  # noqa: E501


        :return: The url of this MasterGet.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this MasterGet.


        :param url: The url of this MasterGet.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def uuid(self):
        """Gets the uuid of this MasterGet.  # noqa: E501


        :return: The uuid of this MasterGet.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this MasterGet.


        :param uuid: The uuid of this MasterGet.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def person(self):
        """Gets the person of this MasterGet.  # noqa: E501


        :return: The person of this MasterGet.  # noqa: E501
        :rtype: Person
        """
        return self._person

    @person.setter
    def person(self, person):
        """Sets the person of this MasterGet.


        :param person: The person of this MasterGet.  # noqa: E501
        :type: Person
        """

        self._person = person

    @property
    def civility(self):
        """Gets the civility of this MasterGet.  # noqa: E501


        :return: The civility of this MasterGet.  # noqa: E501
        :rtype: str
        """
        return self._civility

    @civility.setter
    def civility(self, civility):
        """Sets the civility of this MasterGet.


        :param civility: The civility of this MasterGet.  # noqa: E501
        :type: str
        """

        self._civility = civility

    @property
    def role(self):
        """Gets the role of this MasterGet.  # noqa: E501


        :return: The role of this MasterGet.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this MasterGet.


        :param role: The role of this MasterGet.  # noqa: E501
        :type: str
        """

        self._role = role

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
        if not isinstance(other, MasterGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
