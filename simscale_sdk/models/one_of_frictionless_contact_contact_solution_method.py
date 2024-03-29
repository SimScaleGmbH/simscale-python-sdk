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


class OneOfFrictionlessContactContactSolutionMethod(object):
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
        'augmented_lagrange_coefficient': 'float',
        'contact_stiffness': 'OneOfPenaltyMethodContactStiffness'
    }

    attribute_map = {
        'type': 'type',
        'augmented_lagrange_coefficient': 'augmentedLagrangeCoefficient',
        'contact_stiffness': 'contactStiffness'
    }

    discriminator_value_class_map = {
        'AUGMENTED_LAGRANGE': 'AugmentedLagrangeMethod',
        'PENALTY_METHOD': 'PenaltyMethod'
    }

    def __init__(self, type='PENALTY_METHOD', augmented_lagrange_coefficient=None, contact_stiffness=None, local_vars_configuration=None):  # noqa: E501
        """OneOfFrictionlessContactContactSolutionMethod - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._augmented_lagrange_coefficient = None
        self._contact_stiffness = None
        self.discriminator = 'type'

        self.type = type
        if augmented_lagrange_coefficient is not None:
            self.augmented_lagrange_coefficient = augmented_lagrange_coefficient
        if contact_stiffness is not None:
            self.contact_stiffness = contact_stiffness

    @property
    def type(self):
        """Gets the type of this OneOfFrictionlessContactContactSolutionMethod.  # noqa: E501

        Schema name: PenaltyMethod  # noqa: E501

        :return: The type of this OneOfFrictionlessContactContactSolutionMethod.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfFrictionlessContactContactSolutionMethod.

        Schema name: PenaltyMethod  # noqa: E501

        :param type: The type of this OneOfFrictionlessContactContactSolutionMethod.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def augmented_lagrange_coefficient(self):
        """Gets the augmented_lagrange_coefficient of this OneOfFrictionlessContactContactSolutionMethod.  # noqa: E501


        :return: The augmented_lagrange_coefficient of this OneOfFrictionlessContactContactSolutionMethod.  # noqa: E501
        :rtype: float
        """
        return self._augmented_lagrange_coefficient

    @augmented_lagrange_coefficient.setter
    def augmented_lagrange_coefficient(self, augmented_lagrange_coefficient):
        """Sets the augmented_lagrange_coefficient of this OneOfFrictionlessContactContactSolutionMethod.


        :param augmented_lagrange_coefficient: The augmented_lagrange_coefficient of this OneOfFrictionlessContactContactSolutionMethod.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                augmented_lagrange_coefficient is not None and augmented_lagrange_coefficient > 100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000):  # noqa: E501
            raise ValueError("Invalid value for `augmented_lagrange_coefficient`, must be a value less than or equal to `100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                augmented_lagrange_coefficient is not None and augmented_lagrange_coefficient < 0):  # noqa: E501
            raise ValueError("Invalid value for `augmented_lagrange_coefficient`, must be a value greater than or equal to `0`")  # noqa: E501

        self._augmented_lagrange_coefficient = augmented_lagrange_coefficient

    @property
    def contact_stiffness(self):
        """Gets the contact_stiffness of this OneOfFrictionlessContactContactSolutionMethod.  # noqa: E501


        :return: The contact_stiffness of this OneOfFrictionlessContactContactSolutionMethod.  # noqa: E501
        :rtype: OneOfPenaltyMethodContactStiffness
        """
        return self._contact_stiffness

    @contact_stiffness.setter
    def contact_stiffness(self, contact_stiffness):
        """Sets the contact_stiffness of this OneOfFrictionlessContactContactSolutionMethod.


        :param contact_stiffness: The contact_stiffness of this OneOfFrictionlessContactContactSolutionMethod.  # noqa: E501
        :type: OneOfPenaltyMethodContactStiffness
        """

        self._contact_stiffness = contact_stiffness

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
        if not isinstance(other, OneOfFrictionlessContactContactSolutionMethod):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfFrictionlessContactContactSolutionMethod):
            return True

        return self.to_dict() != other.to_dict()
