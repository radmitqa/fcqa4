from allure_commons.types import AttachmentType
from selenium import webdriver
import allure
import pytest
from selenium.webdriver.common.by import By


class TestAll:

    @allure.severity(allure.severity_level.NORMAL)
    def test_1(self):
        allure.description("Test 1 Home slogan::: ")
        self.driver = webdriver.Chrome()
        print("Chrome started.")
        self.driver.get("http://www.fatcatqa.com")
        status = self.driver.find_element(By.XPATH, '//*[@id="home_siteSlogan"]')
        if status == True:
            assert True
        self.driver.close()


    def test_2(self):
        pytest.skip("Skipp test 2")

    def test_3(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.fatcatqa.com")
        self.driver.maximize_window()
        print("Chrome started and maximized.")
        act_title = self.driver.title
        if act_title == "1234":
            assert True
            self.driver.close()
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshot img 1: ",
                          attachment_type=AttachmentType.PNG)
            self.driver.close()
            assert False