from pages.home_page import HomePage
import unittest
import pytest
import allure

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class HomePageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    @allure.severity(allure.severity_level.NORMAL)
    def classSetup(self, oneTimeSetUp):
        self.hp = HomePage(self.driver)

    @allure.severity(allure.severity_level.NORMAL)
    def test_validateHomePage(self):
        self.hp.verifyHPElements()
        self.hp.verifyHeaderElements()
        self.hp.goToServicesPage()
