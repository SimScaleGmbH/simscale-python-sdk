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


class IsoSurface(object):
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
        'iso_value': 'float',
        'scalar_field': 'ScalarField',
        'solid_color': 'Color',
        'vector_field': 'VectorField',
        'opacity': 'float'
    }

    attribute_map = {
        'iso_scalar': 'isoScalar',
        'iso_value': 'isoValue',
        'scalar_field': 'scalarField',
        'solid_color': 'solidColor',
        'vector_field': 'vectorField',
        'opacity': 'opacity'
    }

    def __init__(self, iso_scalar=None, iso_value=None, scalar_field=None, solid_color=None, vector_field=None, opacity=None, local_vars_configuration=None):  # noqa: E501
        """IsoSurface - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._iso_scalar = None
        self._iso_value = None
        self._scalar_field = None
        self._solid_color = None
        self._vector_field = None
        self._opacity = None
        self.discriminator = None

        if iso_scalar is not None:
            self.iso_scalar = iso_scalar
        if iso_value is not None:
            self.iso_value = iso_value
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
        """Gets the iso_scalar of this IsoSurface.  # noqa: E501


        :return: The iso_scalar of this IsoSurface.  # noqa: E501
        :rtype: ScalarField
        """
        return self._iso_scalar

    @iso_scalar.setter
    def iso_scalar(self, iso_scalar):
        """Sets the iso_scalar of this IsoSurface.


        :param iso_scalar: The iso_scalar of this IsoSurface.  # noqa: E501
        :type: ScalarField
        """

        self._iso_scalar = iso_scalar

    @property
    def iso_value(self):
        """Gets the iso_value of this IsoSurface.  # noqa: E501

        The iso scalar value. Should be within the selected scalar range. Default value is the average between the min and max in the range.  # noqa: E501

        :return: The iso_value of this IsoSurface.  # noqa: E501
        :rtype: float
        """
        return self._iso_value

    @iso_value.setter
    def iso_value(self, iso_value):
        """Sets the iso_value of this IsoSurface.

        The iso scalar value. Should be within the selected scalar range. Default value is the average between the min and max in the range.  # noqa: E501

        :param iso_value: The iso_value of this IsoSurface.  # noqa: E501
        :type: float
        """

        self._iso_value = iso_value

    @property
    def scalar_field(self):
        """Gets the scalar_field of this IsoSurface.  # noqa: E501


        :return: The scalar_field of this IsoSurface.  # noqa: E501
        :rtype: ScalarField
        """
        return self._scalar_field

    @scalar_field.setter
    def scalar_field(self, scalar_field):
        """Sets the scalar_field of this IsoSurface.


        :param scalar_field: The scalar_field of this IsoSurface.  # noqa: E501
        :type: ScalarField
        """

        self._scalar_field = scalar_field

    @property
    def solid_color(self):
        """Gets the solid_color of this IsoSurface.  # noqa: E501


        :return: The solid_color of this IsoSurface.  # noqa: E501
        :rtype: Color
        """
        return self._solid_color

    @solid_color.setter
    def solid_color(self, solid_color):
        """Sets the solid_color of this IsoSurface.


        :param solid_color: The solid_color of this IsoSurface.  # noqa: E501
        :type: Color
        """

        self._solid_color = solid_color

    @property
    def vector_field(self):
        """Gets the vector_field of this IsoSurface.  # noqa: E501


        :return: The vector_field of this IsoSurface.  # noqa: E501
        :rtype: VectorField
        """
        return self._vector_field

    @vector_field.setter
    def vector_field(self, vector_field):
        """Sets the vector_field of this IsoSurface.


        :param vector_field: The vector_field of this IsoSurface.  # noqa: E501
        :type: VectorField
        """

        self._vector_field = vector_field

    @property
    def opacity(self):
        """Gets the opacity of this IsoSurface.  # noqa: E501


        :return: The opacity of this IsoSurface.  # noqa: E501
        :rtype: float
        """
        return self._opacity

    @opacity.setter
    def opacity(self, opacity):
        """Sets the opacity of this IsoSurface.


        :param opacity: The opacity of this IsoSurface.  # noqa: E501
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
        if not isinstance(other, IsoSurface):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IsoSurface):
            return True

        return self.to_dict() != other.to_dict()
