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


class AllocationGet(object):
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
        'master': 'MasterGet',
        'organization': 'OrganizationGet',
        'specialty': 'SpecialtyGet',
        'role': 'str'
    }

    attribute_map = {
        'url': 'url',
        'uuid': 'uuid',
        'master': 'master',
        'organization': 'organization',
        'specialty': 'specialty',
        'role': 'role'
    }

    def __init__(self, url=None, uuid=None, master=None, organization=None, specialty=None, role=None):  # noqa: E501
        """AllocationGet - a model defined in OpenAPI"""  # noqa: E501

        self._url = None
        self._uuid = None
        self._master = None
        self._organization = None
        self._specialty = None
        self._role = None
        self.discriminator = None

        if url is not None:
            self.url = url
        if uuid is not None:
            self.uuid = uuid
        if master is not None:
            self.master = master
        if organization is not None:
            self.organization = organization
        if specialty is not None:
            self.specialty = specialty
        if role is not None:
            self.role = role

    @property
    def url(self):
        """Gets the url of this AllocationGet.  # noqa: E501


        :return: The url of this AllocationGet.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AllocationGet.


        :param url: The url of this AllocationGet.  # noqa: E501
        :type: str
        """

        self._url = url

    @property
    def uuid(self):
        """Gets the uuid of this AllocationGet.  # noqa: E501


        :return: The uuid of this AllocationGet.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this AllocationGet.


        :param uuid: The uuid of this AllocationGet.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def master(self):
        """Gets the master of this AllocationGet.  # noqa: E501


        :return: The master of this AllocationGet.  # noqa: E501
        :rtype: MasterGet
        """
        return self._master

    @master.setter
    def master(self, master):
        """Sets the master of this AllocationGet.


        :param master: The master of this AllocationGet.  # noqa: E501
        :type: MasterGet
        """

        self._master = master

    @property
    def organization(self):
        """Gets the organization of this AllocationGet.  # noqa: E501


        :return: The organization of this AllocationGet.  # noqa: E501
        :rtype: OrganizationGet
        """
        return self._organization

    @organization.setter
    def organization(self, organization):
        """Sets the organization of this AllocationGet.


        :param organization: The organization of this AllocationGet.  # noqa: E501
        :type: OrganizationGet
        """

        self._organization = organization

    @property
    def specialty(self):
        """Gets the specialty of this AllocationGet.  # noqa: E501


        :return: The specialty of this AllocationGet.  # noqa: E501
        :rtype: SpecialtyGet
        """
        return self._specialty

    @specialty.setter
    def specialty(self, specialty):
        """Sets the specialty of this AllocationGet.


        :param specialty: The specialty of this AllocationGet.  # noqa: E501
        :type: SpecialtyGet
        """

        self._specialty = specialty

    @property
    def role(self):
        """Gets the role of this AllocationGet.  # noqa: E501


        :return: The role of this AllocationGet.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this AllocationGet.


        :param role: The role of this AllocationGet.  # noqa: E501
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
        if not isinstance(other, AllocationGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
