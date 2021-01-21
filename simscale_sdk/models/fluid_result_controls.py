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


class FluidResultControls(object):
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
        'forces_moments': 'list[OneOfFluidResultControlsForcesMoments]',
        'surface_data': 'list[OneOfFluidResultControlsSurfaceData]',
        'scalar_transport': 'list[ScalarTransportResultControl]',
        'probe_points': 'list[ProbePointsResultControl]',
        'field_calculations': 'list[OneOfFluidResultControlsFieldCalculations]',
        'transient_result_control': 'TransientResultControl',
        'statistical_averaging_result_control': 'StatisticalAveragingResultControlV2',
        'snapshot_result_control': 'SnapshotResultControl'
    }

    attribute_map = {
        'forces_moments': 'forcesMoments',
        'surface_data': 'surfaceData',
        'scalar_transport': 'scalarTransport',
        'probe_points': 'probePoints',
        'field_calculations': 'fieldCalculations',
        'transient_result_control': 'transientResultControl',
        'statistical_averaging_result_control': 'statisticalAveragingResultControl',
        'snapshot_result_control': 'snapshotResultControl'
    }

    def __init__(self, forces_moments=None, surface_data=None, scalar_transport=None, probe_points=None, field_calculations=None, transient_result_control=None, statistical_averaging_result_control=None, snapshot_result_control=None, local_vars_configuration=None):  # noqa: E501
        """FluidResultControls - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._forces_moments = None
        self._surface_data = None
        self._scalar_transport = None
        self._probe_points = None
        self._field_calculations = None
        self._transient_result_control = None
        self._statistical_averaging_result_control = None
        self._snapshot_result_control = None
        self.discriminator = None

        if forces_moments is not None:
            self.forces_moments = forces_moments
        if surface_data is not None:
            self.surface_data = surface_data
        if scalar_transport is not None:
            self.scalar_transport = scalar_transport
        if probe_points is not None:
            self.probe_points = probe_points
        if field_calculations is not None:
            self.field_calculations = field_calculations
        if transient_result_control is not None:
            self.transient_result_control = transient_result_control
        if statistical_averaging_result_control is not None:
            self.statistical_averaging_result_control = statistical_averaging_result_control
        if snapshot_result_control is not None:
            self.snapshot_result_control = snapshot_result_control

    @property
    def forces_moments(self):
        """Gets the forces_moments of this FluidResultControls.  # noqa: E501


        :return: The forces_moments of this FluidResultControls.  # noqa: E501
        :rtype: list[OneOfFluidResultControlsForcesMoments]
        """
        return self._forces_moments

    @forces_moments.setter
    def forces_moments(self, forces_moments):
        """Sets the forces_moments of this FluidResultControls.


        :param forces_moments: The forces_moments of this FluidResultControls.  # noqa: E501
        :type: list[OneOfFluidResultControlsForcesMoments]
        """

        self._forces_moments = forces_moments

    @property
    def surface_data(self):
        """Gets the surface_data of this FluidResultControls.  # noqa: E501


        :return: The surface_data of this FluidResultControls.  # noqa: E501
        :rtype: list[OneOfFluidResultControlsSurfaceData]
        """
        return self._surface_data

    @surface_data.setter
    def surface_data(self, surface_data):
        """Sets the surface_data of this FluidResultControls.


        :param surface_data: The surface_data of this FluidResultControls.  # noqa: E501
        :type: list[OneOfFluidResultControlsSurfaceData]
        """

        self._surface_data = surface_data

    @property
    def scalar_transport(self):
        """Gets the scalar_transport of this FluidResultControls.  # noqa: E501


        :return: The scalar_transport of this FluidResultControls.  # noqa: E501
        :rtype: list[ScalarTransportResultControl]
        """
        return self._scalar_transport

    @scalar_transport.setter
    def scalar_transport(self, scalar_transport):
        """Sets the scalar_transport of this FluidResultControls.


        :param scalar_transport: The scalar_transport of this FluidResultControls.  # noqa: E501
        :type: list[ScalarTransportResultControl]
        """

        self._scalar_transport = scalar_transport

    @property
    def probe_points(self):
        """Gets the probe_points of this FluidResultControls.  # noqa: E501


        :return: The probe_points of this FluidResultControls.  # noqa: E501
        :rtype: list[ProbePointsResultControl]
        """
        return self._probe_points

    @probe_points.setter
    def probe_points(self, probe_points):
        """Sets the probe_points of this FluidResultControls.


        :param probe_points: The probe_points of this FluidResultControls.  # noqa: E501
        :type: list[ProbePointsResultControl]
        """

        self._probe_points = probe_points

    @property
    def field_calculations(self):
        """Gets the field_calculations of this FluidResultControls.  # noqa: E501


        :return: The field_calculations of this FluidResultControls.  # noqa: E501
        :rtype: list[OneOfFluidResultControlsFieldCalculations]
        """
        return self._field_calculations

    @field_calculations.setter
    def field_calculations(self, field_calculations):
        """Sets the field_calculations of this FluidResultControls.


        :param field_calculations: The field_calculations of this FluidResultControls.  # noqa: E501
        :type: list[OneOfFluidResultControlsFieldCalculations]
        """

        self._field_calculations = field_calculations

    @property
    def transient_result_control(self):
        """Gets the transient_result_control of this FluidResultControls.  # noqa: E501


        :return: The transient_result_control of this FluidResultControls.  # noqa: E501
        :rtype: TransientResultControl
        """
        return self._transient_result_control

    @transient_result_control.setter
    def transient_result_control(self, transient_result_control):
        """Sets the transient_result_control of this FluidResultControls.


        :param transient_result_control: The transient_result_control of this FluidResultControls.  # noqa: E501
        :type: TransientResultControl
        """

        self._transient_result_control = transient_result_control

    @property
    def statistical_averaging_result_control(self):
        """Gets the statistical_averaging_result_control of this FluidResultControls.  # noqa: E501


        :return: The statistical_averaging_result_control of this FluidResultControls.  # noqa: E501
        :rtype: StatisticalAveragingResultControlV2
        """
        return self._statistical_averaging_result_control

    @statistical_averaging_result_control.setter
    def statistical_averaging_result_control(self, statistical_averaging_result_control):
        """Sets the statistical_averaging_result_control of this FluidResultControls.


        :param statistical_averaging_result_control: The statistical_averaging_result_control of this FluidResultControls.  # noqa: E501
        :type: StatisticalAveragingResultControlV2
        """

        self._statistical_averaging_result_control = statistical_averaging_result_control

    @property
    def snapshot_result_control(self):
        """Gets the snapshot_result_control of this FluidResultControls.  # noqa: E501


        :return: The snapshot_result_control of this FluidResultControls.  # noqa: E501
        :rtype: SnapshotResultControl
        """
        return self._snapshot_result_control

    @snapshot_result_control.setter
    def snapshot_result_control(self, snapshot_result_control):
        """Sets the snapshot_result_control of this FluidResultControls.


        :param snapshot_result_control: The snapshot_result_control of this FluidResultControls.  # noqa: E501
        :type: SnapshotResultControl
        """

        self._snapshot_result_control = snapshot_result_control

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
        if not isinstance(other, FluidResultControls):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, FluidResultControls):
            return True

        return self.to_dict() != other.to_dict()
