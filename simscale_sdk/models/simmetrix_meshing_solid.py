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


class SimmetrixMeshingSolid(object):
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
        'sizing': 'OneOfSimmetrixMeshingSolidSizing',
        'refinements': 'list[OneOfSimmetrixMeshingSolidRefinements]',
        'automatic_sweep_parameters': 'OneOfSimmetrixMeshingSolidAutomaticSweepParameters',
        'num_of_processors': 'int',
        'max_meshing_run_time': 'DimensionalTime',
        'advanced_simmetrix_settings': 'AdvancedSimmetrixSolidSettings'
    }

    attribute_map = {
        'type': 'type',
        'sizing': 'sizing',
        'refinements': 'refinements',
        'automatic_sweep_parameters': 'automaticSweepParameters',
        'num_of_processors': 'numOfProcessors',
        'max_meshing_run_time': 'maxMeshingRunTime',
        'advanced_simmetrix_settings': 'advancedSimmetrixSettings'
    }

    def __init__(self, type='SIMMETRIX_MESHING_SOLID', sizing=None, refinements=None, automatic_sweep_parameters=None, num_of_processors=None, max_meshing_run_time=None, advanced_simmetrix_settings=None, local_vars_configuration=None):  # noqa: E501
        """SimmetrixMeshingSolid - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._sizing = None
        self._refinements = None
        self._automatic_sweep_parameters = None
        self._num_of_processors = None
        self._max_meshing_run_time = None
        self._advanced_simmetrix_settings = None
        self.discriminator = None

        self.type = type
        if sizing is not None:
            self.sizing = sizing
        if refinements is not None:
            self.refinements = refinements
        if automatic_sweep_parameters is not None:
            self.automatic_sweep_parameters = automatic_sweep_parameters
        if num_of_processors is not None:
            self.num_of_processors = num_of_processors
        if max_meshing_run_time is not None:
            self.max_meshing_run_time = max_meshing_run_time
        if advanced_simmetrix_settings is not None:
            self.advanced_simmetrix_settings = advanced_simmetrix_settings

    @property
    def type(self):
        """Gets the type of this SimmetrixMeshingSolid.  # noqa: E501

        Schema name: SimmetrixMeshingSolid  # noqa: E501

        :return: The type of this SimmetrixMeshingSolid.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SimmetrixMeshingSolid.

        Schema name: SimmetrixMeshingSolid  # noqa: E501

        :param type: The type of this SimmetrixMeshingSolid.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def sizing(self):
        """Gets the sizing of this SimmetrixMeshingSolid.  # noqa: E501


        :return: The sizing of this SimmetrixMeshingSolid.  # noqa: E501
        :rtype: OneOfSimmetrixMeshingSolidSizing
        """
        return self._sizing

    @sizing.setter
    def sizing(self, sizing):
        """Sets the sizing of this SimmetrixMeshingSolid.


        :param sizing: The sizing of this SimmetrixMeshingSolid.  # noqa: E501
        :type: OneOfSimmetrixMeshingSolidSizing
        """

        self._sizing = sizing

    @property
    def refinements(self):
        """Gets the refinements of this SimmetrixMeshingSolid.  # noqa: E501


        :return: The refinements of this SimmetrixMeshingSolid.  # noqa: E501
        :rtype: list[OneOfSimmetrixMeshingSolidRefinements]
        """
        return self._refinements

    @refinements.setter
    def refinements(self, refinements):
        """Sets the refinements of this SimmetrixMeshingSolid.


        :param refinements: The refinements of this SimmetrixMeshingSolid.  # noqa: E501
        :type: list[OneOfSimmetrixMeshingSolidRefinements]
        """

        self._refinements = refinements

    @property
    def automatic_sweep_parameters(self):
        """Gets the automatic_sweep_parameters of this SimmetrixMeshingSolid.  # noqa: E501


        :return: The automatic_sweep_parameters of this SimmetrixMeshingSolid.  # noqa: E501
        :rtype: OneOfSimmetrixMeshingSolidAutomaticSweepParameters
        """
        return self._automatic_sweep_parameters

    @automatic_sweep_parameters.setter
    def automatic_sweep_parameters(self, automatic_sweep_parameters):
        """Sets the automatic_sweep_parameters of this SimmetrixMeshingSolid.


        :param automatic_sweep_parameters: The automatic_sweep_parameters of this SimmetrixMeshingSolid.  # noqa: E501
        :type: OneOfSimmetrixMeshingSolidAutomaticSweepParameters
        """

        self._automatic_sweep_parameters = automatic_sweep_parameters

    @property
    def num_of_processors(self):
        """Gets the num_of_processors of this SimmetrixMeshingSolid.  # noqa: E501

        <p>Selecting more processor cores might speed up the meshing process. Choosing a smaller computation instance will save core hours. <a href='https://www.simscale.com/docs/simulation-setup/meshing/#number-of-processors' target='_blank'>Learn more</a>.</p>  # noqa: E501

        :return: The num_of_processors of this SimmetrixMeshingSolid.  # noqa: E501
        :rtype: int
        """
        return self._num_of_processors

    @num_of_processors.setter
    def num_of_processors(self, num_of_processors):
        """Sets the num_of_processors of this SimmetrixMeshingSolid.

        <p>Selecting more processor cores might speed up the meshing process. Choosing a smaller computation instance will save core hours. <a href='https://www.simscale.com/docs/simulation-setup/meshing/#number-of-processors' target='_blank'>Learn more</a>.</p>  # noqa: E501

        :param num_of_processors: The num_of_processors of this SimmetrixMeshingSolid.  # noqa: E501
        :type: int
        """
        allowed_values = [-1, 4, 8, 16, 32, 48, 64, 96]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and num_of_processors not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `num_of_processors` ({0}), must be one of {1}"  # noqa: E501
                .format(num_of_processors, allowed_values)
            )

        self._num_of_processors = num_of_processors

    @property
    def max_meshing_run_time(self):
        """Gets the max_meshing_run_time of this SimmetrixMeshingSolid.  # noqa: E501


        :return: The max_meshing_run_time of this SimmetrixMeshingSolid.  # noqa: E501
        :rtype: DimensionalTime
        """
        return self._max_meshing_run_time

    @max_meshing_run_time.setter
    def max_meshing_run_time(self, max_meshing_run_time):
        """Sets the max_meshing_run_time of this SimmetrixMeshingSolid.


        :param max_meshing_run_time: The max_meshing_run_time of this SimmetrixMeshingSolid.  # noqa: E501
        :type: DimensionalTime
        """

        self._max_meshing_run_time = max_meshing_run_time

    @property
    def advanced_simmetrix_settings(self):
        """Gets the advanced_simmetrix_settings of this SimmetrixMeshingSolid.  # noqa: E501


        :return: The advanced_simmetrix_settings of this SimmetrixMeshingSolid.  # noqa: E501
        :rtype: AdvancedSimmetrixSolidSettings
        """
        return self._advanced_simmetrix_settings

    @advanced_simmetrix_settings.setter
    def advanced_simmetrix_settings(self, advanced_simmetrix_settings):
        """Sets the advanced_simmetrix_settings of this SimmetrixMeshingSolid.


        :param advanced_simmetrix_settings: The advanced_simmetrix_settings of this SimmetrixMeshingSolid.  # noqa: E501
        :type: AdvancedSimmetrixSolidSettings
        """

        self._advanced_simmetrix_settings = advanced_simmetrix_settings

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
        if not isinstance(other, SimmetrixMeshingSolid):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SimmetrixMeshingSolid):
            return True

        return self.to_dict() != other.to_dict()
