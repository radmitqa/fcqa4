import logging
import time
from selenium.webdriver.common.by import By
import utilities.custom_logger as cl
from base.basepage import BasePage

class ServicesPage(BasePage):

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
    _page_main_title = "//h1[@id='home_siteSlogan']"  # xpath
    _page_main_subtitle = "//p[@id='home_SecondSiteSlogan']"  # xpath
    _services_main_title = "//h2[@id='section-5d0a0f53588b1-title']" # xpath
    _consultingHeader = "body > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h4:nth-child(2) > strong:nth-child(1)" #css
    _consultingText = "/body > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > p:nth-child(3)" #css
    _consultingImg = "(//SPAN[@class='fa-stack fa-4x img-circle bgLazyload entered loaded'])[1]" #xpath
    _timeframeHeader = "body > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > h4:nth-child(2) > strong:nth-child(1)"
    _timeframeText = "/html/body/div[2]/div[3]/div/section[1]/div[2]/div/div[2]/div[2]/div/p" # xpath
    _timeframeImg = "/html/body/div[2]/div[3]/div/section[1]/div[2]/div/div[2]/div[2]/div/span" # xpath
    _deploymentHeader = "//strong[normalize-space()='DEPLOYMENT']" # xpath
    _deploymentText = "(//P)[3]" # xpath
    _deploymentImg = "//div[@id='s123PjaxMainContainer']//div[3]//div[1]//span[1]" # xpath

    """ Page Actions """

    def getServicesPageMainHeader(self):
        return self.driver.find_element(By.XPATH,"//h2[@id='section-5d0a0f53588b1-title']")

    def getConsultingImg(self):
        return self.driver.find_element(By.XPATH, "(//SPAN[@class='fa-stack fa-4x img-circle bgLazyload entered loaded'])[1]")

    def getConsultingHeader(self):
        return self.driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > h4:nth-child(2) > strong:nth-child(1)")

    def getConsultingSubheaderText(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/section[1]/div[2]/div/div[2]/div[1]/div/p") #xpath

    def getTimeFrameImg(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/section[1]/div[2]/div/div[2]/div[2]/div/span")

    def getTimeFrameHeader(self):
        return self.driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > section:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > h4:nth-child(2) > strong:nth-child(1)")

    def getTimeFrameText(self):
        return self.driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/section[1]/div[2]/div/div[2]/div[2]/div/p")

    def getDeploymentImg(self):
        return self.driver.find_element(By.XPATH, "//div[@id='s123PjaxMainContainer']//div[3]//div[1]//span[1]")

    def getDeploymentHeader(self):
        return self.driver.find_element(By.XPATH, "//strong[normalize-space()='DEPLOYMENT']") #xpath

    def getDeploymentText(self):
        return self.driver.find_element(By.XPATH, "(//P)[4]") # xpath

    def getTopBarHomeLink(self):
        return self.driver.find_element(By.CSS_SELECTOR, "ul[class='navPages nav navbar-nav'] li[class='moduleMenu active'] span[class='txt-container']")

    def getTopBarServicesLink(self):
        return self.driver.find_element(By.XPATH, "//ul[@class='navPages nav navbar-nav']//span[@class='txt-container'][normalize-space()='Services']")

    def verifyLogoIsDisplayed(self):
        self.isElementPresent(self._logo_img, locatorType="css")
        print("Logo is displayed.")

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
        return self.driver.find_element(By.CSS_SELECTOR, "div[id='websiteHeader'] li:nth-child(4) a:nth-child(1) span:nth-child(1)")

    def verifyContactLinkTopBarIsDisplayed(self):
        self.isElementPresent(self._contact_link_top_bar, locatorType="css")
        print("Top Bar - Contact Button is displayed with text: ." + self.getTopBarContactLink().text)

    def getTopBarSampleLink(self):
        return self.driver.find_element(By.XPATH, '//*[@id="top-menu"]/ul[1]/li[5]/a/span')

    def verifySampleLinkTopBarIsDisplayed(self):
        self.isElementPresent(self._sample_link_top_bar, locatorType='xpath')
        print("Top Bar - Sample Button is displayed with text: ." + self.getTopBarSampleLink().text)

    def assertServicesPageHeaderTitle(self):
        act_title = self.getServicesPageMainHeader().text
        exp_title = "SERVICES"
        if act_title == exp_title:
            print("Services Page - Actual Main Title: " + act_title + " and Expected Main Title: " + exp_title + " are matching.")

    def verifyConsultingImgIsDisplayed(self):
        self.isElementPresent(self._consultingImg, locatorType="xpath")
        print("Consulting Image displayed.")

    def assertConsultingHeader(self):
        act_title = self.getConsultingHeader().text
        exp_title = "CONSULTING"
        if act_title == exp_title:
            print("Consulting Header Title is: " + act_title)

    def assertConsultingSubtitle(self):
        subtitle = self.getConsultingSubheaderText().text
        print("Consulting section text is: " + subtitle)

    def verifyTimeFrameImgIsDisplayed(self):
        self.isElementPresent(self._timeframeImg, locatorType="xpath")
        print("Time Frame Image displayed.")

    def assertTimeFrameHeader(self):
        act_title = self.getTimeFrameHeader().text
        exp_title = "TIME FRAME"
        if act_title == exp_title:
            print("Time Frame Header Title is: " + act_title)

    def assertTimeFrameSubtitle(self):
        subtitle = self.getTimeFrameText().text
        print("Time Frame section text is: " + subtitle)

    def verifyDeploymentImgIsDisplayed(self):
        self.isElementPresent(self._deploymentImg, locatorType="xpath")
        print("Deployment Image displayed.")

    def assertDeploymentHeader(self):
        act_title = self.getDeploymentHeader().text
        exp_title = "DEPLOYMENT"
        if act_title == exp_title:
            print("Deployment Header Title is: " + act_title)

    def assertDeploymentSubtitle(self):
        subtitle = self.getDeploymentText().text
        print("Deployment section text is: " + subtitle)

    def clickAboutTopBarLink(self):
        self.elementClick(self._about_link_top_bar, locatorType="xpath")
        print("Clicked on Button: " + self.getTopBarAboutLink().text)

    def clickServicesTopBarLink(self):
        self.elementClick(self._services_link_top_bar, locatorType="xpath")
        print("Clicked on Button: " + self.getTopBarAboutLink().text)

    def getPageTitle(self):
        print("Title of Page is: " + self.driver.title)

    """ Tests """

    def verifyHeaderElements(self):
        self.verifyLogoIsDisplayed()
        self.verifyHomeLinkTopBarIsDisplayed()
        self.verifyServicesLinkTopBarIsDisplayed()
        self.verifyAboutLinkTopBarIsDisplayed()
        self.verifyContactLinkTopBarIsDisplayed()
        self.verifySampleLinkTopBarIsDisplayed()

    def verifyServicesPageElements(self):
        self.clickServicesTopBarLink()
        time.sleep(3)
        self.getPageTitle()
        self.assertServicesPageHeaderTitle()
        self.verifyConsultingImgIsDisplayed()
        self.assertConsultingHeader()
        self.assertConsultingSubtitle()
        self.verifyTimeFrameImgIsDisplayed()
        self.assertTimeFrameHeader()
        self.assertTimeFrameSubtitle()
        self.verifyDeploymentImgIsDisplayed()
        self.assertDeploymentHeader()
        self.assertDeploymentSubtitle()
