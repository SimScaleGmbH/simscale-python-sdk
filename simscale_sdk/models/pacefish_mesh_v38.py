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


class PacefishMeshV38(object):
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
        'primary_topology': 'OneOfPacefishMeshV38PrimaryTopology',
        'refinements': 'list[OneOfPacefishMeshV38Refinements]'
    }

    attribute_map = {
        'type': 'type',
        'fineness': 'fineness',
        'reference_length': 'referenceLength',
        'primary_topology': 'primaryTopology',
        'refinements': 'refinements'
    }

    def __init__(self, type='PACEFISH_MESH_V38', fineness=None, reference_length=None, primary_topology=None, refinements=None, local_vars_configuration=None):  # noqa: E501
        """PacefishMeshV38 - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._fineness = None
        self._reference_length = None
        self._primary_topology = None
        self._refinements = None
        self.discriminator = None

        self.type = type
        if fineness is not None:
            self.fineness = fineness
        if reference_length is not None:
            self.reference_length = reference_length
        if primary_topology is not None:
            self.primary_topology = primary_topology
        if refinements is not None:
            self.refinements = refinements

    @property
    def type(self):
        """Gets the type of this PacefishMeshV38.  # noqa: E501

        <p>Choose between <i>Automatic</i> and <i>Manual</i> mesh settings. <a href='https://www.simscale.com/docs/analysis-types/incompressible-lbm/#mesh' target='_blank'>Learn more.</a></p><p><b>Note:</b> Mesh fineness impacts the accuracy of your results as well as computing time and result size. A finer mesh will be more demanding in terms of machine size and memory but lead to more accurate results in most cases.</p>  Schema name: PacefishMeshV38  # noqa: E501

        :return: The type of this PacefishMeshV38.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PacefishMeshV38.

        <p>Choose between <i>Automatic</i> and <i>Manual</i> mesh settings. <a href='https://www.simscale.com/docs/analysis-types/incompressible-lbm/#mesh' target='_blank'>Learn more.</a></p><p><b>Note:</b> Mesh fineness impacts the accuracy of your results as well as computing time and result size. A finer mesh will be more demanding in terms of machine size and memory but lead to more accurate results in most cases.</p>  Schema name: PacefishMeshV38  # noqa: E501

        :param type: The type of this PacefishMeshV38.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def fineness(self):
        """Gets the fineness of this PacefishMeshV38.  # noqa: E501


        :return: The fineness of this PacefishMeshV38.  # noqa: E501
        :rtype: str
        """
        return self._fineness

    @fineness.setter
    def fineness(self, fineness):
        """Sets the fineness of this PacefishMeshV38.


        :param fineness: The fineness of this PacefishMeshV38.  # noqa: E501
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
        """Gets the reference_length of this PacefishMeshV38.  # noqa: E501


        :return: The reference_length of this PacefishMeshV38.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._reference_length

    @reference_length.setter
    def reference_length(self, reference_length):
        """Sets the reference_length of this PacefishMeshV38.


        :param reference_length: The reference_length of this PacefishMeshV38.  # noqa: E501
        :type: DimensionalLength
        """

        self._reference_length = reference_length

    @property
    def primary_topology(self):
        """Gets the primary_topology of this PacefishMeshV38.  # noqa: E501


        :return: The primary_topology of this PacefishMeshV38.  # noqa: E501
        :rtype: OneOfPacefishMeshV38PrimaryTopology
        """
        return self._primary_topology

    @primary_topology.setter
    def primary_topology(self, primary_topology):
        """Sets the primary_topology of this PacefishMeshV38.


        :param primary_topology: The primary_topology of this PacefishMeshV38.  # noqa: E501
        :type: OneOfPacefishMeshV38PrimaryTopology
        """

        self._primary_topology = primary_topology

    @property
    def refinements(self):
        """Gets the refinements of this PacefishMeshV38.  # noqa: E501


        :return: The refinements of this PacefishMeshV38.  # noqa: E501
        :rtype: list[OneOfPacefishMeshV38Refinements]
        """
        return self._refinements

    @refinements.setter
    def refinements(self, refinements):
        """Sets the refinements of this PacefishMeshV38.


        :param refinements: The refinements of this PacefishMeshV38.  # noqa: E501
        :type: list[OneOfPacefishMeshV38Refinements]
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
        if not isinstance(other, PacefishMeshV38):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, PacefishMeshV38):
            return True

        return self.to_dict() != other.to_dict()
