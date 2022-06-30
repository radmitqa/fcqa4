import pytest
import allure
from pages.sample_page import SamplePage
import unittest

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SamplePageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    @allure.severity(allure.severity_level.NORMAL)
    def classSetup(self, oneTimeSetUp):
        self.sap = SamplePage(self.driver)

    def test_validateSamplePage(self):
        self.sap.verifyHeaderElements()
        self.sap.verifySamplePageElements()
        self.sap.verifyFooterElements()