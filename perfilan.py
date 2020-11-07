import unittest
import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

class PerfilanTest(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome(executable_path =r'C:\chromedriver\chromedriver.exe') 

    def test_login(self):
        driver = self.driver
        driver.get("https://panel.perfilan.com")
        
        user = driver.find_element_by_id("txtUsuario")
        user.send_keys("user")        
        sleep(2)

        pw = driver.find_element_by_id("txtPass")
        pw.send_keys("pass")        
        sleep(2)

        login = driver.find_element_by_id("btn-inicio")  
        login.click()   
        sleep(4)  

        prospectos = driver.find_element_by_xpath('//*[@id="menuCollapse"]/a[3]')
        prospectos.click()
        sleep(9) 

        search = driver.find_element_by_xpath('//*[@id="table_prospectos_filter"]/label/input')
        search.send_keys("Monica")
        sleep(5) 

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='Resultados de la prueba'))

