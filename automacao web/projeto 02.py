from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

dados = {'nome': 'Ana Letícia Becker Gomes',
         'data_nascimento': '24-04-2000',
         'email': 'aleticiabg@gmail.com'}

navegador = webdriver.Edge()

navegador.get('https://form.jotform.com/221878303914661')
sleep(2)

navegador.find_element('id', 'input_42').send_keys(dados['nome'])
navegador.find_element('id', 'lite_mode_7').send_keys(dados['data_nascimento'])
navegador.find_element('id', 'input_5').send_keys(dados['email'])

navegador.find_element('id', 'input_40').click()


input()