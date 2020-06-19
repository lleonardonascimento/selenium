from selenium.webdriver import Firefox
import time


matricula = 123
senha = 123

driver = Firefox()
driver.get('http://177.70.147.197:8080/sig/app.html#/servicosonline/portal-servidor')

time.sleep(8)

# faz o login
driver.find_element_by_id('radio_1').click()
driver.find_element_by_id("51inputText").send_keys(matricula)
driver.find_element_by_id("52inputText").send_keys(senha)
driver.find_element_by_xpath('//*[@aria-label="Validar"]').click()

time.sleep(1)

#clica em ponto eletrônico
driver.find_element_by_xpath('//*[@heading="Ponto eletrônico"]').click()

time.sleep(5)

#seleciona a linha da tabela com a matrícula correta
driver.find_element_by_xpath('//div[@class="ui-grid-viewport"]//div//div//div//div//div[@title="22397"').click()

time.sleep(5)

driver.find_element_by_xpath('//*[@title="imprimir"]').click()






