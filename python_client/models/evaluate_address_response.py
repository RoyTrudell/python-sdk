# coding: utf-8

"""
    Yodlee Core APIs

    This file describes the Yodlee Platform APIs, using the swagger notation. You can use this swagger file to generate client side SDKs to the Yodlee Platform APIs for many different programming languages. You can generate a client SDK for Python, Java, javascript, PHP or other languages according to your development needs. For more details about our APIs themselves, please refer to https://developer.yodlee.com/Yodlee_API/.  # noqa: E501

    OpenAPI spec version: 1.1.0
    Contact: developer@yodlee.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from python_client.models.account_address import AccountAddress  # noqa: F401,E501


class EvaluateAddressResponse(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'address': 'list[AccountAddress]',
        'is_valid_address': 'bool'
    }

    attribute_map = {
        'address': 'address',
        'is_valid_address': 'isValidAddress'
    }

    def __init__(self, address=None, is_valid_address=None):  # noqa: E501
        """EvaluateAddressResponse - a model defined in Swagger"""  # noqa: E501

        self._address = None
        self._is_valid_address = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if is_valid_address is not None:
            self.is_valid_address = is_valid_address

    @property
    def address(self):
        """Gets the address of this EvaluateAddressResponse.  # noqa: E501


        :return: The address of this EvaluateAddressResponse.  # noqa: E501
        :rtype: list[AccountAddress]
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this EvaluateAddressResponse.


        :param address: The address of this EvaluateAddressResponse.  # noqa: E501
        :type: list[AccountAddress]
        """

        self._address = address

    @property
    def is_valid_address(self):
        """Gets the is_valid_address of this EvaluateAddressResponse.  # noqa: E501


        :return: The is_valid_address of this EvaluateAddressResponse.  # noqa: E501
        :rtype: bool
        """
        return self._is_valid_address

    @is_valid_address.setter
    def is_valid_address(self, is_valid_address):
        """Sets the is_valid_address of this EvaluateAddressResponse.


        :param is_valid_address: The is_valid_address of this EvaluateAddressResponse.  # noqa: E501
        :type: bool
        """

        self._is_valid_address = is_valid_address

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
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
        if issubclass(EvaluateAddressResponse, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, EvaluateAddressResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
