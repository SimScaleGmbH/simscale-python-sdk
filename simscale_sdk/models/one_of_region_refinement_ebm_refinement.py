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


class OneOfRegionRefinementEBMRefinement(object):
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
        'length': 'DimensionalLength',
        'distance_refinement_lengths': 'list[RefinementLength]'
    }

    attribute_map = {
        'type': 'type',
        'length': 'length',
        'distance_refinement_lengths': 'distanceRefinementLengths'
    }

    discriminator_value_class_map = {
        'INSIDE': 'InsideRegionRefinementWithLength',
        'DISTANCE': 'DistanceRegionRefinementWithLength'
    }

    def __init__(self, type='DISTANCE', length=None, distance_refinement_lengths=None, local_vars_configuration=None):  # noqa: E501
        """OneOfRegionRefinementEBMRefinement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._length = None
        self._distance_refinement_lengths = None
        self.discriminator = 'type'

        self.type = type
        if length is not None:
            self.length = length
        if distance_refinement_lengths is not None:
            self.distance_refinement_lengths = distance_refinement_lengths

    @property
    def type(self):
        """Gets the type of this OneOfRegionRefinementEBMRefinement.  # noqa: E501

        Schema name: DistanceRegionRefinementWithLength  # noqa: E501

        :return: The type of this OneOfRegionRefinementEBMRefinement.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfRegionRefinementEBMRefinement.

        Schema name: DistanceRegionRefinementWithLength  # noqa: E501

        :param type: The type of this OneOfRegionRefinementEBMRefinement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def length(self):
        """Gets the length of this OneOfRegionRefinementEBMRefinement.  # noqa: E501


        :return: The length of this OneOfRegionRefinementEBMRefinement.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._length

    @length.setter
    def length(self, length):
        """Sets the length of this OneOfRegionRefinementEBMRefinement.


        :param length: The length of this OneOfRegionRefinementEBMRefinement.  # noqa: E501
        :type: DimensionalLength
        """

        self._length = length

    @property
    def distance_refinement_lengths(self):
        """Gets the distance_refinement_lengths of this OneOfRegionRefinementEBMRefinement.  # noqa: E501

        Define the desired cell size based on the distance to the surface of the assigned volumes. The distances need to be specified in <u>increasing order</u>, while the sizes must be in <u>decreasing order</u>. When the distance is 0, the corresponding size is applied inside the specified volumes.  # noqa: E501

        :return: The distance_refinement_lengths of this OneOfRegionRefinementEBMRefinement.  # noqa: E501
        :rtype: list[RefinementLength]
        """
        return self._distance_refinement_lengths

    @distance_refinement_lengths.setter
    def distance_refinement_lengths(self, distance_refinement_lengths):
        """Sets the distance_refinement_lengths of this OneOfRegionRefinementEBMRefinement.

        Define the desired cell size based on the distance to the surface of the assigned volumes. The distances need to be specified in <u>increasing order</u>, while the sizes must be in <u>decreasing order</u>. When the distance is 0, the corresponding size is applied inside the specified volumes.  # noqa: E501

        :param distance_refinement_lengths: The distance_refinement_lengths of this OneOfRegionRefinementEBMRefinement.  # noqa: E501
        :type: list[RefinementLength]
        """

        self._distance_refinement_lengths = distance_refinement_lengths

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
        if not isinstance(other, OneOfRegionRefinementEBMRefinement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfRegionRefinementEBMRefinement):
            return True

        return self.to_dict() != other.to_dict()
