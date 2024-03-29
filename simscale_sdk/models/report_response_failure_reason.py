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


class ReportResponseFailureReason(object):
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
        'severity': 'str',
        'code': 'str',
        'message': 'str',
        'details': 'dict(str, object)'
    }

    attribute_map = {
        'severity': 'severity',
        'code': 'code',
        'message': 'message',
        'details': 'details'
    }

    def __init__(self, severity=None, code=None, message=None, details=None, local_vars_configuration=None):  # noqa: E501
        """ReportResponseFailureReason - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._severity = None
        self._code = None
        self._message = None
        self._details = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if code is not None:
            self.code = code
        if message is not None:
            self.message = message
        if details is not None:
            self.details = details

    @property
    def severity(self):
        """Gets the severity of this ReportResponseFailureReason.  # noqa: E501


        :return: The severity of this ReportResponseFailureReason.  # noqa: E501
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ReportResponseFailureReason.


        :param severity: The severity of this ReportResponseFailureReason.  # noqa: E501
        :type: str
        """
        allowed_values = ["INFO", "SUCCESS", "WARNING", "ERROR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and severity not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `severity` ({0}), must be one of {1}"  # noqa: E501
                .format(severity, allowed_values)
            )

        self._severity = severity

    @property
    def code(self):
        """Gets the code of this ReportResponseFailureReason.  # noqa: E501

        Code for e.g. programmatic handling of error conditions.  # noqa: E501

        :return: The code of this ReportResponseFailureReason.  # noqa: E501
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ReportResponseFailureReason.

        Code for e.g. programmatic handling of error conditions.  # noqa: E501

        :param code: The code of this ReportResponseFailureReason.  # noqa: E501
        :type: str
        """

        self._code = code

    @property
    def message(self):
        """Gets the message of this ReportResponseFailureReason.  # noqa: E501

        Human-readable description of the entry.  # noqa: E501

        :return: The message of this ReportResponseFailureReason.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ReportResponseFailureReason.

        Human-readable description of the entry.  # noqa: E501

        :param message: The message of this ReportResponseFailureReason.  # noqa: E501
        :type: str
        """

        self._message = message

    @property
    def details(self):
        """Gets the details of this ReportResponseFailureReason.  # noqa: E501

        Additional data to interpret and handle the entry.  # noqa: E501

        :return: The details of this ReportResponseFailureReason.  # noqa: E501
        :rtype: dict(str, object)
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this ReportResponseFailureReason.

        Additional data to interpret and handle the entry.  # noqa: E501

        :param details: The details of this ReportResponseFailureReason.  # noqa: E501
        :type: dict(str, object)
        """

        self._details = details

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
        if not isinstance(other, ReportResponseFailureReason):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, ReportResponseFailureReason):
            return True

        return self.to_dict() != other.to_dict()
