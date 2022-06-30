from pages.services_page import ServicesPage
import unittest
import pytest
import allure

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ServicesPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    @allure.severity(allure.severity_level.NORMAL)
    def classSetup(self, oneTimeSetUp):
        self.sp = ServicesPage(self.driver)

    def test_validateServicesPage(self):
        self.sp.verifyHeaderElements()
        self.sp.verifyServicesPageElements()

