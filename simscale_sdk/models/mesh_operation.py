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


class MeshOperation(object):
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
        'mesh_operation_id': 'str',
        'name': 'str',
        'version': 'str',
        'geometry_id': 'str',
        'model': 'Algorithm',
        'created_at': 'datetime',
        'modified_at': 'datetime',
        'started_at': 'datetime',
        'finished_at': 'datetime',
        'compute_resource': 'MeshOperationComputeResource',
        'status': 'Status',
        'progress': 'float',
        'mesh_id': 'str'
    }

    attribute_map = {
        'mesh_operation_id': 'meshOperationId',
        'name': 'name',
        'version': 'version',
        'geometry_id': 'geometryId',
        'model': 'model',
        'created_at': 'createdAt',
        'modified_at': 'modifiedAt',
        'started_at': 'startedAt',
        'finished_at': 'finishedAt',
        'compute_resource': 'computeResource',
        'status': 'status',
        'progress': 'progress',
        'mesh_id': 'meshId'
    }

    def __init__(self, mesh_operation_id=None, name=None, version='5.0', geometry_id=None, model=None, created_at=None, modified_at=None, started_at=None, finished_at=None, compute_resource=None, status=None, progress=None, mesh_id=None, local_vars_configuration=None):  # noqa: E501
        """MeshOperation - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._mesh_operation_id = None
        self._name = None
        self._version = None
        self._geometry_id = None
        self._model = None
        self._created_at = None
        self._modified_at = None
        self._started_at = None
        self._finished_at = None
        self._compute_resource = None
        self._status = None
        self._progress = None
        self._mesh_id = None
        self.discriminator = None

        if mesh_operation_id is not None:
            self.mesh_operation_id = mesh_operation_id
        self.name = name
        self.version = version
        self.geometry_id = geometry_id
        self.model = model
        if created_at is not None:
            self.created_at = created_at
        if modified_at is not None:
            self.modified_at = modified_at
        if started_at is not None:
            self.started_at = started_at
        if finished_at is not None:
            self.finished_at = finished_at
        if compute_resource is not None:
            self.compute_resource = compute_resource
        if status is not None:
            self.status = status
        if progress is not None:
            self.progress = progress
        if mesh_id is not None:
            self.mesh_id = mesh_id

    @property
    def mesh_operation_id(self):
        """Gets the mesh_operation_id of this MeshOperation.  # noqa: E501

        The mesh operation ID.  # noqa: E501

        :return: The mesh_operation_id of this MeshOperation.  # noqa: E501
        :rtype: str
        """
        return self._mesh_operation_id

    @mesh_operation_id.setter
    def mesh_operation_id(self, mesh_operation_id):
        """Sets the mesh_operation_id of this MeshOperation.

        The mesh operation ID.  # noqa: E501

        :param mesh_operation_id: The mesh_operation_id of this MeshOperation.  # noqa: E501
        :type: str
        """

        self._mesh_operation_id = mesh_operation_id

    @property
    def name(self):
        """Gets the name of this MeshOperation.  # noqa: E501

        The name of the mesh operation.  # noqa: E501

        :return: The name of this MeshOperation.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MeshOperation.

        The name of the mesh operation.  # noqa: E501

        :param name: The name of this MeshOperation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def version(self):
        """Gets the version of this MeshOperation.  # noqa: E501


        :return: The version of this MeshOperation.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this MeshOperation.


        :param version: The version of this MeshOperation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and version is None:  # noqa: E501
            raise ValueError("Invalid value for `version`, must not be `None`")  # noqa: E501

        self._version = version

    @property
    def geometry_id(self):
        """Gets the geometry_id of this MeshOperation.  # noqa: E501

        The geometry ID of the mesh operation.  # noqa: E501

        :return: The geometry_id of this MeshOperation.  # noqa: E501
        :rtype: str
        """
        return self._geometry_id

    @geometry_id.setter
    def geometry_id(self, geometry_id):
        """Sets the geometry_id of this MeshOperation.

        The geometry ID of the mesh operation.  # noqa: E501

        :param geometry_id: The geometry_id of this MeshOperation.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and geometry_id is None:  # noqa: E501
            raise ValueError("Invalid value for `geometry_id`, must not be `None`")  # noqa: E501

        self._geometry_id = geometry_id

    @property
    def model(self):
        """Gets the model of this MeshOperation.  # noqa: E501


        :return: The model of this MeshOperation.  # noqa: E501
        :rtype: Algorithm
        """
        return self._model

    @model.setter
    def model(self, model):
        """Sets the model of this MeshOperation.


        :param model: The model of this MeshOperation.  # noqa: E501
        :type: Algorithm
        """
        if self.local_vars_configuration.client_side_validation and model is None:  # noqa: E501
            raise ValueError("Invalid value for `model`, must not be `None`")  # noqa: E501

        self._model = model

    @property
    def created_at(self):
        """Gets the created_at of this MeshOperation.  # noqa: E501

        The time the mesh operation was created.  # noqa: E501

        :return: The created_at of this MeshOperation.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this MeshOperation.

        The time the mesh operation was created.  # noqa: E501

        :param created_at: The created_at of this MeshOperation.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def modified_at(self):
        """Gets the modified_at of this MeshOperation.  # noqa: E501

        The time the mesh operation was last modified.  # noqa: E501

        :return: The modified_at of this MeshOperation.  # noqa: E501
        :rtype: datetime
        """
        return self._modified_at

    @modified_at.setter
    def modified_at(self, modified_at):
        """Sets the modified_at of this MeshOperation.

        The time the mesh operation was last modified.  # noqa: E501

        :param modified_at: The modified_at of this MeshOperation.  # noqa: E501
        :type: datetime
        """

        self._modified_at = modified_at

    @property
    def started_at(self):
        """Gets the started_at of this MeshOperation.  # noqa: E501

        The time the mesh operation was started.  # noqa: E501

        :return: The started_at of this MeshOperation.  # noqa: E501
        :rtype: datetime
        """
        return self._started_at

    @started_at.setter
    def started_at(self, started_at):
        """Sets the started_at of this MeshOperation.

        The time the mesh operation was started.  # noqa: E501

        :param started_at: The started_at of this MeshOperation.  # noqa: E501
        :type: datetime
        """

        self._started_at = started_at

    @property
    def finished_at(self):
        """Gets the finished_at of this MeshOperation.  # noqa: E501

        The time the mesh operation was finished.  # noqa: E501

        :return: The finished_at of this MeshOperation.  # noqa: E501
        :rtype: datetime
        """
        return self._finished_at

    @finished_at.setter
    def finished_at(self, finished_at):
        """Sets the finished_at of this MeshOperation.

        The time the mesh operation was finished.  # noqa: E501

        :param finished_at: The finished_at of this MeshOperation.  # noqa: E501
        :type: datetime
        """

        self._finished_at = finished_at

    @property
    def compute_resource(self):
        """Gets the compute_resource of this MeshOperation.  # noqa: E501


        :return: The compute_resource of this MeshOperation.  # noqa: E501
        :rtype: MeshOperationComputeResource
        """
        return self._compute_resource

    @compute_resource.setter
    def compute_resource(self, compute_resource):
        """Sets the compute_resource of this MeshOperation.


        :param compute_resource: The compute_resource of this MeshOperation.  # noqa: E501
        :type: MeshOperationComputeResource
        """

        self._compute_resource = compute_resource

    @property
    def status(self):
        """Gets the status of this MeshOperation.  # noqa: E501


        :return: The status of this MeshOperation.  # noqa: E501
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MeshOperation.


        :param status: The status of this MeshOperation.  # noqa: E501
        :type: Status
        """

        self._status = status

    @property
    def progress(self):
        """Gets the progress of this MeshOperation.  # noqa: E501

        The current progress while the mesh operation is in progress.  # noqa: E501

        :return: The progress of this MeshOperation.  # noqa: E501
        :rtype: float
        """
        return self._progress

    @progress.setter
    def progress(self, progress):
        """Sets the progress of this MeshOperation.

        The current progress while the mesh operation is in progress.  # noqa: E501

        :param progress: The progress of this MeshOperation.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                progress is not None and progress > 1):  # noqa: E501
            raise ValueError("Invalid value for `progress`, must be a value less than or equal to `1`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                progress is not None and progress < 0):  # noqa: E501
            raise ValueError("Invalid value for `progress`, must be a value greater than or equal to `0`")  # noqa: E501

        self._progress = progress

    @property
    def mesh_id(self):
        """Gets the mesh_id of this MeshOperation.  # noqa: E501

        The ID of the generated mesh.  # noqa: E501

        :return: The mesh_id of this MeshOperation.  # noqa: E501
        :rtype: str
        """
        return self._mesh_id

    @mesh_id.setter
    def mesh_id(self, mesh_id):
        """Sets the mesh_id of this MeshOperation.

        The ID of the generated mesh.  # noqa: E501

        :param mesh_id: The mesh_id of this MeshOperation.  # noqa: E501
        :type: str
        """

        self._mesh_id = mesh_id

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
        if not isinstance(other, MeshOperation):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MeshOperation):
            return True

        return self.to_dict() != other.to_dict()
