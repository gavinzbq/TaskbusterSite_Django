# -*- coding: utf-8 -*-
from selenium import webdriver
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import unittest

#caps = DesiredCapabilities.FIREFOX
#caps['marionette'] = True

#caps['binary'] = '/Applications/Firefox.app/Contents/MacOS/firefox-bin'
#geckodriver = '/usr/local/bin/geckodriver'

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        #sself.browser = webdriver.Firefox(capabilities=caps)
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        #self.browser.get('http://www.google.com')
        self.assertIn('Welcome to Django', self.browser.title)

if __name__ == '__main__':
    unittest.main(warnings='ignore')
