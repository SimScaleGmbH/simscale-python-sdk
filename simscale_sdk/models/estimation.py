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


class Estimation(object):
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
        'duration': 'Duration',
        'compute_resource': 'ComputeResource',
        'cell_count': 'CellCount',
        'total_run_count': 'int'
    }

    attribute_map = {
        'duration': 'duration',
        'compute_resource': 'computeResource',
        'cell_count': 'cellCount',
        'total_run_count': 'totalRunCount'
    }

    def __init__(self, duration=None, compute_resource=None, cell_count=None, total_run_count=None, local_vars_configuration=None):  # noqa: E501
        """Estimation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._duration = None
        self._compute_resource = None
        self._cell_count = None
        self._total_run_count = None
        self.discriminator = None

        if duration is not None:
            self.duration = duration
        if compute_resource is not None:
            self.compute_resource = compute_resource
        if cell_count is not None:
            self.cell_count = cell_count
        if total_run_count is not None:
            self.total_run_count = total_run_count

    @property
    def duration(self):
        """Gets the duration of this Estimation.  # noqa: E501


        :return: The duration of this Estimation.  # noqa: E501
        :rtype: Duration
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this Estimation.


        :param duration: The duration of this Estimation.  # noqa: E501
        :type: Duration
        """

        self._duration = duration

    @property
    def compute_resource(self):
        """Gets the compute_resource of this Estimation.  # noqa: E501


        :return: The compute_resource of this Estimation.  # noqa: E501
        :rtype: ComputeResource
        """
        return self._compute_resource

    @compute_resource.setter
    def compute_resource(self, compute_resource):
        """Sets the compute_resource of this Estimation.


        :param compute_resource: The compute_resource of this Estimation.  # noqa: E501
        :type: ComputeResource
        """

        self._compute_resource = compute_resource

    @property
    def cell_count(self):
        """Gets the cell_count of this Estimation.  # noqa: E501


        :return: The cell_count of this Estimation.  # noqa: E501
        :rtype: CellCount
        """
        return self._cell_count

    @cell_count.setter
    def cell_count(self, cell_count):
        """Sets the cell_count of this Estimation.


        :param cell_count: The cell_count of this Estimation.  # noqa: E501
        :type: CellCount
        """

        self._cell_count = cell_count

    @property
    def total_run_count(self):
        """Gets the total_run_count of this Estimation.  # noqa: E501

        The total number of jobs that will be triggered for this simulation run or mesh operation.  # noqa: E501

        :return: The total_run_count of this Estimation.  # noqa: E501
        :rtype: int
        """
        return self._total_run_count

    @total_run_count.setter
    def total_run_count(self, total_run_count):
        """Sets the total_run_count of this Estimation.

        The total number of jobs that will be triggered for this simulation run or mesh operation.  # noqa: E501

        :param total_run_count: The total_run_count of this Estimation.  # noqa: E501
        :type: int
        """

        self._total_run_count = total_run_count

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
        if not isinstance(other, Estimation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Estimation):
            return True

        return self.to_dict() != other.to_dict()
