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


class SimmetrixExtrusionMeshRefinement(object):
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
        'sizing_type': 'OneOfSimmetrixExtrusionMeshRefinementSizingType',
        'surface_element_type': 'str',
        'specify_local_size': 'bool',
        'max_element_size': 'DimensionalLength',
        'source_topological_reference': 'TopologicalReference',
        'destination_topological_reference': 'TopologicalReference'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'sizing_type': 'sizingType',
        'surface_element_type': 'surfaceElementType',
        'specify_local_size': 'specifyLocalSize',
        'max_element_size': 'maxElementSize',
        'source_topological_reference': 'sourceTopologicalReference',
        'destination_topological_reference': 'destinationTopologicalReference'
    }

    def __init__(self, type='SIMMETRIX_EXTRUSION_MESH_REFINEMENT', name=None, sizing_type=None, surface_element_type=None, specify_local_size=None, max_element_size=None, source_topological_reference=None, destination_topological_reference=None, local_vars_configuration=None):  # noqa: E501
        """SimmetrixExtrusionMeshRefinement - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._sizing_type = None
        self._surface_element_type = None
        self._specify_local_size = None
        self._max_element_size = None
        self._source_topological_reference = None
        self._destination_topological_reference = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if sizing_type is not None:
            self.sizing_type = sizing_type
        if surface_element_type is not None:
            self.surface_element_type = surface_element_type
        if specify_local_size is not None:
            self.specify_local_size = specify_local_size
        if max_element_size is not None:
            self.max_element_size = max_element_size
        if source_topological_reference is not None:
            self.source_topological_reference = source_topological_reference
        if destination_topological_reference is not None:
            self.destination_topological_reference = destination_topological_reference

    @property
    def type(self):
        """Gets the type of this SimmetrixExtrusionMeshRefinement.  # noqa: E501

        Schema name: SimmetrixExtrusionMeshRefinement  # noqa: E501

        :return: The type of this SimmetrixExtrusionMeshRefinement.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SimmetrixExtrusionMeshRefinement.

        Schema name: SimmetrixExtrusionMeshRefinement  # noqa: E501

        :param type: The type of this SimmetrixExtrusionMeshRefinement.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this SimmetrixExtrusionMeshRefinement.  # noqa: E501


        :return: The name of this SimmetrixExtrusionMeshRefinement.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SimmetrixExtrusionMeshRefinement.


        :param name: The name of this SimmetrixExtrusionMeshRefinement.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sizing_type(self):
        """Gets the sizing_type of this SimmetrixExtrusionMeshRefinement.  # noqa: E501


        :return: The sizing_type of this SimmetrixExtrusionMeshRefinement.  # noqa: E501
        :rtype: OneOfSimmetrixExtrusionMeshRefinementSizingType
        """
        return self._sizing_type

    @sizing_type.setter
    def sizing_type(self, sizing_type):
        """Sets the sizing_type of this SimmetrixExtrusionMeshRefinement.


        :param sizing_type: The sizing_type of this SimmetrixExtrusionMeshRefinement.  # noqa: E501
        :type: OneOfSimmetrixExtrusionMeshRefinementSizingType
        """

        self._sizing_type = sizing_type

    @property
    def surface_element_type(self):
        """Gets the surface_element_type of this SimmetrixExtrusionMeshRefinement.  # noqa: E501


        :return: The surface_element_type of this SimmetrixExtrusionMeshRefinement.  # noqa: E501
        :rtype: str
        """
        return self._surface_element_type

    @surface_element_type.setter
    def surface_element_type(self, surface_element_type):
        """Sets the surface_element_type of this SimmetrixExtrusionMeshRefinement.


        :param surface_element_type: The surface_element_type of this SimmetrixExtrusionMeshRefinement.  # noqa: E501
        :type: str
        """
        allowed_values = ["TRIANGULAR", "QUADDOMINANT"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and surface_element_type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `surface_element_type` ({0}), must be one of {1}"  # noqa: E501
                .format(surface_element_type, allowed_values)
            )

        self._surface_element_type = surface_element_type

    @property
    def specify_local_size(self):
        """Gets the specify_local_size of this SimmetrixExtrusionMeshRefinement.  # noqa: E501


        :return: The specify_local_size of this SimmetrixExtrusionMeshRefinement.  # noqa: E501
        :rtype: bool
        """
        return self._specify_local_size

    @specify_local_size.setter
    def specify_local_size(self, specify_local_size):
        """Sets the specify_local_size of this SimmetrixExtrusionMeshRefinement.


        :param specify_local_size: The specify_local_size of this SimmetrixExtrusionMeshRefinement.  # noqa: E501
        :type: bool
        """

        self._specify_local_size = specify_local_size

    @property
    def max_element_size(self):
        """Gets the max_element_size of this SimmetrixExtrusionMeshRefinement.  # noqa: E501


        :return: The max_element_size of this SimmetrixExtrusionMeshRefinement.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._max_element_size

    @max_element_size.setter
    def max_element_size(self, max_element_size):
        """Sets the max_element_size of this SimmetrixExtrusionMeshRefinement.


        :param max_element_size: The max_element_size of this SimmetrixExtrusionMeshRefinement.  # noqa: E501
        :type: DimensionalLength
        """

        self._max_element_size = max_element_size

    @property
    def source_topological_reference(self):
        """Gets the source_topological_reference of this SimmetrixExtrusionMeshRefinement.  # noqa: E501


        :return: The source_topological_reference of this SimmetrixExtrusionMeshRefinement.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._source_topological_reference

    @source_topological_reference.setter
    def source_topological_reference(self, source_topological_reference):
        """Sets the source_topological_reference of this SimmetrixExtrusionMeshRefinement.


        :param source_topological_reference: The source_topological_reference of this SimmetrixExtrusionMeshRefinement.  # noqa: E501
        :type: TopologicalReference
        """

        self._source_topological_reference = source_topological_reference

    @property
    def destination_topological_reference(self):
        """Gets the destination_topological_reference of this SimmetrixExtrusionMeshRefinement.  # noqa: E501


        :return: The destination_topological_reference of this SimmetrixExtrusionMeshRefinement.  # noqa: E501
        :rtype: TopologicalReference
        """
        return self._destination_topological_reference

    @destination_topological_reference.setter
    def destination_topological_reference(self, destination_topological_reference):
        """Sets the destination_topological_reference of this SimmetrixExtrusionMeshRefinement.


        :param destination_topological_reference: The destination_topological_reference of this SimmetrixExtrusionMeshRefinement.  # noqa: E501
        :type: TopologicalReference
        """

        self._destination_topological_reference = destination_topological_reference

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
        if not isinstance(other, SimmetrixExtrusionMeshRefinement):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimmetrixExtrusionMeshRefinement):
            return True

        return self.to_dict() != other.to_dict()
