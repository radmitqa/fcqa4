import pytest
import allure
from pages.about_page import AboutPage
import unittest

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class AboutPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    @allure.severity(allure.severity_level.NORMAL)
    def classSetup(self, oneTimeSetUp):
        self.ap = AboutPage(self.driver)

    def test_validateAboutPage(self):
        self.ap.verifyHeaderElements()
        self.ap.verifyAboutPageElements()