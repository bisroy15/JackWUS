
from selenium import webdriver
import pytest
from Config.config import configData




####### PyTest HTML Report ########

# Hook to add Environment info to HTML Report

def pytest_configure(config):
    config._metadata['Project Name'] = 'JW NA'
    config._metadata['Module Name'] = 'Login'
    config._metadata['Tester'] = 'Biswadip'


# Hook for delete/modify Environment into HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
