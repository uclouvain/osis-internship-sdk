# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_internship_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_internship_sdk.model.allocation_get import AllocationGet
from osis_internship_sdk.model.cohort_get import CohortGet
from osis_internship_sdk.model.country import Country
from osis_internship_sdk.model.inline_response404 import InlineResponse404
from osis_internship_sdk.model.internship_get import InternshipGet
from osis_internship_sdk.model.master_get import MasterGet
from osis_internship_sdk.model.organization_get import OrganizationGet
from osis_internship_sdk.model.paging import Paging
from osis_internship_sdk.model.period_get import PeriodGet
from osis_internship_sdk.model.person import Person
from osis_internship_sdk.model.score_get import ScoreGet
from osis_internship_sdk.model.specialty_get import SpecialtyGet
from osis_internship_sdk.model.student import Student
from osis_internship_sdk.model.student_affectation_get import StudentAffectationGet
from osis_internship_sdk.model.student_get import StudentGet
