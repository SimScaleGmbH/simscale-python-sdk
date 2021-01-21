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


class SimulationRun(object):
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
        'run_id': 'str',
        'name': 'str',
        'created_at': 'datetime',
        'started_at': 'datetime',
        'finished_at': 'datetime',
        'duration': 'str',
        'compute_resource': 'SimulationRunComputeResource',
        'status': 'Status',
        'progress': 'float'
    }

    attribute_map = {
        'run_id': 'runId',
        'name': 'name',
        'created_at': 'createdAt',
        'started_at': 'startedAt',
        'finished_at': 'finishedAt',
        'duration': 'duration',
        'compute_resource': 'computeResource',
        'status': 'status',
        'progress': 'progress'
    }

    def __init__(self, run_id=None, name=None, created_at=None, started_at=None, finished_at=None, duration=None, compute_resource=None, status=None, progress=None, local_vars_configuration=None):  # noqa: E501
        """SimulationRun - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._run_id = None
        self._name = None
        self._created_at = None
        self._started_at = None
        self._finished_at = None
        self._duration = None
        self._compute_resource = None
        self._status = None
        self._progress = None
        self.discriminator = None

        if run_id is not None:
            self.run_id = run_id
        self.name = name
        if created_at is not None:
            self.created_at = created_at
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        if duration is not None:
            self.duration = duration
        if compute_resource is not None:
            self.compute_resource = compute_resource
        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress

    @property
    def run_id(self):
        """Gets the run_id of this SimulationRun.  # noqa: E501


        :return: The run_id of this SimulationRun.  # noqa: E501
        :rtype: str
        """
        return self._run_id

    @run_id.setter
    def run_id(self, run_id):
        """Sets the run_id of this SimulationRun.


        :param run_id: The run_id of this SimulationRun.  # noqa: E501
        :type: str
        """

        self._run_id = run_id

    @property
    def name(self):
        """Gets the name of this SimulationRun.  # noqa: E501

        The name of the simulation run.  # noqa: E501

        :return: The name of this SimulationRun.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SimulationRun.

        The name of the simulation run.  # noqa: E501

        :param name: The name of this SimulationRun.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def created_at(self):
        """Gets the created_at of this SimulationRun.  # noqa: E501

        The time when the simulation run was created.  # noqa: E501

        :return: The created_at of this SimulationRun.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this SimulationRun.

        The time when the simulation run was created.  # noqa: E501

        :param created_at: The created_at of this SimulationRun.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def started_at(self):
        """Gets the started_at of this SimulationRun.  # noqa: E501

        The time when the simulation run was started.  # noqa: E501

        :return: The started_at of this SimulationRun.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this SimulationRun.

        The time when the simulation run was started.  # noqa: E501

        :param started_at: The started_at of this SimulationRun.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this SimulationRun.  # noqa: E501

        The time when the simulation run was finished.  # noqa: E501

        :return: The finished_at of this SimulationRun.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this SimulationRun.

        The time when the simulation run was finished.  # noqa: E501

        :param finished_at: The finished_at of this SimulationRun.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def duration(self):
        """Gets the duration of this SimulationRun.  # noqa: E501

        The actual duration of the simulation run.  # noqa: E501

        :return: The duration of this SimulationRun.  # noqa: E501
        :rtype: str
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        """Sets the duration of this SimulationRun.

        The actual duration of the simulation run.  # noqa: E501

        :param duration: The duration of this SimulationRun.  # noqa: E501
        :type: str
        """

        self._duration = duration

    @property
    def compute_resource(self):
        """Gets the compute_resource of this SimulationRun.  # noqa: E501


        :return: The compute_resource of this SimulationRun.  # noqa: E501
        :rtype: SimulationRunComputeResource
        """
        return self._compute_resource

    @compute_resource.setter
    def compute_resource(self, compute_resource):
        """Sets the compute_resource of this SimulationRun.


        :param compute_resource: The compute_resource of this SimulationRun.  # noqa: E501
        :type: SimulationRunComputeResource
        """

        self._compute_resource = compute_resource

    @property
    def status(self):
        """Gets the status of this SimulationRun.  # noqa: E501


        :return: The status of this SimulationRun.  # noqa: E501
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this SimulationRun.


        :param status: The status of this SimulationRun.  # noqa: E501
        :type: Status
        """

        self._status = status

    @property
    def progress(self):
        """Gets the progress of this SimulationRun.  # noqa: E501

        The current progress while the simulation run is in progress.  # noqa: E501

        :return: The progress of this SimulationRun.  # noqa: E501
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this SimulationRun.

        The current progress while the simulation run is in progress.  # noqa: E501

        :param progress: The progress of this SimulationRun.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                progress is not None and progress > 1):  # noqa: E501
            raise ValueError("Invalid value for `progress`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                progress is not None and progress < 0):  # noqa: E501
            raise ValueError("Invalid value for `progress`, must be a value greater than or equal to `0`")  # noqa: E501

        self._progress = progress

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
        if not isinstance(other, SimulationRun):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimulationRun):
            return True

        return self.to_dict() != other.to_dict()
