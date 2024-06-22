"""Module containing the validation tests of the plugin_submission_tests."""
import os

import pytest
import yaml

from workflows import Exceptions
from workflows import constants as wc
from workflows import plugin_submission_tests


def test_correct_file_test():
    """Test the plugin_submission_tests on a correct submission.yml file."""
    with open(os.path.join(wc.SUBMISSION_MOCKS_DIR, "submission.yml")) as file:
        data = yaml.safe_load(file)
    plugin_submission_tests.contains_model_name_test(data)
    plugin_submission_tests.contains_model_type_test(data)
    plugin_submission_tests.contains_output_var_name_test(data)
    plugin_submission_tests.contains_parameter_set_name_test(data)
    plugin_submission_tests.contains_setup_variables_test(data)
    plugin_submission_tests.contains_custom_forcing_name_test(data)
    plugin_submission_tests.contains_custom_forcing_variables_test(data)

def test_empty_submission_test():
    """Test the plugin_submission_tests on an empty submission.yml file."""
    with open(os.path.join(wc.SUBMISSION_MOCKS_DIR, 'emptysubmission.yml')) as file:
        data = yaml.safe_load(file)
    with pytest.raises(Exceptions.NotFoundException):
        plugin_submission_tests.contains_model_name_test(data)
    with pytest.raises(Exceptions.NotFoundException):
        plugin_submission_tests.contains_model_type_test(data)
    with pytest.raises(Exceptions.NotFoundException):
        plugin_submission_tests.contains_output_var_name_test(data)
    with pytest.raises(Exceptions.NotFoundException):
        plugin_submission_tests.contains_parameter_set_name_test(data)
    with pytest.raises(Exceptions.NotFoundException):
        plugin_submission_tests.contains_setup_variables_test(data)
    with pytest.raises(Exceptions.NotFoundException):
        plugin_submission_tests.contains_custom_forcing_name_test(data)
    with pytest.raises(Exceptions.NotFoundException):
        plugin_submission_tests.contains_custom_forcing_variables_test(data)

def test_bad_repo_name_submission_test():
    """Test the plugin_submission_tests on a submission.yml file with bad naming."""
    with open(os.path.join(wc.SUBMISSION_MOCKS_DIR, 'badsubmission.yml')) as file:
        data = yaml.safe_load(file)
    with pytest.raises(Exceptions.WrongFormatException):
        plugin_submission_tests.contains_model_name_test(data)
    with pytest.raises(Exceptions.WrongFormatException):
        plugin_submission_tests.contains_model_type_test(data)
    with pytest.raises(Exceptions.WrongFormatException):
        plugin_submission_tests.contains_output_var_name_test(data)
    plugin_submission_tests.contains_parameter_set_name_test(data)
    plugin_submission_tests.contains_setup_variables_test(data)
    plugin_submission_tests.contains_custom_forcing_name_test(data)
    plugin_submission_tests.contains_custom_forcing_variables_test(data)
