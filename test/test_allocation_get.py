"""
    Internship API

    This API delivers data for the Internship project.  # noqa: E501

    The version of the OpenAPI document: 1.1.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_internship_sdk
from osis_internship_sdk.model.master_get import MasterGet
from osis_internship_sdk.model.organization_get import OrganizationGet
from osis_internship_sdk.model.specialty_get import SpecialtyGet
globals()['MasterGet'] = MasterGet
globals()['OrganizationGet'] = OrganizationGet
globals()['SpecialtyGet'] = SpecialtyGet
from osis_internship_sdk.model.allocation_get import AllocationGet


class TestAllocationGet(unittest.TestCase):
    """AllocationGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testAllocationGet(self):
        """Test AllocationGet"""
        # FIXME: construct object with mandatory attributes with example values
        # model = AllocationGet()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
