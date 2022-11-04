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


class OneOfPenaltyMethodContactStiffness(object):
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
        'penalty_coefficient': 'float'
    }

    attribute_map = {
        'type': 'type',
        'penalty_coefficient': 'penaltyCoefficient'
    }

    discriminator_value_class_map = {
        'LOW_CONTACT_STIFFNESS': 'LowContactStiffness',
        'MODERATE_CONTACT_STIFFNESS': 'ModerateContactStiffness',
        'HIGH_CONTACT_STIFFNESS': 'HighContactStiffness',
        'CUSTOM_CONTACT_STIFFNESS': 'CustomContactStiffness'
    }

    def __init__(self, type='CUSTOM_CONTACT_STIFFNESS', penalty_coefficient=None, local_vars_configuration=None):  # noqa: E501
        """OneOfPenaltyMethodContactStiffness - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._penalty_coefficient = None
        self.discriminator = 'type'

        self.type = type
        if penalty_coefficient is not None:
            self.penalty_coefficient = penalty_coefficient

    @property
    def type(self):
        """Gets the type of this OneOfPenaltyMethodContactStiffness.  # noqa: E501

        Schema name: CustomContactStiffness  # noqa: E501

        :return: The type of this OneOfPenaltyMethodContactStiffness.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfPenaltyMethodContactStiffness.

        Schema name: CustomContactStiffness  # noqa: E501

        :param type: The type of this OneOfPenaltyMethodContactStiffness.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def penalty_coefficient(self):
        """Gets the penalty_coefficient of this OneOfPenaltyMethodContactStiffness.  # noqa: E501

        <p>Define the penalty coefficient for the contact pair. As a good starting point this value should be about 5-50 times as high as the softest of the materials in this contact definition and below 1e16. A higher value reduces interpenetration but may also lead to numerical instabilities and divergence. The independence of the results from this parameter should be checked.</p>  # noqa: E501

        :return: The penalty_coefficient of this OneOfPenaltyMethodContactStiffness.  # noqa: E501
        :rtype: float
        """
        return self._penalty_coefficient

    @penalty_coefficient.setter
    def penalty_coefficient(self, penalty_coefficient):
        """Sets the penalty_coefficient of this OneOfPenaltyMethodContactStiffness.

        <p>Define the penalty coefficient for the contact pair. As a good starting point this value should be about 5-50 times as high as the softest of the materials in this contact definition and below 1e16. A higher value reduces interpenetration but may also lead to numerical instabilities and divergence. The independence of the results from this parameter should be checked.</p>  # noqa: E501

        :param penalty_coefficient: The penalty_coefficient of this OneOfPenaltyMethodContactStiffness.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                penalty_coefficient is not None and penalty_coefficient > 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):  # noqa: E501
            raise ValueError("Invalid value for `penalty_coefficient`, must be a value less than or equal to `100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                penalty_coefficient is not None and penalty_coefficient < 0):  # noqa: E501
            raise ValueError("Invalid value for `penalty_coefficient`, must be a value greater than or equal to `0`")  # noqa: E501

        self._penalty_coefficient = penalty_coefficient

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
        if not isinstance(other, OneOfPenaltyMethodContactStiffness):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfPenaltyMethodContactStiffness):
            return True

        return self.to_dict() != other.to_dict()
