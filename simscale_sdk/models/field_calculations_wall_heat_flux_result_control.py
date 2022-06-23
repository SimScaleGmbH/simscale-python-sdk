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


class FieldCalculationsWallHeatFluxResultControl(object):
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
        'name': 'str',
        'result_type': 'WallHeatFluxResultType',
        'compute_heat_transfer_coefficient': 'bool',
        'reference_temperature_result_type': 'OneOfFieldCalculationsWallHeatFluxResultControlReferenceTemperatureResultType',
        'compute_nusselt_number': 'bool',
        'reference_nusselt_number_length': 'DimensionalLength'
    }

    attribute_map = {
        'type': 'type',
        'name': 'name',
        'result_type': 'resultType',
        'compute_heat_transfer_coefficient': 'computeHeatTransferCoefficient',
        'reference_temperature_result_type': 'referenceTemperatureResultType',
        'compute_nusselt_number': 'computeNusseltNumber',
        'reference_nusselt_number_length': 'referenceNusseltNumberLength'
    }

    def __init__(self, type='WALL_HEAT_FLUX', name=None, result_type=None, compute_heat_transfer_coefficient=None, reference_temperature_result_type=None, compute_nusselt_number=None, reference_nusselt_number_length=None, local_vars_configuration=None):  # noqa: E501
        """FieldCalculationsWallHeatFluxResultControl - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._name = None
        self._result_type = None
        self._compute_heat_transfer_coefficient = None
        self._reference_temperature_result_type = None
        self._compute_nusselt_number = None
        self._reference_nusselt_number_length = None
        self.discriminator = None

        self.type = type
        if name is not None:
            self.name = name
        if result_type is not None:
            self.result_type = result_type
        if compute_heat_transfer_coefficient is not None:
            self.compute_heat_transfer_coefficient = compute_heat_transfer_coefficient
        if reference_temperature_result_type is not None:
            self.reference_temperature_result_type = reference_temperature_result_type
        if compute_nusselt_number is not None:
            self.compute_nusselt_number = compute_nusselt_number
        if reference_nusselt_number_length is not None:
            self.reference_nusselt_number_length = reference_nusselt_number_length

    @property
    def type(self):
        """Gets the type of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501

        Schema name: FieldCalculationsWallHeatFluxResultControl  # noqa: E501

        :return: The type of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this FieldCalculationsWallHeatFluxResultControl.

        Schema name: FieldCalculationsWallHeatFluxResultControl  # noqa: E501

        :param type: The type of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def name(self):
        """Gets the name of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501


        :return: The name of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FieldCalculationsWallHeatFluxResultControl.


        :param name: The name of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501
        :type: str
        """
        if (self.local_vars_configuration.client_side_validation and
                name is not None and not re.search(r'^[A-Za-z()][-+0-9a-zA-Z_()\h]{0,199}$', name)):  # noqa: E501
            raise ValueError(r"Invalid value for `name`, must be a follow pattern or equal to `/^[A-Za-z()][-+0-9a-zA-Z_()\h]{0,199}$/`")  # noqa: E501

        self._name = name

    @property
    def result_type(self):
        """Gets the result_type of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501


        :return: The result_type of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501
        :rtype: WallHeatFluxResultType
        """
        return self._result_type

    @result_type.setter
    def result_type(self, result_type):
        """Sets the result_type of this FieldCalculationsWallHeatFluxResultControl.


        :param result_type: The result_type of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501
        :type: WallHeatFluxResultType
        """

        self._result_type = result_type

    @property
    def compute_heat_transfer_coefficient(self):
        """Gets the compute_heat_transfer_coefficient of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501


        :return: The compute_heat_transfer_coefficient of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501
        :rtype: bool
        """
        return self._compute_heat_transfer_coefficient

    @compute_heat_transfer_coefficient.setter
    def compute_heat_transfer_coefficient(self, compute_heat_transfer_coefficient):
        """Sets the compute_heat_transfer_coefficient of this FieldCalculationsWallHeatFluxResultControl.


        :param compute_heat_transfer_coefficient: The compute_heat_transfer_coefficient of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501
        :type: bool
        """

        self._compute_heat_transfer_coefficient = compute_heat_transfer_coefficient

    @property
    def reference_temperature_result_type(self):
        """Gets the reference_temperature_result_type of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501


        :return: The reference_temperature_result_type of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501
        :rtype: OneOfFieldCalculationsWallHeatFluxResultControlReferenceTemperatureResultType
        """
        return self._reference_temperature_result_type

    @reference_temperature_result_type.setter
    def reference_temperature_result_type(self, reference_temperature_result_type):
        """Sets the reference_temperature_result_type of this FieldCalculationsWallHeatFluxResultControl.


        :param reference_temperature_result_type: The reference_temperature_result_type of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501
        :type: OneOfFieldCalculationsWallHeatFluxResultControlReferenceTemperatureResultType
        """

        self._reference_temperature_result_type = reference_temperature_result_type

    @property
    def compute_nusselt_number(self):
        """Gets the compute_nusselt_number of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501


        :return: The compute_nusselt_number of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501
        :rtype: bool
        """
        return self._compute_nusselt_number

    @compute_nusselt_number.setter
    def compute_nusselt_number(self, compute_nusselt_number):
        """Sets the compute_nusselt_number of this FieldCalculationsWallHeatFluxResultControl.


        :param compute_nusselt_number: The compute_nusselt_number of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501
        :type: bool
        """

        self._compute_nusselt_number = compute_nusselt_number

    @property
    def reference_nusselt_number_length(self):
        """Gets the reference_nusselt_number_length of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501


        :return: The reference_nusselt_number_length of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501
        :rtype: DimensionalLength
        """
        return self._reference_nusselt_number_length

    @reference_nusselt_number_length.setter
    def reference_nusselt_number_length(self, reference_nusselt_number_length):
        """Sets the reference_nusselt_number_length of this FieldCalculationsWallHeatFluxResultControl.


        :param reference_nusselt_number_length: The reference_nusselt_number_length of this FieldCalculationsWallHeatFluxResultControl.  # noqa: E501
        :type: DimensionalLength
        """

        self._reference_nusselt_number_length = reference_nusselt_number_length

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
        if not isinstance(other, FieldCalculationsWallHeatFluxResultControl):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FieldCalculationsWallHeatFluxResultControl):
            return True

        return self.to_dict() != other.to_dict()
