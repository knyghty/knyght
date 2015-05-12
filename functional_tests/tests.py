from django.test import LiveServerTestCase

from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_homepage_browse(self):
        # Bertram lands on the hompage of the site.
        self.browser.get(self.live_server_url)

        # He sees knyg.ht in the title.
        self.assertIn('knyg.ht', self.browser.title)

        # He also sees knyg.ht in the header.
        header = self.browser.find_element_by_id('header')
        self.assertIn('knyg.ht', header.text)

        # And the main navigation menu.
        nav = self.browser.find_element_by_xpath("//header[@id='header']/nav")
        self.assertTrue(nav)
