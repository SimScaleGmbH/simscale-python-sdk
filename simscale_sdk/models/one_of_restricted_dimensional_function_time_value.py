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


class OneOfRestrictedDimensionalFunctionTimeValue(object):
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
        'value': 'float',
        'expression': 'str',
        'available_variables': 'list[FunctionParameter]',
        'coefficients': 'list[float]',
        'parameter_base_unit': 'str',
        'label': 'str',
        'table_id': 'str',
        'result_index': 'list[int]',
        'independent_variables': 'list[TableFunctionParameter]',
        'separator': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'expression': 'expression',
        'available_variables': 'availableVariables',
        'coefficients': 'coefficients',
        'parameter_base_unit': 'parameterBaseUnit',
        'label': 'label',
        'table_id': 'tableId',
        'result_index': 'resultIndex',
        'independent_variables': 'independentVariables',
        'separator': 'separator'
    }

    discriminator_value_class_map = {
        'CONSTANT': 'ConstantFunction',
        'EXPRESSION': 'ExpressionFunction',
        'POLYNOMIAL': 'PolynomialFunction',
        'RESTRICTED_TABLE_DEFINED': 'RestrictedTableDefinedFunction'
    }

    def __init__(self, type='RESTRICTED_TABLE_DEFINED', value=None, expression=None, available_variables=None, coefficients=None, parameter_base_unit=None, label=None, table_id=None, result_index=None, independent_variables=None, separator=None, local_vars_configuration=None):  # noqa: E501
        """OneOfRestrictedDimensionalFunctionTimeValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._value = None
        self._expression = None
        self._available_variables = None
        self._coefficients = None
        self._parameter_base_unit = None
        self._label = None
        self._table_id = None
        self._result_index = None
        self._independent_variables = None
        self._separator = None
        self.discriminator = 'type'

        self.type = type
        if value is not None:
            self.value = value
        if expression is not None:
            self.expression = expression
        if available_variables is not None:
            self.available_variables = available_variables
        if coefficients is not None:
            self.coefficients = coefficients
        self.parameter_base_unit = parameter_base_unit
        if label is not None:
            self.label = label
        if table_id is not None:
            self.table_id = table_id
        if result_index is not None:
            self.result_index = result_index
        if independent_variables is not None:
            self.independent_variables = independent_variables
        if separator is not None:
            self.separator = separator

    @property
    def type(self):
        """Gets the type of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501

        Schema name: RestrictedTableDefinedFunction  # noqa: E501

        :return: The type of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfRestrictedDimensionalFunctionTimeValue.

        Schema name: RestrictedTableDefinedFunction  # noqa: E501

        :param type: The type of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def value(self):
        """Gets the value of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501


        :return: The value of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OneOfRestrictedDimensionalFunctionTimeValue.


        :param value: The value of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def expression(self):
        """Gets the expression of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501


        :return: The expression of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this OneOfRestrictedDimensionalFunctionTimeValue.


        :param expression: The expression of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :type: str
        """

        self._expression = expression

    @property
    def available_variables(self):
        """Gets the available_variables of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501


        :return: The available_variables of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :rtype: list[FunctionParameter]
        """
        return self._available_variables

    @available_variables.setter
    def available_variables(self, available_variables):
        """Sets the available_variables of this OneOfRestrictedDimensionalFunctionTimeValue.


        :param available_variables: The available_variables of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :type: list[FunctionParameter]
        """

        self._available_variables = available_variables

    @property
    def coefficients(self):
        """Gets the coefficients of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501


        :return: The coefficients of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :rtype: list[float]
        """
        return self._coefficients

    @coefficients.setter
    def coefficients(self, coefficients):
        """Sets the coefficients of this OneOfRestrictedDimensionalFunctionTimeValue.


        :param coefficients: The coefficients of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :type: list[float]
        """

        self._coefficients = coefficients

    @property
    def parameter_base_unit(self):
        """Gets the parameter_base_unit of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501


        :return: The parameter_base_unit of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :rtype: str
        """
        return self._parameter_base_unit

    @parameter_base_unit.setter
    def parameter_base_unit(self, parameter_base_unit):
        """Sets the parameter_base_unit of this OneOfRestrictedDimensionalFunctionTimeValue.


        :param parameter_base_unit: The parameter_base_unit of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and parameter_base_unit is None:  # noqa: E501
            raise ValueError("Invalid value for `parameter_base_unit`, must not be `None`")  # noqa: E501

        self._parameter_base_unit = parameter_base_unit

    @property
    def label(self):
        """Gets the label of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501


        :return: The label of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this OneOfRestrictedDimensionalFunctionTimeValue.


        :param label: The label of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def table_id(self):
        """Gets the table_id of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501

        The ID of the imported table.  # noqa: E501

        :return: The table_id of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :rtype: str
        """
        return self._table_id

    @table_id.setter
    def table_id(self, table_id):
        """Sets the table_id of this OneOfRestrictedDimensionalFunctionTimeValue.

        The ID of the imported table.  # noqa: E501

        :param table_id: The table_id of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :type: str
        """

        self._table_id = table_id

    @property
    def result_index(self):
        """Gets the result_index of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501

        Indicates which column(s) of the table contains the result values. One-based indexing must be used. For example, set this field to '[2]' if the second column of the table contains the dependent variable values.  # noqa: E501

        :return: The result_index of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :rtype: list[int]
        """
        return self._result_index

    @result_index.setter
    def result_index(self, result_index):
        """Sets the result_index of this OneOfRestrictedDimensionalFunctionTimeValue.

        Indicates which column(s) of the table contains the result values. One-based indexing must be used. For example, set this field to '[2]' if the second column of the table contains the dependent variable values.  # noqa: E501

        :param result_index: The result_index of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :type: list[int]
        """

        self._result_index = result_index

    @property
    def independent_variables(self):
        """Gets the independent_variables of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501


        :return: The independent_variables of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :rtype: list[TableFunctionParameter]
        """
        return self._independent_variables

    @independent_variables.setter
    def independent_variables(self, independent_variables):
        """Sets the independent_variables of this OneOfRestrictedDimensionalFunctionTimeValue.


        :param independent_variables: The independent_variables of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :type: list[TableFunctionParameter]
        """

        self._independent_variables = independent_variables

    @property
    def separator(self):
        """Gets the separator of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501

        Values in each row are separated by this character. Also known as a delimiter.  # noqa: E501

        :return: The separator of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :rtype: str
        """
        return self._separator

    @separator.setter
    def separator(self, separator):
        """Sets the separator of this OneOfRestrictedDimensionalFunctionTimeValue.

        Values in each row are separated by this character. Also known as a delimiter.  # noqa: E501

        :param separator: The separator of this OneOfRestrictedDimensionalFunctionTimeValue.  # noqa: E501
        :type: str
        """

        self._separator = separator

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
        if not isinstance(other, OneOfRestrictedDimensionalFunctionTimeValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfRestrictedDimensionalFunctionTimeValue):
            return True

        return self.to_dict() != other.to_dict()
