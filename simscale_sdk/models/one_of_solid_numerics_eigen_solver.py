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


class OneOfSolidNumericsEigenSolver(object):
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
        'prec_soren': 'float',
        'nmax_iter_soren': 'int',
        'subspace_settings': 'OneOfBatheWilsonSubspaceSettings',
        'prec_ortho': 'float',
        'nmax_iter_ortho': 'int',
        'prec_lanczos': 'float',
        'max_iter_qr': 'int',
        'mode_rigid': 'bool',
        'prec_bathe': 'float',
        'nmax_iter_bathe': 'int',
        'prec_jacobi': 'float',
        'max_iter_jacobi': 'int',
        'type_qz': 'str'
    }

    attribute_map = {
        'type': 'type',
        'prec_soren': 'precSoren',
        'nmax_iter_soren': 'nmaxIterSoren',
        'subspace_settings': 'subspaceSettings',
        'prec_ortho': 'precOrtho',
        'nmax_iter_ortho': 'nmaxIterOrtho',
        'prec_lanczos': 'precLanczos',
        'max_iter_qr': 'maxIterQR',
        'mode_rigid': 'modeRigid',
        'prec_bathe': 'precBathe',
        'nmax_iter_bathe': 'nmaxIterBathe',
        'prec_jacobi': 'precJacobi',
        'max_iter_jacobi': 'maxIterJacobi',
        'type_qz': 'typeQZ'
    }

    discriminator_value_class_map = {
        'SORENSEN': 'IRAMSorensen',
        'TRI_DIAG': 'Lanczos',
        'JACOBI': 'BatheWilson',
        'QZ': 'QZ'
    }

    def __init__(self, type='QZ', prec_soren=None, nmax_iter_soren=None, subspace_settings=None, prec_ortho=None, nmax_iter_ortho=None, prec_lanczos=None, max_iter_qr=None, mode_rigid=None, prec_bathe=None, nmax_iter_bathe=None, prec_jacobi=None, max_iter_jacobi=None, type_qz=None, local_vars_configuration=None):  # noqa: E501
        """OneOfSolidNumericsEigenSolver - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._prec_soren = None
        self._nmax_iter_soren = None
        self._subspace_settings = None
        self._prec_ortho = None
        self._nmax_iter_ortho = None
        self._prec_lanczos = None
        self._max_iter_qr = None
        self._mode_rigid = None
        self._prec_bathe = None
        self._nmax_iter_bathe = None
        self._prec_jacobi = None
        self._max_iter_jacobi = None
        self._type_qz = None
        self.discriminator = 'type'

        self.type = type
        if prec_soren is not None:
            self.prec_soren = prec_soren
        if nmax_iter_soren is not None:
            self.nmax_iter_soren = nmax_iter_soren
        if subspace_settings is not None:
            self.subspace_settings = subspace_settings
        if prec_ortho is not None:
            self.prec_ortho = prec_ortho
        if nmax_iter_ortho is not None:
            self.nmax_iter_ortho = nmax_iter_ortho
        if prec_lanczos is not None:
            self.prec_lanczos = prec_lanczos
        if max_iter_qr is not None:
            self.max_iter_qr = max_iter_qr
        if mode_rigid is not None:
            self.mode_rigid = mode_rigid
        if prec_bathe is not None:
            self.prec_bathe = prec_bathe
        if nmax_iter_bathe is not None:
            self.nmax_iter_bathe = nmax_iter_bathe
        if prec_jacobi is not None:
            self.prec_jacobi = prec_jacobi
        if max_iter_jacobi is not None:
            self.max_iter_jacobi = max_iter_jacobi
        if type_qz is not None:
            self.type_qz = type_qz

    @property
    def type(self):
        """Gets the type of this OneOfSolidNumericsEigenSolver.  # noqa: E501

        Schema name: QZ  # noqa: E501

        :return: The type of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this OneOfSolidNumericsEigenSolver.

        Schema name: QZ  # noqa: E501

        :param type: The type of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501

        self._type = type

    @property
    def prec_soren(self):
        """Gets the prec_soren of this OneOfSolidNumericsEigenSolver.  # noqa: E501


        :return: The prec_soren of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :rtype: float
        """
        return self._prec_soren

    @prec_soren.setter
    def prec_soren(self, prec_soren):
        """Sets the prec_soren of this OneOfSolidNumericsEigenSolver.


        :param prec_soren: The prec_soren of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                prec_soren is not None and prec_soren < 0):  # noqa: E501
            raise ValueError("Invalid value for `prec_soren`, must be a value greater than or equal to `0`")  # noqa: E501

        self._prec_soren = prec_soren

    @property
    def nmax_iter_soren(self):
        """Gets the nmax_iter_soren of this OneOfSolidNumericsEigenSolver.  # noqa: E501


        :return: The nmax_iter_soren of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :rtype: int
        """
        return self._nmax_iter_soren

    @nmax_iter_soren.setter
    def nmax_iter_soren(self, nmax_iter_soren):
        """Sets the nmax_iter_soren of this OneOfSolidNumericsEigenSolver.


        :param nmax_iter_soren: The nmax_iter_soren of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                nmax_iter_soren is not None and nmax_iter_soren < 1):  # noqa: E501
            raise ValueError("Invalid value for `nmax_iter_soren`, must be a value greater than or equal to `1`")  # noqa: E501

        self._nmax_iter_soren = nmax_iter_soren

    @property
    def subspace_settings(self):
        """Gets the subspace_settings of this OneOfSolidNumericsEigenSolver.  # noqa: E501


        :return: The subspace_settings of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :rtype: OneOfBatheWilsonSubspaceSettings
        """
        return self._subspace_settings

    @subspace_settings.setter
    def subspace_settings(self, subspace_settings):
        """Sets the subspace_settings of this OneOfSolidNumericsEigenSolver.


        :param subspace_settings: The subspace_settings of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :type: OneOfBatheWilsonSubspaceSettings
        """

        self._subspace_settings = subspace_settings

    @property
    def prec_ortho(self):
        """Gets the prec_ortho of this OneOfSolidNumericsEigenSolver.  # noqa: E501


        :return: The prec_ortho of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :rtype: float
        """
        return self._prec_ortho

    @prec_ortho.setter
    def prec_ortho(self, prec_ortho):
        """Sets the prec_ortho of this OneOfSolidNumericsEigenSolver.


        :param prec_ortho: The prec_ortho of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                prec_ortho is not None and prec_ortho < 0):  # noqa: E501
            raise ValueError("Invalid value for `prec_ortho`, must be a value greater than or equal to `0`")  # noqa: E501

        self._prec_ortho = prec_ortho

    @property
    def nmax_iter_ortho(self):
        """Gets the nmax_iter_ortho of this OneOfSolidNumericsEigenSolver.  # noqa: E501


        :return: The nmax_iter_ortho of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :rtype: int
        """
        return self._nmax_iter_ortho

    @nmax_iter_ortho.setter
    def nmax_iter_ortho(self, nmax_iter_ortho):
        """Sets the nmax_iter_ortho of this OneOfSolidNumericsEigenSolver.


        :param nmax_iter_ortho: The nmax_iter_ortho of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                nmax_iter_ortho is not None and nmax_iter_ortho < 0):  # noqa: E501
            raise ValueError("Invalid value for `nmax_iter_ortho`, must be a value greater than or equal to `0`")  # noqa: E501

        self._nmax_iter_ortho = nmax_iter_ortho

    @property
    def prec_lanczos(self):
        """Gets the prec_lanczos of this OneOfSolidNumericsEigenSolver.  # noqa: E501


        :return: The prec_lanczos of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :rtype: float
        """
        return self._prec_lanczos

    @prec_lanczos.setter
    def prec_lanczos(self, prec_lanczos):
        """Sets the prec_lanczos of this OneOfSolidNumericsEigenSolver.


        :param prec_lanczos: The prec_lanczos of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                prec_lanczos is not None and prec_lanczos < 0):  # noqa: E501
            raise ValueError("Invalid value for `prec_lanczos`, must be a value greater than or equal to `0`")  # noqa: E501

        self._prec_lanczos = prec_lanczos

    @property
    def max_iter_qr(self):
        """Gets the max_iter_qr of this OneOfSolidNumericsEigenSolver.  # noqa: E501


        :return: The max_iter_qr of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :rtype: int
        """
        return self._max_iter_qr

    @max_iter_qr.setter
    def max_iter_qr(self, max_iter_qr):
        """Sets the max_iter_qr of this OneOfSolidNumericsEigenSolver.


        :param max_iter_qr: The max_iter_qr of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_iter_qr is not None and max_iter_qr < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_iter_qr`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_iter_qr = max_iter_qr

    @property
    def mode_rigid(self):
        """Gets the mode_rigid of this OneOfSolidNumericsEigenSolver.  # noqa: E501


        :return: The mode_rigid of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :rtype: bool
        """
        return self._mode_rigid

    @mode_rigid.setter
    def mode_rigid(self, mode_rigid):
        """Sets the mode_rigid of this OneOfSolidNumericsEigenSolver.


        :param mode_rigid: The mode_rigid of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :type: bool
        """

        self._mode_rigid = mode_rigid

    @property
    def prec_bathe(self):
        """Gets the prec_bathe of this OneOfSolidNumericsEigenSolver.  # noqa: E501


        :return: The prec_bathe of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :rtype: float
        """
        return self._prec_bathe

    @prec_bathe.setter
    def prec_bathe(self, prec_bathe):
        """Sets the prec_bathe of this OneOfSolidNumericsEigenSolver.


        :param prec_bathe: The prec_bathe of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                prec_bathe is not None and prec_bathe < 0):  # noqa: E501
            raise ValueError("Invalid value for `prec_bathe`, must be a value greater than or equal to `0`")  # noqa: E501

        self._prec_bathe = prec_bathe

    @property
    def nmax_iter_bathe(self):
        """Gets the nmax_iter_bathe of this OneOfSolidNumericsEigenSolver.  # noqa: E501


        :return: The nmax_iter_bathe of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :rtype: int
        """
        return self._nmax_iter_bathe

    @nmax_iter_bathe.setter
    def nmax_iter_bathe(self, nmax_iter_bathe):
        """Sets the nmax_iter_bathe of this OneOfSolidNumericsEigenSolver.


        :param nmax_iter_bathe: The nmax_iter_bathe of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                nmax_iter_bathe is not None and nmax_iter_bathe < 0):  # noqa: E501
            raise ValueError("Invalid value for `nmax_iter_bathe`, must be a value greater than or equal to `0`")  # noqa: E501

        self._nmax_iter_bathe = nmax_iter_bathe

    @property
    def prec_jacobi(self):
        """Gets the prec_jacobi of this OneOfSolidNumericsEigenSolver.  # noqa: E501


        :return: The prec_jacobi of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :rtype: float
        """
        return self._prec_jacobi

    @prec_jacobi.setter
    def prec_jacobi(self, prec_jacobi):
        """Sets the prec_jacobi of this OneOfSolidNumericsEigenSolver.


        :param prec_jacobi: The prec_jacobi of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :type: float
        """
        if (self.local_vars_configuration.client_side_validation and
                prec_jacobi is not None and prec_jacobi < 0):  # noqa: E501
            raise ValueError("Invalid value for `prec_jacobi`, must be a value greater than or equal to `0`")  # noqa: E501

        self._prec_jacobi = prec_jacobi

    @property
    def max_iter_jacobi(self):
        """Gets the max_iter_jacobi of this OneOfSolidNumericsEigenSolver.  # noqa: E501


        :return: The max_iter_jacobi of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :rtype: int
        """
        return self._max_iter_jacobi

    @max_iter_jacobi.setter
    def max_iter_jacobi(self, max_iter_jacobi):
        """Sets the max_iter_jacobi of this OneOfSolidNumericsEigenSolver.


        :param max_iter_jacobi: The max_iter_jacobi of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :type: int
        """
        if (self.local_vars_configuration.client_side_validation and
                max_iter_jacobi is not None and max_iter_jacobi < 0):  # noqa: E501
            raise ValueError("Invalid value for `max_iter_jacobi`, must be a value greater than or equal to `0`")  # noqa: E501

        self._max_iter_jacobi = max_iter_jacobi

    @property
    def type_qz(self):
        """Gets the type_qz of this OneOfSolidNumericsEigenSolver.  # noqa: E501


        :return: The type_qz of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :rtype: str
        """
        return self._type_qz

    @type_qz.setter
    def type_qz(self, type_qz):
        """Sets the type_qz of this OneOfSolidNumericsEigenSolver.


        :param type_qz: The type_qz of this OneOfSolidNumericsEigenSolver.  # noqa: E501
        :type: str
        """
        allowed_values = ["QZ_SIMPLE", "QZ_EQUI", "QZ_QR"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type_qz not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type_qz` ({0}), must be one of {1}"  # noqa: E501
                .format(type_qz, allowed_values)
            )

        self._type_qz = type_qz

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
        if not isinstance(other, OneOfSolidNumericsEigenSolver):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, OneOfSolidNumericsEigenSolver):
            return True

        return self.to_dict() != other.to_dict()
