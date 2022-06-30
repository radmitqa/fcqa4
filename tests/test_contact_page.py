from pages.contact_page import ContactPage
import unittest
import pytest
import allure

@allure.severity(allure.severity_level.NORMAL)
@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class ContactPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    @allure.severity(allure.severity_level.NORMAL)
    def classSetup(self, oneTimeSetUp):
        self.cp = ContactPage(self.driver)

    def test_validateContactsPage(self):
        self.cp.verifyHeaderElements()
        self.cp.goToContactPage()
        self.cp.verifyContactPageElements()
        self.cp.enterDataToForm()
        self.cp.closeConfirmationPopUp()
