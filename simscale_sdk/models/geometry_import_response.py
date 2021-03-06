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


class GeometryImportResponse(object):
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
        'geometry_import_id': 'str',
        'status': 'Status',
        'geometry_id': 'str',
        'failure_reason': 'LogEntry'
    }

    attribute_map = {
        'geometry_import_id': 'geometryImportId',
        'status': 'status',
        'geometry_id': 'geometryId',
        'failure_reason': 'failureReason'
    }

    def __init__(self, geometry_import_id=None, status=None, geometry_id=None, failure_reason=None, local_vars_configuration=None):  # noqa: E501
        """GeometryImportResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._geometry_import_id = None
        self._status = None
        self._geometry_id = None
        self._failure_reason = None
        self.discriminator = None

        self.geometry_import_id = geometry_import_id
        self.status = status
        if geometry_id is not None:
            self.geometry_id = geometry_id
        if failure_reason is not None:
            self.failure_reason = failure_reason

    @property
    def geometry_import_id(self):
        """Gets the geometry_import_id of this GeometryImportResponse.  # noqa: E501

        The ID of the geometry import operation.  # noqa: E501

        :return: The geometry_import_id of this GeometryImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._geometry_import_id

    @geometry_import_id.setter
    def geometry_import_id(self, geometry_import_id):
        """Sets the geometry_import_id of this GeometryImportResponse.

        The ID of the geometry import operation.  # noqa: E501

        :param geometry_import_id: The geometry_import_id of this GeometryImportResponse.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and geometry_import_id is None:  # noqa: E501
            raise ValueError("Invalid value for `geometry_import_id`, must not be `None`")  # noqa: E501

        self._geometry_import_id = geometry_import_id

    @property
    def status(self):
        """Gets the status of this GeometryImportResponse.  # noqa: E501


        :return: The status of this GeometryImportResponse.  # noqa: E501
        :rtype: Status
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this GeometryImportResponse.


        :param status: The status of this GeometryImportResponse.  # noqa: E501
        :type: Status
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

    @property
    def geometry_id(self):
        """Gets the geometry_id of this GeometryImportResponse.  # noqa: E501

        The ID of the imported geometry when the import succeeded.  # noqa: E501

        :return: The geometry_id of this GeometryImportResponse.  # noqa: E501
        :rtype: str
        """
        return self._geometry_id

    @geometry_id.setter
    def geometry_id(self, geometry_id):
        """Sets the geometry_id of this GeometryImportResponse.

        The ID of the imported geometry when the import succeeded.  # noqa: E501

        :param geometry_id: The geometry_id of this GeometryImportResponse.  # noqa: E501
        :type: str
        """

        self._geometry_id = geometry_id

    @property
    def failure_reason(self):
        """Gets the failure_reason of this GeometryImportResponse.  # noqa: E501


        :return: The failure_reason of this GeometryImportResponse.  # noqa: E501
        :rtype: LogEntry
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this GeometryImportResponse.


        :param failure_reason: The failure_reason of this GeometryImportResponse.  # noqa: E501
        :type: LogEntry
        """

        self._failure_reason = failure_reason

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
        if not isinstance(other, GeometryImportResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, GeometryImportResponse):
            return True

        return self.to_dict() != other.to_dict()
