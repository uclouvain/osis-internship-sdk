"""
    Internship API

    This API delivers data for the Internship project.  # noqa: E501

    The version of the OpenAPI document: 1.1.15
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_internship_sdk
from osis_internship_sdk.model.organization_get import OrganizationGet
from osis_internship_sdk.model.period_get import PeriodGet
from osis_internship_sdk.model.specialty_get import SpecialtyGet
globals()['OrganizationGet'] = OrganizationGet
globals()['PeriodGet'] = PeriodGet
globals()['SpecialtyGet'] = SpecialtyGet
from osis_internship_sdk.model.person_affectation_get import PersonAffectationGet


class TestPersonAffectationGet(unittest.TestCase):
    """PersonAffectationGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPersonAffectationGet(self):
        """Test PersonAffectationGet"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PersonAffectationGet()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
