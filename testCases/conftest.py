import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

@pytest.fixture()
def setup():
    mobile_emulation = {
        "deviceName": "Pixel 2"
    }
    chrome_options = Options()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    return driver

@pytest.hookimpl(optionalhook=True)
def pytest_configure(config):
    if not hasattr(config, 'worker input'):  # To ensure it's not running in a worker process
        config._metadata = {}  # Initialize the metadata dictionary

@pytest.hookimpl(optionalhook=True)

## Pytest HTML report
def pytest_metadata(config):
    config.metadata['Project Name'] = 'borrowApp'
    config.metadata['Module Name'] = 'LoginPage'
    config.metadata['Tester'] = 'Shivakumar'


@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)
