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

from python_client.models.account_dataset import AccountDataset  # noqa: F401,E501
from python_client.models.login_form import LoginForm  # noqa: F401,E501
from python_client.models.provider_account_preferences import ProviderAccountPreferences  # noqa: F401,E501


class ProviderAccountDetail(object):
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
        'last_updated': 'str',
        'consent_id': 'int',
        'login_form': 'list[LoginForm]',
        'preferences': 'ProviderAccountPreferences',
        'created_date': 'str',
        'aggregation_source': 'str',
        'provider_id': 'int',
        'request_id': 'str',
        'is_manual': 'bool',
        'id': 'int',
        'dataset': 'list[AccountDataset]',
        'status': 'str'
    }

    attribute_map = {
        'last_updated': 'lastUpdated',
        'consent_id': 'consentId',
        'login_form': 'loginForm',
        'preferences': 'preferences',
        'created_date': 'createdDate',
        'aggregation_source': 'aggregationSource',
        'provider_id': 'providerId',
        'request_id': 'requestId',
        'is_manual': 'isManual',
        'id': 'id',
        'dataset': 'dataset',
        'status': 'status'
    }

    def __init__(self, last_updated=None, consent_id=None, login_form=None, preferences=None, created_date=None, aggregation_source=None, provider_id=None, request_id=None, is_manual=None, id=None, dataset=None, status=None):  # noqa: E501
        """ProviderAccountDetail - a model defined in Swagger"""  # noqa: E501

        self._last_updated = None
        self._consent_id = None
        self._login_form = None
        self._preferences = None
        self._created_date = None
        self._aggregation_source = None
        self._provider_id = None
        self._request_id = None
        self._is_manual = None
        self._id = None
        self._dataset = None
        self._status = None
        self.discriminator = None

        if last_updated is not None:
            self.last_updated = last_updated
        self.consent_id = consent_id
        if login_form is not None:
            self.login_form = login_form
        if preferences is not None:
            self.preferences = preferences
        if created_date is not None:
            self.created_date = created_date
        if aggregation_source is not None:
            self.aggregation_source = aggregation_source
        if provider_id is not None:
            self.provider_id = provider_id
        if request_id is not None:
            self.request_id = request_id
        if is_manual is not None:
            self.is_manual = is_manual
        if id is not None:
            self.id = id
        if dataset is not None:
            self.dataset = dataset
        if status is not None:
            self.status = status

    @property
    def last_updated(self):
        """Gets the last_updated of this ProviderAccountDetail.  # noqa: E501

        Indicate when the providerAccount is last updated successfully.<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :return: The last_updated of this ProviderAccountDetail.  # noqa: E501
        :rtype: str
        """
        return self._last_updated

    @last_updated.setter
    def last_updated(self, last_updated):
        """Sets the last_updated of this ProviderAccountDetail.

        Indicate when the providerAccount is last updated successfully.<br><br><b>Account Type</b>: Aggregated<br><b>Endpoints</b>:<ul><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :param last_updated: The last_updated of this ProviderAccountDetail.  # noqa: E501
        :type: str
        """

        self._last_updated = last_updated

    @property
    def consent_id(self):
        """Gets the consent_id of this ProviderAccountDetail.  # noqa: E501

        Consent Id generated through POST Consent.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul>  # noqa: E501

        :return: The consent_id of this ProviderAccountDetail.  # noqa: E501
        :rtype: int
        """
        return self._consent_id

    @consent_id.setter
    def consent_id(self, consent_id):
        """Sets the consent_id of this ProviderAccountDetail.

        Consent Id generated through POST Consent.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul>  # noqa: E501

        :param consent_id: The consent_id of this ProviderAccountDetail.  # noqa: E501
        :type: int
        """
        if consent_id is None:
            raise ValueError("Invalid value for `consent_id`, must not be `None`")  # noqa: E501

        self._consent_id = consent_id

    @property
    def login_form(self):
        """Gets the login_form of this ProviderAccountDetail.  # noqa: E501

        This entity gets returned in the response for only MFA based provider accounts during the add/update account polling process. This indicates that the MFA information is expected from the user to complete the process. This represents the structure of MFA form that is displayed to the user in the provider site.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul>  # noqa: E501

        :return: The login_form of this ProviderAccountDetail.  # noqa: E501
        :rtype: list[LoginForm]
        """
        return self._login_form

    @login_form.setter
    def login_form(self, login_form):
        """Sets the login_form of this ProviderAccountDetail.

        This entity gets returned in the response for only MFA based provider accounts during the add/update account polling process. This indicates that the MFA information is expected from the user to complete the process. This represents the structure of MFA form that is displayed to the user in the provider site.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul>  # noqa: E501

        :param login_form: The login_form of this ProviderAccountDetail.  # noqa: E501
        :type: list[LoginForm]
        """

        self._login_form = login_form

    @property
    def preferences(self):
        """Gets the preferences of this ProviderAccountDetail.  # noqa: E501

        User preference values for Auto-Refresh and DataExtracts Notification<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>GET providerAccounts/{providerAccountId}</li></ul>  # noqa: E501

        :return: The preferences of this ProviderAccountDetail.  # noqa: E501
        :rtype: ProviderAccountPreferences
        """
        return self._preferences

    @preferences.setter
    def preferences(self, preferences):
        """Sets the preferences of this ProviderAccountDetail.

        User preference values for Auto-Refresh and DataExtracts Notification<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>GET providerAccounts/{providerAccountId}</li></ul>  # noqa: E501

        :param preferences: The preferences of this ProviderAccountDetail.  # noqa: E501
        :type: ProviderAccountPreferences
        """

        self._preferences = preferences

    @property
    def created_date(self):
        """Gets the created_date of this ProviderAccountDetail.  # noqa: E501

        The date on when the provider account is created in the system.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul>  # noqa: E501

        :return: The created_date of this ProviderAccountDetail.  # noqa: E501
        :rtype: str
        """
        return self._created_date

    @created_date.setter
    def created_date(self, created_date):
        """Sets the created_date of this ProviderAccountDetail.

        The date on when the provider account is created in the system.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul>  # noqa: E501

        :param created_date: The created_date of this ProviderAccountDetail.  # noqa: E501
        :type: str
        """

        self._created_date = created_date

    @property
    def aggregation_source(self):
        """Gets the aggregation_source of this ProviderAccountDetail.  # noqa: E501

        The source through which the providerAccount is added in the system.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li><li>GET dataExtracts/userData</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :return: The aggregation_source of this ProviderAccountDetail.  # noqa: E501
        :rtype: str
        """
        return self._aggregation_source

    @aggregation_source.setter
    def aggregation_source(self, aggregation_source):
        """Sets the aggregation_source of this ProviderAccountDetail.

        The source through which the providerAccount is added in the system.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li><li>GET dataExtracts/userData</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :param aggregation_source: The aggregation_source of this ProviderAccountDetail.  # noqa: E501
        :type: str
        """
        allowed_values = ["SYSTEM", "USER"]  # noqa: E501
        if aggregation_source not in allowed_values:
            raise ValueError(
                "Invalid value for `aggregation_source` ({0}), must be one of {1}"  # noqa: E501
                .format(aggregation_source, allowed_values)
            )

        self._aggregation_source = aggregation_source

    @property
    def provider_id(self):
        """Gets the provider_id of this ProviderAccountDetail.  # noqa: E501

        Unique identifier for the provider resource. This denotes the provider for which the provider account id is generated by the user.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :return: The provider_id of this ProviderAccountDetail.  # noqa: E501
        :rtype: int
        """
        return self._provider_id

    @provider_id.setter
    def provider_id(self, provider_id):
        """Sets the provider_id of this ProviderAccountDetail.

        Unique identifier for the provider resource. This denotes the provider for which the provider account id is generated by the user.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :param provider_id: The provider_id of this ProviderAccountDetail.  # noqa: E501
        :type: int
        """

        self._provider_id = provider_id

    @property
    def request_id(self):
        """Gets the request_id of this ProviderAccountDetail.  # noqa: E501

        Unique id generated to indicate the request.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul>  # noqa: E501

        :return: The request_id of this ProviderAccountDetail.  # noqa: E501
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ProviderAccountDetail.

        Unique id generated to indicate the request.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li></ul>  # noqa: E501

        :param request_id: The request_id of this ProviderAccountDetail.  # noqa: E501
        :type: str
        """

        self._request_id = request_id

    @property
    def is_manual(self):
        """Gets the is_manual of this ProviderAccountDetail.  # noqa: E501

        Indicates whether account is a manual or aggregated provider account.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :return: The is_manual of this ProviderAccountDetail.  # noqa: E501
        :rtype: bool
        """
        return self._is_manual

    @is_manual.setter
    def is_manual(self, is_manual):
        """Sets the is_manual of this ProviderAccountDetail.

        Indicates whether account is a manual or aggregated provider account.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :param is_manual: The is_manual of this ProviderAccountDetail.  # noqa: E501
        :type: bool
        """

        self._is_manual = is_manual

    @property
    def id(self):
        """Gets the id of this ProviderAccountDetail.  # noqa: E501

        Unique identifier for the provider account resource. This is created during account addition.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :return: The id of this ProviderAccountDetail.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProviderAccountDetail.

        Unique identifier for the provider account resource. This is created during account addition.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :param id: The id of this ProviderAccountDetail.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def dataset(self):
        """Gets the dataset of this ProviderAccountDetail.  # noqa: E501

        Logical grouping of dataset attributes into datasets such as Basic Aggregation Data, Account Profile and Documents.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :return: The dataset of this ProviderAccountDetail.  # noqa: E501
        :rtype: list[AccountDataset]
        """
        return self._dataset

    @dataset.setter
    def dataset(self, dataset):
        """Sets the dataset of this ProviderAccountDetail.

        Logical grouping of dataset attributes into datasets such as Basic Aggregation Data, Account Profile and Documents.<br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li><li>GET dataExtracts/userData</li></ul>  # noqa: E501

        :param dataset: The dataset of this ProviderAccountDetail.  # noqa: E501
        :type: list[AccountDataset]
        """

        self._dataset = dataset

    @property
    def status(self):
        """Gets the status of this ProviderAccountDetail.  # noqa: E501

        The status of last update attempted for the account. <br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li><li>GET dataExtracts/userData</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :return: The status of this ProviderAccountDetail.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ProviderAccountDetail.

        The status of last update attempted for the account. <br><br><b>Endpoints</b>:<ul><li>GET providerAccounts</li><li>POST providerAccounts</li><li>PUT providerAccounts/{providerAccountId}</li><li>GET providerAccounts/{providerAccountId}</li><li>GET dataExtracts/userData</li></ul><b>Applicable Values</b><br>  # noqa: E501

        :param status: The status of this ProviderAccountDetail.  # noqa: E501
        :type: str
        """
        allowed_values = ["LOGIN_IN_PROGRESS", "USER_INPUT_REQUIRED", "IN_PROGRESS", "PARTIAL_SUCCESS", "SUCCESS", "FAILED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(ProviderAccountDetail, dict):
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
        if not isinstance(other, ProviderAccountDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
