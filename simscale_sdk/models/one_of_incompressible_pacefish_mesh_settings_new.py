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


class OneOfIncompressiblePacefishMeshSettingsNew(object):
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
        'fineness': 'str',
        'reference_length': 'DimensionalLength',
        'reynolds_scaling': 'float',
        'refinements': 'list[OneOfPacefishAutomeshRefinements]',
        'primary_topology': 'OneOfPacefishAutomeshPrimaryTopology',
        'new_fineness': 'OneOfPacefishAutomeshNewFineness',
        'reference_length_computation': 'OneOfPacefishAutomeshReferenceLengthComputation'
    }

    attribute_map = {
        'type': 'type',
        'fineness': 'fineness',
        'reference_length': 'referenceLength',
        'reynolds_scaling': 'reynoldsScaling',
        'refinements': 'refinements',
        'primary_topology': 'primaryTopology',
        'new_fineness': 'newFineness',
        'reference_length_computation': 'referenceLengthComputation'
    }

    discriminator_value_class_map = {
        'PACEFISH_MESH_LEGACY': 'PacefishMeshLegacy',
        'PACEFISH_MESH_V38': 'PacefishMeshV38',
        'PACEFISH_AUTOMESH': 'PacefishAutomesh'
    }

    def __init__(self, type='PACEFISH_AUTOMESH', fineness=None, reference_length=None, reynolds_scaling=None, refinements=None, primary_topology=None, new_fineness=None, reference_length_computation=None, local_vars_configuration=None):  # noqa: E501
        """OneOfIncompressiblePacefishMeshSettingsNew - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._fineness = None
        self._reference_length = None
        self._reynolds_scaling = None
        self._refinements = None
        self._primary_topology = None
        self._new_fineness = None
        self._reference_length_computation = None
        self.discriminator = 'type'

        self.type = type
        if fineness is not None:
            self.fineness = fineness
        if reference_length is not None:
            self.reference_length = reference_length
        if reynolds_scaling is not None:
            self.reynolds_scaling = reynolds_scaling
        if refinements is not None:
            self.refinements = refinements
        if primary_topology is not None:
            self.primary_topology = primary_topology
        if new_fineness is not None:
            self.new_fineness = new_fineness
        if reference_length_computation is not None:
            self.reference_length_computation = reference_length_computation

    @property
    def type(self):
        """Gets the type of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501


        :return: The type of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfIncompressiblePacefishMeshSettingsNew.


        :param type: The type of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def fineness(self):
        """Gets the fineness of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501


        :return: The fineness of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501
        :rtype: str
        """
        return self._fineness

    @fineness.setter
    def fineness(self, fineness):
        """Sets the fineness of this OneOfIncompressiblePacefishMeshSettingsNew.


        :param fineness: The fineness of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501
        :type: str
        """
        allowed_values = ["VERY_COARSE", "COARSE", "MODERATE", "FINE", "VERY_FINE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and fineness not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `fineness` ({0}), must be one of {1}"  # noqa: E501
                .format(fineness, allowed_values)
            )

        self._fineness = fineness

    @property
    def reference_length(self):
        """Gets the reference_length of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501


        :return: The reference_length of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._reference_length

    @reference_length.setter
    def reference_length(self, reference_length):
        """Sets the reference_length of this OneOfIncompressiblePacefishMeshSettingsNew.


        :param reference_length: The reference_length of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501
        :type: DimensionalLength
        """

        self._reference_length = reference_length

    @property
    def reynolds_scaling(self):
        """Gets the reynolds_scaling of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501

        Use this factor to scale the Reynolds number of your simulation. For example, to change the Reynolds number from 10<sup>8</sup> to 10<sup>6</sup>, set this factor to 0.01.  # noqa: E501

        :return: The reynolds_scaling of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501
        :rtype: float
        """
        return self._reynolds_scaling

    @reynolds_scaling.setter
    def reynolds_scaling(self, reynolds_scaling):
        """Sets the reynolds_scaling of this OneOfIncompressiblePacefishMeshSettingsNew.

        Use this factor to scale the Reynolds number of your simulation. For example, to change the Reynolds number from 10<sup>8</sup> to 10<sup>6</sup>, set this factor to 0.01.  # noqa: E501

        :param reynolds_scaling: The reynolds_scaling of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                reynolds_scaling is not None and reynolds_scaling < 0):  # noqa: E501
            raise ValueError("Invalid value for `reynolds_scaling`, must be a value greater than or equal to `0`")  # noqa: E501

        self._reynolds_scaling = reynolds_scaling

    @property
    def refinements(self):
        """Gets the refinements of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501


        :return: The refinements of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501
        :rtype: list[OneOfPacefishAutomeshRefinements]
        """
        return self._refinements

    @refinements.setter
    def refinements(self, refinements):
        """Sets the refinements of this OneOfIncompressiblePacefishMeshSettingsNew.


        :param refinements: The refinements of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501
        :type: list[OneOfPacefishAutomeshRefinements]
        """

        self._refinements = refinements

    @property
    def primary_topology(self):
        """Gets the primary_topology of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501


        :return: The primary_topology of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501
        :rtype: OneOfPacefishAutomeshPrimaryTopology
        """
        return self._primary_topology

    @primary_topology.setter
    def primary_topology(self, primary_topology):
        """Sets the primary_topology of this OneOfIncompressiblePacefishMeshSettingsNew.


        :param primary_topology: The primary_topology of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501
        :type: OneOfPacefishAutomeshPrimaryTopology
        """

        self._primary_topology = primary_topology

    @property
    def new_fineness(self):
        """Gets the new_fineness of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501


        :return: The new_fineness of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501
        :rtype: OneOfPacefishAutomeshNewFineness
        """
        return self._new_fineness

    @new_fineness.setter
    def new_fineness(self, new_fineness):
        """Sets the new_fineness of this OneOfIncompressiblePacefishMeshSettingsNew.


        :param new_fineness: The new_fineness of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501
        :type: OneOfPacefishAutomeshNewFineness
        """

        self._new_fineness = new_fineness

    @property
    def reference_length_computation(self):
        """Gets the reference_length_computation of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501


        :return: The reference_length_computation of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501
        :rtype: OneOfPacefishAutomeshReferenceLengthComputation
        """
        return self._reference_length_computation

    @reference_length_computation.setter
    def reference_length_computation(self, reference_length_computation):
        """Sets the reference_length_computation of this OneOfIncompressiblePacefishMeshSettingsNew.


        :param reference_length_computation: The reference_length_computation of this OneOfIncompressiblePacefishMeshSettingsNew.  # noqa: E501
        :type: OneOfPacefishAutomeshReferenceLengthComputation
        """

        self._reference_length_computation = reference_length_computation

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
        if not isinstance(other, OneOfIncompressiblePacefishMeshSettingsNew):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfIncompressiblePacefishMeshSettingsNew):
            return True

        return self.to_dict() != other.to_dict()
