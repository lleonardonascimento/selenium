from selenium.webdriver import Firefox
from time import sleep


matricula = 123
senha = 123
# alterado para evitar erro de linha muito longa!!
url = "http://177.70.147.197:8080/sig/app.html#/servicosonline/portal-servidor"

driver = Firefox()
driver.get(url)
sleep(8)

# faz o login
# Clica no radio para mudar para matricula!!
driver.find_element_by_id("radio_1").click()
sleep(1)
# Preenche o input com a matricula
driver.find_element_by_xpath('//*[@id="51inputText"]').send_keys(matricula)
# Preenche o input com a senha
driver.find_element_by_xpath('//*[@id="52inputText"]').send_keys(senha)
# Clica em validar
driver.find_element_by_xpath('//*[@aria-label="Validar"]').click()

sleep(1)

# clica em ponto eletrônico
driver.find_element_by_xpath('//*[@heading="Ponto eletrônico"]').click()

sleep(5)

# seleciona a linha da tabela com a matrícula correta
driver.find_element_by_xpath(
    '//div[@class="ui-grid-viewport"]//div//div//div//div//div[@title="22397"'
).click()

sleep(5)

driver.find_element_by_xpath('//*[@title="imprimir"]').click()
