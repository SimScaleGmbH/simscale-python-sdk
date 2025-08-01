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


class OneOfPlasticityMarcPlasticityModel(object):
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
        'yield_stress': 'DimensionalPressure',
        'hardening_model': 'OneOfBilinearModelMarcHardeningModel',
        'hardening_rule': 'OneOfMultilinearModelMarcHardeningRule',
        'stress_strain_curve': 'DimensionalFunctionPressure'
    }

    attribute_map = {
        'type': 'type',
        'yield_stress': 'yieldStress',
        'hardening_model': 'hardeningModel',
        'hardening_rule': 'hardeningRule',
        'stress_strain_curve': 'stressStrainCurve'
    }

    discriminator_value_class_map = {
        'BILINEAR': 'BilinearModelMarc',
        'MULTILINEAR': 'MultilinearModelMarc'
    }

    def __init__(self, type='MULTILINEAR', yield_stress=None, hardening_model=None, hardening_rule=None, stress_strain_curve=None, local_vars_configuration=None):  # noqa: E501
        """OneOfPlasticityMarcPlasticityModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._yield_stress = None
        self._hardening_model = None
        self._hardening_rule = None
        self._stress_strain_curve = None
        self.discriminator = 'type'

        self.type = type
        if yield_stress is not None:
            self.yield_stress = yield_stress
        if hardening_model is not None:
            self.hardening_model = hardening_model
        if hardening_rule is not None:
            self.hardening_rule = hardening_rule
        if stress_strain_curve is not None:
            self.stress_strain_curve = stress_strain_curve

    @property
    def type(self):
        """Gets the type of this OneOfPlasticityMarcPlasticityModel.  # noqa: E501

        Schema name: MultilinearModelMarc  # noqa: E501

        :return: The type of this OneOfPlasticityMarcPlasticityModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfPlasticityMarcPlasticityModel.

        Schema name: MultilinearModelMarc  # noqa: E501

        :param type: The type of this OneOfPlasticityMarcPlasticityModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def yield_stress(self):
        """Gets the yield_stress of this OneOfPlasticityMarcPlasticityModel.  # noqa: E501


        :return: The yield_stress of this OneOfPlasticityMarcPlasticityModel.  # noqa: E501
        :rtype: DimensionalPressure
        """
        return self._yield_stress

    @yield_stress.setter
    def yield_stress(self, yield_stress):
        """Sets the yield_stress of this OneOfPlasticityMarcPlasticityModel.


        :param yield_stress: The yield_stress of this OneOfPlasticityMarcPlasticityModel.  # noqa: E501
        :type: DimensionalPressure
        """

        self._yield_stress = yield_stress

    @property
    def hardening_model(self):
        """Gets the hardening_model of this OneOfPlasticityMarcPlasticityModel.  # noqa: E501


        :return: The hardening_model of this OneOfPlasticityMarcPlasticityModel.  # noqa: E501
        :rtype: OneOfBilinearModelMarcHardeningModel
        """
        return self._hardening_model

    @hardening_model.setter
    def hardening_model(self, hardening_model):
        """Sets the hardening_model of this OneOfPlasticityMarcPlasticityModel.


        :param hardening_model: The hardening_model of this OneOfPlasticityMarcPlasticityModel.  # noqa: E501
        :type: OneOfBilinearModelMarcHardeningModel
        """

        self._hardening_model = hardening_model

    @property
    def hardening_rule(self):
        """Gets the hardening_rule of this OneOfPlasticityMarcPlasticityModel.  # noqa: E501


        :return: The hardening_rule of this OneOfPlasticityMarcPlasticityModel.  # noqa: E501
        :rtype: OneOfMultilinearModelMarcHardeningRule
        """
        return self._hardening_rule

    @hardening_rule.setter
    def hardening_rule(self, hardening_rule):
        """Sets the hardening_rule of this OneOfPlasticityMarcPlasticityModel.


        :param hardening_rule: The hardening_rule of this OneOfPlasticityMarcPlasticityModel.  # noqa: E501
        :type: OneOfMultilinearModelMarcHardeningRule
        """

        self._hardening_rule = hardening_rule

    @property
    def stress_strain_curve(self):
        """Gets the stress_strain_curve of this OneOfPlasticityMarcPlasticityModel.  # noqa: E501


        :return: The stress_strain_curve of this OneOfPlasticityMarcPlasticityModel.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._stress_strain_curve

    @stress_strain_curve.setter
    def stress_strain_curve(self, stress_strain_curve):
        """Sets the stress_strain_curve of this OneOfPlasticityMarcPlasticityModel.


        :param stress_strain_curve: The stress_strain_curve of this OneOfPlasticityMarcPlasticityModel.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._stress_strain_curve = stress_strain_curve

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
        if not isinstance(other, OneOfPlasticityMarcPlasticityModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfPlasticityMarcPlasticityModel):
            return True

        return self.to_dict() != other.to_dict()
