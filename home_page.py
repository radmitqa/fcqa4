import logging
from selenium.webdriver.common.by import By
import utilities.custom_logger as cl
from base.basepage import BasePage
import allure

@allure.severity(allure.severity_level.NORMAL)
class HomePage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """ Page Elements """

    _logo_img = "div[class='site_container'] img[alt='Fat Cat QA - Automation by the standard.']" # css selector
    _home_link_top_bar = "ul[class='navPages nav navbar-nav'] li[class='moduleMenu active'] span[class='txt-container']"  # css selector
    _services_link_top_bar = "//ul[@class='navPages nav navbar-nav']//span[@class='txt-container'][normalize-space()='Services']"  # xpath
    _about_link_top_bar = "div[id='websiteHeader'] li:nth-child(3) a:nth-child(1) span:nth-child(1)" # css selector
    _contact_link_top_bar = "div[id='websiteHeader'] li:nth-child(4) a:nth-child(1) span:nth-child(1)" # css selector
    _sample_link_top_bar = '//*[@id="top-menu"]/ul[1]/li[5]/a/span' # xpath
    _page_main_title = "//h1[@id='home_siteSlogan']"  # xpath
    _page_main_subtitle = "//p[@id='home_SecondSiteSlogan']"  # xpath

    """ Page Actions """

    def getMainPageHeaderTitle(self):
        return self.driver.find_element(By.XPATH, "//h1[@id='home_siteSlogan']")

    def getMainPageHeaderSubtitle(self):
        return self.driver.find_element(By.XPATH, "//p[@id='home_SecondSiteSlogan']")

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
        return self.driver.find_element(By.CSS_SELECTOR, "div[id='websiteHeader'] li:nth-child(3) a:nth-child(1) span:nth-child(1)")

    def verifyAboutLinkTopBarIsDisplayed(self):
        self.isElementPresent(self._about_link_top_bar, locatorType="css")
        print("Top Bar - About Button is displayed with text: ." + self.getTopBarAboutLink().text)

    def getTopBarContactLink(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[id='websiteHeader'] li:nth-child(4) a:nth-child(1) span:nth-child(1)")

    def verifyContactLinkTopBarIsDisplayed(self):
        self.isElementPresent(self._contact_link_top_bar, locatorType="css")
        print("Top Bar - Contact Button is displayed with text: ." + self.getTopBarContactLink().text)

    def getTopBarSampleLink(self):
        return self.driver.find_element(By.XPATH, '//*[@id="top-menu"]/ul[1]/li[5]/a/span')

    def verifySampleLinkTopBarIsDisplayed(self):
        self.isElementPresent(self._sample_link_top_bar, locatorType='xpath')
        print("Top Bar - Sample Button is displayed with text: ." + self.getTopBarSampleLink().text)

    def assertMainPageHeaderTitle(self):
        act_title = self.getMainPageHeaderTitle().text
        exp_title = "Fat Cat QA"
        if act_title == exp_title:
            print("Home Page - Actual Main Title: " + act_title + ", Expected Main Title: " + exp_title + " are matching.")

    def assertMainPageHeaderSubtitle(self):
        act_subtitle = self.getMainPageHeaderSubtitle().text
        exp_subtitle = "Automate your business applications - by the standard."
        if act_subtitle == exp_subtitle:
            print("Home Page - Actual Main Subtitle: " + act_subtitle + " and Expected Main Subtitle: " + exp_subtitle + " are matching.")

    def clickServicesTopBarLink(self):
        self.elementClick(self._services_link_top_bar, locatorType="xpath")
        print("Clicked on button: " + self.getTopBarServicesLink().text)

    def getPageTitle(self):
        print("Title of Page is: " + self.driver.title)

    """ Tests """

    @allure.severity(allure.severity_level.NORMAL)
    def verifyHeaderElements(self):
        self.verifyLogoIsDisplayed()
        self.verifyHomeLinkTopBarIsDisplayed()
        self.verifyServicesLinkTopBarIsDisplayed()
        self.verifyAboutLinkTopBarIsDisplayed()
        self.verifyContactLinkTopBarIsDisplayed()
        self.verifySampleLinkTopBarIsDisplayed()

    @allure.severity(allure.severity_level.MINOR)
    def verifyHPElements(self):
        self.getPageTitle()
        self.assertMainPageHeaderTitle()
        self.assertMainPageHeaderSubtitle()

    def goToServicesPage(self):
        self.clickServicesTopBarLink()

