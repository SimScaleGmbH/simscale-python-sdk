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


class ComponentVectorFunction(object):
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
        'x': 'OneOfComponentVectorFunctionX',
        'y': 'OneOfComponentVectorFunctionY',
        'z': 'OneOfComponentVectorFunctionZ'
    }

    attribute_map = {
        'type': 'type',
        'x': 'x',
        'y': 'y',
        'z': 'z'
    }

    def __init__(self, type='COMPONENT', x=None, y=None, z=None, local_vars_configuration=None):  # noqa: E501
        """ComponentVectorFunction - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._x = None
        self._y = None
        self._z = None
        self.discriminator = None

        self.type = type
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z

    @property
    def type(self):
        """Gets the type of this ComponentVectorFunction.  # noqa: E501

        Schema name: ComponentVectorFunction  # noqa: E501

        :return: The type of this ComponentVectorFunction.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ComponentVectorFunction.

        Schema name: ComponentVectorFunction  # noqa: E501

        :param type: The type of this ComponentVectorFunction.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def x(self):
        """Gets the x of this ComponentVectorFunction.  # noqa: E501


        :return: The x of this ComponentVectorFunction.  # noqa: E501
        :rtype: OneOfComponentVectorFunctionX
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this ComponentVectorFunction.


        :param x: The x of this ComponentVectorFunction.  # noqa: E501
        :type: OneOfComponentVectorFunctionX
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this ComponentVectorFunction.  # noqa: E501


        :return: The y of this ComponentVectorFunction.  # noqa: E501
        :rtype: OneOfComponentVectorFunctionY
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this ComponentVectorFunction.


        :param y: The y of this ComponentVectorFunction.  # noqa: E501
        :type: OneOfComponentVectorFunctionY
        """

        self._y = y

    @property
    def z(self):
        """Gets the z of this ComponentVectorFunction.  # noqa: E501


        :return: The z of this ComponentVectorFunction.  # noqa: E501
        :rtype: OneOfComponentVectorFunctionZ
        """
        return self._z

    @z.setter
    def z(self, z):
        """Sets the z of this ComponentVectorFunction.


        :param z: The z of this ComponentVectorFunction.  # noqa: E501
        :type: OneOfComponentVectorFunctionZ
        """

        self._z = z

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
        if not isinstance(other, ComponentVectorFunction):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ComponentVectorFunction):
            return True

        return self.to_dict() != other.to_dict()
