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


class OneOfDimensionalVectorFunctionSpeedValue(object):
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
        'x': 'OneOfComponentVectorFunctionX',
        'y': 'OneOfComponentVectorFunctionY',
        'z': 'OneOfComponentVectorFunctionZ',
        'label': 'str',
        'object_id': 'str',
        'result_index': 'list[int]',
        'independent_variables': 'list[TableFunctionParameter]',
        'separator': 'str',
        'out_of_bounds': 'str'
    }

    attribute_map = {
        'type': 'type',
        'x': 'x',
        'y': 'y',
        'z': 'z',
        'label': 'label',
        'object_id': 'objectId',
        'result_index': 'resultIndex',
        'independent_variables': 'independentVariables',
        'separator': 'separator',
        'out_of_bounds': 'outOfBounds'
    }

    discriminator_value_class_map = {
        'COMPONENT': 'ComponentVectorFunction',
        'TABLE_DEFINED': 'TableDefinedVectorFunction'
    }

    def __init__(self, type='TABLE_DEFINED', x=None, y=None, z=None, label=None, object_id=None, result_index=None, independent_variables=None, separator=None, out_of_bounds=None, local_vars_configuration=None):  # noqa: E501
        """OneOfDimensionalVectorFunctionSpeedValue - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._x = None
        self._y = None
        self._z = None
        self._label = None
        self._object_id = None
        self._result_index = None
        self._independent_variables = None
        self._separator = None
        self._out_of_bounds = None
        self.discriminator = 'type'

        self.type = type
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y
        if z is not None:
            self.z = z
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

    @property
    def type(self):
        """Gets the type of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501


        :return: The type of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfDimensionalVectorFunctionSpeedValue.


        :param type: The type of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def x(self):
        """Gets the x of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501


        :return: The x of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :rtype: OneOfComponentVectorFunctionX
        """
        return self._x

    @x.setter
    def x(self, x):
        """Sets the x of this OneOfDimensionalVectorFunctionSpeedValue.


        :param x: The x of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :type: OneOfComponentVectorFunctionX
        """

        self._x = x

    @property
    def y(self):
        """Gets the y of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501


        :return: The y of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :rtype: OneOfComponentVectorFunctionY
        """
        return self._y

    @y.setter
    def y(self, y):
        """Sets the y of this OneOfDimensionalVectorFunctionSpeedValue.


        :param y: The y of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :type: OneOfComponentVectorFunctionY
        """

        self._y = y

    @property
    def z(self):
        """Gets the z of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501


        :return: The z of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :rtype: OneOfComponentVectorFunctionZ
        """
        return self._z

    @z.setter
    def z(self, z):
        """Sets the z of this OneOfDimensionalVectorFunctionSpeedValue.


        :param z: The z of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :type: OneOfComponentVectorFunctionZ
        """

        self._z = z

    @property
    def label(self):
        """Gets the label of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501


        :return: The label of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this OneOfDimensionalVectorFunctionSpeedValue.


        :param label: The label of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def object_id(self):
        """Gets the object_id of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501


        :return: The object_id of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :rtype: str
        """
        return self._object_id

    @object_id.setter
    def object_id(self, object_id):
        """Sets the object_id of this OneOfDimensionalVectorFunctionSpeedValue.


        :param object_id: The object_id of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :type: str
        """

        self._object_id = object_id

    @property
    def result_index(self):
        """Gets the result_index of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501


        :return: The result_index of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :rtype: list[int]
        """
        return self._result_index

    @result_index.setter
    def result_index(self, result_index):
        """Sets the result_index of this OneOfDimensionalVectorFunctionSpeedValue.


        :param result_index: The result_index of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :type: list[int]
        """

        self._result_index = result_index

    @property
    def independent_variables(self):
        """Gets the independent_variables of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501


        :return: The independent_variables of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :rtype: list[TableFunctionParameter]
        """
        return self._independent_variables

    @independent_variables.setter
    def independent_variables(self, independent_variables):
        """Sets the independent_variables of this OneOfDimensionalVectorFunctionSpeedValue.


        :param independent_variables: The independent_variables of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :type: list[TableFunctionParameter]
        """

        self._independent_variables = independent_variables

    @property
    def separator(self):
        """Gets the separator of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501


        :return: The separator of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :rtype: str
        """
        return self._separator

    @separator.setter
    def separator(self, separator):
        """Sets the separator of this OneOfDimensionalVectorFunctionSpeedValue.


        :param separator: The separator of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :type: str
        """

        self._separator = separator

    @property
    def out_of_bounds(self):
        """Gets the out_of_bounds of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501


        :return: The out_of_bounds of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :rtype: str
        """
        return self._out_of_bounds

    @out_of_bounds.setter
    def out_of_bounds(self, out_of_bounds):
        """Sets the out_of_bounds of this OneOfDimensionalVectorFunctionSpeedValue.


        :param out_of_bounds: The out_of_bounds of this OneOfDimensionalVectorFunctionSpeedValue.  # noqa: E501
        :type: str
        """
        allowed_values = ["CLAMP"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and out_of_bounds not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `out_of_bounds` ({0}), must be one of {1}"  # noqa: E501
                .format(out_of_bounds, allowed_values)
            )

        self._out_of_bounds = out_of_bounds

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
        if not isinstance(other, OneOfDimensionalVectorFunctionSpeedValue):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfDimensionalVectorFunctionSpeedValue):
            return True

        return self.to_dict() != other.to_dict()
