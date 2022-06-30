import logging
import time
from selenium.webdriver.common.by import By
import utilities.custom_logger as cl
from base.basepage import BasePage

class ContactPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """ Page Elements """

    _logo_img = "div[class='site_container'] img[alt='Fat Cat QA - Automation by the standard.']" # css selector
    _home_link_top_bar = "ul[class='navPages nav navbar-nav'] li[class='moduleMenu active'] span[class='txt-container']"  # css selector
    _services_link_top_bar = "//ul[@class='navPages nav navbar-nav']//span[@class='txt-container'][normalize-space()='Services']"  # xpath
    _about_link_top_bar = '//*[@id="top-menu"]/ul[1]/li[3]/a/span' # xpath
    _contact_link_top_bar = '//*[@id="top-menu"]/ul[1]/li[4]/a/span' # xpath
    _contact_page_main_header = '//*[@id="section-5b0a4ba521825-title"]' # xpath
    _sample_link_top_bar = '//*[@id="top-menu"]/ul[1]/li[5]/a/span'  # xpath
    _location_info = '//*[contains(text(), "Belgrade, Serbia")]'
    _phone_info = '//div[contains(@class, "col-md-5")]/ul[2]/li[1]' # xpath
    _email_info = '//*[contains(text(), "radovanmitrovic.qa@gmail.com")]' # xpath
    _contact_info_text = '//*[contains(text(), "https://www.linkedin.com/in/radovan-mitrovic-a84a6096/")]' # xpath
    _name_control = '//input[@name="contact_name"]'
    _phone_control = '//input[@name="contact_phone"]'
    _email_address_control = '//input[@name="contact_email"]'
    _message_control = '//textarea[@name="contact_message"]'
    _contact_us_button = '//button[contains(@class, "btn-primary")]'
    _footer_title = '//span[contains(@class, "footer_name")]'
    _footer_subtitle = '//*[contains(text(), "Copyright © 2022 All rights reserved")]'
    _footer_home_btn = '//ul[contains(@class, "hidden-xs")]/li[1]/a/span'
    _footer_services_btn = '//ul[contains(@class, "hidden-xs")]/li[2]/a/span'
    _footer_about_btn = '//ul[contains(@class, "hidden-xs")]/li[3]/a/span'
    _footer_contact_btn = '//ul[contains(@class, "hidden-xs")]/li[4]/a/span'
    _footer_up_btn = '//*[@id="gotoTop"]/i'
    _confirmation_header = '//h4[contains(@class, "modal-title")]'
    _confirmation_body = '//div[contains(@class, "bootbox-body")]'
    _confirmation_ok_btn = '//div[contains(@class, "modal-footer")]/button'

    """ Page Actions """

    def verifyLogoIsDisplayed(self):
        self.isElementPresent(self._logo_img, locatorType="css")
        print("Logo is displayed.")

    def getTopBarHomeLink(self):
        return self.driver.find_element(By.CSS_SELECTOR, "ul[class='navPages nav navbar-nav'] li[class='moduleMenu active'] span[class='txt-container']")

    def getTopBarServicesLink(self):
        return self.driver.find_element(By.XPATH, "//ul[@class='navPages nav navbar-nav']//span[@class='txt-container'][normalize-space()='Services']")

    def verifyHomeLinkTopBarIsDisplayed(self):
        self.isElementPresent(self._home_link_top_bar, locatorType="css")
        print("Top Bar - Home Button is displayed with text: " + self.getTopBarHomeLink().text)

    def verifyServicesLinkTopBarIsDisplayed(self):
        self.isElementPresent(self._services_link_top_bar, locatorType="xpath")
        print("Top Bar - Services Button is displayed with text: " + self.getTopBarServicesLink().text)

    def getTopBarAboutLink(self):
        return self.driver.find_element(By.XPATH, '//*[@id="top-menu"]/ul[1]/li[3]/a/span')

    def verifyAboutLinkTopBarIsDisplayed(self):
        self.isElementPresent(self._about_link_top_bar, locatorType="xpath")
        print("Top Bar - About Button is displayed with text: ." + self.getTopBarAboutLink().text)

    def getTopBarContactLink(self):
        return self.driver.find_element(By.XPATH,'//*[@id="top-menu"]/ul[1]/li[4]/a/span')

    def verifyContactLinkTopBarIsDisplayed(self):
        self.isElementPresent(self._contact_link_top_bar, locatorType="xpath")
        print("Top Bar - Contact Button is displayed with text: ." + self.getTopBarContactLink().text)

    def getTopBarSampleLink(self):
        return self.driver.find_element(By.XPATH, '//*[@id="top-menu"]/ul[1]/li[5]/a/span')

    def verifySampleLinkTopBarIsDisplayed(self):
        self.isElementPresent(self._sample_link_top_bar, locatorType='xpath')
        print("Top Bar - Contact Button is displayed with text: ." + self.getTopBarSampleLink().text)

    def clickContactTopBarLink(self):
        self.elementClick(self._contact_link_top_bar, locatorType="xpath")
        print("Clicked on Button: " + self.getTopBarContactLink().text)

    def getPageTitle(self):
        print("Title of Page is: " + self.driver.title)

    def getContactPageMainHeader(self):
        return self.driver.find_element(By.XPATH, '//*[@id="section-5b0a4ba521825-title"]')

    def assertContactPageHeaderTitle(self):
        act_title = self.getContactPageMainHeader().text
        exp_title = "CONTACT"
        if act_title == exp_title:
            print("Contact Page - Actual Main Title: " + act_title + " and Expected Main Title: " + exp_title + " are matching.")

    def getLocationInfo(self):
        return self.driver.find_element(By.XPATH, '//*[contains(text(), "Belgrade, Serbia")]')

    def verifyLocationInfoIsDisplayed(self):
        self.isElementPresent(self._location_info, locatorType="xpath")
        print("Location Info is displayed containing text: " + self.getLocationInfo().text)

    def getPhoneInfo(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "col-md-5")]/ul[2]/li[1]')

    def verifyPhoneInfoIsDisplayed(self):
        self.isElementPresent(self._phone_info, locatorType="xpath")
        print("Phone Info is displayed containing text: " + self.getPhoneInfo().text)

    def getEmailInfo(self):
        return self.driver.find_element(By.XPATH, '//*[contains(text(), "radovanmitrovic.qa@gmail.com")]')

    def verifyEmailInfoIsDisplayed(self):
        self.isElementPresent(self._email_info, locatorType="xpath")
        print("Email Info is displayed containing text: " + self.getEmailInfo().text)

    def getContactText(self):
        return self.driver.find_element(By.XPATH, '//*[contains(text(), "https://www.linkedin.com/in/radovan-mitrovic-a84a6096/")]')

    def verifyContactTextIsDisplayed(self):
        self.isElementPresent(self._contact_info_text, locatorType="xpath")
        print("Contact Text is displayed containing text: " + self.getContactText().text)

    def enterNameControl(self):
        self.sendKeys("TestName", '//input[@name="contact_name"]', locatorType="xpath")
        print("Data Input 'TestName' to Name Control.")

    def enterPhoneControl(self):
        self.sendKeys("01234567890", '//input[@name="contact_phone"]', locatorType="xpath")
        print("Data Input '01234567890' to Phone Control.")

    def enterEmailControl(self):
        self.sendKeys("test@emailtest.com", '//input[@name="contact_email"]', locatorType="xpath")
        print("Data Input 'test@emailtest.com' to Email Control.")

    def enterMessageControl(self):
        self.sendKeys("Test Message No 1.", '//textarea[@name="contact_message"]', locatorType="xpath")
        print("Data Input 'Test Message No 1.' to Message Control.")

    def clickContactUsButton(self):
        self.elementClick('//button[contains(@class, "btn-primary")]', locatorType="xpath")
        print("Clicked ContactUs Button.")

    def getFooterTitle(self):
        return self.driver.find_element(By.XPATH, '//span[contains(@class, "footer_name")]')

    def verifyFooterTitleText(self):
        self.isElementPresent(self._footer_title, locatorType="xpath")
        print("Footer Title Text is: " + self.getFooterTitle().text)

    def getFooterSubtitle(self):
        return self.driver.find_element(By.XPATH, '//*[contains(text(), "Copyright © 2022 All rights reserved")]')

    def verifyFooterSubtitleText(self):
        self.isElementPresent(self._footer_subtitle, locatorType="xpath")
        print("Footer Subtitle Text is: " + self.getFooterSubtitle().text)

    def getFooterHomeBtn(self):
        return self.driver.find_element(By.XPATH, '//ul[contains(@class, "hidden-xs")]/li[1]/a/span')

    def verifyFooterHomeLink(self):
        self.isElementPresent(self._footer_home_btn, locatorType="xpath")
        print("Footer Home Button is displayed with text: " + self.getFooterHomeBtn().text)

    def getFooterServicesBtn(self):
        return self.driver.find_element(By.XPATH, '//ul[contains(@class, "hidden-xs")]/li[2]/a/span')

    def verifyFooterServicesLink(self):
        self.isElementPresent(self._footer_services_btn, locatorType="xpath")
        print("Footer Services Button is displayed with text: " + self.getFooterServicesBtn().text)

    def getFooterAboutBtn(self):
        return self.driver.find_element(By.XPATH, '//ul[contains(@class, "hidden-xs")]/li[3]/a/span')

    def verifyFooterAboutLink(self):
        self.isElementPresent(self._footer_about_btn, locatorType="xpath")
        print("Footer About Button is displayed with text: " + self.getFooterAboutBtn().text)

    def getFooterContactBtn(self):
        return self.driver.find_element(By.XPATH, '//ul[contains(@class, "hidden-xs")]/li[4]/a/span')

    def verifyFooterContactLink(self):
        self.isElementPresent(self._footer_contact_btn, locatorType="xpath")
        print("Footer Contact Button is displayed with text: " + self.getFooterContactBtn().text)

    def verifyFooterUpButton(self):
        self.isElementPresent(self._footer_up_btn, locatorType="xpath")
        print("Footer Up Button is displayed.")

    def getConfirmationHeader(self):
        return self.driver.find_element(By.XPATH, '//h4[contains(@class, "modal-title")]')

    def getConfirmationBody(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "bootbox-body")]')

    def getConfirmationOkBtn(self):
        return self.driver.find_element(By.XPATH, '//div[contains(@class, "modal-footer")]/button')

    def verifyConfirmationHeaderText(self):
        self.isElementPresent(self._confirmation_header, locatorType="xpath")
        print("Confirmation Header displayed containing text: " + self.getConfirmationHeader().text)

    def verifyConfirmationBodyText(self):
        self.isElementPresent(self._confirmation_body, locatorType="xpath")
        print("Confirmation Body displayed containing text: " + self.getConfirmationBody().text)

    def verifyConfirmationOkButton(self):
        self.isElementPresent(self._confirmation_ok_btn, locatorType="xpath")
        print("Confirmation Form - OK button displayed containing text: " + self.getConfirmationOkBtn().text)

    def clickConfirmationOKButton(self):
        self.elementClick(self._confirmation_ok_btn, locatorType="xpath")
        print("Click Confirmation OK button.")

    """ Tests """

    def verifyHeaderElements(self):
        self.verifyLogoIsDisplayed()
        self.verifyHomeLinkTopBarIsDisplayed()
        self.verifyServicesLinkTopBarIsDisplayed()
        self.verifyAboutLinkTopBarIsDisplayed()
        self.verifyContactLinkTopBarIsDisplayed()
        self.verifySampleLinkTopBarIsDisplayed()

    def goToContactPage(self):
        self.clickContactTopBarLink()
        time.sleep(3)

    def verifyContactPageElements(self):
        self.getPageTitle()
        self.assertContactPageHeaderTitle()
        self.verifyLocationInfoIsDisplayed()
        self.verifyPhoneInfoIsDisplayed()
        self.verifyEmailInfoIsDisplayed()
        self.verifyContactTextIsDisplayed()

    def enterDataToForm(self):
        self.enterNameControl()
        self.enterPhoneControl()
        self.enterEmailControl()
        self.enterMessageControl()
        self.clickContactUsButton()
        time.sleep(2)

    def closeConfirmationPopUp(self):
        self.verifyConfirmationHeaderText()
        self.verifyConfirmationBodyText()
        self.verifyConfirmationOkButton()
        self.clickConfirmationOKButton()
        time.sleep(2)
