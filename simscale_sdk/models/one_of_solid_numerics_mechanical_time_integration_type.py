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


class OneOfSolidNumericsMechanicalTimeIntegrationType(object):
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
        'scheme': 'OneOfExplicitTimeIntegrationTypeScheme',
        'scheme_formulation': 'str',
        'mass_matrix_shift': 'float',
        'stop_on_cfl_criterion': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'scheme': 'scheme',
        'scheme_formulation': 'schemeFormulation',
        'mass_matrix_shift': 'massMatrixShift',
        'stop_on_cfl_criterion': 'stopOnCFLCriterion'
    }

    discriminator_value_class_map = {
        'IMPLICIT': 'ImplicitTimeIntegrationType',
        'EXPLICIT': 'ExplicitTimeIntegrationType'
    }

    def __init__(self, type='EXPLICIT', scheme=None, scheme_formulation=None, mass_matrix_shift=None, stop_on_cfl_criterion=True, local_vars_configuration=None):  # noqa: E501
        """OneOfSolidNumericsMechanicalTimeIntegrationType - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._scheme = None
        self._scheme_formulation = None
        self._mass_matrix_shift = None
        self._stop_on_cfl_criterion = None
        self.discriminator = 'type'

        self.type = type
        if scheme is not None:
            self.scheme = scheme
        if scheme_formulation is not None:
            self.scheme_formulation = scheme_formulation
        if mass_matrix_shift is not None:
            self.mass_matrix_shift = mass_matrix_shift
        self.stop_on_cfl_criterion = stop_on_cfl_criterion

    @property
    def type(self):
        """Gets the type of this OneOfSolidNumericsMechanicalTimeIntegrationType.  # noqa: E501


        :return: The type of this OneOfSolidNumericsMechanicalTimeIntegrationType.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfSolidNumericsMechanicalTimeIntegrationType.


        :param type: The type of this OneOfSolidNumericsMechanicalTimeIntegrationType.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def scheme(self):
        """Gets the scheme of this OneOfSolidNumericsMechanicalTimeIntegrationType.  # noqa: E501


        :return: The scheme of this OneOfSolidNumericsMechanicalTimeIntegrationType.  # noqa: E501
        :rtype: OneOfExplicitTimeIntegrationTypeScheme
        """
        return self._scheme

    @scheme.setter
    def scheme(self, scheme):
        """Sets the scheme of this OneOfSolidNumericsMechanicalTimeIntegrationType.


        :param scheme: The scheme of this OneOfSolidNumericsMechanicalTimeIntegrationType.  # noqa: E501
        :type: OneOfExplicitTimeIntegrationTypeScheme
        """

        self._scheme = scheme

    @property
    def scheme_formulation(self):
        """Gets the scheme_formulation of this OneOfSolidNumericsMechanicalTimeIntegrationType.  # noqa: E501

        <p>Choose the primary variable for the time integration scheme.</p>  # noqa: E501

        :return: The scheme_formulation of this OneOfSolidNumericsMechanicalTimeIntegrationType.  # noqa: E501
        :rtype: str
        """
        return self._scheme_formulation

    @scheme_formulation.setter
    def scheme_formulation(self, scheme_formulation):
        """Sets the scheme_formulation of this OneOfSolidNumericsMechanicalTimeIntegrationType.

        <p>Choose the primary variable for the time integration scheme.</p>  # noqa: E501

        :param scheme_formulation: The scheme_formulation of this OneOfSolidNumericsMechanicalTimeIntegrationType.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACCELERATION"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and scheme_formulation not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `scheme_formulation` ({0}), must be one of {1}"  # noqa: E501
                .format(scheme_formulation, allowed_values)
            )

        self._scheme_formulation = scheme_formulation

    @property
    def mass_matrix_shift(self):
        """Gets the mass_matrix_shift of this OneOfSolidNumericsMechanicalTimeIntegrationType.  # noqa: E501

        <p>This parameter c<sub>K</sub> allows the shifting of the mass matrix with the stiffness matrix multiplied by c<sub>K</sub>: <b>M</b><sup>'</sup>=<b>M</b> + c<sub>K</sub>*<b>K</b>. This makes it possible to strongly improve convergence in dynamics with implicit time scheme by imposing a cut-off frequency inversely proportional to the value of c<sub>K</sub> (at the cost of a light distortion of all the eigen frequencies of the system).</p>  # noqa: E501

        :return: The mass_matrix_shift of this OneOfSolidNumericsMechanicalTimeIntegrationType.  # noqa: E501
        :rtype: float
        """
        return self._mass_matrix_shift

    @mass_matrix_shift.setter
    def mass_matrix_shift(self, mass_matrix_shift):
        """Sets the mass_matrix_shift of this OneOfSolidNumericsMechanicalTimeIntegrationType.

        <p>This parameter c<sub>K</sub> allows the shifting of the mass matrix with the stiffness matrix multiplied by c<sub>K</sub>: <b>M</b><sup>'</sup>=<b>M</b> + c<sub>K</sub>*<b>K</b>. This makes it possible to strongly improve convergence in dynamics with implicit time scheme by imposing a cut-off frequency inversely proportional to the value of c<sub>K</sub> (at the cost of a light distortion of all the eigen frequencies of the system).</p>  # noqa: E501

        :param mass_matrix_shift: The mass_matrix_shift of this OneOfSolidNumericsMechanicalTimeIntegrationType.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                mass_matrix_shift is not None and mass_matrix_shift < 0):  # noqa: E501
            raise ValueError("Invalid value for `mass_matrix_shift`, must be a value greater than or equal to `0`")  # noqa: E501

        self._mass_matrix_shift = mass_matrix_shift

    @property
    def stop_on_cfl_criterion(self):
        """Gets the stop_on_cfl_criterion of this OneOfSolidNumericsMechanicalTimeIntegrationType.  # noqa: E501

        <p>If activated the simulation run is stopped when at some point the Courant-Friedrichs-Lewy (CFL) condition is violated.</p>  # noqa: E501

        :return: The stop_on_cfl_criterion of this OneOfSolidNumericsMechanicalTimeIntegrationType.  # noqa: E501
        :rtype: bool
        """
        return self._stop_on_cfl_criterion

    @stop_on_cfl_criterion.setter
    def stop_on_cfl_criterion(self, stop_on_cfl_criterion):
        """Sets the stop_on_cfl_criterion of this OneOfSolidNumericsMechanicalTimeIntegrationType.

        <p>If activated the simulation run is stopped when at some point the Courant-Friedrichs-Lewy (CFL) condition is violated.</p>  # noqa: E501

        :param stop_on_cfl_criterion: The stop_on_cfl_criterion of this OneOfSolidNumericsMechanicalTimeIntegrationType.  # noqa: E501
        :type: bool
        """
        if self.local_vars_configuration.client_side_validation and stop_on_cfl_criterion is None:  # noqa: E501
            raise ValueError("Invalid value for `stop_on_cfl_criterion`, must not be `None`")  # noqa: E501

        self._stop_on_cfl_criterion = stop_on_cfl_criterion

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
        if not isinstance(other, OneOfSolidNumericsMechanicalTimeIntegrationType):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfSolidNumericsMechanicalTimeIntegrationType):
            return True

        return self.to_dict() != other.to_dict()
