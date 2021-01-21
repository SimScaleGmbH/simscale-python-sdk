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


class IRAMSorensen(object):
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
        'prec_soren': 'float',
        'nmax_iter_soren': 'int'
    }

    attribute_map = {
        'type': 'type',
        'prec_soren': 'precSoren',
        'nmax_iter_soren': 'nmaxIterSoren'
    }

    def __init__(self, type='SORENSEN', prec_soren=None, nmax_iter_soren=None, local_vars_configuration=None):  # noqa: E501
        """IRAMSorensen - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._prec_soren = None
        self._nmax_iter_soren = None
        self.discriminator = None

        self.type = type
        if prec_soren is not None:
            self.prec_soren = prec_soren
        if nmax_iter_soren is not None:
            self.nmax_iter_soren = nmax_iter_soren

    @property
    def type(self):
        """Gets the type of this IRAMSorensen.  # noqa: E501


        :return: The type of this IRAMSorensen.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IRAMSorensen.


        :param type: The type of this IRAMSorensen.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def prec_soren(self):
        """Gets the prec_soren of this IRAMSorensen.  # noqa: E501


        :return: The prec_soren of this IRAMSorensen.  # noqa: E501
        :rtype: float
        """
        return self._prec_soren

    @prec_soren.setter
    def prec_soren(self, prec_soren):
        """Sets the prec_soren of this IRAMSorensen.


        :param prec_soren: The prec_soren of this IRAMSorensen.  # noqa: E501
        :type: float
        """

        self._prec_soren = prec_soren

    @property
    def nmax_iter_soren(self):
        """Gets the nmax_iter_soren of this IRAMSorensen.  # noqa: E501


        :return: The nmax_iter_soren of this IRAMSorensen.  # noqa: E501
        :rtype: int
        """
        return self._nmax_iter_soren

    @nmax_iter_soren.setter
    def nmax_iter_soren(self, nmax_iter_soren):
        """Sets the nmax_iter_soren of this IRAMSorensen.


        :param nmax_iter_soren: The nmax_iter_soren of this IRAMSorensen.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                nmax_iter_soren is not None and nmax_iter_soren < 0):  # noqa: E501
            raise ValueError("Invalid value for `nmax_iter_soren`, must be a value greater than or equal to `0`")  # noqa: E501

        self._nmax_iter_soren = nmax_iter_soren

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
        if not isinstance(other, IRAMSorensen):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IRAMSorensen):
            return True

        return self.to_dict() != other.to_dict()
