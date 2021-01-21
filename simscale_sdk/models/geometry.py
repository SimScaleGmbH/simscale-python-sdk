# coding: utf-8

"""
    SimScale API

    The version of the OpenAPI document: 0.0.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from simscale_sdk.configuration import Configuration


class Geometry(object):
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
        'geometry_id': 'str',
        'name': 'str',
        'created_at': 'datetime',
        'format': 'str'
    }

    attribute_map = {
        'geometry_id': 'geometryId',
        'name': 'name',
        'created_at': 'createdAt',
        'format': 'format'
    }

    def __init__(self, geometry_id=None, name=None, created_at=None, format=None, local_vars_configuration=None):  # noqa: E501
        """Geometry - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._geometry_id = None
        self._name = None
        self._created_at = None
        self._format = None
        self.discriminator = None

        if geometry_id is not None:
            self.geometry_id = geometry_id
        if name is not None:
            self.name = name
        if created_at is not None:
            self.created_at = created_at
        if format is not None:
            self.format = format

    @property
    def geometry_id(self):
        """Gets the geometry_id of this Geometry.  # noqa: E501


        :return: The geometry_id of this Geometry.  # noqa: E501
        :rtype: str
        """
        return self._geometry_id

    @geometry_id.setter
    def geometry_id(self, geometry_id):
        """Sets the geometry_id of this Geometry.


        :param geometry_id: The geometry_id of this Geometry.  # noqa: E501
        :type: str
        """

        self._geometry_id = geometry_id

    @property
    def name(self):
        """Gets the name of this Geometry.  # noqa: E501

        The name of the geometry.  # noqa: E501

        :return: The name of this Geometry.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Geometry.

        The name of the geometry.  # noqa: E501

        :param name: The name of this Geometry.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this Geometry.  # noqa: E501

        The time when the geometry was imported.  # noqa: E501

        :return: The created_at of this Geometry.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Geometry.

        The time when the geometry was imported.  # noqa: E501

        :param created_at: The created_at of this Geometry.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def format(self):
        """Gets the format of this Geometry.  # noqa: E501

        The geometry format.  # noqa: E501

        :return: The format of this Geometry.  # noqa: E501
        :rtype: str
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this Geometry.

        The geometry format.  # noqa: E501

        :param format: The format of this Geometry.  # noqa: E501
        :type: str
        """

        self._format = format

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
        if not isinstance(other, Geometry):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Geometry):
            return True

        return self.to_dict() != other.to_dict()
