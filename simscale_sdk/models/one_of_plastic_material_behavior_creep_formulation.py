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


class OneOfPlasticMaterialBehaviorCreepFormulation(object):
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
        'n': 'float',
        'm': 'float',
        's': 'float'
    }

    attribute_map = {
        'type': 'type',
        'a': 'a',
        'n': 'n',
        'm': 'm',
        's': 's'
    }

    discriminator_value_class_map = {
        'NORTON': 'NortonCreepFormulation',
        'NO_CREEP': 'NoCreepFormulation',
        'STRAIN_HARDENING': 'StrainHardeningCreepFormulation',
        'TIME_HARDENING': 'TimeHardeningCreepFormulation',
        'GAROFALO': 'GarofaloCreepFormulation'
    }

    def __init__(self, type='GAROFALO', a=None, n=None, m=None, s=None, local_vars_configuration=None):  # noqa: E501
        """OneOfPlasticMaterialBehaviorCreepFormulation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._a = None
        self._n = None
        self._m = None
        self._s = None
        self.discriminator = 'type'

        self.type = type
        if a is not None:
            self.a = a
        if n is not None:
            self.n = n
        if m is not None:
            self.m = m
        if s is not None:
            self.s = s

    @property
    def type(self):
        """Gets the type of this OneOfPlasticMaterialBehaviorCreepFormulation.  # noqa: E501


        :return: The type of this OneOfPlasticMaterialBehaviorCreepFormulation.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfPlasticMaterialBehaviorCreepFormulation.


        :param type: The type of this OneOfPlasticMaterialBehaviorCreepFormulation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def a(self):
        """Gets the a of this OneOfPlasticMaterialBehaviorCreepFormulation.  # noqa: E501


        :return: The a of this OneOfPlasticMaterialBehaviorCreepFormulation.  # noqa: E501
        :rtype: DimensionalStrainRate
        """
        return self._a

    @a.setter
    def a(self, a):
        """Sets the a of this OneOfPlasticMaterialBehaviorCreepFormulation.


        :param a: The a of this OneOfPlasticMaterialBehaviorCreepFormulation.  # noqa: E501
        :type: DimensionalStrainRate
        """

        self._a = a

    @property
    def n(self):
        """Gets the n of this OneOfPlasticMaterialBehaviorCreepFormulation.  # noqa: E501

        <p>Define the parameter <b>&sigma;<sub>0</sub></b> of the Garofalo creep formulation: <ul><b>&epsilon;&#775; = &epsilon;<sub>0</sub>* &sinh(&sigma;/(&sigma<sub>0</sub>))<sup>n</sup></b></ul></p>  # noqa: E501

        :return: The n of this OneOfPlasticMaterialBehaviorCreepFormulation.  # noqa: E501
        :rtype: float
        """
        return self._n

    @n.setter
    def n(self, n):
        """Sets the n of this OneOfPlasticMaterialBehaviorCreepFormulation.

        <p>Define the parameter <b>&sigma;<sub>0</sub></b> of the Garofalo creep formulation: <ul><b>&epsilon;&#775; = &epsilon;<sub>0</sub>* &sinh(&sigma;/(&sigma<sub>0</sub>))<sup>n</sup></b></ul></p>  # noqa: E501

        :param n: The n of this OneOfPlasticMaterialBehaviorCreepFormulation.  # noqa: E501
        :type: float
        """

        self._n = n

    @property
    def m(self):
        """Gets the m of this OneOfPlasticMaterialBehaviorCreepFormulation.  # noqa: E501

        <p>Define the parameter <b>m</b> of the Time Hardening creep formulation: <ul><b>&epsilon;&#775; = A*&sigma;<sup>n</sup>*t<sup>m</sup></b></ul></p>  # noqa: E501

        :return: The m of this OneOfPlasticMaterialBehaviorCreepFormulation.  # noqa: E501
        :rtype: float
        """
        return self._m

    @m.setter
    def m(self, m):
        """Sets the m of this OneOfPlasticMaterialBehaviorCreepFormulation.

        <p>Define the parameter <b>m</b> of the Time Hardening creep formulation: <ul><b>&epsilon;&#775; = A*&sigma;<sup>n</sup>*t<sup>m</sup></b></ul></p>  # noqa: E501

        :param m: The m of this OneOfPlasticMaterialBehaviorCreepFormulation.  # noqa: E501
        :type: float
        """

        self._m = m

    @property
    def s(self):
        """Gets the s of this OneOfPlasticMaterialBehaviorCreepFormulation.  # noqa: E501

        <p>Define the parameter <b>&epsilon;<sub>0</sub></b> of the Garofalo creep formulation: <ul><b>&epsilon;&#775; = &epsilon;<sub>0</sub>* &sinh(&sigma;/(&sigma<sub>0</sub>))<sup>n</sup></b></ul></p>  # noqa: E501

        :return: The s of this OneOfPlasticMaterialBehaviorCreepFormulation.  # noqa: E501
        :rtype: float
        """
        return self._s

    @s.setter
    def s(self, s):
        """Sets the s of this OneOfPlasticMaterialBehaviorCreepFormulation.

        <p>Define the parameter <b>&epsilon;<sub>0</sub></b> of the Garofalo creep formulation: <ul><b>&epsilon;&#775; = &epsilon;<sub>0</sub>* &sinh(&sigma;/(&sigma<sub>0</sub>))<sup>n</sup></b></ul></p>  # noqa: E501

        :param s: The s of this OneOfPlasticMaterialBehaviorCreepFormulation.  # noqa: E501
        :type: float
        """

        self._s = s

    def get_real_child_model(self, data):
        """Returns the real base class specified by the discriminator"""
        discriminator_key = self.attribute_map[self.discriminator]
        discriminator_value = data[discriminator_key]
        return self.discriminator_value_class_map.get(discriminator_value)

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
        if not isinstance(other, OneOfPlasticMaterialBehaviorCreepFormulation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfPlasticMaterialBehaviorCreepFormulation):
            return True

        return self.to_dict() != other.to_dict()
