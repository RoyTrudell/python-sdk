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

from python_client.models.container_attributes import ContainerAttributes  # noqa: F401,E501


class Attribute(object):
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
        'container': 'list[str]',
        'container_attributes': 'ContainerAttributes',
        'name': 'str'
    }

    attribute_map = {
        'container': 'container',
        'container_attributes': 'containerAttributes',
        'name': 'name'
    }

    def __init__(self, container=None, container_attributes=None, name=None):  # noqa: E501
        """Attribute - a model defined in Swagger"""  # noqa: E501

        self._container = None
        self._container_attributes = None
        self._name = None
        self.discriminator = None

        if container is not None:
            self.container = container
        if container_attributes is not None:
            self.container_attributes = container_attributes
        if name is not None:
            self.name = name

    @property
    def container(self):
        """Gets the container of this Attribute.  # noqa: E501

        Containers for which the attributes are supported.<br><br><b>Endpoints</b>:<ul><li>GET providers</li><li>GET providers/{providerId}</li></ul>  # noqa: E501

        :return: The container of this Attribute.  # noqa: E501
        :rtype: list[str]
        """
        return self._container

    @container.setter
    def container(self, container):
        """Sets the container of this Attribute.

        Containers for which the attributes are supported.<br><br><b>Endpoints</b>:<ul><li>GET providers</li><li>GET providers/{providerId}</li></ul>  # noqa: E501

        :param container: The container of this Attribute.  # noqa: E501
        :type: list[str]
        """
        allowed_values = ["bank", "creditCard", "investment", "insurance", "loan", "reward", "bill", "realEstate", "otherAssets", "otherLiabilities"]  # noqa: E501
        if not set(container).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `container` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(container) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._container = container

    @property
    def container_attributes(self):
        """Gets the container_attributes of this Attribute.  # noqa: E501


        :return: The container_attributes of this Attribute.  # noqa: E501
        :rtype: ContainerAttributes
        """
        return self._container_attributes

    @container_attributes.setter
    def container_attributes(self, container_attributes):
        """Sets the container_attributes of this Attribute.


        :param container_attributes: The container_attributes of this Attribute.  # noqa: E501
        :type: ContainerAttributes
        """

        self._container_attributes = container_attributes

    @property
    def name(self):
        """Gets the name of this Attribute.  # noqa: E501

        Attributes that are supported for a dataset.<br><br><b>Endpoints</b>:<ul><li>GET providers</li><li>GET providers/{providerId}</li></ul>  # noqa: E501

        :return: The name of this Attribute.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Attribute.

        Attributes that are supported for a dataset.<br><br><b>Endpoints</b>:<ul><li>GET providers</li><li>GET providers/{providerId}</li></ul>  # noqa: E501

        :param name: The name of this Attribute.  # noqa: E501
        :type: str
        """
        allowed_values = ["BASIC_ACCOUNT_INFO", "TRANSACTIONS", "STATEMENTS", "HOLDINGS", "ACCOUNT_DETAILS", "TAX", "EBILLS", "FULL_ACCT_NUMBER", "BANK_TRANSFER_CODE", "HOLDER_NAME", "HOLDER_DETAILS", "PAYMENT_PROFILE", "PAYMENT_DETAILS", "INTEREST_DETAILS", "COVERAGE"]  # noqa: E501
        if name not in allowed_values:
            raise ValueError(
                "Invalid value for `name` ({0}), must be one of {1}"  # noqa: E501
                .format(name, allowed_values)
            )

        self._name = name

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
        if issubclass(Attribute, dict):
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
        if not isinstance(other, Attribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
