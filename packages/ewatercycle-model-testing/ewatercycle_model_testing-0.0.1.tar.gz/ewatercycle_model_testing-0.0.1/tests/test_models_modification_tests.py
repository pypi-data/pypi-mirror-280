"""Module containing the validation tests of the models_modification_tests."""
import os

import pytest

from workflows import Exceptions
from workflows import constants as wc
from workflows import models_modification_tests


def test_correct_models_txt_test():
    """Test the models_modification_tests on a correct models.txt file."""
    with open(os.path.join(wc.SUBMISSION_MOCKS_DIR, 'models.txt'), "r", encoding="utf8") as file:
        file = file.readlines()
    models_modification_tests.contains_name_test(file)
    models_modification_tests.includes_repository_link_test(file)

def test_no_data_test():
    """Test the models_modification_tests on a models.txt file with no data."""
    with open(os.path.join(wc.SUBMISSION_MOCKS_DIR, "nodatamodels.txt"), "r", encoding="utf8") as file:
        file = file.readlines()
    with pytest.raises(Exceptions.NotFoundException):
        models_modification_tests.contains_name_test(file)
    with pytest.raises(Exceptions.NotFoundException):
        models_modification_tests.includes_repository_link_test(file)

def test_bad_naming_test():
    """Test the models_modification_tests on a models.txt file with incorrect naming."""
    with open(os.path.join(wc.SUBMISSION_MOCKS_DIR, "badreponamemodels.txt"), "r", encoding="utf8") as file:
        file = file.readlines()
    with pytest.raises(Exceptions.NotFoundException):
        models_modification_tests.contains_name_test(file)
    with pytest.raises(Exceptions.WrongFormatException):
        models_modification_tests.includes_repository_link_test(file)
