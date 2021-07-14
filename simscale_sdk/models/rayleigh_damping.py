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


class RayleighDamping(object):
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
        'stiffness_proportional_coefficient': 'DimensionalTime',
        'mass_proportional_coefficient': 'DimensionalFrequency'
    }

    attribute_map = {
        'type': 'type',
        'stiffness_proportional_coefficient': 'stiffnessProportionalCoefficient',
        'mass_proportional_coefficient': 'massProportionalCoefficient'
    }

    def __init__(self, type='RAYLEIGH', stiffness_proportional_coefficient=None, mass_proportional_coefficient=None, local_vars_configuration=None):  # noqa: E501
        """RayleighDamping - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._stiffness_proportional_coefficient = None
        self._mass_proportional_coefficient = None
        self.discriminator = None

        self.type = type
        if stiffness_proportional_coefficient is not None:
            self.stiffness_proportional_coefficient = stiffness_proportional_coefficient
        if mass_proportional_coefficient is not None:
            self.mass_proportional_coefficient = mass_proportional_coefficient

    @property
    def type(self):
        """Gets the type of this RayleighDamping.  # noqa: E501

        <p>Choose if damping effects should be considered. The supported damping types are:<ul><li><p><b>Rayleigh Damping</b> which is also known as <i>proportional viscous damping</i>. This model assumes that the damping is proportional to the vibrating velocity.</p></ul><ul><li><p><b>Hysteretic Damping</b>, also known as <i>structural damping</i>. Here the damping is assumed to be proportional to the displacement.</p></ul><br><a href= https://www.simscale.com/docs/simulation-setup/materials/damping/' target='_blank'>Learn more</a>.   Schema name: RayleighDamping  # noqa: E501

        :return: The type of this RayleighDamping.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this RayleighDamping.

        <p>Choose if damping effects should be considered. The supported damping types are:<ul><li><p><b>Rayleigh Damping</b> which is also known as <i>proportional viscous damping</i>. This model assumes that the damping is proportional to the vibrating velocity.</p></ul><ul><li><p><b>Hysteretic Damping</b>, also known as <i>structural damping</i>. Here the damping is assumed to be proportional to the displacement.</p></ul><br><a href= https://www.simscale.com/docs/simulation-setup/materials/damping/' target='_blank'>Learn more</a>.   Schema name: RayleighDamping  # noqa: E501

        :param type: The type of this RayleighDamping.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def stiffness_proportional_coefficient(self):
        """Gets the stiffness_proportional_coefficient of this RayleighDamping.  # noqa: E501


        :return: The stiffness_proportional_coefficient of this RayleighDamping.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._stiffness_proportional_coefficient

    @stiffness_proportional_coefficient.setter
    def stiffness_proportional_coefficient(self, stiffness_proportional_coefficient):
        """Sets the stiffness_proportional_coefficient of this RayleighDamping.


        :param stiffness_proportional_coefficient: The stiffness_proportional_coefficient of this RayleighDamping.  # noqa: E501
        :type: DimensionalTime
        """

        self._stiffness_proportional_coefficient = stiffness_proportional_coefficient

    @property
    def mass_proportional_coefficient(self):
        """Gets the mass_proportional_coefficient of this RayleighDamping.  # noqa: E501


        :return: The mass_proportional_coefficient of this RayleighDamping.  # noqa: E501
        :rtype: DimensionalFrequency
        """
        return self._mass_proportional_coefficient

    @mass_proportional_coefficient.setter
    def mass_proportional_coefficient(self, mass_proportional_coefficient):
        """Sets the mass_proportional_coefficient of this RayleighDamping.


        :param mass_proportional_coefficient: The mass_proportional_coefficient of this RayleighDamping.  # noqa: E501
        :type: DimensionalFrequency
        """

        self._mass_proportional_coefficient = mass_proportional_coefficient

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
        if not isinstance(other, RayleighDamping):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, RayleighDamping):
            return True

        return self.to_dict() != other.to_dict()
