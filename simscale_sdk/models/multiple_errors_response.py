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


class MultipleErrorsResponse(object):
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
        'severity': 'LogSeverity',
        'entries': 'list[LogEntry]',
        'trace': 'str'
    }

    attribute_map = {
        'severity': 'severity',
        'entries': 'entries',
        'trace': 'trace'
    }

    def __init__(self, severity=None, entries=None, trace=None, local_vars_configuration=None):  # noqa: E501
        """MultipleErrorsResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._severity = None
        self._entries = None
        self._trace = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if entries is not None:
            self.entries = entries
        if trace is not None:
            self.trace = trace

    @property
    def severity(self):
        """Gets the severity of this MultipleErrorsResponse.  # noqa: E501


        :return: The severity of this MultipleErrorsResponse.  # noqa: E501
        :rtype: LogSeverity
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this MultipleErrorsResponse.


        :param severity: The severity of this MultipleErrorsResponse.  # noqa: E501
        :type: LogSeverity
        """

        self._severity = severity

    @property
    def entries(self):
        """Gets the entries of this MultipleErrorsResponse.  # noqa: E501


        :return: The entries of this MultipleErrorsResponse.  # noqa: E501
        :rtype: list[LogEntry]
        """
        return self._entries

    @entries.setter
    def entries(self, entries):
        """Sets the entries of this MultipleErrorsResponse.


        :param entries: The entries of this MultipleErrorsResponse.  # noqa: E501
        :type: list[LogEntry]
        """

        self._entries = entries

    @property
    def trace(self):
        """Gets the trace of this MultipleErrorsResponse.  # noqa: E501


        :return: The trace of this MultipleErrorsResponse.  # noqa: E501
        :rtype: str
        """
        return self._trace

    @trace.setter
    def trace(self, trace):
        """Sets the trace of this MultipleErrorsResponse.


        :param trace: The trace of this MultipleErrorsResponse.  # noqa: E501
        :type: str
        """

        self._trace = trace

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
        if not isinstance(other, MultipleErrorsResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MultipleErrorsResponse):
            return True

        return self.to_dict() != other.to_dict()
