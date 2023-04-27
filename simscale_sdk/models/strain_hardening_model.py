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


class StrainHardeningModel(object):
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
        'yield_stress': 'DimensionalFunctionPressure',
        'ultimate_stress': 'DimensionalFunctionPressure',
        'ultimate_strain': 'ConstantFunction'
    }

    attribute_map = {
        'type': 'type',
        'yield_stress': 'yieldStress',
        'ultimate_stress': 'ultimateStress',
        'ultimate_strain': 'ultimateStrain'
    }

    def __init__(self, type='STRAIN_HARDENING', yield_stress=None, ultimate_stress=None, ultimate_strain=None, local_vars_configuration=None):  # noqa: E501
        """StrainHardeningModel - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._yield_stress = None
        self._ultimate_stress = None
        self._ultimate_strain = None
        self.discriminator = None

        self.type = type
        if yield_stress is not None:
            self.yield_stress = yield_stress
        if ultimate_stress is not None:
            self.ultimate_stress = ultimate_stress
        if ultimate_strain is not None:
            self.ultimate_strain = ultimate_strain

    @property
    def type(self):
        """Gets the type of this StrainHardeningModel.  # noqa: E501

        Choose the material behavior for your problem. </p> <br /><br />Important remarks:<br /> <ul><li>Choose <b>Strain Hardening</b> if the material response is a combination of linear elastic behavior and plastic hardening behavior, where the material becomes progressively stiffer with increasing strain.</li><li>Choose <b>Perfect Plasticity</b> if the material response is a combination of linear elastic and perfect plastic hardening behavior (constant stress for applied strain).</li></ul>  Schema name: StrainHardeningModel  # noqa: E501

        :return: The type of this StrainHardeningModel.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this StrainHardeningModel.

        Choose the material behavior for your problem. </p> <br /><br />Important remarks:<br /> <ul><li>Choose <b>Strain Hardening</b> if the material response is a combination of linear elastic behavior and plastic hardening behavior, where the material becomes progressively stiffer with increasing strain.</li><li>Choose <b>Perfect Plasticity</b> if the material response is a combination of linear elastic and perfect plastic hardening behavior (constant stress for applied strain).</li></ul>  Schema name: StrainHardeningModel  # noqa: E501

        :param type: The type of this StrainHardeningModel.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def yield_stress(self):
        """Gets the yield_stress of this StrainHardeningModel.  # noqa: E501


        :return: The yield_stress of this StrainHardeningModel.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._yield_stress

    @yield_stress.setter
    def yield_stress(self, yield_stress):
        """Sets the yield_stress of this StrainHardeningModel.


        :param yield_stress: The yield_stress of this StrainHardeningModel.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._yield_stress = yield_stress

    @property
    def ultimate_stress(self):
        """Gets the ultimate_stress of this StrainHardeningModel.  # noqa: E501


        :return: The ultimate_stress of this StrainHardeningModel.  # noqa: E501
        :rtype: DimensionalFunctionPressure
        """
        return self._ultimate_stress

    @ultimate_stress.setter
    def ultimate_stress(self, ultimate_stress):
        """Sets the ultimate_stress of this StrainHardeningModel.


        :param ultimate_stress: The ultimate_stress of this StrainHardeningModel.  # noqa: E501
        :type: DimensionalFunctionPressure
        """

        self._ultimate_stress = ultimate_stress

    @property
    def ultimate_strain(self):
        """Gets the ultimate_strain of this StrainHardeningModel.  # noqa: E501


        :return: The ultimate_strain of this StrainHardeningModel.  # noqa: E501
        :rtype: ConstantFunction
        """
        return self._ultimate_strain

    @ultimate_strain.setter
    def ultimate_strain(self, ultimate_strain):
        """Sets the ultimate_strain of this StrainHardeningModel.


        :param ultimate_strain: The ultimate_strain of this StrainHardeningModel.  # noqa: E501
        :type: ConstantFunction
        """

        self._ultimate_strain = ultimate_strain

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
        if not isinstance(other, StrainHardeningModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, StrainHardeningModel):
            return True

        return self.to_dict() != other.to_dict()
