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


class DistanceVolumeCustomSizing(object):
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
        'distance_sizing_values': 'list[DistanceSizing]',
        'curvature': 'OneOfDistanceVolumeCustomSizingCurvature'
    }

    attribute_map = {
        'type': 'type',
        'distance_sizing_values': 'distanceSizingValues',
        'curvature': 'curvature'
    }

    def __init__(self, type='DISTANCE_CUSTOM_SIZING', distance_sizing_values=None, curvature=None, local_vars_configuration=None):  # noqa: E501
        """DistanceVolumeCustomSizing - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._distance_sizing_values = None
        self._curvature = None
        self.discriminator = None

        self.type = type
        if distance_sizing_values is not None:
            self.distance_sizing_values = distance_sizing_values
        if curvature is not None:
            self.curvature = curvature

    @property
    def type(self):
        """Gets the type of this DistanceVolumeCustomSizing.  # noqa: E501

        Schema name: DistanceVolumeCustomSizing  # noqa: E501

        :return: The type of this DistanceVolumeCustomSizing.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this DistanceVolumeCustomSizing.

        Schema name: DistanceVolumeCustomSizing  # noqa: E501

        :param type: The type of this DistanceVolumeCustomSizing.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def distance_sizing_values(self):
        """Gets the distance_sizing_values of this DistanceVolumeCustomSizing.  # noqa: E501

        Define the desired cell size based on the distance to the surface of the assigned volumes. The distances need to be specified in <u>increasing order</u>, while the sizes must be in <u>decreasing order</u>. When the distance is 0, the corresponding size is applied inside the specified volumes.  # noqa: E501

        :return: The distance_sizing_values of this DistanceVolumeCustomSizing.  # noqa: E501
        :rtype: list[DistanceSizing]
        """
        return self._distance_sizing_values

    @distance_sizing_values.setter
    def distance_sizing_values(self, distance_sizing_values):
        """Sets the distance_sizing_values of this DistanceVolumeCustomSizing.

        Define the desired cell size based on the distance to the surface of the assigned volumes. The distances need to be specified in <u>increasing order</u>, while the sizes must be in <u>decreasing order</u>. When the distance is 0, the corresponding size is applied inside the specified volumes.  # noqa: E501

        :param distance_sizing_values: The distance_sizing_values of this DistanceVolumeCustomSizing.  # noqa: E501
        :type: list[DistanceSizing]
        """

        self._distance_sizing_values = distance_sizing_values

    @property
    def curvature(self):
        """Gets the curvature of this DistanceVolumeCustomSizing.  # noqa: E501


        :return: The curvature of this DistanceVolumeCustomSizing.  # noqa: E501
        :rtype: OneOfDistanceVolumeCustomSizingCurvature
        """
        return self._curvature

    @curvature.setter
    def curvature(self, curvature):
        """Sets the curvature of this DistanceVolumeCustomSizing.


        :param curvature: The curvature of this DistanceVolumeCustomSizing.  # noqa: E501
        :type: OneOfDistanceVolumeCustomSizingCurvature
        """

        self._curvature = curvature

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
        if not isinstance(other, DistanceVolumeCustomSizing):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, DistanceVolumeCustomSizing):
            return True

        return self.to_dict() != other.to_dict()
