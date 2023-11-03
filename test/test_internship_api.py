"""
    Internship API

    This API delivers data for the Internship project.  # noqa: E501

    The version of the OpenAPI document: 1.1.14
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_internship_sdk
from osis_internship_sdk.api.internship_api import InternshipApi  # noqa: E501


class TestInternshipApi(unittest.TestCase):
    """InternshipApi unit test stubs"""

    def setUp(self):
        self.api = InternshipApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_choices_get(self):
        """Test case for choices_get

        """
        pass

    def test_cohorts_get(self):
        """Test case for cohorts_get

        """
        pass

    def test_cohorts_name_get(self):
        """Test case for cohorts_name_get

        """
        pass

    def test_cohorts_name_is_open_for_selection_get(self):
        """Test case for cohorts_name_is_open_for_selection_get

        """
        pass

    def test_delete_choices_internship_uuid_delete(self):
        """Test case for delete_choices_internship_uuid_delete

        """
        pass

    def test_first_choices_count_cohort_name_get(self):
        """Test case for first_choices_count_cohort_name_get

        """
        pass

    def test_internships_get(self):
        """Test case for internships_get

        """
        pass

    def test_internships_uuid_get(self):
        """Test case for internships_uuid_get

        """
        pass

    def test_masters_allocations_get(self):
        """Test case for masters_allocations_get

        """
        pass

    def test_masters_allocations_post(self):
        """Test case for masters_allocations_post

        """
        pass

    def test_masters_allocations_uuid_delete(self):
        """Test case for masters_allocations_uuid_delete

        """
        pass

    def test_masters_allocations_uuid_get(self):
        """Test case for masters_allocations_uuid_get

        """
        pass

    def test_masters_get(self):
        """Test case for masters_get

        """
        pass

    def test_masters_post(self):
        """Test case for masters_post

        """
        pass

    def test_masters_uuid_activate_account_post(self):
        """Test case for masters_uuid_activate_account_post

        """
        pass

    def test_masters_uuid_allocations_get(self):
        """Test case for masters_uuid_allocations_get

        """
        pass

    def test_masters_uuid_get(self):
        """Test case for masters_uuid_get

        """
        pass

    def test_offers_get(self):
        """Test case for offers_get

        """
        pass

    def test_organizations_get(self):
        """Test case for organizations_get

        """
        pass

    def test_organizations_uuid_get(self):
        """Test case for organizations_uuid_get

        """
        pass

    def test_periods_get(self):
        """Test case for periods_get

        """
        pass

    def test_periods_uuid_get(self):
        """Test case for periods_uuid_get

        """
        pass

    def test_person_affectations_cohort_person_uuid_get(self):
        """Test case for person_affectations_cohort_person_uuid_get

        """
        pass

    def test_place_evaluation_affectation_uuid_get(self):
        """Test case for place_evaluation_affectation_uuid_get

        """
        pass

    def test_place_evaluation_affectation_uuid_put(self):
        """Test case for place_evaluation_affectation_uuid_put

        """
        pass

    def test_place_evaluation_items_cohort_get(self):
        """Test case for place_evaluation_items_cohort_get

        """
        pass

    def test_save_choice_internship_uuid_post(self):
        """Test case for save_choice_internship_uuid_post

        """
        pass

    def test_scores_affectation_uuid_get(self):
        """Test case for scores_affectation_uuid_get

        """
        pass

    def test_scores_affectation_uuid_put(self):
        """Test case for scores_affectation_uuid_put

        """
        pass

    def test_scores_affectation_uuid_validate_post(self):
        """Test case for scores_affectation_uuid_validate_post

        """
        pass

    def test_specialties_get(self):
        """Test case for specialties_get

        """
        pass

    def test_specialties_uuid_get(self):
        """Test case for specialties_uuid_get

        """
        pass

    def test_students_affectations_affectation_uuid_get(self):
        """Test case for students_affectations_affectation_uuid_get

        """
        pass

    def test_students_affectations_specialty_organization_get(self):
        """Test case for students_affectations_specialty_organization_get

        """
        pass

    def test_students_affectations_specialty_organization_stats_get(self):
        """Test case for students_affectations_specialty_organization_stats_get

        """
        pass

    def test_students_get(self):
        """Test case for students_get

        """
        pass

    def test_students_global_id_get(self):
        """Test case for students_global_id_get

        """
        pass


if __name__ == '__main__':
    unittest.main()
