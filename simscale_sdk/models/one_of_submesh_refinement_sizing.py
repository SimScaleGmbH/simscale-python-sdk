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


class OneOfSubmeshRefinementSizing(object):
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
        'minimum_edge_length': 'DimensionalLength',
        'maximum_edge_length': 'DimensionalLength',
        'grading': 'OneOfManualMeshSizingGrading'
    }

    attribute_map = {
        'type': 'type',
        'fineness': 'fineness',
        'minimum_edge_length': 'minimumEdgeLength',
        'maximum_edge_length': 'maximumEdgeLength',
        'grading': 'grading'
    }

    discriminator_value_class_map = {
        'AUTOMATIC': 'AutomaticMeshSizing',
        'MANUAL': 'ManualMeshSizing'
    }

    def __init__(self, type='MANUAL', fineness=None, minimum_edge_length=None, maximum_edge_length=None, grading=None, local_vars_configuration=None):  # noqa: E501
        """OneOfSubmeshRefinementSizing - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._fineness = None
        self._minimum_edge_length = None
        self._maximum_edge_length = None
        self._grading = None
        self.discriminator = 'type'

        self.type = type
        if fineness is not None:
            self.fineness = fineness
        if minimum_edge_length is not None:
            self.minimum_edge_length = minimum_edge_length
        if maximum_edge_length is not None:
            self.maximum_edge_length = maximum_edge_length
        if grading is not None:
            self.grading = grading

    @property
    def type(self):
        """Gets the type of this OneOfSubmeshRefinementSizing.  # noqa: E501

        Schema name: ManualMeshSizing  # noqa: E501

        :return: The type of this OneOfSubmeshRefinementSizing.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfSubmeshRefinementSizing.

        Schema name: ManualMeshSizing  # noqa: E501

        :param type: The type of this OneOfSubmeshRefinementSizing.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def fineness(self):
        """Gets the fineness of this OneOfSubmeshRefinementSizing.  # noqa: E501

        <p>Choose between <i>Automatic</i> and <i>Manual</i> mesh settings. <a href='https://www.simscale.com/docs/analysis-types/incompressible-lbm/#mesh' target='_blank'>Learn more.</a></p><p><b>Note:</b> Mesh fineness impacts the accuracy of your results as well as computing time and result size. A finer mesh will be more demanding in terms of machine size and memory but lead to more accurate results in most cases.</p>  # noqa: E501

        :return: The fineness of this OneOfSubmeshRefinementSizing.  # noqa: E501
        :rtype: str
        """
        return self._fineness

    @fineness.setter
    def fineness(self, fineness):
        """Sets the fineness of this OneOfSubmeshRefinementSizing.

        <p>Choose between <i>Automatic</i> and <i>Manual</i> mesh settings. <a href='https://www.simscale.com/docs/analysis-types/incompressible-lbm/#mesh' target='_blank'>Learn more.</a></p><p><b>Note:</b> Mesh fineness impacts the accuracy of your results as well as computing time and result size. A finer mesh will be more demanding in terms of machine size and memory but lead to more accurate results in most cases.</p>  # noqa: E501

        :param fineness: The fineness of this OneOfSubmeshRefinementSizing.  # noqa: E501
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
    def minimum_edge_length(self):
        """Gets the minimum_edge_length of this OneOfSubmeshRefinementSizing.  # noqa: E501


        :return: The minimum_edge_length of this OneOfSubmeshRefinementSizing.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._minimum_edge_length

    @minimum_edge_length.setter
    def minimum_edge_length(self, minimum_edge_length):
        """Sets the minimum_edge_length of this OneOfSubmeshRefinementSizing.


        :param minimum_edge_length: The minimum_edge_length of this OneOfSubmeshRefinementSizing.  # noqa: E501
        :type: DimensionalLength
        """

        self._minimum_edge_length = minimum_edge_length

    @property
    def maximum_edge_length(self):
        """Gets the maximum_edge_length of this OneOfSubmeshRefinementSizing.  # noqa: E501


        :return: The maximum_edge_length of this OneOfSubmeshRefinementSizing.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._maximum_edge_length

    @maximum_edge_length.setter
    def maximum_edge_length(self, maximum_edge_length):
        """Sets the maximum_edge_length of this OneOfSubmeshRefinementSizing.


        :param maximum_edge_length: The maximum_edge_length of this OneOfSubmeshRefinementSizing.  # noqa: E501
        :type: DimensionalLength
        """

        self._maximum_edge_length = maximum_edge_length

    @property
    def grading(self):
        """Gets the grading of this OneOfSubmeshRefinementSizing.  # noqa: E501


        :return: The grading of this OneOfSubmeshRefinementSizing.  # noqa: E501
        :rtype: OneOfManualMeshSizingGrading
        """
        return self._grading

    @grading.setter
    def grading(self, grading):
        """Sets the grading of this OneOfSubmeshRefinementSizing.


        :param grading: The grading of this OneOfSubmeshRefinementSizing.  # noqa: E501
        :type: OneOfManualMeshSizingGrading
        """

        self._grading = grading

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
        if not isinstance(other, OneOfSubmeshRefinementSizing):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfSubmeshRefinementSizing):
            return True

        return self.to_dict() != other.to_dict()
