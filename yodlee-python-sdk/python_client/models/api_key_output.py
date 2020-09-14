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


class ApiKeyOutput(object):
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
        'created_date': 'str',
        'public_key': 'str',
        'key': 'str'
    }

    attribute_map = {
        'expires_in': 'expiresIn',
        'created_date': 'createdDate',
        'public_key': 'publicKey',
        'key': 'key'
    }

    def __init__(self, expires_in=None, created_date=None, public_key=None, key=None):  # noqa: E501
        """ApiKeyOutput - a model defined in Swagger"""  # noqa: E501

        self._expires_in = None
        self._created_date = None
        self._public_key = None
        self._key = None
        self.discriminator = None

        if expires_in is not None:
            self.expires_in = expires_in
        if created_date is not None:
            self.created_date = created_date
        if public_key is not None:
            self.public_key = public_key
        if key is not None:
            self.key = key

    @property
    def expires_in(self):
        """Gets the expires_in of this ApiKeyOutput.  # noqa: E501

        Time in seconds after which the JWT token created for users expires.<br><br><b>Endpoints</b>:<ul><li>GET /auth/apiKey</li><li>POST /auth/apiKey</li></ul>  # noqa: E501

        :return: The expires_in of this ApiKeyOutput.  # noqa: E501
        :rtype: int
        """
        return self._expires_in

    @expires_in.setter
    def expires_in(self, expires_in):
        """Sets the expires_in of this ApiKeyOutput.

        Time in seconds after which the JWT token created for users expires.<br><br><b>Endpoints</b>:<ul><li>GET /auth/apiKey</li><li>POST /auth/apiKey</li></ul>  # noqa: E501

        :param expires_in: The expires_in of this ApiKeyOutput.  # noqa: E501
        :type: int
        """

        self._expires_in = expires_in

    @property
    def created_date(self):
        """Gets the created_date of this ApiKeyOutput.  # noqa: E501

        The date on which the apiKey was created for the customer.<br><br><b>Endpoints</b>:<ul><li>GET /auth/apiKey</li><li>POST /auth/apiKey</li></ul>  # noqa: E501

        :return: The created_date of this ApiKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ApiKeyOutput.

        The date on which the apiKey was created for the customer.<br><br><b>Endpoints</b>:<ul><li>GET /auth/apiKey</li><li>POST /auth/apiKey</li></ul>  # noqa: E501

        :param created_date: The created_date of this ApiKeyOutput.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def public_key(self):
        """Gets the public_key of this ApiKeyOutput.  # noqa: E501

        Public key uploaded by the customer while generating ApiKey.<br><br><b>Endpoints</b>:<ul><li>GET /auth/apiKey</li><li>POST /auth/apiKey</li></ul>  # noqa: E501

        :return: The public_key of this ApiKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this ApiKeyOutput.

        Public key uploaded by the customer while generating ApiKey.<br><br><b>Endpoints</b>:<ul><li>GET /auth/apiKey</li><li>POST /auth/apiKey</li></ul>  # noqa: E501

        :param public_key: The public_key of this ApiKeyOutput.  # noqa: E501
        :type: str
        """
        if public_key is not None and len(public_key) > 2147483647:
            raise ValueError("Invalid value for `public_key`, length must be less than or equal to `2147483647`")  # noqa: E501
        if public_key is not None and len(public_key) < 1:
            raise ValueError("Invalid value for `public_key`, length must be greater than or equal to `1`")  # noqa: E501

        self._public_key = public_key

    @property
    def key(self):
        """Gets the key of this ApiKeyOutput.  # noqa: E501

        ApiKey or the issuer key used to generate the JWT token for authentication.<br><br><b>Endpoints</b>:<ul><li>GET /auth/apiKey</li><li>POST /auth/apiKey</li></ul>  # noqa: E501

        :return: The key of this ApiKeyOutput.  # noqa: E501
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this ApiKeyOutput.

        ApiKey or the issuer key used to generate the JWT token for authentication.<br><br><b>Endpoints</b>:<ul><li>GET /auth/apiKey</li><li>POST /auth/apiKey</li></ul>  # noqa: E501

        :param key: The key of this ApiKeyOutput.  # noqa: E501
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
        if issubclass(ApiKeyOutput, dict):
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
        if not isinstance(other, ApiKeyOutput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
