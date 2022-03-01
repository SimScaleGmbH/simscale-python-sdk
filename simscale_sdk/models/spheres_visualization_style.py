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


class SpheresVisualizationStyle(object):
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
        'representation': 'str',
        'num_pulses': 'int'
    }

    attribute_map = {
        'representation': 'representation',
        'num_pulses': 'numPulses'
    }

    def __init__(self, representation='SPHERES', num_pulses=15, local_vars_configuration=None):  # noqa: E501
        """SpheresVisualizationStyle - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._representation = None
        self._num_pulses = None
        self.discriminator = None

        self.representation = representation
        self.num_pulses = num_pulses

    @property
    def representation(self):
        """Gets the representation of this SpheresVisualizationStyle.  # noqa: E501

        The representation to use for particle traces.  # noqa: E501

        :return: The representation of this SpheresVisualizationStyle.  # noqa: E501
        :rtype: str
        """
        return self._representation

    @representation.setter
    def representation(self, representation):
        """Sets the representation of this SpheresVisualizationStyle.

        The representation to use for particle traces.  # noqa: E501

        :param representation: The representation of this SpheresVisualizationStyle.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and representation is None:  # noqa: E501
            raise ValueError("Invalid value for `representation`, must not be `None`")  # noqa: E501

        self._representation = representation

    @property
    def num_pulses(self):
        """Gets the num_pulses of this SpheresVisualizationStyle.  # noqa: E501

        This value specifies how many pulses there should be in the model.  # noqa: E501

        :return: The num_pulses of this SpheresVisualizationStyle.  # noqa: E501
        :rtype: int
        """
        return self._num_pulses

    @num_pulses.setter
    def num_pulses(self, num_pulses):
        """Sets the num_pulses of this SpheresVisualizationStyle.

        This value specifies how many pulses there should be in the model.  # noqa: E501

        :param num_pulses: The num_pulses of this SpheresVisualizationStyle.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and num_pulses is None:  # noqa: E501
            raise ValueError("Invalid value for `num_pulses`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                num_pulses is not None and num_pulses > 200):  # noqa: E501
            raise ValueError("Invalid value for `num_pulses`, must be a value less than or equal to `200`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                num_pulses is not None and num_pulses < 5):  # noqa: E501
            raise ValueError("Invalid value for `num_pulses`, must be a value greater than or equal to `5`")  # noqa: E501

        self._num_pulses = num_pulses

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
        if not isinstance(other, SpheresVisualizationStyle):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SpheresVisualizationStyle):
            return True

        return self.to_dict() != other.to_dict()