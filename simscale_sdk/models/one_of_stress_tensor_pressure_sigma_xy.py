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


class OneOfStressTensorPressureSigmaXY(object):
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
        'object_id': 'str',
        'result_index': 'list[int]',
        'independent_variables': 'list[TableFunctionParameter]',
        'separator': 'str',
        'out_of_bounds': 'str',
        'interpolation': 'str',
        'left_extrapolation': 'str',
        'right_extrapolation': 'str'
    }

    attribute_map = {
        'type': 'type',
        'value': 'value',
        'expression': 'expression',
        'available_variables': 'availableVariables',
        'coefficients': 'coefficients',
        'parameter_base_unit': 'parameterBaseUnit',
        'label': 'label',
        'object_id': 'objectId',
        'result_index': 'resultIndex',
        'independent_variables': 'independentVariables',
        'separator': 'separator',
        'out_of_bounds': 'outOfBounds',
        'interpolation': 'interpolation',
        'left_extrapolation': 'leftExtrapolation',
        'right_extrapolation': 'rightExtrapolation'
    }

    discriminator_value_class_map = {
        'CONSTANT': 'ConstantFunction',
        'EXPRESSION': 'ExpressionFunction',
        'POLYNOMIAL': 'PolynomialFunction',
        'TABLE_DEFINED': 'TableDefinedFunction'
    }

    def __init__(self, type='TABLE_DEFINED', value=None, expression=None, available_variables=None, coefficients=None, parameter_base_unit=None, label=None, object_id=None, result_index=None, independent_variables=None, separator=None, out_of_bounds=None, interpolation=None, left_extrapolation=None, right_extrapolation=None, local_vars_configuration=None):  # noqa: E501
        """OneOfStressTensorPressureSigmaXY - a model defined in OpenAPI"""  # noqa: E501
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
        self._object_id = None
        self._result_index = None
        self._independent_variables = None
        self._separator = None
        self._out_of_bounds = None
        self._interpolation = None
        self._left_extrapolation = None
        self._right_extrapolation = None
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
        if object_id is not None:
            self.object_id = object_id
        if result_index is not None:
            self.result_index = result_index
        if independent_variables is not None:
            self.independent_variables = independent_variables
        if separator is not None:
            self.separator = separator
        if out_of_bounds is not None:
            self.out_of_bounds = out_of_bounds
        if interpolation is not None:
            self.interpolation = interpolation
        if left_extrapolation is not None:
            self.left_extrapolation = left_extrapolation
        if right_extrapolation is not None:
            self.right_extrapolation = right_extrapolation

    @property
    def type(self):
        """Gets the type of this OneOfStressTensorPressureSigmaXY.  # noqa: E501


        :return: The type of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfStressTensorPressureSigmaXY.


        :param type: The type of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def value(self):
        """Gets the value of this OneOfStressTensorPressureSigmaXY.  # noqa: E501


        :return: The value of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :rtype: float
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this OneOfStressTensorPressureSigmaXY.


        :param value: The value of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :type: float
        """

        self._value = value

    @property
    def expression(self):
        """Gets the expression of this OneOfStressTensorPressureSigmaXY.  # noqa: E501


        :return: The expression of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :rtype: str
        """
        return self._expression

    @expression.setter
    def expression(self, expression):
        """Sets the expression of this OneOfStressTensorPressureSigmaXY.


        :param expression: The expression of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :type: str
        """

        self._expression = expression

    @property
    def available_variables(self):
        """Gets the available_variables of this OneOfStressTensorPressureSigmaXY.  # noqa: E501


        :return: The available_variables of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :rtype: list[FunctionParameter]
        """
        return self._available_variables

    @available_variables.setter
    def available_variables(self, available_variables):
        """Sets the available_variables of this OneOfStressTensorPressureSigmaXY.


        :param available_variables: The available_variables of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :type: list[FunctionParameter]
        """

        self._available_variables = available_variables

    @property
    def coefficients(self):
        """Gets the coefficients of this OneOfStressTensorPressureSigmaXY.  # noqa: E501


        :return: The coefficients of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :rtype: list[float]
        """
        return self._coefficients

    @coefficients.setter
    def coefficients(self, coefficients):
        """Sets the coefficients of this OneOfStressTensorPressureSigmaXY.


        :param coefficients: The coefficients of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :type: list[float]
        """

        self._coefficients = coefficients

    @property
    def parameter_base_unit(self):
        """Gets the parameter_base_unit of this OneOfStressTensorPressureSigmaXY.  # noqa: E501


        :return: The parameter_base_unit of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :rtype: str
        """
        return self._parameter_base_unit

    @parameter_base_unit.setter
    def parameter_base_unit(self, parameter_base_unit):
        """Sets the parameter_base_unit of this OneOfStressTensorPressureSigmaXY.


        :param parameter_base_unit: The parameter_base_unit of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and parameter_base_unit is None:  # noqa: E501
            raise ValueError("Invalid value for `parameter_base_unit`, must not be `None`")  # noqa: E501

        self._parameter_base_unit = parameter_base_unit

    @property
    def label(self):
        """Gets the label of this OneOfStressTensorPressureSigmaXY.  # noqa: E501


        :return: The label of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this OneOfStressTensorPressureSigmaXY.


        :param label: The label of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def object_id(self):
        """Gets the object_id of this OneOfStressTensorPressureSigmaXY.  # noqa: E501


        :return: The object_id of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this OneOfStressTensorPressureSigmaXY.


        :param object_id: The object_id of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def result_index(self):
        """Gets the result_index of this OneOfStressTensorPressureSigmaXY.  # noqa: E501


        :return: The result_index of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :rtype: list[int]
        """
        return self._result_index

    @result_index.setter
    def result_index(self, result_index):
        """Sets the result_index of this OneOfStressTensorPressureSigmaXY.


        :param result_index: The result_index of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :type: list[int]
        """

        self._result_index = result_index

    @property
    def independent_variables(self):
        """Gets the independent_variables of this OneOfStressTensorPressureSigmaXY.  # noqa: E501


        :return: The independent_variables of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :rtype: list[TableFunctionParameter]
        """
        return self._independent_variables

    @independent_variables.setter
    def independent_variables(self, independent_variables):
        """Sets the independent_variables of this OneOfStressTensorPressureSigmaXY.


        :param independent_variables: The independent_variables of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :type: list[TableFunctionParameter]
        """

        self._independent_variables = independent_variables

    @property
    def separator(self):
        """Gets the separator of this OneOfStressTensorPressureSigmaXY.  # noqa: E501


        :return: The separator of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :rtype: str
        """
        return self._separator

    @separator.setter
    def separator(self, separator):
        """Sets the separator of this OneOfStressTensorPressureSigmaXY.


        :param separator: The separator of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :type: str
        """

        self._separator = separator

    @property
    def out_of_bounds(self):
        """Gets the out_of_bounds of this OneOfStressTensorPressureSigmaXY.  # noqa: E501


        :return: The out_of_bounds of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :rtype: str
        """
        return self._out_of_bounds

    @out_of_bounds.setter
    def out_of_bounds(self, out_of_bounds):
        """Sets the out_of_bounds of this OneOfStressTensorPressureSigmaXY.


        :param out_of_bounds: The out_of_bounds of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLAMP"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and out_of_bounds not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `out_of_bounds` ({0}), must be one of {1}"  # noqa: E501
                .format(out_of_bounds, allowed_values)
            )

        self._out_of_bounds = out_of_bounds

    @property
    def interpolation(self):
        """Gets the interpolation of this OneOfStressTensorPressureSigmaXY.  # noqa: E501


        :return: The interpolation of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :rtype: str
        """
        return self._interpolation

    @interpolation.setter
    def interpolation(self, interpolation):
        """Sets the interpolation of this OneOfStressTensorPressureSigmaXY.


        :param interpolation: The interpolation of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :type: str
        """
        allowed_values = ["LINEAR", "LOGARITHMIC"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and interpolation not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `interpolation` ({0}), must be one of {1}"  # noqa: E501
                .format(interpolation, allowed_values)
            )

        self._interpolation = interpolation

    @property
    def left_extrapolation(self):
        """Gets the left_extrapolation of this OneOfStressTensorPressureSigmaXY.  # noqa: E501


        :return: The left_extrapolation of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :rtype: str
        """
        return self._left_extrapolation

    @left_extrapolation.setter
    def left_extrapolation(self, left_extrapolation):
        """Sets the left_extrapolation of this OneOfStressTensorPressureSigmaXY.


        :param left_extrapolation: The left_extrapolation of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONSTANT", "LINEAR", "NONE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and left_extrapolation not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `left_extrapolation` ({0}), must be one of {1}"  # noqa: E501
                .format(left_extrapolation, allowed_values)
            )

        self._left_extrapolation = left_extrapolation

    @property
    def right_extrapolation(self):
        """Gets the right_extrapolation of this OneOfStressTensorPressureSigmaXY.  # noqa: E501


        :return: The right_extrapolation of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :rtype: str
        """
        return self._right_extrapolation

    @right_extrapolation.setter
    def right_extrapolation(self, right_extrapolation):
        """Sets the right_extrapolation of this OneOfStressTensorPressureSigmaXY.


        :param right_extrapolation: The right_extrapolation of this OneOfStressTensorPressureSigmaXY.  # noqa: E501
        :type: str
        """
        allowed_values = ["CONSTANT", "LINEAR", "NONE"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and right_extrapolation not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `right_extrapolation` ({0}), must be one of {1}"  # noqa: E501
                .format(right_extrapolation, allowed_values)
            )

        self._right_extrapolation = right_extrapolation

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
        if not isinstance(other, OneOfStressTensorPressureSigmaXY):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfStressTensorPressureSigmaXY):
            return True

        return self.to_dict() != other.to_dict()
