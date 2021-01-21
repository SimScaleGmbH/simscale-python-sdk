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


class ThetaTimeIntegrationScheme(object):
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
        'theta': 'float'
    }

    attribute_map = {
        'type': 'type',
        'theta': 'theta'
    }

    def __init__(self, type='THETA_METHOD', theta=None, local_vars_configuration=None):  # noqa: E501
        """ThetaTimeIntegrationScheme - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._theta = None
        self.discriminator = None

        self.type = type
        if theta is not None:
            self.theta = theta

    @property
    def type(self):
        """Gets the type of this ThetaTimeIntegrationScheme.  # noqa: E501


        :return: The type of this ThetaTimeIntegrationScheme.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ThetaTimeIntegrationScheme.


        :param type: The type of this ThetaTimeIntegrationScheme.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def theta(self):
        """Gets the theta of this ThetaTimeIntegrationScheme.  # noqa: E501

        The parameter <b>&theta;</b> must be ranging between 0.5 and 1.0: 0.5 corresponds to a minimum, 1.0 to a maximum of numerical dissipation. The selection of <b>&theta;</b> = 1.0 leads to the <b>Euler scheme</b>, whereas <b>&theta;</b> = 0.5 leads to the <i>Crank-Nicolson</i> scheme of order 2.  # noqa: E501

        :return: The theta of this ThetaTimeIntegrationScheme.  # noqa: E501
        :rtype: float
        """
        return self._theta

    @theta.setter
    def theta(self, theta):
        """Sets the theta of this ThetaTimeIntegrationScheme.

        The parameter <b>&theta;</b> must be ranging between 0.5 and 1.0: 0.5 corresponds to a minimum, 1.0 to a maximum of numerical dissipation. The selection of <b>&theta;</b> = 1.0 leads to the <b>Euler scheme</b>, whereas <b>&theta;</b> = 0.5 leads to the <i>Crank-Nicolson</i> scheme of order 2.  # noqa: E501

        :param theta: The theta of this ThetaTimeIntegrationScheme.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                theta is not None and theta > 1):  # noqa: E501
            raise ValueError("Invalid value for `theta`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                theta is not None and theta < 0.5):  # noqa: E501
            raise ValueError("Invalid value for `theta`, must be a value greater than or equal to `0.5`")  # noqa: E501

        self._theta = theta

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
        if not isinstance(other, ThetaTimeIntegrationScheme):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ThetaTimeIntegrationScheme):
            return True

        return self.to_dict() != other.to_dict()
