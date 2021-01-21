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


class NortonCreepFormulation(object):
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
        'a': 'DimensionalStrainRate',
        'n': 'float'
    }

    attribute_map = {
        'type': 'type',
        'a': 'a',
        'n': 'n'
    }

    def __init__(self, type='NORTON', a=None, n=None, local_vars_configuration=None):  # noqa: E501
        """NortonCreepFormulation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._a = None
        self._n = None
        self.discriminator = None

        self.type = type
        if a is not None:
            self.a = a
        if n is not None:
            self.n = n

    @property
    def type(self):
        """Gets the type of this NortonCreepFormulation.  # noqa: E501


        :return: The type of this NortonCreepFormulation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this NortonCreepFormulation.


        :param type: The type of this NortonCreepFormulation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def a(self):
        """Gets the a of this NortonCreepFormulation.  # noqa: E501


        :return: The a of this NortonCreepFormulation.  # noqa: E501
        :rtype: DimensionalStrainRate
        """
        return self._a

    @a.setter
    def a(self, a):
        """Sets the a of this NortonCreepFormulation.


        :param a: The a of this NortonCreepFormulation.  # noqa: E501
        :type: DimensionalStrainRate
        """

        self._a = a

    @property
    def n(self):
        """Gets the n of this NortonCreepFormulation.  # noqa: E501

        <p>Define the parameter <b>n</b> of the Norton creep formulation: <ul><b>&epsilon;&#775; = A*&sigma;<sup>n</sup></b></ul></p>  # noqa: E501

        :return: The n of this NortonCreepFormulation.  # noqa: E501
        :rtype: float
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this NortonCreepFormulation.

        <p>Define the parameter <b>n</b> of the Norton creep formulation: <ul><b>&epsilon;&#775; = A*&sigma;<sup>n</sup></b></ul></p>  # noqa: E501

        :param n: The n of this NortonCreepFormulation.  # noqa: E501
        :type: float
        """

        self._n = n

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
        if not isinstance(other, NortonCreepFormulation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, NortonCreepFormulation):
            return True

        return self.to_dict() != other.to_dict()
