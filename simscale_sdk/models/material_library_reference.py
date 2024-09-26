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


class MaterialLibraryReference(object):
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
        'material_group_id': 'str',
        'material_id': 'str',
        'interpolation_parameters': 'dict(str, InterpolationParameter)'
    }

    attribute_map = {
        'material_group_id': 'materialGroupId',
        'material_id': 'materialId',
        'interpolation_parameters': 'interpolationParameters'
    }

    def __init__(self, material_group_id=None, material_id=None, interpolation_parameters=None, local_vars_configuration=None):  # noqa: E501
        """MaterialLibraryReference - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._material_group_id = None
        self._material_id = None
        self._interpolation_parameters = None
        self.discriminator = None

        if material_group_id is not None:
            self.material_group_id = material_group_id
        if material_id is not None:
            self.material_id = material_id
        if interpolation_parameters is not None:
            self.interpolation_parameters = interpolation_parameters

    @property
    def material_group_id(self):
        """Gets the material_group_id of this MaterialLibraryReference.  # noqa: E501


        :return: The material_group_id of this MaterialLibraryReference.  # noqa: E501
        :rtype: str
        """
        return self._material_group_id

    @material_group_id.setter
    def material_group_id(self, material_group_id):
        """Sets the material_group_id of this MaterialLibraryReference.


        :param material_group_id: The material_group_id of this MaterialLibraryReference.  # noqa: E501
        :type: str
        """

        self._material_group_id = material_group_id

    @property
    def material_id(self):
        """Gets the material_id of this MaterialLibraryReference.  # noqa: E501


        :return: The material_id of this MaterialLibraryReference.  # noqa: E501
        :rtype: str
        """
        return self._material_id

    @material_id.setter
    def material_id(self, material_id):
        """Sets the material_id of this MaterialLibraryReference.


        :param material_id: The material_id of this MaterialLibraryReference.  # noqa: E501
        :type: str
        """

        self._material_id = material_id

    @property
    def interpolation_parameters(self):
        """Gets the interpolation_parameters of this MaterialLibraryReference.  # noqa: E501


        :return: The interpolation_parameters of this MaterialLibraryReference.  # noqa: E501
        :rtype: dict(str, InterpolationParameter)
        """
        return self._interpolation_parameters

    @interpolation_parameters.setter
    def interpolation_parameters(self, interpolation_parameters):
        """Sets the interpolation_parameters of this MaterialLibraryReference.


        :param interpolation_parameters: The interpolation_parameters of this MaterialLibraryReference.  # noqa: E501
        :type: dict(str, InterpolationParameter)
        """

        self._interpolation_parameters = interpolation_parameters

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
        if not isinstance(other, MaterialLibraryReference):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MaterialLibraryReference):
            return True

        return self.to_dict() != other.to_dict()