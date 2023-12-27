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


class Point(object):
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
        'type': 'str',
        'id': 'str',
        'name': 'str',
        'center': 'DimensionalVectorLength'
    }

    attribute_map = {
        'type': 'type',
        'id': 'id',
        'name': 'name',
        'center': 'center'
    }

    def __init__(self, type='POINT', id=None, name=None, center=None, local_vars_configuration=None):  # noqa: E501
        """Point - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._id = None
        self._name = None
        self._center = None
        self.discriminator = None

        self.type = type
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if center is not None:
            self.center = center

    @property
    def type(self):
        """Gets the type of this Point.  # noqa: E501

        Schema name: Point  # noqa: E501

        :return: The type of this Point.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Point.

        Schema name: Point  # noqa: E501

        :param type: The type of this Point.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def id(self):
        """Gets the id of this Point.  # noqa: E501


        :return: The id of this Point.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Point.


        :param id: The id of this Point.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this Point.  # noqa: E501


        :return: The name of this Point.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Point.


        :param name: The name of this Point.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[A-Za-z()][-+0-9a-zA-Z_()\h]{0,199}$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[A-Za-z()][-+0-9a-zA-Z_()\h]{0,199}$/`")  # noqa: E501

        self._name = name

    @property
    def center(self):
        """Gets the center of this Point.  # noqa: E501


        :return: The center of this Point.  # noqa: E501
        :rtype: DimensionalVectorLength
        """
        return self._center

    @center.setter
    def center(self, center):
        """Sets the center of this Point.


        :param center: The center of this Point.  # noqa: E501
        :type: DimensionalVectorLength
        """

        self._center = center

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
        if not isinstance(other, Point):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Point):
            return True

        return self.to_dict() != other.to_dict()
