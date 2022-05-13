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


class OneOfPacefishAutomeshReynoldsScalingType(object):
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
        'reynolds_scaling_factor': 'float'
    }

    attribute_map = {
        'type': 'type',
        'reynolds_scaling_factor': 'reynoldsScalingFactor'
    }

    discriminator_value_class_map = {
        'AUTOMATIC_REYNOLDS_SCALING': 'AutomaticReynoldsScaling',
        'MANUAL_REYNOLDS_SCALING': 'ManualReynoldsScaling'
    }

    def __init__(self, type='MANUAL_REYNOLDS_SCALING', reynolds_scaling_factor=None, local_vars_configuration=None):  # noqa: E501
        """OneOfPacefishAutomeshReynoldsScalingType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._reynolds_scaling_factor = None
        self.discriminator = 'type'

        self.type = type
        if reynolds_scaling_factor is not None:
            self.reynolds_scaling_factor = reynolds_scaling_factor

    @property
    def type(self):
        """Gets the type of this OneOfPacefishAutomeshReynoldsScalingType.  # noqa: E501

        Schema name: ManualReynoldsScaling  # noqa: E501

        :return: The type of this OneOfPacefishAutomeshReynoldsScalingType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfPacefishAutomeshReynoldsScalingType.

        Schema name: ManualReynoldsScaling  # noqa: E501

        :param type: The type of this OneOfPacefishAutomeshReynoldsScalingType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def reynolds_scaling_factor(self):
        """Gets the reynolds_scaling_factor of this OneOfPacefishAutomeshReynoldsScalingType.  # noqa: E501


        :return: The reynolds_scaling_factor of this OneOfPacefishAutomeshReynoldsScalingType.  # noqa: E501
        :rtype: float
        """
        return self._reynolds_scaling_factor

    @reynolds_scaling_factor.setter
    def reynolds_scaling_factor(self, reynolds_scaling_factor):
        """Sets the reynolds_scaling_factor of this OneOfPacefishAutomeshReynoldsScalingType.


        :param reynolds_scaling_factor: The reynolds_scaling_factor of this OneOfPacefishAutomeshReynoldsScalingType.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                reynolds_scaling_factor is not None and reynolds_scaling_factor > 1):  # noqa: E501
            raise ValueError("Invalid value for `reynolds_scaling_factor`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                reynolds_scaling_factor is not None and reynolds_scaling_factor < 0.001):  # noqa: E501
            raise ValueError("Invalid value for `reynolds_scaling_factor`, must be a value greater than or equal to `0.001`")  # noqa: E501

        self._reynolds_scaling_factor = reynolds_scaling_factor

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
        if not isinstance(other, OneOfPacefishAutomeshReynoldsScalingType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfPacefishAutomeshReynoldsScalingType):
            return True

        return self.to_dict() != other.to_dict()
