# selenium é uma biblioteca para automações do navegador.
# edge, chrome, firefox, opera

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

navegador = webdriver.Edge()

navegador.get('https://www.google.com')
navegador.find_element('name', 'q').send_keys('Senac' + Keys.ENTER)

input()