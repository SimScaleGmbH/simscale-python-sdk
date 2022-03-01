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


class WindComfortMesh(object):
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
        'wind_comfort_fineness': 'OneOfWindComfortMeshWindComfortFineness',
        'refinements': 'list[OneOfWindComfortMeshRefinements]'
    }

    attribute_map = {
        'wind_comfort_fineness': 'windComfortFineness',
        'refinements': 'refinements'
    }

    def __init__(self, wind_comfort_fineness=None, refinements=None, local_vars_configuration=None):  # noqa: E501
        """WindComfortMesh - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._wind_comfort_fineness = None
        self._refinements = None
        self.discriminator = None

        if wind_comfort_fineness is not None:
            self.wind_comfort_fineness = wind_comfort_fineness
        if refinements is not None:
            self.refinements = refinements

    @property
    def wind_comfort_fineness(self):
        """Gets the wind_comfort_fineness of this WindComfortMesh.  # noqa: E501


        :return: The wind_comfort_fineness of this WindComfortMesh.  # noqa: E501
        :rtype: OneOfWindComfortMeshWindComfortFineness
        """
        return self._wind_comfort_fineness

    @wind_comfort_fineness.setter
    def wind_comfort_fineness(self, wind_comfort_fineness):
        """Sets the wind_comfort_fineness of this WindComfortMesh.


        :param wind_comfort_fineness: The wind_comfort_fineness of this WindComfortMesh.  # noqa: E501
        :type: OneOfWindComfortMeshWindComfortFineness
        """

        self._wind_comfort_fineness = wind_comfort_fineness

    @property
    def refinements(self):
        """Gets the refinements of this WindComfortMesh.  # noqa: E501


        :return: The refinements of this WindComfortMesh.  # noqa: E501
        :rtype: list[OneOfWindComfortMeshRefinements]
        """
        return self._refinements

    @refinements.setter
    def refinements(self, refinements):
        """Sets the refinements of this WindComfortMesh.


        :param refinements: The refinements of this WindComfortMesh.  # noqa: E501
        :type: list[OneOfWindComfortMeshRefinements]
        """

        self._refinements = refinements

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
        if not isinstance(other, WindComfortMesh):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, WindComfortMesh):
            return True

        return self.to_dict() != other.to_dict()