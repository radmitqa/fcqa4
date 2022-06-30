import logging
import time
from selenium.webdriver.common.by import By
import utilities.custom_logger as cl
from base.basepage import BasePage

class AboutPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """ Page Elements """

    _logo_img = "div[class='site_container'] img[alt='Fat Cat QA - Automation by the standard.']" # css selector
    _home_link_top_bar = "ul[class='navPages nav navbar-nav'] li[class='moduleMenu active'] span[class='txt-container']"  # css selector
    _services_link_top_bar = "//ul[@class='navPages nav navbar-nav']//span[@class='txt-container'][normalize-space()='Services']"  # xpath
    _about_link_top_bar = '//*[@id="top-menu"]/ul[1]/li[3]/a/span' # xpath
    _contact_link_top_bar = "div[id='websiteHeader'] li:nth-child(4) a:nth-child(1) span:nth-child(1)" # css selector
    _sample_link_top_bar = '//*[@id="top-menu"]/ul[1]/li[5]/a/span'  # xpath
    _about_page_main_header = '//*[@id="section-5b0a4ba50e4e8-title"]' # xpath
    _about_text_1 = '//*[@id="section-5b0a4ba50e4e8"]/div[2]/div/div/div' # xpath
    _about_section_img = '//img[contains(@class, "img-rounded")]' # xpath

    """ Page Actions """

    def getTopBarHomeLink(self):
        return self.driver.find_element(By.CSS_SELECTOR, "ul[class='navPages nav navbar-nav'] li[class='moduleMenu active'] span[class='txt-container']")

    def getTopBarServicesLink(self):
        return self.driver.find_element(By.XPATH, "//ul[@class='navPages nav navbar-nav']//span[@class='txt-container'][normalize-space()='Services']")

    def getTopBarAboutLink(self):
        return self.driver.find_element(By.XPATH, '//*[@id="top-menu"]/ul[1]/li[3]/a/span')

    def getTopBarContactLink(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[id='websiteHeader'] li:nth-child(4) a:nth-child(1) span:nth-child(1)")

    def getAboutText1(self):
        return self.driver.find_element(By.XPATH, '//*[@id="section-5b0a4ba50e4e8"]/div[2]/div/div/div')

    def getAboutText2(self):
        return self.driver.find_element(By.XPATH, '//*[contains(text(), "You can trust us with your QA automation tasks via")]')

    def getAboutText3(self):
        return self.driver.find_element(By.XPATH, '//*[contains(text(), "Welcome to the Fat Cat QA.")]')

    def getAboutSectionImage(self):
        return self.driver.find_element(By.XPATH, '//img[contains(@class, "img-rounded")]')

    def getTopBarSampleLink(self):
        return self.driver.find_element(By.XPATH, '//*[@id="top-menu"]/ul[1]/li[5]/a/span')

    def verifyLogoIsDisplayed(self):
        self.isElementPresent(self._logo_img, locatorType="css")
        print("Logo is displayed.")

    def verifyHomeLinkTopBarIsDisplayed(self):
        self.isElementPresent(self._home_link_top_bar, locatorType="css")
        print("Top Bar - Home Button is displayed with text: " + self.getTopBarHomeLink().text)

    def verifyServicesLinkTopBarIsDisplayed(self):
        self.isElementPresent(self._services_link_top_bar, locatorType="xpath")
        print("Top Bar - Services Button is displayed with text: " + self.getTopBarServicesLink().text)

    def verifyAboutLinkTopBarIsDisplayed(self):
        self.isElementPresent(self._about_link_top_bar, locatorType="xpath")
        print("Top Bar - About Button is displayed with text: ." + self.getTopBarAboutLink().text)

    def verifyContactLinkTopBarIsDisplayed(self):
        self.isElementPresent(self._contact_link_top_bar, locatorType="css")
        print("Top Bar - Contact Button is displayed with text: ." + self.getTopBarContactLink().text)

    def verifySampleLinkTopBarIsDisplayed(self):
        self.isElementPresent(self._sample_link_top_bar, locatorType='xpath')
        print("Top Bar - Sample Button is displayed with text: ." + self.getTopBarSampleLink().text)

    def clickAboutTopBarLink(self):
        self.elementClick(self._about_link_top_bar, locatorType="xpath")
        print("Clicked on Button: " + self.getTopBarAboutLink().text)

    def getPageTitle(self):
        print("Title of Page is: " + self.driver.title)

    def getAboutPageMainHeader(self):
        return self.driver.find_element(By.XPATH, '//*[@id="section-5b0a4ba50e4e8-title"]')

    def assertAboutPageHeaderTitle(self):
        act_title = self.getAboutPageMainHeader().text
        exp_title = "ABOUT"
        if act_title == exp_title:
            print("Services Page - Actual Main Title: " + act_title + " and Expected Main Title: " + exp_title + " are matching.")

    def verifyAboutText1IsDisplayed(self):
        self.isElementPresent(self._about_text_1, locatorType="xpath")
        print("About Section Text 1 is: " + self.getAboutText1().text)

    def verifyAboutSectionImageIsDisplayed(self):
        self.isElementPresent(self._about_section_img, locatorType="xpath")
        print("About section Image is displayed.")

    def clickContactTopBarLink(self):
        self.elementClick(self._contact_link_top_bar, locatorType="xpath")
        print("Clicked on Button: " + self.getTopBarContactLink().text)

    """ Tests """

    def verifyHeaderElements(self):
        self.verifyLogoIsDisplayed()
        self.verifyHomeLinkTopBarIsDisplayed()
        self.verifyServicesLinkTopBarIsDisplayed()
        self.verifyAboutLinkTopBarIsDisplayed()
        self.verifyContactLinkTopBarIsDisplayed()
        self.verifySampleLinkTopBarIsDisplayed()

    def verifyAboutPageElements(self):
        self.clickAboutTopBarLink()
        time.sleep(3)
        self.getPageTitle()
        self.assertAboutPageHeaderTitle()
        self.verifyAboutText1IsDisplayed()
        self.verifyAboutSectionImageIsDisplayed()

    def goToContactPage(self):
        self.clickContactTopBarLink()
        time.sleep(3)
