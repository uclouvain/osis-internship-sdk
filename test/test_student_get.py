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
from osis_internship_sdk.model.person import Person
globals()['CohortGet'] = CohortGet
globals()['Person'] = Person
from osis_internship_sdk.model.student_get import StudentGet


class TestStudentGet(unittest.TestCase):
    """StudentGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStudentGet(self):
        """Test StudentGet"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StudentGet()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
