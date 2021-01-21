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


class OneOfNewtonResolutionTypeJacobianMatrix(object):
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
        'max_newton_iteration': 'int',
        'reactualization_iteration': 'int',
        'reactualization_increment': 'int',
        'change_jacobian_matrix': 'OneOfTangentJacobianMatrixChangeJacobianMatrix'
    }

    attribute_map = {
        'type': 'type',
        'max_newton_iteration': 'maxNewtonIteration',
        'reactualization_iteration': 'reactualizationIteration',
        'reactualization_increment': 'reactualizationIncrement',
        'change_jacobian_matrix': 'changeJacobianMatrix'
    }

    discriminator_value_class_map = {
        'TANGENT': 'TangentJacobianMatrix',
        'ELASTIC': 'ElasticJacobianMatrix'
    }

    def __init__(self, type='ELASTIC', max_newton_iteration=35, reactualization_iteration=None, reactualization_increment=None, change_jacobian_matrix=None, local_vars_configuration=None):  # noqa: E501
        """OneOfNewtonResolutionTypeJacobianMatrix - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._max_newton_iteration = None
        self._reactualization_iteration = None
        self._reactualization_increment = None
        self._change_jacobian_matrix = None
        self.discriminator = 'type'

        self.type = type
        self.max_newton_iteration = max_newton_iteration
        self.reactualization_iteration = reactualization_iteration
        if reactualization_increment is not None:
            self.reactualization_increment = reactualization_increment
        if change_jacobian_matrix is not None:
            self.change_jacobian_matrix = change_jacobian_matrix

    @property
    def type(self):
        """Gets the type of this OneOfNewtonResolutionTypeJacobianMatrix.  # noqa: E501


        :return: The type of this OneOfNewtonResolutionTypeJacobianMatrix.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfNewtonResolutionTypeJacobianMatrix.


        :param type: The type of this OneOfNewtonResolutionTypeJacobianMatrix.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def max_newton_iteration(self):
        """Gets the max_newton_iteration of this OneOfNewtonResolutionTypeJacobianMatrix.  # noqa: E501

        <p>Maximum number of allowed Newton iterations per time increment. If this value is reached the simulation is considered non-converging. If an automatic time stepping is activated the time increment is reduced in order to reach convergence.</p>  # noqa: E501

        :return: The max_newton_iteration of this OneOfNewtonResolutionTypeJacobianMatrix.  # noqa: E501
        :rtype: int
        """
        return self._max_newton_iteration

    @max_newton_iteration.setter
    def max_newton_iteration(self, max_newton_iteration):
        """Sets the max_newton_iteration of this OneOfNewtonResolutionTypeJacobianMatrix.

        <p>Maximum number of allowed Newton iterations per time increment. If this value is reached the simulation is considered non-converging. If an automatic time stepping is activated the time increment is reduced in order to reach convergence.</p>  # noqa: E501

        :param max_newton_iteration: The max_newton_iteration of this OneOfNewtonResolutionTypeJacobianMatrix.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and max_newton_iteration is None:  # noqa: E501
            raise ValueError("Invalid value for `max_newton_iteration`, must not be `None`")  # noqa: E501

        self._max_newton_iteration = max_newton_iteration

    @property
    def reactualization_iteration(self):
        """Gets the reactualization_iteration of this OneOfNewtonResolutionTypeJacobianMatrix.  # noqa: E501

        <p>Select how often the Jacobian matrix should be recomputed. If this parameter is set to 10, the Jacobian matrix is recomputed every 10th iteration within a given time step. If it is set to 0, the Jacobian matrix is not updated within any time step.</p>  # noqa: E501

        :return: The reactualization_iteration of this OneOfNewtonResolutionTypeJacobianMatrix.  # noqa: E501
        :rtype: int
        """
        return self._reactualization_iteration

    @reactualization_iteration.setter
    def reactualization_iteration(self, reactualization_iteration):
        """Sets the reactualization_iteration of this OneOfNewtonResolutionTypeJacobianMatrix.

        <p>Select how often the Jacobian matrix should be recomputed. If this parameter is set to 10, the Jacobian matrix is recomputed every 10th iteration within a given time step. If it is set to 0, the Jacobian matrix is not updated within any time step.</p>  # noqa: E501

        :param reactualization_iteration: The reactualization_iteration of this OneOfNewtonResolutionTypeJacobianMatrix.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and reactualization_iteration is None:  # noqa: E501
            raise ValueError("Invalid value for `reactualization_iteration`, must not be `None`")  # noqa: E501

        self._reactualization_iteration = reactualization_iteration

    @property
    def reactualization_increment(self):
        """Gets the reactualization_increment of this OneOfNewtonResolutionTypeJacobianMatrix.  # noqa: E501

        <p>Select how often the Jacobian matrix should be recomputed. If this parameter is set to 10, the Jacobian matrix is recomputed every 10th time step. If it is set to 0, the Jacobian matrix is never updated.</p>  # noqa: E501

        :return: The reactualization_increment of this OneOfNewtonResolutionTypeJacobianMatrix.  # noqa: E501
        :rtype: int
        """
        return self._reactualization_increment

    @reactualization_increment.setter
    def reactualization_increment(self, reactualization_increment):
        """Sets the reactualization_increment of this OneOfNewtonResolutionTypeJacobianMatrix.

        <p>Select how often the Jacobian matrix should be recomputed. If this parameter is set to 10, the Jacobian matrix is recomputed every 10th time step. If it is set to 0, the Jacobian matrix is never updated.</p>  # noqa: E501

        :param reactualization_increment: The reactualization_increment of this OneOfNewtonResolutionTypeJacobianMatrix.  # noqa: E501
        :type: int
        """

        self._reactualization_increment = reactualization_increment

    @property
    def change_jacobian_matrix(self):
        """Gets the change_jacobian_matrix of this OneOfNewtonResolutionTypeJacobianMatrix.  # noqa: E501


        :return: The change_jacobian_matrix of this OneOfNewtonResolutionTypeJacobianMatrix.  # noqa: E501
        :rtype: OneOfTangentJacobianMatrixChangeJacobianMatrix
        """
        return self._change_jacobian_matrix

    @change_jacobian_matrix.setter
    def change_jacobian_matrix(self, change_jacobian_matrix):
        """Sets the change_jacobian_matrix of this OneOfNewtonResolutionTypeJacobianMatrix.


        :param change_jacobian_matrix: The change_jacobian_matrix of this OneOfNewtonResolutionTypeJacobianMatrix.  # noqa: E501
        :type: OneOfTangentJacobianMatrixChangeJacobianMatrix
        """

        self._change_jacobian_matrix = change_jacobian_matrix

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
        if not isinstance(other, OneOfNewtonResolutionTypeJacobianMatrix):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfNewtonResolutionTypeJacobianMatrix):
            return True

        return self.to_dict() != other.to_dict()
