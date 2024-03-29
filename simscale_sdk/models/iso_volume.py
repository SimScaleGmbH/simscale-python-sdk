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


class IsoVolume(object):
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
        'iso_scalar': 'ScalarField',
        'minimum_iso_value': 'float',
        'maximum_iso_value': 'float',
        'scalar_field': 'ScalarField',
        'solid_color': 'Color',
        'vector_field': 'VectorField',
        'opacity': 'float'
    }

    attribute_map = {
        'iso_scalar': 'isoScalar',
        'minimum_iso_value': 'minimumIsoValue',
        'maximum_iso_value': 'maximumIsoValue',
        'scalar_field': 'scalarField',
        'solid_color': 'solidColor',
        'vector_field': 'vectorField',
        'opacity': 'opacity'
    }

    def __init__(self, iso_scalar=None, minimum_iso_value=None, maximum_iso_value=None, scalar_field=None, solid_color=None, vector_field=None, opacity=None, local_vars_configuration=None):  # noqa: E501
        """IsoVolume - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._iso_scalar = None
        self._minimum_iso_value = None
        self._maximum_iso_value = None
        self._scalar_field = None
        self._solid_color = None
        self._vector_field = None
        self._opacity = None
        self.discriminator = None

        if iso_scalar is not None:
            self.iso_scalar = iso_scalar
        if minimum_iso_value is not None:
            self.minimum_iso_value = minimum_iso_value
        if maximum_iso_value is not None:
            self.maximum_iso_value = maximum_iso_value
        if scalar_field is not None:
            self.scalar_field = scalar_field
        if solid_color is not None:
            self.solid_color = solid_color
        if vector_field is not None:
            self.vector_field = vector_field
        if opacity is not None:
            self.opacity = opacity

    @property
    def iso_scalar(self):
        """Gets the iso_scalar of this IsoVolume.  # noqa: E501


        :return: The iso_scalar of this IsoVolume.  # noqa: E501
        :rtype: ScalarField
        """
        return self._iso_scalar

    @iso_scalar.setter
    def iso_scalar(self, iso_scalar):
        """Sets the iso_scalar of this IsoVolume.


        :param iso_scalar: The iso_scalar of this IsoVolume.  # noqa: E501
        :type: ScalarField
        """

        self._iso_scalar = iso_scalar

    @property
    def minimum_iso_value(self):
        """Gets the minimum_iso_value of this IsoVolume.  # noqa: E501

        The iso scalar minimum value. Should be within the selected scalar range and smaller than the maximumIsoValue. Default value is the third of the range between min and max.  # noqa: E501

        :return: The minimum_iso_value of this IsoVolume.  # noqa: E501
        :rtype: float
        """
        return self._minimum_iso_value

    @minimum_iso_value.setter
    def minimum_iso_value(self, minimum_iso_value):
        """Sets the minimum_iso_value of this IsoVolume.

        The iso scalar minimum value. Should be within the selected scalar range and smaller than the maximumIsoValue. Default value is the third of the range between min and max.  # noqa: E501

        :param minimum_iso_value: The minimum_iso_value of this IsoVolume.  # noqa: E501
        :type: float
        """

        self._minimum_iso_value = minimum_iso_value

    @property
    def maximum_iso_value(self):
        """Gets the maximum_iso_value of this IsoVolume.  # noqa: E501

        The iso scalar maximum value. Should be within the selected scalar range and larger than the minimumIsoValue. Default value is 2 thirds of the range between min and max.  # noqa: E501

        :return: The maximum_iso_value of this IsoVolume.  # noqa: E501
        :rtype: float
        """
        return self._maximum_iso_value

    @maximum_iso_value.setter
    def maximum_iso_value(self, maximum_iso_value):
        """Sets the maximum_iso_value of this IsoVolume.

        The iso scalar maximum value. Should be within the selected scalar range and larger than the minimumIsoValue. Default value is 2 thirds of the range between min and max.  # noqa: E501

        :param maximum_iso_value: The maximum_iso_value of this IsoVolume.  # noqa: E501
        :type: float
        """

        self._maximum_iso_value = maximum_iso_value

    @property
    def scalar_field(self):
        """Gets the scalar_field of this IsoVolume.  # noqa: E501


        :return: The scalar_field of this IsoVolume.  # noqa: E501
        :rtype: ScalarField
        """
        return self._scalar_field

    @scalar_field.setter
    def scalar_field(self, scalar_field):
        """Sets the scalar_field of this IsoVolume.


        :param scalar_field: The scalar_field of this IsoVolume.  # noqa: E501
        :type: ScalarField
        """

        self._scalar_field = scalar_field

    @property
    def solid_color(self):
        """Gets the solid_color of this IsoVolume.  # noqa: E501


        :return: The solid_color of this IsoVolume.  # noqa: E501
        :rtype: Color
        """
        return self._solid_color

    @solid_color.setter
    def solid_color(self, solid_color):
        """Sets the solid_color of this IsoVolume.


        :param solid_color: The solid_color of this IsoVolume.  # noqa: E501
        :type: Color
        """

        self._solid_color = solid_color

    @property
    def vector_field(self):
        """Gets the vector_field of this IsoVolume.  # noqa: E501


        :return: The vector_field of this IsoVolume.  # noqa: E501
        :rtype: VectorField
        """
        return self._vector_field

    @vector_field.setter
    def vector_field(self, vector_field):
        """Sets the vector_field of this IsoVolume.


        :param vector_field: The vector_field of this IsoVolume.  # noqa: E501
        :type: VectorField
        """

        self._vector_field = vector_field

    @property
    def opacity(self):
        """Gets the opacity of this IsoVolume.  # noqa: E501


        :return: The opacity of this IsoVolume.  # noqa: E501
        :rtype: float
        """
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        """Sets the opacity of this IsoVolume.


        :param opacity: The opacity of this IsoVolume.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                opacity is not None and opacity > 1.0):  # noqa: E501
            raise ValueError("Invalid value for `opacity`, must be a value less than or equal to `1.0`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                opacity is not None and opacity < 0.0):  # noqa: E501
            raise ValueError("Invalid value for `opacity`, must be a value greater than or equal to `0.0`")  # noqa: E501

        self._opacity = opacity

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
        if not isinstance(other, IsoVolume):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IsoVolume):
            return True

        return self.to_dict() != other.to_dict()
