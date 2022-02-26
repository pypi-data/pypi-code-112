# coding: utf-8

"""
    printnanny-api-client

    Official API client library for print-nanny.com  # noqa: E501

    The version of the OpenAPI document: 0.0.0
    Contact: leigh@print-nanny.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import printnanny_api_client
from printnanny_api_client.models.system_info import SystemInfo  # noqa: E501
from printnanny_api_client.rest import ApiException

class TestSystemInfo(unittest.TestCase):
    """SystemInfo unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test SystemInfo
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = printnanny_api_client.models.system_info.SystemInfo()  # noqa: E501
        if include_optional :
            return SystemInfo(
                id = 56, 
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                machine_id = '', 
                hardware = '', 
                revision = '', 
                model = '', 
                serial = '', 
                cores = -2147483648, 
                ram = -9223372036854775808, 
                image_version = '', 
                ansible_collection_version = '', 
                device = 56
            )
        else :
            return SystemInfo(
                id = 56,
                created_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                updated_dt = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                machine_id = '',
                hardware = '',
                revision = '',
                model = '',
                serial = '',
                cores = -2147483648,
                ram = -9223372036854775808,
                image_version = '',
                ansible_collection_version = '',
                device = 56,
        )

    def testSystemInfo(self):
        """Test SystemInfo"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
