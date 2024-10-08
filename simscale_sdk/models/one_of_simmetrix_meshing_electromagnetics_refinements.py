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


class OneOfSimmetrixMeshingElectromagneticsRefinements(object):
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
        'name': 'str',
        'refinement': 'OneOfRegionRefinementWithLengthRefinement',
        'curvature': 'OneOfSimmetrixLocalSizingRefinementCurvature',
        'topological_reference': 'TopologicalReference',
        'geometry_primitive_uuids': 'list[str]',
        'sizing': 'OneOfSurfaceCustomSizingSizing',
        'custom_sizing_modes': 'OneOfVolumeCustomSizingCustomSizingModes',
        'max_element_size': 'DimensionalLength'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'refinement': 'refinement',
        'curvature': 'curvature',
        'topological_reference': 'topologicalReference',
        'geometry_primitive_uuids': 'geometryPrimitiveUuids',
        'sizing': 'sizing',
        'custom_sizing_modes': 'customSizingModes',
        'max_element_size': 'maxElementSize'
    }

    discriminator_value_class_map = {
        'REGION_LENGTH': 'RegionRefinementWithLength',
        'SURFACE_CUSTOM_SIZING': 'SurfaceCustomSizing',
        'VOLUME_CUSTOM_SIZING': 'VolumeCustomSizing',
        'SIMMETRIX_LOCAL_SIZING_V10': 'SimmetrixLocalSizingRefinement'
    }

    def __init__(self, type='SIMMETRIX_LOCAL_SIZING_V10', name=None, refinement=None, curvature=None, topological_reference=None, geometry_primitive_uuids=None, sizing=None, custom_sizing_modes=None, max_element_size=None, local_vars_configuration=None):  # noqa: E501
        """OneOfSimmetrixMeshingElectromagneticsRefinements - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._refinement = None
        self._curvature = None
        self._topological_reference = None
        self._geometry_primitive_uuids = None
        self._sizing = None
        self._custom_sizing_modes = None
        self._max_element_size = None
        self.discriminator = 'type'

        self.type = type
        if name is not None:
            self.name = name
        if refinement is not None:
            self.refinement = refinement
        if curvature is not None:
            self.curvature = curvature
        if topological_reference is not None:
            self.topological_reference = topological_reference
        if geometry_primitive_uuids is not None:
            self.geometry_primitive_uuids = geometry_primitive_uuids
        if sizing is not None:
            self.sizing = sizing
        if custom_sizing_modes is not None:
            self.custom_sizing_modes = custom_sizing_modes
        if max_element_size is not None:
            self.max_element_size = max_element_size

    @property
    def type(self):
        """Gets the type of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501

        Refine specific faces of interest or complex geometrical shapes by defining a local element size. This will ensure a relatively uniform mesh.  Schema name: SimmetrixLocalSizingRefinement  # noqa: E501

        :return: The type of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfSimmetrixMeshingElectromagneticsRefinements.

        Refine specific faces of interest or complex geometrical shapes by defining a local element size. This will ensure a relatively uniform mesh.  Schema name: SimmetrixLocalSizingRefinement  # noqa: E501

        :param type: The type of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501


        :return: The name of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this OneOfSimmetrixMeshingElectromagneticsRefinements.


        :param name: The name of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def refinement(self):
        """Gets the refinement of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501


        :return: The refinement of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :rtype: OneOfRegionRefinementWithLengthRefinement
        """
        return self._refinement

    @refinement.setter
    def refinement(self, refinement):
        """Sets the refinement of this OneOfSimmetrixMeshingElectromagneticsRefinements.


        :param refinement: The refinement of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :type: OneOfRegionRefinementWithLengthRefinement
        """

        self._refinement = refinement

    @property
    def curvature(self):
        """Gets the curvature of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501


        :return: The curvature of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :rtype: OneOfSimmetrixLocalSizingRefinementCurvature
        """
        return self._curvature

    @curvature.setter
    def curvature(self, curvature):
        """Sets the curvature of this OneOfSimmetrixMeshingElectromagneticsRefinements.


        :param curvature: The curvature of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :type: OneOfSimmetrixLocalSizingRefinementCurvature
        """

        self._curvature = curvature

    @property
    def topological_reference(self):
        """Gets the topological_reference of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501


        :return: The topological_reference of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._topological_reference

    @topological_reference.setter
    def topological_reference(self, topological_reference):
        """Sets the topological_reference of this OneOfSimmetrixMeshingElectromagneticsRefinements.


        :param topological_reference: The topological_reference of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :type: TopologicalReference
        """

        self._topological_reference = topological_reference

    @property
    def geometry_primitive_uuids(self):
        """Gets the geometry_primitive_uuids of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501


        :return: The geometry_primitive_uuids of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :rtype: list[str]
        """
        return self._geometry_primitive_uuids

    @geometry_primitive_uuids.setter
    def geometry_primitive_uuids(self, geometry_primitive_uuids):
        """Sets the geometry_primitive_uuids of this OneOfSimmetrixMeshingElectromagneticsRefinements.


        :param geometry_primitive_uuids: The geometry_primitive_uuids of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :type: list[str]
        """

        self._geometry_primitive_uuids = geometry_primitive_uuids

    @property
    def sizing(self):
        """Gets the sizing of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501


        :return: The sizing of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :rtype: OneOfSurfaceCustomSizingSizing
        """
        return self._sizing

    @sizing.setter
    def sizing(self, sizing):
        """Sets the sizing of this OneOfSimmetrixMeshingElectromagneticsRefinements.


        :param sizing: The sizing of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :type: OneOfSurfaceCustomSizingSizing
        """

        self._sizing = sizing

    @property
    def custom_sizing_modes(self):
        """Gets the custom_sizing_modes of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501


        :return: The custom_sizing_modes of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :rtype: OneOfVolumeCustomSizingCustomSizingModes
        """
        return self._custom_sizing_modes

    @custom_sizing_modes.setter
    def custom_sizing_modes(self, custom_sizing_modes):
        """Sets the custom_sizing_modes of this OneOfSimmetrixMeshingElectromagneticsRefinements.


        :param custom_sizing_modes: The custom_sizing_modes of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :type: OneOfVolumeCustomSizingCustomSizingModes
        """

        self._custom_sizing_modes = custom_sizing_modes

    @property
    def max_element_size(self):
        """Gets the max_element_size of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501


        :return: The max_element_size of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._max_element_size

    @max_element_size.setter
    def max_element_size(self, max_element_size):
        """Sets the max_element_size of this OneOfSimmetrixMeshingElectromagneticsRefinements.


        :param max_element_size: The max_element_size of this OneOfSimmetrixMeshingElectromagneticsRefinements.  # noqa: E501
        :type: DimensionalLength
        """

        self._max_element_size = max_element_size

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
        if not isinstance(other, OneOfSimmetrixMeshingElectromagneticsRefinements):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfSimmetrixMeshingElectromagneticsRefinements):
            return True

        return self.to_dict() != other.to_dict()
