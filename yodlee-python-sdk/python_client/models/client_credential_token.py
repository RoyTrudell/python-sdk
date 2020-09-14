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


class ClientCredentialToken(object):
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
        'expires_in': 'int',
        'issued_at': 'str',
        'access_token': 'str'
    }

    attribute_map = {
        'expires_in': 'expiresIn',
        'issued_at': 'issuedAt',
        'access_token': 'accessToken'
    }

    def __init__(self, expires_in=None, issued_at=None, access_token=None):  # noqa: E501
        """ClientCredentialToken - a model defined in Swagger"""  # noqa: E501

        self._expires_in = None
        self._issued_at = None
        self._access_token = None
        self.discriminator = None

        if expires_in is not None:
            self.expires_in = expires_in
        if issued_at is not None:
            self.issued_at = issued_at
        if access_token is not None:
            self.access_token = access_token

    @property
    def expires_in(self):
        """Gets the expires_in of this ClientCredentialToken.  # noqa: E501

        Time in seconds after which the issued accessToken expires.<br><br><b>Endpoints</b>:<ul><li>POST /auth/token</li></ul>  # noqa: E501

        :return: The expires_in of this ClientCredentialToken.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this ClientCredentialToken.

        Time in seconds after which the issued accessToken expires.<br><br><b>Endpoints</b>:<ul><li>POST /auth/token</li></ul>  # noqa: E501

        :param expires_in: The expires_in of this ClientCredentialToken.  # noqa: E501
        :type: int
        """

        self._expires_in = expires_in

    @property
    def issued_at(self):
        """Gets the issued_at of this ClientCredentialToken.  # noqa: E501

        The date and time on which accessToken was created for the customer.<br><br><b>Endpoints</b>:<ul><li>POST /auth/token</li></ul>  # noqa: E501

        :return: The issued_at of this ClientCredentialToken.  # noqa: E501
        :rtype: str
        """
        return self._issued_at

    @issued_at.setter
    def issued_at(self, issued_at):
        """Sets the issued_at of this ClientCredentialToken.

        The date and time on which accessToken was created for the customer.<br><br><b>Endpoints</b>:<ul><li>POST /auth/token</li></ul>  # noqa: E501

        :param issued_at: The issued_at of this ClientCredentialToken.  # noqa: E501
        :type: str
        """

        self._issued_at = issued_at

    @property
    def access_token(self):
        """Gets the access_token of this ClientCredentialToken.  # noqa: E501

        Access Token to access YSL 1.1 services.<br><br><b>Endpoints</b>:<ul><li>POST /auth/token</li></ul>  # noqa: E501

        :return: The access_token of this ClientCredentialToken.  # noqa: E501
        :rtype: str
        """
        return self._access_token

    @access_token.setter
    def access_token(self, access_token):
        """Sets the access_token of this ClientCredentialToken.

        Access Token to access YSL 1.1 services.<br><br><b>Endpoints</b>:<ul><li>POST /auth/token</li></ul>  # noqa: E501

        :param access_token: The access_token of this ClientCredentialToken.  # noqa: E501
        :type: str
        """

        self._access_token = access_token

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
        if issubclass(ClientCredentialToken, dict):
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
        if not isinstance(other, ClientCredentialToken):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other