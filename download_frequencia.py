from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from time import sleep

# lê o arquivo e armazena o conteudo em 'f'
with open("pw.txt", "r") as target:
    f = target.read()

# TODO
# como o retorno de uma string com o metodo split é uma lista
# armazena em sua respectivas var
(matricula, senha) = f.split(" ")

# alterado para evitar erro de linha muito longa!!
url = "http://177.70.147.197:8080/sig/app.html#/servicosonline/portal-servidor"

driver = Firefox()
wait = WebDriverWait(driver, 10)
driver.get(url)
sleep(4)


def login(matricula, senha):
    """Loga no sistema """
    # Clica no radio para mudar para matricula!!
    driver.find_element_by_id("radio_1").click()
    sleep(1)
    # Preenche o input com a matricula
    driver.find_element_by_xpath('//*[@id="51inputText"]').send_keys(matricula)
    # Preenche o input com a senha
    driver.find_element_by_xpath('//*[@id="52inputText"]').send_keys(senha)
    # Clica em validar
    driver.find_element_by_xpath('//*[@aria-label="Validar"]').click()
    print("Logado com a Mat: {}".format(matricula))


def deslogar():
    driver.find_element_by_xpath("/html/body/div/div/md-toolbar/div/a").click()
    print("Deslogando")
    driver.get(url)


def verificaPopup():
    # popup
    try:
        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/pd-tela-padrao/div/div/md-toolbar/div/h4"
        )

        driver.find_element_by_xpath(
            "/html/body/div[1]/div/div/div/pd-tela-padrao/div/div/md-toolbar/div/button"
        ).click()
    except:
        pass


# clica em ponto eletrônico

login(matricula, senha)
sleep(3)
verificaPopup()
sleep(2)

driver.find_element_by_xpath('//*[@heading="Ponto eletrônico"]').click()
sleep(3)
driver.find_element_by_xpath(
    "/html/body/div/div/md-content/div/ui-view/div/pd-index-modulo/div/div/div/pd-tela-padrao/div/form/div[1]/div/pd-tela-padrao-body/div[3]/pd-tab/div/div/div/div[3]/div/pd-legend/div/fieldset/ng-transclude/div/pd-grid/div/div[1]/div/div[2]/div[2]/div/div[1]"
).click()
sleep(8)
elem = driver.find_element_by_css_selector("button.md-raised:nth-child(2)")
elem.location_once_scrolled_into_view
elem.click()

# # seleciona a linha da tabela com a matrícula correta
# driver.find_element_by_xpath(
#     '//div[@class="ui-grid-viewport"]//div//div//div//div//div[@title="22397"'
# ).click()

# sleep(5)

# driver.find_element_by_xpath('//*[@title="imprimir"]').click()


# dados = driver.find_element_by_xpath('/html/body/div/div/md-content/div/ui-view/div/pd-index-modulo/div/div/div/pd-tela-padrao/div/form/div[1]/div/pd-tela-padrao-body/div[3]/pd-tab/div/div/div/div[3]/div/pd-legend/div/fieldset/ng-transclude/div/pd-grid/div/div[1]/div/div[2]/div[2]')

# # aterna para nova janela
# driver.switch_to.window(driver.window_handles[-1])

# #verifica se mudou de aba corretamente
# driver.current_url

# # 'http://177.70.147.197:8080/sig/jasperservlet'

# # faz o donw do arquivo
# driver.find_element_by_xpath('//*[@id="download"]').click()

# #fecha a aba
# driver.close()
