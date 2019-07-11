# coding: utf-8

"""
    LAMP Platform

    The LAMP Platform API.  # noqa: E501

    OpenAPI spec version: 0.1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ResponseMeta(object):
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
        'link': 'ResponseMetaLink',
        'access': 'ResponseMetaAccess'
    }

    attribute_map = {
        'link': 'link',
        'access': 'access'
    }

    def __init__(self, link=None, access=None):  # noqa: E501
        """ResponseMeta - a model defined in OpenAPI"""  # noqa: E501

        self._link = None
        self._access = None
        self.discriminator = None

        if link is not None:
            self.link = link
        if access is not None:
            self.access = access

    @property
    def link(self):
        """Gets the link of this ResponseMeta.  # noqa: E501


        :return: The link of this ResponseMeta.  # noqa: E501
        :rtype: ResponseMetaLink
        """
        return self._link

    @link.setter
    def link(self, link):
        """Sets the link of this ResponseMeta.


        :param link: The link of this ResponseMeta.  # noqa: E501
        :type: ResponseMetaLink
        """

        self._link = link

    @property
    def access(self):
        """Gets the access of this ResponseMeta.  # noqa: E501


        :return: The access of this ResponseMeta.  # noqa: E501
        :rtype: ResponseMetaAccess
        """
        return self._access

    @access.setter
    def access(self, access):
        """Sets the access of this ResponseMeta.


        :param access: The access of this ResponseMeta.  # noqa: E501
        :type: ResponseMetaAccess
        """

        self._access = access

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
        if not isinstance(other, ResponseMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other