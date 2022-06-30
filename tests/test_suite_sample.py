import unittest
from tests.test_home_page import HomePageTest
from tests.test_services_page import ServicesPageTest
from tests.test_about_page import AboutPageTest
from tests.test_contact_page import ContactPageTest
from tests.test_sample_page import SamplePageTest

""" Cases """

tc1 = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
tc2 = unittest.TestLoader().loadTestsFromTestCase(ServicesPageTest)
tc3 = unittest.TestLoader().loadTestsFromTestCase(AboutPageTest)
tc4 = unittest.TestLoader().loadTestsFromTestCase(ContactPageTest)
tc5 = unittest.TestLoader().loadTestsFromTestCase(SamplePageTest)

""" Test Collection """
smokeTest = unittest.TestSuite([tc1, tc2, tc3, tc4, tc5])
unittest.TextTestRunner(verbosity=2).run(smokeTest)