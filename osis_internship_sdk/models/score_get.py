# coding: utf-8

"""
    Internship API

    This API delivers data for the Internship project.  # noqa: E501

    OpenAPI spec version: 1
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class ScoreGet(object):
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
        'uuid': 'str',
        'student': 'Student',
        'period': 'PeriodGet',
        'cohort': 'CohortGet',
        'excused': 'bool',
        'reason': 'str',
        'score': 'float',
        'comments': 'object',
        'apd_1': 'str',
        'apd_2': 'str',
        'apd_3': 'str',
        'apd_4': 'str',
        'apd_5': 'str',
        'apd_6': 'str',
        'apd_7': 'str',
        'apd_8': 'str',
        'apd_9': 'str',
        'apd_10': 'str',
        'apd_11': 'str',
        'apd_12': 'str',
        'apd_13': 'str',
        'apd_14': 'str',
        'apd_15': 'str'
    }

    attribute_map = {
        'uuid': 'uuid',
        'student': 'student',
        'period': 'period',
        'cohort': 'cohort',
        'excused': 'excused',
        'reason': 'reason',
        'score': 'score',
        'comments': 'comments',
        'apd_1': 'APD_1',
        'apd_2': 'APD_2',
        'apd_3': 'APD_3',
        'apd_4': 'APD_4',
        'apd_5': 'APD_5',
        'apd_6': 'APD_6',
        'apd_7': 'APD_7',
        'apd_8': 'APD_8',
        'apd_9': 'APD_9',
        'apd_10': 'APD_10',
        'apd_11': 'APD_11',
        'apd_12': 'APD_12',
        'apd_13': 'APD_13',
        'apd_14': 'APD_14',
        'apd_15': 'APD_15'
    }

    def __init__(self, uuid=None, student=None, period=None, cohort=None, excused=None, reason=None, score=None, comments=None, apd_1=None, apd_2=None, apd_3=None, apd_4=None, apd_5=None, apd_6=None, apd_7=None, apd_8=None, apd_9=None, apd_10=None, apd_11=None, apd_12=None, apd_13=None, apd_14=None, apd_15=None):  # noqa: E501
        """ScoreGet - a model defined in OpenAPI"""  # noqa: E501

        self._uuid = None
        self._student = None
        self._period = None
        self._cohort = None
        self._excused = None
        self._reason = None
        self._score = None
        self._comments = None
        self._apd_1 = None
        self._apd_2 = None
        self._apd_3 = None
        self._apd_4 = None
        self._apd_5 = None
        self._apd_6 = None
        self._apd_7 = None
        self._apd_8 = None
        self._apd_9 = None
        self._apd_10 = None
        self._apd_11 = None
        self._apd_12 = None
        self._apd_13 = None
        self._apd_14 = None
        self._apd_15 = None
        self.discriminator = None

        if uuid is not None:
            self.uuid = uuid
        if student is not None:
            self.student = student
        if period is not None:
            self.period = period
        if cohort is not None:
            self.cohort = cohort
        if excused is not None:
            self.excused = excused
        if reason is not None:
            self.reason = reason
        if score is not None:
            self.score = score
        if comments is not None:
            self.comments = comments
        if apd_1 is not None:
            self.apd_1 = apd_1
        if apd_2 is not None:
            self.apd_2 = apd_2
        if apd_3 is not None:
            self.apd_3 = apd_3
        if apd_4 is not None:
            self.apd_4 = apd_4
        if apd_5 is not None:
            self.apd_5 = apd_5
        if apd_6 is not None:
            self.apd_6 = apd_6
        if apd_7 is not None:
            self.apd_7 = apd_7
        if apd_8 is not None:
            self.apd_8 = apd_8
        if apd_9 is not None:
            self.apd_9 = apd_9
        if apd_10 is not None:
            self.apd_10 = apd_10
        if apd_11 is not None:
            self.apd_11 = apd_11
        if apd_12 is not None:
            self.apd_12 = apd_12
        if apd_13 is not None:
            self.apd_13 = apd_13
        if apd_14 is not None:
            self.apd_14 = apd_14
        if apd_15 is not None:
            self.apd_15 = apd_15

    @property
    def uuid(self):
        """Gets the uuid of this ScoreGet.  # noqa: E501


        :return: The uuid of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._uuid

    @uuid.setter
    def uuid(self, uuid):
        """Sets the uuid of this ScoreGet.


        :param uuid: The uuid of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._uuid = uuid

    @property
    def student(self):
        """Gets the student of this ScoreGet.  # noqa: E501


        :return: The student of this ScoreGet.  # noqa: E501
        :rtype: Student
        """
        return self._student

    @student.setter
    def student(self, student):
        """Sets the student of this ScoreGet.


        :param student: The student of this ScoreGet.  # noqa: E501
        :type: Student
        """

        self._student = student

    @property
    def period(self):
        """Gets the period of this ScoreGet.  # noqa: E501


        :return: The period of this ScoreGet.  # noqa: E501
        :rtype: PeriodGet
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ScoreGet.


        :param period: The period of this ScoreGet.  # noqa: E501
        :type: PeriodGet
        """

        self._period = period

    @property
    def cohort(self):
        """Gets the cohort of this ScoreGet.  # noqa: E501


        :return: The cohort of this ScoreGet.  # noqa: E501
        :rtype: CohortGet
        """
        return self._cohort

    @cohort.setter
    def cohort(self, cohort):
        """Sets the cohort of this ScoreGet.


        :param cohort: The cohort of this ScoreGet.  # noqa: E501
        :type: CohortGet
        """

        self._cohort = cohort

    @property
    def excused(self):
        """Gets the excused of this ScoreGet.  # noqa: E501


        :return: The excused of this ScoreGet.  # noqa: E501
        :rtype: bool
        """
        return self._excused

    @excused.setter
    def excused(self, excused):
        """Sets the excused of this ScoreGet.


        :param excused: The excused of this ScoreGet.  # noqa: E501
        :type: bool
        """

        self._excused = excused

    @property
    def reason(self):
        """Gets the reason of this ScoreGet.  # noqa: E501


        :return: The reason of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this ScoreGet.


        :param reason: The reason of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._reason = reason

    @property
    def score(self):
        """Gets the score of this ScoreGet.  # noqa: E501


        :return: The score of this ScoreGet.  # noqa: E501
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this ScoreGet.


        :param score: The score of this ScoreGet.  # noqa: E501
        :type: float
        """

        self._score = score

    @property
    def comments(self):
        """Gets the comments of this ScoreGet.  # noqa: E501


        :return: The comments of this ScoreGet.  # noqa: E501
        :rtype: object
        """
        return self._comments

    @comments.setter
    def comments(self, comments):
        """Sets the comments of this ScoreGet.


        :param comments: The comments of this ScoreGet.  # noqa: E501
        :type: object
        """

        self._comments = comments

    @property
    def apd_1(self):
        """Gets the apd_1 of this ScoreGet.  # noqa: E501


        :return: The apd_1 of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._apd_1

    @apd_1.setter
    def apd_1(self, apd_1):
        """Sets the apd_1 of this ScoreGet.


        :param apd_1: The apd_1 of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._apd_1 = apd_1

    @property
    def apd_2(self):
        """Gets the apd_2 of this ScoreGet.  # noqa: E501


        :return: The apd_2 of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._apd_2

    @apd_2.setter
    def apd_2(self, apd_2):
        """Sets the apd_2 of this ScoreGet.


        :param apd_2: The apd_2 of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._apd_2 = apd_2

    @property
    def apd_3(self):
        """Gets the apd_3 of this ScoreGet.  # noqa: E501


        :return: The apd_3 of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._apd_3

    @apd_3.setter
    def apd_3(self, apd_3):
        """Sets the apd_3 of this ScoreGet.


        :param apd_3: The apd_3 of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._apd_3 = apd_3

    @property
    def apd_4(self):
        """Gets the apd_4 of this ScoreGet.  # noqa: E501


        :return: The apd_4 of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._apd_4

    @apd_4.setter
    def apd_4(self, apd_4):
        """Sets the apd_4 of this ScoreGet.


        :param apd_4: The apd_4 of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._apd_4 = apd_4

    @property
    def apd_5(self):
        """Gets the apd_5 of this ScoreGet.  # noqa: E501


        :return: The apd_5 of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._apd_5

    @apd_5.setter
    def apd_5(self, apd_5):
        """Sets the apd_5 of this ScoreGet.


        :param apd_5: The apd_5 of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._apd_5 = apd_5

    @property
    def apd_6(self):
        """Gets the apd_6 of this ScoreGet.  # noqa: E501


        :return: The apd_6 of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._apd_6

    @apd_6.setter
    def apd_6(self, apd_6):
        """Sets the apd_6 of this ScoreGet.


        :param apd_6: The apd_6 of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._apd_6 = apd_6

    @property
    def apd_7(self):
        """Gets the apd_7 of this ScoreGet.  # noqa: E501


        :return: The apd_7 of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._apd_7

    @apd_7.setter
    def apd_7(self, apd_7):
        """Sets the apd_7 of this ScoreGet.


        :param apd_7: The apd_7 of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._apd_7 = apd_7

    @property
    def apd_8(self):
        """Gets the apd_8 of this ScoreGet.  # noqa: E501


        :return: The apd_8 of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._apd_8

    @apd_8.setter
    def apd_8(self, apd_8):
        """Sets the apd_8 of this ScoreGet.


        :param apd_8: The apd_8 of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._apd_8 = apd_8

    @property
    def apd_9(self):
        """Gets the apd_9 of this ScoreGet.  # noqa: E501


        :return: The apd_9 of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._apd_9

    @apd_9.setter
    def apd_9(self, apd_9):
        """Sets the apd_9 of this ScoreGet.


        :param apd_9: The apd_9 of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._apd_9 = apd_9

    @property
    def apd_10(self):
        """Gets the apd_10 of this ScoreGet.  # noqa: E501


        :return: The apd_10 of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._apd_10

    @apd_10.setter
    def apd_10(self, apd_10):
        """Sets the apd_10 of this ScoreGet.


        :param apd_10: The apd_10 of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._apd_10 = apd_10

    @property
    def apd_11(self):
        """Gets the apd_11 of this ScoreGet.  # noqa: E501


        :return: The apd_11 of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._apd_11

    @apd_11.setter
    def apd_11(self, apd_11):
        """Sets the apd_11 of this ScoreGet.


        :param apd_11: The apd_11 of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._apd_11 = apd_11

    @property
    def apd_12(self):
        """Gets the apd_12 of this ScoreGet.  # noqa: E501


        :return: The apd_12 of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._apd_12

    @apd_12.setter
    def apd_12(self, apd_12):
        """Sets the apd_12 of this ScoreGet.


        :param apd_12: The apd_12 of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._apd_12 = apd_12

    @property
    def apd_13(self):
        """Gets the apd_13 of this ScoreGet.  # noqa: E501


        :return: The apd_13 of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._apd_13

    @apd_13.setter
    def apd_13(self, apd_13):
        """Sets the apd_13 of this ScoreGet.


        :param apd_13: The apd_13 of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._apd_13 = apd_13

    @property
    def apd_14(self):
        """Gets the apd_14 of this ScoreGet.  # noqa: E501


        :return: The apd_14 of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._apd_14

    @apd_14.setter
    def apd_14(self, apd_14):
        """Sets the apd_14 of this ScoreGet.


        :param apd_14: The apd_14 of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._apd_14 = apd_14

    @property
    def apd_15(self):
        """Gets the apd_15 of this ScoreGet.  # noqa: E501


        :return: The apd_15 of this ScoreGet.  # noqa: E501
        :rtype: str
        """
        return self._apd_15

    @apd_15.setter
    def apd_15(self, apd_15):
        """Sets the apd_15 of this ScoreGet.


        :param apd_15: The apd_15 of this ScoreGet.  # noqa: E501
        :type: str
        """

        self._apd_15 = apd_15

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
        if not isinstance(other, ScoreGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
