"""
    Internship API

    This API delivers data for the Internship project.  # noqa: E501

    The version of the OpenAPI document: 1.1.6
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_internship_sdk
from osis_internship_sdk.model.cohort_get import CohortGet
from osis_internship_sdk.model.country import Country
globals()['CohortGet'] = CohortGet
globals()['Country'] = Country
from osis_internship_sdk.model.organization_get import OrganizationGet


class TestOrganizationGet(unittest.TestCase):
    """OrganizationGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testOrganizationGet(self):
        """Test OrganizationGet"""
        # FIXME: construct object with mandatory attributes with example values
        # model = OrganizationGet()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
