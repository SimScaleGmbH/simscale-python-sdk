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


class OneOfComputingCoreDomainDecomposition(object):
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
        'max_element_group_size': 'int',
        'num_partitions': 'int',
        'partitioner': 'str'
    }

    attribute_map = {
        'type': 'type',
        'max_element_group_size': 'maxElementGroupSize',
        'num_partitions': 'numPartitions',
        'partitioner': 'partitioner'
    }

    discriminator_value_class_map = {
        'AUTOMATIC': 'AutomaticDomainDecomposition',
        'CENTRALIZED': 'CentralizedDomainDecomposition',
        'ELEMENT_GROUPS': 'ElementGroupsDomainDecomposition',
        'CUSTOM': 'CustomDomainDecomposition'
    }

    def __init__(self, type='CUSTOM', max_element_group_size=None, num_partitions=None, partitioner=None, local_vars_configuration=None):  # noqa: E501
        """OneOfComputingCoreDomainDecomposition - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._max_element_group_size = None
        self._num_partitions = None
        self._partitioner = None
        self.discriminator = 'type'

        self.type = type
        if max_element_group_size is not None:
            self.max_element_group_size = max_element_group_size
        if num_partitions is not None:
            self.num_partitions = num_partitions
        if partitioner is not None:
            self.partitioner = partitioner

    @property
    def type(self):
        """Gets the type of this OneOfComputingCoreDomainDecomposition.  # noqa: E501

        Schema name: CustomDomainDecomposition  # noqa: E501

        :return: The type of this OneOfComputingCoreDomainDecomposition.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfComputingCoreDomainDecomposition.

        Schema name: CustomDomainDecomposition  # noqa: E501

        :param type: The type of this OneOfComputingCoreDomainDecomposition.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def max_element_group_size(self):
        """Gets the max_element_group_size of this OneOfComputingCoreDomainDecomposition.  # noqa: E501


        :return: The max_element_group_size of this OneOfComputingCoreDomainDecomposition.  # noqa: E501
        :rtype: int
        """
        return self._max_element_group_size

    @max_element_group_size.setter
    def max_element_group_size(self, max_element_group_size):
        """Sets the max_element_group_size of this OneOfComputingCoreDomainDecomposition.


        :param max_element_group_size: The max_element_group_size of this OneOfComputingCoreDomainDecomposition.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_element_group_size is not None and max_element_group_size < 1):  # noqa: E501
            raise ValueError("Invalid value for `max_element_group_size`, must be a value greater than or equal to `1`")  # noqa: E501

        self._max_element_group_size = max_element_group_size

    @property
    def num_partitions(self):
        """Gets the num_partitions of this OneOfComputingCoreDomainDecomposition.  # noqa: E501


        :return: The num_partitions of this OneOfComputingCoreDomainDecomposition.  # noqa: E501
        :rtype: int
        """
        return self._num_partitions

    @num_partitions.setter
    def num_partitions(self, num_partitions):
        """Sets the num_partitions of this OneOfComputingCoreDomainDecomposition.


        :param num_partitions: The num_partitions of this OneOfComputingCoreDomainDecomposition.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                num_partitions is not None and num_partitions < 1):  # noqa: E501
            raise ValueError("Invalid value for `num_partitions`, must be a value greater than or equal to `1`")  # noqa: E501

        self._num_partitions = num_partitions

    @property
    def partitioner(self):
        """Gets the partitioner of this OneOfComputingCoreDomainDecomposition.  # noqa: E501


        :return: The partitioner of this OneOfComputingCoreDomainDecomposition.  # noqa: E501
        :rtype: str
        """
        return self._partitioner

    @partitioner.setter
    def partitioner(self, partitioner):
        """Sets the partitioner of this OneOfComputingCoreDomainDecomposition.


        :param partitioner: The partitioner of this OneOfComputingCoreDomainDecomposition.  # noqa: E501
        :type: str
        """
        allowed_values = ["METIS", "SCOTCH"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and partitioner not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `partitioner` ({0}), must be one of {1}"  # noqa: E501
                .format(partitioner, allowed_values)
            )

        self._partitioner = partitioner

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
        if not isinstance(other, OneOfComputingCoreDomainDecomposition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfComputingCoreDomainDecomposition):
            return True

        return self.to_dict() != other.to_dict()
