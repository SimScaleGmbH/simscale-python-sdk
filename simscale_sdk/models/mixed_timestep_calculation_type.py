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


class MixedTimestepCalculationType(object):
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
        'fixed_subdivision': 'FixedSubdivision',
        'adaptive_augmentation': 'AdaptiveAugmentation'
    }

    attribute_map = {
        'type': 'type',
        'fixed_subdivision': 'fixedSubdivision',
        'adaptive_augmentation': 'adaptiveAugmentation'
    }

    def __init__(self, type='MIXED', fixed_subdivision=None, adaptive_augmentation=None, local_vars_configuration=None):  # noqa: E501
        """MixedTimestepCalculationType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._fixed_subdivision = None
        self._adaptive_augmentation = None
        self.discriminator = None

        self.type = type
        if fixed_subdivision is not None:
            self.fixed_subdivision = fixed_subdivision
        if adaptive_augmentation is not None:
            self.adaptive_augmentation = adaptive_augmentation

    @property
    def type(self):
        """Gets the type of this MixedTimestepCalculationType.  # noqa: E501


        :return: The type of this MixedTimestepCalculationType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this MixedTimestepCalculationType.


        :param type: The type of this MixedTimestepCalculationType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def fixed_subdivision(self):
        """Gets the fixed_subdivision of this MixedTimestepCalculationType.  # noqa: E501


        :return: The fixed_subdivision of this MixedTimestepCalculationType.  # noqa: E501
        :rtype: FixedSubdivision
        """
        return self._fixed_subdivision

    @fixed_subdivision.setter
    def fixed_subdivision(self, fixed_subdivision):
        """Sets the fixed_subdivision of this MixedTimestepCalculationType.


        :param fixed_subdivision: The fixed_subdivision of this MixedTimestepCalculationType.  # noqa: E501
        :type: FixedSubdivision
        """

        self._fixed_subdivision = fixed_subdivision

    @property
    def adaptive_augmentation(self):
        """Gets the adaptive_augmentation of this MixedTimestepCalculationType.  # noqa: E501


        :return: The adaptive_augmentation of this MixedTimestepCalculationType.  # noqa: E501
        :rtype: AdaptiveAugmentation
        """
        return self._adaptive_augmentation

    @adaptive_augmentation.setter
    def adaptive_augmentation(self, adaptive_augmentation):
        """Sets the adaptive_augmentation of this MixedTimestepCalculationType.


        :param adaptive_augmentation: The adaptive_augmentation of this MixedTimestepCalculationType.  # noqa: E501
        :type: AdaptiveAugmentation
        """

        self._adaptive_augmentation = adaptive_augmentation

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
        if not isinstance(other, MixedTimestepCalculationType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MixedTimestepCalculationType):
            return True

        return self.to_dict() != other.to_dict()
