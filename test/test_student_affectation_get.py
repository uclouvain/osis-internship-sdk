"""
    Internship API

    This API delivers data for the Internship project.  # noqa: E501

    The version of the OpenAPI document: 1.1.9
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_internship_sdk
from osis_internship_sdk.model.period_get import PeriodGet
from osis_internship_sdk.model.score_list_get import ScoreListGet
from osis_internship_sdk.model.student import Student
globals()['PeriodGet'] = PeriodGet
globals()['ScoreListGet'] = ScoreListGet
globals()['Student'] = Student
from osis_internship_sdk.model.student_affectation_get import StudentAffectationGet


class TestStudentAffectationGet(unittest.TestCase):
    """StudentAffectationGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testStudentAffectationGet(self):
        """Test StudentAffectationGet"""
        # FIXME: construct object with mandatory attributes with example values
        # model = StudentAffectationGet()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
