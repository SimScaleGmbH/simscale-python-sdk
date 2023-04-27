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


class ReportRequest(object):
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
        'name': 'str',
        'description': 'str',
        'result_ids': 'list[str]',
        'report_properties': 'OneOfReportProperties',
        'report_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'result_ids': 'resultIds',
        'report_properties': 'reportProperties',
        'report_id': 'reportId'
    }

    def __init__(self, name=None, description=None, result_ids=None, report_properties=None, report_id=None, local_vars_configuration=None):  # noqa: E501
        """ReportRequest - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._name = None
        self._description = None
        self._result_ids = None
        self._report_properties = None
        self._report_id = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        self.result_ids = result_ids
        self.report_properties = report_properties
        if report_id is not None:
            self.report_id = report_id

    @property
    def name(self):
        """Gets the name of this ReportRequest.  # noqa: E501

        The name of the report.  # noqa: E501

        :return: The name of this ReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ReportRequest.

        The name of the report.  # noqa: E501

        :param name: The name of this ReportRequest.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) > 200):
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                name is not None and len(name) < 1):
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this ReportRequest.  # noqa: E501

        The description of the report.  # noqa: E501

        :return: The description of this ReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ReportRequest.

        The description of the report.  # noqa: E501

        :param description: The description of this ReportRequest.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) > 1000):
            raise ValueError("Invalid value for `description`, length must be less than or equal to `1000`")  # noqa: E501
        if (self.local_vars_configuration.client_side_validation and
                description is not None and len(description) < 1):
            raise ValueError("Invalid value for `description`, length must be greater than or equal to `1`")  # noqa: E501

        self._description = description

    @property
    def result_ids(self):
        """Gets the result_ids of this ReportRequest.  # noqa: E501

        The resultIds the report should be created for.  # noqa: E501

        :return: The result_ids of this ReportRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._result_ids

    @result_ids.setter
    def result_ids(self, result_ids):
        """Sets the result_ids of this ReportRequest.

        The resultIds the report should be created for.  # noqa: E501

        :param result_ids: The result_ids of this ReportRequest.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and result_ids is None:  # noqa: E501
            raise ValueError("Invalid value for `result_ids`, must not be `None`")  # noqa: E501

        self._result_ids = result_ids

    @property
    def report_properties(self):
        """Gets the report_properties of this ReportRequest.  # noqa: E501


        :return: The report_properties of this ReportRequest.  # noqa: E501
        :rtype: OneOfReportProperties
        """
        return self._report_properties

    @report_properties.setter
    def report_properties(self, report_properties):
        """Sets the report_properties of this ReportRequest.


        :param report_properties: The report_properties of this ReportRequest.  # noqa: E501
        :type: OneOfReportProperties
        """
        if self.local_vars_configuration.client_side_validation and report_properties is None:  # noqa: E501
            raise ValueError("Invalid value for `report_properties`, must not be `None`")  # noqa: E501

        self._report_properties = report_properties

    @property
    def report_id(self):
        """Gets the report_id of this ReportRequest.  # noqa: E501

        If provided, the newly created report will have this value for its UUID.  # noqa: E501

        :return: The report_id of this ReportRequest.  # noqa: E501
        :rtype: str
        """
        return self._report_id

    @report_id.setter
    def report_id(self, report_id):
        """Sets the report_id of this ReportRequest.

        If provided, the newly created report will have this value for its UUID.  # noqa: E501

        :param report_id: The report_id of this ReportRequest.  # noqa: E501
        :type: str
        """

        self._report_id = report_id

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
        if not isinstance(other, ReportRequest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportRequest):
            return True

        return self.to_dict() != other.to_dict()
