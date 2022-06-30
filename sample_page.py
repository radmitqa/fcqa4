import logging
import time
from selenium.webdriver.common.by import By
import utilities.custom_logger as cl
from base.basepage import BasePage

class SamplePage(BasePage):

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
    _sample_link_top_bar = '//*[@id="top-menu"]/ul[1]/li[5]/a/span' # xpath
    _sample_page_main_header = '//*[@id="section-62b99adb357df-title"]' # xpath
    _sample_page_subheader_1 = '//*[contains(text(), "About the sample project")]'
    _sample_page_subheader_2 = '//*[contains(text(), "Sample solution for the fatcatqa.com website")]'
    _sample_page_text_1 = '//*[contains(text(), "This is the sample of QA automation solution project")]'
    _sample_page_text_2 = '//*[contains(text(), "The architecture and the structure of the project is")]'
    _sample_page_main_pic = '//img[contains(@class, "imageWidth100")]'
    _sample_page_text_3 = '//*[contains(text(), "The Getting Started document in the project will provide")]'
    _sample_page_read_more_link = '//*[contains(text(), "Read More")]'
    _footer_title = '//span[contains(@class, "footer_name")]'
    _footer_subtitle = '//*[contains(text(), "Copyright © 2022 All rights reserved")]'
    _footer_home_btn = '//ul[contains(@class, "hidden-xs")]/li[1]/a/span'
    _footer_services_btn = '//ul[contains(@class, "hidden-xs")]/li[2]/a/span'
    _footer_about_btn = '//ul[contains(@class, "hidden-xs")]/li[3]/a/span'
    _footer_contact_btn = '//ul[contains(@class, "hidden-xs")]/li[4]/a/span'
    _footer_up_btn = '//*[@id="gotoTop"]/i'

    """ Page Actions """

    def getTopBarHomeLink(self):
        return self.driver.find_element(By.CSS_SELECTOR, "ul[class='navPages nav navbar-nav'] li[class='moduleMenu active'] span[class='txt-container']")

    def getTopBarServicesLink(self):
        return self.driver.find_element(By.XPATH, "//ul[@class='navPages nav navbar-nav']//span[@class='txt-container'][normalize-space()='Services']")

    def getTopBarAboutLink(self):
        return self.driver.find_element(By.XPATH, '//*[@id="top-menu"]/ul[1]/li[3]/a/span')

    def getTopBarContactLink(self):
        return self.driver.find_element(By.CSS_SELECTOR, "div[id='websiteHeader'] li:nth-child(4) a:nth-child(1) span:nth-child(1)")

    def getTopBarSampleLink(self):
        return self.driver.find_element(By.XPATH, '//*[@id="top-menu"]/ul[1]/li[5]/a/span')

    def verifySampleLinkTopBarIsDisplayed(self):
        self.isElementPresent(self._sample_link_top_bar, locatorType='xpath')
        print("Top Bar - Sample Button is displayed with text: ." + self.getTopBarSampleLink().text)

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

    def getPageTitle(self):
        print("Title of Page is: " + self.driver.title)

    def clickSampleTopBarLink(self):
        self.elementClick(self._sample_link_top_bar, locatorType="xpath")
        print("Clicked on Button: " + self.getTopBarSampleLink().text)

    def getSamplePageMainHeader(self):
        return self.driver.find_element(By.XPATH, '//*[@id="section-62b99adb357df-title"]')

    def assertSamplePageHeaderTitle(self):
        act_title = self.getSamplePageMainHeader().text
        exp_title = "SAMPLE"
        if act_title == exp_title:
            print(
                "Sample Page - Actual Main Title: " + act_title + " and Expected Main Title: " + exp_title + " are matching.")

    def getSamplePageSubheader1(self):
        return self.driver.find_element(By.XPATH, '//*[contains(text(), "About the sample project")]')

    def getSamplePageSubheader2(self):
        return self.driver.find_element(By.XPATH, '//*[contains(text(), "Sample solution for the fatcatqa.com website")]')

    def verifySamplePageSubheader1IsDisplayed(self):
        self.isElementPresent(self._sample_page_subheader_1, locatorType="xpath")
        print("Sample Page - Subheader 1 text is: " + self.getSamplePageSubheader1().text)

    def verifySamplePageSubheader2IsDisplayed(self):
        self.isElementPresent(self._sample_page_subheader_2, locatorType="xpath")
        print("Sample Page - Subheader 2 text is: " + self.getSamplePageSubheader2().text)

    def getSamplePageText1(self):
        return self.driver.find_element(By.XPATH,'//*[contains(text(), "This is the sample of QA automation solution project")]')

    def verifySamplePageText1IsDisplayed(self):
        self.isElementPresent(self._sample_page_text_1, locatorType="xpath")
        print("Sample Page Text 1 is: " + self.getSamplePageText1().text)

    def getSamplePageMainPic(self):
        return self.driver.find_element(By.XPATH,'//img[contains(@class, "imageWidth100")]')

    def verifySamplePageMainPicIsDisplayed(self):
        self.isElementPresent(self._sample_page_main_pic, locatorType="xpath")
        print("Sample Page Main Picture is displayed.")

    def getSamplePageText2(self):
        return self.driver.find_element(By.XPATH,'//*[contains(text(), "The architecture and the structure of the project is")]')

    def verifySamplePageText2IsDisplayed(self):
        self.isElementPresent(self._sample_page_text_2, locatorType="xpath")
        print("Sample Page Text 2 is: " + self.getSamplePageText2().text)

    def scrollDown(self):
        self.driver.execute_script("window.scrollBy(100, 800);")
        time.sleep(2)

    def getSamplePageText3(self):
        return self.driver.find_element(By.XPATH,'//*[contains(text(), "The Getting Started document in the project will provide")]')

    def verifySamplePageText3IsDisplayed(self):
        self.isElementPresent(self._sample_page_text_3, locatorType="xpath")
        print("Sample Page Text 2 is: " + self.getSamplePageText3().text)

    def getSamplePageReadMoreLink(self):
        return self.driver.find_element(By.XPATH,'//*[contains(text(), "Read More")]')

    def verifySamplePageReadMoreLinkIsDisplayed(self):
        self.isElementPresent(self._sample_page_read_more_link, locatorType="xpath")
        print("Sample Page - Read More Link is: " + self.getSamplePageReadMoreLink().text)

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

    """ Tests """

    def verifyHeaderElements(self):
        self.verifyLogoIsDisplayed()
        self.verifyHomeLinkTopBarIsDisplayed()
        self.verifyServicesLinkTopBarIsDisplayed()
        self.verifyAboutLinkTopBarIsDisplayed()
        self.verifyContactLinkTopBarIsDisplayed()
        self.verifySampleLinkTopBarIsDisplayed()

    def verifySamplePageElements(self):
        self.clickSampleTopBarLink()
        time.sleep(3)
        self.getPageTitle()
        self.assertSamplePageHeaderTitle()
        self.verifySamplePageSubheader1IsDisplayed()
        self.verifySamplePageSubheader2IsDisplayed()
        self.verifySamplePageText1IsDisplayed()
        self.verifySamplePageMainPicIsDisplayed()
        self.scrollDown()
        self.verifySamplePageText2IsDisplayed()
        self.verifySamplePageText3IsDisplayed()
        self.verifySamplePageReadMoreLinkIsDisplayed()

    def verifyFooterElements(self):
        self.verifyFooterTitleText()
        self.verifyFooterSubtitleText()
        self.verifyFooterHomeLink()
        self.verifyFooterServicesLink()
        self.verifyFooterAboutLink()
        self.verifyFooterContactLink()
        self.verifyFooterUpButton()
