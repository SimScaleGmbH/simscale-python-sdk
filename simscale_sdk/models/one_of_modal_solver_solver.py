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


class OneOfModalSolverSolver(object):
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
        'advanced_mumps_settings': 'AdvancedMUMPSSettings',
        'renumbering_method': 'str',
        'force_symmetric': 'bool',
        'precision_singularity_detection': 'int',
        'stop_if_singular': 'bool',
        'eliminate_lagrange_multipliers': 'bool'
    }

    attribute_map = {
        'type': 'type',
        'advanced_mumps_settings': 'advancedMumpsSettings',
        'renumbering_method': 'renumberingMethod',
        'force_symmetric': 'forceSymmetric',
        'precision_singularity_detection': 'precisionSingularityDetection',
        'stop_if_singular': 'stopIfSingular',
        'eliminate_lagrange_multipliers': 'eliminateLagrangeMultipliers'
    }

    discriminator_value_class_map = {
        'MUMPS': 'MUMPSSolver',
        'MULTIFRONT': 'MultifrontalSolver'
    }

    def __init__(self, type='MULTIFRONT', advanced_mumps_settings=None, renumbering_method=None, force_symmetric=None, precision_singularity_detection=None, stop_if_singular=None, eliminate_lagrange_multipliers=None, local_vars_configuration=None):  # noqa: E501
        """OneOfModalSolverSolver - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._advanced_mumps_settings = None
        self._renumbering_method = None
        self._force_symmetric = None
        self._precision_singularity_detection = None
        self._stop_if_singular = None
        self._eliminate_lagrange_multipliers = None
        self.discriminator = 'type'

        self.type = type
        if advanced_mumps_settings is not None:
            self.advanced_mumps_settings = advanced_mumps_settings
        if renumbering_method is not None:
            self.renumbering_method = renumbering_method
        if force_symmetric is not None:
            self.force_symmetric = force_symmetric
        if precision_singularity_detection is not None:
            self.precision_singularity_detection = precision_singularity_detection
        if stop_if_singular is not None:
            self.stop_if_singular = stop_if_singular
        if eliminate_lagrange_multipliers is not None:
            self.eliminate_lagrange_multipliers = eliminate_lagrange_multipliers

    @property
    def type(self):
        """Gets the type of this OneOfModalSolverSolver.  # noqa: E501

        Schema name: MultifrontalSolver  # noqa: E501

        :return: The type of this OneOfModalSolverSolver.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfModalSolverSolver.

        Schema name: MultifrontalSolver  # noqa: E501

        :param type: The type of this OneOfModalSolverSolver.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def advanced_mumps_settings(self):
        """Gets the advanced_mumps_settings of this OneOfModalSolverSolver.  # noqa: E501


        :return: The advanced_mumps_settings of this OneOfModalSolverSolver.  # noqa: E501
        :rtype: AdvancedMUMPSSettings
        """
        return self._advanced_mumps_settings

    @advanced_mumps_settings.setter
    def advanced_mumps_settings(self, advanced_mumps_settings):
        """Sets the advanced_mumps_settings of this OneOfModalSolverSolver.


        :param advanced_mumps_settings: The advanced_mumps_settings of this OneOfModalSolverSolver.  # noqa: E501
        :type: AdvancedMUMPSSettings
        """

        self._advanced_mumps_settings = advanced_mumps_settings

    @property
    def renumbering_method(self):
        """Gets the renumbering_method of this OneOfModalSolverSolver.  # noqa: E501

        Choose a renumbering method for the solution process.<br/>For large models around and above 50000 degrees of freedom you should consider using MDA.  # noqa: E501

        :return: The renumbering_method of this OneOfModalSolverSolver.  # noqa: E501
        :rtype: str
        """
        return self._renumbering_method

    @renumbering_method.setter
    def renumbering_method(self, renumbering_method):
        """Sets the renumbering_method of this OneOfModalSolverSolver.

        Choose a renumbering method for the solution process.<br/>For large models around and above 50000 degrees of freedom you should consider using MDA.  # noqa: E501

        :param renumbering_method: The renumbering_method of this OneOfModalSolverSolver.  # noqa: E501
        :type: str
        """
        allowed_values = ["MDA", "MD"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and renumbering_method not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `renumbering_method` ({0}), must be one of {1}"  # noqa: E501
                .format(renumbering_method, allowed_values)
            )

        self._renumbering_method = renumbering_method

    @property
    def force_symmetric(self):
        """Gets the force_symmetric of this OneOfModalSolverSolver.  # noqa: E501

        Choose if you want to enforce a symmetric matrix.  # noqa: E501

        :return: The force_symmetric of this OneOfModalSolverSolver.  # noqa: E501
        :rtype: bool
        """
        return self._force_symmetric

    @force_symmetric.setter
    def force_symmetric(self, force_symmetric):
        """Sets the force_symmetric of this OneOfModalSolverSolver.

        Choose if you want to enforce a symmetric matrix.  # noqa: E501

        :param force_symmetric: The force_symmetric of this OneOfModalSolverSolver.  # noqa: E501
        :type: bool
        """

        self._force_symmetric = force_symmetric

    @property
    def precision_singularity_detection(self):
        """Gets the precision_singularity_detection of this OneOfModalSolverSolver.  # noqa: E501

        Define the precision value for the detection of a singular matrix. Positive values enable the check, with 9 being a good starting point. Smaller values make the check more strict. This is an advanced option that should only be used to debug a model.  # noqa: E501

        :return: The precision_singularity_detection of this OneOfModalSolverSolver.  # noqa: E501
        :rtype: int
        """
        return self._precision_singularity_detection

    @precision_singularity_detection.setter
    def precision_singularity_detection(self, precision_singularity_detection):
        """Sets the precision_singularity_detection of this OneOfModalSolverSolver.

        Define the precision value for the detection of a singular matrix. Positive values enable the check, with 9 being a good starting point. Smaller values make the check more strict. This is an advanced option that should only be used to debug a model.  # noqa: E501

        :param precision_singularity_detection: The precision_singularity_detection of this OneOfModalSolverSolver.  # noqa: E501
        :type: int
        """

        self._precision_singularity_detection = precision_singularity_detection

    @property
    def stop_if_singular(self):
        """Gets the stop_if_singular of this OneOfModalSolverSolver.  # noqa: E501

        Choose if the calculation should be stopped if the problem turns out to be singular.  # noqa: E501

        :return: The stop_if_singular of this OneOfModalSolverSolver.  # noqa: E501
        :rtype: bool
        """
        return self._stop_if_singular

    @stop_if_singular.setter
    def stop_if_singular(self, stop_if_singular):
        """Sets the stop_if_singular of this OneOfModalSolverSolver.

        Choose if the calculation should be stopped if the problem turns out to be singular.  # noqa: E501

        :param stop_if_singular: The stop_if_singular of this OneOfModalSolverSolver.  # noqa: E501
        :type: bool
        """

        self._stop_if_singular = stop_if_singular

    @property
    def eliminate_lagrange_multipliers(self):
        """Gets the eliminate_lagrange_multipliers of this OneOfModalSolverSolver.  # noqa: E501

        This option makes it possible to eliminate the Lagrange Multipliers which are introduced by generalized boundary conditions like bonded contact, remote boundary conditions and symmetry conditions. If activated, this option removes the Lagrange Multipliers which leads to a reduction of the total number of unknowns and can increase the robustness of iterative solvers.  # noqa: E501

        :return: The eliminate_lagrange_multipliers of this OneOfModalSolverSolver.  # noqa: E501
        :rtype: bool
        """
        return self._eliminate_lagrange_multipliers

    @eliminate_lagrange_multipliers.setter
    def eliminate_lagrange_multipliers(self, eliminate_lagrange_multipliers):
        """Sets the eliminate_lagrange_multipliers of this OneOfModalSolverSolver.

        This option makes it possible to eliminate the Lagrange Multipliers which are introduced by generalized boundary conditions like bonded contact, remote boundary conditions and symmetry conditions. If activated, this option removes the Lagrange Multipliers which leads to a reduction of the total number of unknowns and can increase the robustness of iterative solvers.  # noqa: E501

        :param eliminate_lagrange_multipliers: The eliminate_lagrange_multipliers of this OneOfModalSolverSolver.  # noqa: E501
        :type: bool
        """

        self._eliminate_lagrange_multipliers = eliminate_lagrange_multipliers

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
        if not isinstance(other, OneOfModalSolverSolver):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfModalSolverSolver):
            return True

        return self.to_dict() != other.to_dict()
