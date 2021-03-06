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


class ConfigsPublicKey(object):
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
        'alias': 'str',
        'key': 'str'
    }

    attribute_map = {
        'alias': 'alias',
        'key': 'key'
    }

    def __init__(self, alias=None, key=None):  # noqa: E501
        """ConfigsPublicKey - a model defined in Swagger"""  # noqa: E501

        self._alias = None
        self._key = None
        self.discriminator = None

        if alias is not None:
            self.alias = alias
        if key is not None:
            self.key = key

    @property
    def alias(self):
        """Gets the alias of this ConfigsPublicKey.  # noqa: E501

        The key name used for encryption.<br><br><b>Endpoints</b>:<ul><li>GET configs/publicKey</li></ul>  # noqa: E501

        :return: The alias of this ConfigsPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._alias

    @alias.setter
    def alias(self, alias):
        """Sets the alias of this ConfigsPublicKey.

        The key name used for encryption.<br><br><b>Endpoints</b>:<ul><li>GET configs/publicKey</li></ul>  # noqa: E501

        :param alias: The alias of this ConfigsPublicKey.  # noqa: E501
        :type: str
        """

        self._alias = alias

    @property
    def key(self):
        """Gets the key of this ConfigsPublicKey.  # noqa: E501

        Public key that the customer should be using to encrypt the credentials and answers before sending to the add and update providerAccounts APIs.<br><br><b>Endpoints</b>:<ul><li>GET configs/publicKey</li></ul>  # noqa: E501

        :return: The key of this ConfigsPublicKey.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ConfigsPublicKey.

        Public key that the customer should be using to encrypt the credentials and answers before sending to the add and update providerAccounts APIs.<br><br><b>Endpoints</b>:<ul><li>GET configs/publicKey</li></ul>  # noqa: E501

        :param key: The key of this ConfigsPublicKey.  # noqa: E501
        :type: str
        """

        self._key = key

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
        if issubclass(ConfigsPublicKey, dict):
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
        if not isinstance(other, ConfigsPublicKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
