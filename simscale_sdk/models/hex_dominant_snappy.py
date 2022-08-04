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


class HexDominantSnappy(object):
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
        'meshing_mode': 'str',
        'sizing': 'OneOfHexDominantSnappySizing',
        'physics_based_meshing': 'bool',
        'num_of_processors': 'int',
        'refinements': 'list[OneOfHexDominantSnappyRefinements]'
    }

    attribute_map = {
        'type': 'type',
        'meshing_mode': 'meshingMode',
        'sizing': 'sizing',
        'physics_based_meshing': 'physicsBasedMeshing',
        'num_of_processors': 'numOfProcessors',
        'refinements': 'refinements'
    }

    def __init__(self, type='HEX_DOMINANT_SNAPPY_V5', meshing_mode=None, sizing=None, physics_based_meshing=None, num_of_processors=None, refinements=None, local_vars_configuration=None):  # noqa: E501
        """HexDominantSnappy - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._meshing_mode = None
        self._sizing = None
        self._physics_based_meshing = None
        self._num_of_processors = None
        self._refinements = None
        self.discriminator = None

        self.type = type
        if meshing_mode is not None:
            self.meshing_mode = meshing_mode
        if sizing is not None:
            self.sizing = sizing
        if physics_based_meshing is not None:
            self.physics_based_meshing = physics_based_meshing
        if num_of_processors is not None:
            self.num_of_processors = num_of_processors
        if refinements is not None:
            self.refinements = refinements

    @property
    def type(self):
        """Gets the type of this HexDominantSnappy.  # noqa: E501

        Schema name: HexDominantSnappy  # noqa: E501

        :return: The type of this HexDominantSnappy.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this HexDominantSnappy.

        Schema name: HexDominantSnappy  # noqa: E501

        :param type: The type of this HexDominantSnappy.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def meshing_mode(self):
        """Gets the meshing_mode of this HexDominantSnappy.  # noqa: E501

        <p>The <a href='https://www.simscale.com/docs/simulation-setup/meshing/hex-dominant/#meshing-mode' target='_blank'>meshing mode</a> defines how the mesher should generate the mesh.</p><ul><li>The <b>Internal</b> mode will create the mesh <u>inside</u> of the geometry body. If the CAD consists of multiple solids, the mesher will attempt to create a multiregion mesh which is suitable for conjugate heat transfer analyses. Use this mode if the CAD model already represents the final fluid domain.</li><li><b>External</b> meshing will create the mesh <u>outside</u> of the bodies. The absolute dimensions of the mesh are determined by the <i>Background Mesh Box</i>. Use this mode in case you want to extract the fluid domain around your model.</li><li>The option <b>Material point</b> allows you to define a point inside the domain where the mesh will be placed. It can be used to select which part (or enclosed volume) of the model or should be meshed. The mesh will surround the material point and extend until the boundaries of the body. The location of the material point is defined by the <i>Material Point</i> geometry primitive.</li></ul>  # noqa: E501

        :return: The meshing_mode of this HexDominantSnappy.  # noqa: E501
        :rtype: str
        """
        return self._meshing_mode

    @meshing_mode.setter
    def meshing_mode(self, meshing_mode):
        """Sets the meshing_mode of this HexDominantSnappy.

        <p>The <a href='https://www.simscale.com/docs/simulation-setup/meshing/hex-dominant/#meshing-mode' target='_blank'>meshing mode</a> defines how the mesher should generate the mesh.</p><ul><li>The <b>Internal</b> mode will create the mesh <u>inside</u> of the geometry body. If the CAD consists of multiple solids, the mesher will attempt to create a multiregion mesh which is suitable for conjugate heat transfer analyses. Use this mode if the CAD model already represents the final fluid domain.</li><li><b>External</b> meshing will create the mesh <u>outside</u> of the bodies. The absolute dimensions of the mesh are determined by the <i>Background Mesh Box</i>. Use this mode in case you want to extract the fluid domain around your model.</li><li>The option <b>Material point</b> allows you to define a point inside the domain where the mesh will be placed. It can be used to select which part (or enclosed volume) of the model or should be meshed. The mesh will surround the material point and extend until the boundaries of the body. The location of the material point is defined by the <i>Material Point</i> geometry primitive.</li></ul>  # noqa: E501

        :param meshing_mode: The meshing_mode of this HexDominantSnappy.  # noqa: E501
        :type: str
        """
        allowed_values = ["INTERNAL"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and meshing_mode not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `meshing_mode` ({0}), must be one of {1}"  # noqa: E501
                .format(meshing_mode, allowed_values)
            )

        self._meshing_mode = meshing_mode

    @property
    def sizing(self):
        """Gets the sizing of this HexDominantSnappy.  # noqa: E501


        :return: The sizing of this HexDominantSnappy.  # noqa: E501
        :rtype: OneOfHexDominantSnappySizing
        """
        return self._sizing

    @sizing.setter
    def sizing(self, sizing):
        """Sets the sizing of this HexDominantSnappy.


        :param sizing: The sizing of this HexDominantSnappy.  # noqa: E501
        :type: OneOfHexDominantSnappySizing
        """

        self._sizing = sizing

    @property
    def physics_based_meshing(self):
        """Gets the physics_based_meshing of this HexDominantSnappy.  # noqa: E501

        This toggle enables the automatic creation of boundary layers at no-slip walls. When toggled on, the meshing is started together with the simulation run.  # noqa: E501

        :return: The physics_based_meshing of this HexDominantSnappy.  # noqa: E501
        :rtype: bool
        """
        return self._physics_based_meshing

    @physics_based_meshing.setter
    def physics_based_meshing(self, physics_based_meshing):
        """Sets the physics_based_meshing of this HexDominantSnappy.

        This toggle enables the automatic creation of boundary layers at no-slip walls. When toggled on, the meshing is started together with the simulation run.  # noqa: E501

        :param physics_based_meshing: The physics_based_meshing of this HexDominantSnappy.  # noqa: E501
        :type: bool
        """

        self._physics_based_meshing = physics_based_meshing

    @property
    def num_of_processors(self):
        """Gets the num_of_processors of this HexDominantSnappy.  # noqa: E501

        <p>Selecting more processor cores might speed up the meshing process. Choosing a smaller computation instance will save core hours. <a href='https://www.simscale.com/docs/simulation-setup/meshing/#number-of-processors' target='_blank'>Learn more</a>.</p>  # noqa: E501

        :return: The num_of_processors of this HexDominantSnappy.  # noqa: E501
        :rtype: int
        """
        return self._num_of_processors

    @num_of_processors.setter
    def num_of_processors(self, num_of_processors):
        """Sets the num_of_processors of this HexDominantSnappy.

        <p>Selecting more processor cores might speed up the meshing process. Choosing a smaller computation instance will save core hours. <a href='https://www.simscale.com/docs/simulation-setup/meshing/#number-of-processors' target='_blank'>Learn more</a>.</p>  # noqa: E501

        :param num_of_processors: The num_of_processors of this HexDominantSnappy.  # noqa: E501
        :type: int
        """
        allowed_values = [-1, 4, 8, 16, 32, 64, 96]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and num_of_processors not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `num_of_processors` ({0}), must be one of {1}"  # noqa: E501
                .format(num_of_processors, allowed_values)
            )

        self._num_of_processors = num_of_processors

    @property
    def refinements(self):
        """Gets the refinements of this HexDominantSnappy.  # noqa: E501


        :return: The refinements of this HexDominantSnappy.  # noqa: E501
        :rtype: list[OneOfHexDominantSnappyRefinements]
        """
        return self._refinements

    @refinements.setter
    def refinements(self, refinements):
        """Sets the refinements of this HexDominantSnappy.


        :param refinements: The refinements of this HexDominantSnappy.  # noqa: E501
        :type: list[OneOfHexDominantSnappyRefinements]
        """

        self._refinements = refinements

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
        if not isinstance(other, HexDominantSnappy):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, HexDominantSnappy):
            return True

        return self.to_dict() != other.to_dict()
