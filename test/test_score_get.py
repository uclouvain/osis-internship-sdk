"""
    Internship API

    This API delivers data for the Internship project.  # noqa: E501

    The version of the OpenAPI document: 1.0.11
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_internship_sdk
from osis_internship_sdk.model.cohort_get import CohortGet
from osis_internship_sdk.model.period_get import PeriodGet
from osis_internship_sdk.model.student import Student
globals()['CohortGet'] = CohortGet
globals()['PeriodGet'] = PeriodGet
globals()['Student'] = Student
from osis_internship_sdk.model.score_get import ScoreGet


class TestScoreGet(unittest.TestCase):
    """ScoreGet unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testScoreGet(self):
        """Test ScoreGet"""
        # FIXME: construct object with mandatory attributes with example values
        # model = ScoreGet()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
