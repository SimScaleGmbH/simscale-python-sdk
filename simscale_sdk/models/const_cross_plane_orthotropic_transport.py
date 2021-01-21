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


class ConstCrossPlaneOrthotropicTransport(object):
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
        'conductivity': 'CrossPlaneOrthotropicConductivity',
        'orientation': 'OneOfConstCrossPlaneOrthotropicTransportOrientation',
        'thermo': 'HConstThermo'
    }

    attribute_map = {
        'type': 'type',
        'conductivity': 'conductivity',
        'orientation': 'orientation',
        'thermo': 'thermo'
    }

    def __init__(self, type='CONST_CROSS_PLANE_ORTHO', conductivity=None, orientation=None, thermo=None, local_vars_configuration=None):  # noqa: E501
        """ConstCrossPlaneOrthotropicTransport - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._conductivity = None
        self._orientation = None
        self._thermo = None
        self.discriminator = None

        self.type = type
        if conductivity is not None:
            self.conductivity = conductivity
        if orientation is not None:
            self.orientation = orientation
        if thermo is not None:
            self.thermo = thermo

    @property
    def type(self):
        """Gets the type of this ConstCrossPlaneOrthotropicTransport.  # noqa: E501


        :return: The type of this ConstCrossPlaneOrthotropicTransport.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ConstCrossPlaneOrthotropicTransport.


        :param type: The type of this ConstCrossPlaneOrthotropicTransport.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def conductivity(self):
        """Gets the conductivity of this ConstCrossPlaneOrthotropicTransport.  # noqa: E501


        :return: The conductivity of this ConstCrossPlaneOrthotropicTransport.  # noqa: E501
        :rtype: CrossPlaneOrthotropicConductivity
        """
        return self._conductivity

    @conductivity.setter
    def conductivity(self, conductivity):
        """Sets the conductivity of this ConstCrossPlaneOrthotropicTransport.


        :param conductivity: The conductivity of this ConstCrossPlaneOrthotropicTransport.  # noqa: E501
        :type: CrossPlaneOrthotropicConductivity
        """

        self._conductivity = conductivity

    @property
    def orientation(self):
        """Gets the orientation of this ConstCrossPlaneOrthotropicTransport.  # noqa: E501


        :return: The orientation of this ConstCrossPlaneOrthotropicTransport.  # noqa: E501
        :rtype: OneOfConstCrossPlaneOrthotropicTransportOrientation
        """
        return self._orientation

    @orientation.setter
    def orientation(self, orientation):
        """Sets the orientation of this ConstCrossPlaneOrthotropicTransport.


        :param orientation: The orientation of this ConstCrossPlaneOrthotropicTransport.  # noqa: E501
        :type: OneOfConstCrossPlaneOrthotropicTransportOrientation
        """

        self._orientation = orientation

    @property
    def thermo(self):
        """Gets the thermo of this ConstCrossPlaneOrthotropicTransport.  # noqa: E501


        :return: The thermo of this ConstCrossPlaneOrthotropicTransport.  # noqa: E501
        :rtype: HConstThermo
        """
        return self._thermo

    @thermo.setter
    def thermo(self, thermo):
        """Sets the thermo of this ConstCrossPlaneOrthotropicTransport.


        :param thermo: The thermo of this ConstCrossPlaneOrthotropicTransport.  # noqa: E501
        :type: HConstThermo
        """

        self._thermo = thermo

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
        if not isinstance(other, ConstCrossPlaneOrthotropicTransport):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ConstCrossPlaneOrthotropicTransport):
            return True

        return self.to_dict() != other.to_dict()
