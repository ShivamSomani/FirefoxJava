from selenium import webdriver
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary


class RunFFTest():
    def test(self):

        driver = webdriver.Firefox(
            executable_path="/Users/shivam.somani/Documents/selenium_dependencies/geckodriver")
        driver.get("http://www.google.com")

ff = RunFFTest()
ff.test()

