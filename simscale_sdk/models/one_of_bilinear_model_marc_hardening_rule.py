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


class OneOfBilinearModelMarcHardeningRule(object):
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
        'kinematic_fraction': 'float'
    }

    attribute_map = {
        'type': 'type',
        'kinematic_fraction': 'kinematicFraction'
    }

    discriminator_value_class_map = {
        'ISOTROPIC': 'IsotropicPlasticHardeningMarc',
        'KINEMATIC': 'KinematicPlasticHardeningMarc',
        'COMBINED': 'CombinedPlasticHardeningMarc'
    }

    def __init__(self, type='COMBINED', kinematic_fraction=None, local_vars_configuration=None):  # noqa: E501
        """OneOfBilinearModelMarcHardeningRule - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._kinematic_fraction = None
        self.discriminator = 'type'

        self.type = type
        if kinematic_fraction is not None:
            self.kinematic_fraction = kinematic_fraction

    @property
    def type(self):
        """Gets the type of this OneOfBilinearModelMarcHardeningRule.  # noqa: E501

        Schema name: CombinedPlasticHardeningMarc  # noqa: E501

        :return: The type of this OneOfBilinearModelMarcHardeningRule.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfBilinearModelMarcHardeningRule.

        Schema name: CombinedPlasticHardeningMarc  # noqa: E501

        :param type: The type of this OneOfBilinearModelMarcHardeningRule.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def kinematic_fraction(self):
        """Gets the kinematic_fraction of this OneOfBilinearModelMarcHardeningRule.  # noqa: E501


        :return: The kinematic_fraction of this OneOfBilinearModelMarcHardeningRule.  # noqa: E501
        :rtype: float
        """
        return self._kinematic_fraction

    @kinematic_fraction.setter
    def kinematic_fraction(self, kinematic_fraction):
        """Sets the kinematic_fraction of this OneOfBilinearModelMarcHardeningRule.


        :param kinematic_fraction: The kinematic_fraction of this OneOfBilinearModelMarcHardeningRule.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                kinematic_fraction is not None and kinematic_fraction > 1):  # noqa: E501
            raise ValueError("Invalid value for `kinematic_fraction`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                kinematic_fraction is not None and kinematic_fraction < 0):  # noqa: E501
            raise ValueError("Invalid value for `kinematic_fraction`, must be a value greater than or equal to `0`")  # noqa: E501

        self._kinematic_fraction = kinematic_fraction

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
        if not isinstance(other, OneOfBilinearModelMarcHardeningRule):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfBilinearModelMarcHardeningRule):
            return True

        return self.to_dict() != other.to_dict()
