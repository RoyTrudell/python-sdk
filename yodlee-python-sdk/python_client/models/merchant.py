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
from python_client.models.contact import Contact  # noqa: F401,E501
from python_client.models.coordinates import Coordinates  # noqa: F401,E501


class Merchant(object):
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
        'website': 'str',
        'address': 'AccountAddress',
        'contact': 'Contact',
        'category_label': 'list[str]',
        'coordinates': 'Coordinates',
        'name': 'str',
        'id': 'str',
        'source': 'str'
    }

    attribute_map = {
        'website': 'website',
        'address': 'address',
        'contact': 'contact',
        'category_label': 'categoryLabel',
        'coordinates': 'coordinates',
        'name': 'name',
        'id': 'id',
        'source': 'source'
    }

    def __init__(self, website=None, address=None, contact=None, category_label=None, coordinates=None, name=None, id=None, source=None):  # noqa: E501
        """Merchant - a model defined in Swagger"""  # noqa: E501

        self._website = None
        self._address = None
        self._contact = None
        self._category_label = None
        self._coordinates = None
        self._name = None
        self._id = None
        self._source = None
        self.discriminator = None

        if website is not None:
            self.website = website
        if address is not None:
            self.address = address
        if contact is not None:
            self.contact = contact
        if category_label is not None:
            self.category_label = category_label
        if coordinates is not None:
            self.coordinates = coordinates
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if source is not None:
            self.source = source

    @property
    def website(self):
        """Gets the website of this Merchant.  # noqa: E501

        The website of the merchant.<br><br><b>Applicable containers</b>: bank,creditCard,investment,loan<br>  # noqa: E501

        :return: The website of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._website

    @website.setter
    def website(self, website):
        """Sets the website of this Merchant.

        The website of the merchant.<br><br><b>Applicable containers</b>: bank,creditCard,investment,loan<br>  # noqa: E501

        :param website: The website of this Merchant.  # noqa: E501
        :type: str
        """

        self._website = website

    @property
    def address(self):
        """Gets the address of this Merchant.  # noqa: E501

        The address of the merchant associated with the transaction is populated in the merchant address field.<br><b>Note</b>: The merchant address field is not available by default and customers will have to specifically request the merchant's address (that includes city, state, and ZIP of the merchant). The merchant address field is available only for merchants in the United States.<br><br><b>Applicable containers</b>: bank,creditCard<br>  # noqa: E501

        :return: The address of this Merchant.  # noqa: E501
        :rtype: AccountAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this Merchant.

        The address of the merchant associated with the transaction is populated in the merchant address field.<br><b>Note</b>: The merchant address field is not available by default and customers will have to specifically request the merchant's address (that includes city, state, and ZIP of the merchant). The merchant address field is available only for merchants in the United States.<br><br><b>Applicable containers</b>: bank,creditCard<br>  # noqa: E501

        :param address: The address of this Merchant.  # noqa: E501
        :type: AccountAddress
        """

        self._address = address

    @property
    def contact(self):
        """Gets the contact of this Merchant.  # noqa: E501

        The merchant contact information like phone and email.<br><br><b>Applicable containers</b>: bank,creditCard,investment,loan<br>  # noqa: E501

        :return: The contact of this Merchant.  # noqa: E501
        :rtype: Contact
        """
        return self._contact

    @contact.setter
    def contact(self, contact):
        """Sets the contact of this Merchant.

        The merchant contact information like phone and email.<br><br><b>Applicable containers</b>: bank,creditCard,investment,loan<br>  # noqa: E501

        :param contact: The contact of this Merchant.  # noqa: E501
        :type: Contact
        """

        self._contact = contact

    @property
    def category_label(self):
        """Gets the category_label of this Merchant.  # noqa: E501

        The business categories of the merchant.<br><br><b>Applicable containers</b>: bank,creditCard<br><b>Applicable Values</b><br>  # noqa: E501

        :return: The category_label of this Merchant.  # noqa: E501
        :rtype: list[str]
        """
        return self._category_label

    @category_label.setter
    def category_label(self, category_label):
        """Sets the category_label of this Merchant.

        The business categories of the merchant.<br><br><b>Applicable containers</b>: bank,creditCard<br><b>Applicable Values</b><br>  # noqa: E501

        :param category_label: The category_label of this Merchant.  # noqa: E501
        :type: list[str]
        """

        self._category_label = category_label

    @property
    def coordinates(self):
        """Gets the coordinates of this Merchant.  # noqa: E501

        The merchant geolocation coordinates like latitude and longitude.<br><br><b>Applicable containers</b>: bank,creditCard,loan<br>  # noqa: E501

        :return: The coordinates of this Merchant.  # noqa: E501
        :rtype: Coordinates
        """
        return self._coordinates

    @coordinates.setter
    def coordinates(self, coordinates):
        """Sets the coordinates of this Merchant.

        The merchant geolocation coordinates like latitude and longitude.<br><br><b>Applicable containers</b>: bank,creditCard,loan<br>  # noqa: E501

        :param coordinates: The coordinates of this Merchant.  # noqa: E501
        :type: Coordinates
        """

        self._coordinates = coordinates

    @property
    def name(self):
        """Gets the name of this Merchant.  # noqa: E501

        The name of the merchant.<br><br><b>Applicable containers</b>: bank,creditCard,investment,insurance,loan<br>  # noqa: E501

        :return: The name of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Merchant.

        The name of the merchant.<br><br><b>Applicable containers</b>: bank,creditCard,investment,insurance,loan<br>  # noqa: E501

        :param name: The name of this Merchant.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this Merchant.  # noqa: E501

        Identifier of the merchant.<br><br><b>Applicable containers</b>: bank,creditCard,investment,insurance,loan<br>  # noqa: E501

        :return: The id of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Merchant.

        Identifier of the merchant.<br><br><b>Applicable containers</b>: bank,creditCard,investment,insurance,loan<br>  # noqa: E501

        :param id: The id of this Merchant.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def source(self):
        """Gets the source of this Merchant.  # noqa: E501

        The source through which merchant information is retrieved.<br><br><b>Applicable containers</b>: bank,creditCard,investment,insurance,loan<br><b>Applicable Values</b><br>  # noqa: E501

        :return: The source of this Merchant.  # noqa: E501
        :rtype: str
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this Merchant.

        The source through which merchant information is retrieved.<br><br><b>Applicable containers</b>: bank,creditCard,investment,insurance,loan<br><b>Applicable Values</b><br>  # noqa: E501

        :param source: The source of this Merchant.  # noqa: E501
        :type: str
        """
        allowed_values = ["YODLEE", "FACTUAL"]  # noqa: E501
        if source not in allowed_values:
            raise ValueError(
                "Invalid value for `source` ({0}), must be one of {1}"  # noqa: E501
                .format(source, allowed_values)
            )

        self._source = source

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
        if issubclass(Merchant, dict):
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
        if not isinstance(other, Merchant):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other