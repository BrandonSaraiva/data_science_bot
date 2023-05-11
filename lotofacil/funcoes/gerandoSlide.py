import threading
import time
import pyautogui
import keyboard
from funcoes.continuar import on_right_press
from funcoes.continuar import on_up_press
from selenium import webdriver
from selenium.webdriver.common.by import By

from funcoes.playmp3 import play_audio

def slides():
    driver = webdriver.Chrome()
    driver.set_window_position(0, 0)
    driver.set_window_size(1910, 1090)
    driver.minimize_window()
    time.sleep(1)
    driver.get("https://peach.self.team/")
    time.sleep(3)

    # mudando a lingua
    div = driver.find_element(By.CSS_SELECTOR, ".css-2uchni")
    div.click()

    time.sleep(2)

    # Usando execute_script():
    elem = driver.find_element(By.CSS_SELECTOR, ".css-mnkj38:nth-child(7)")
    driver.execute_script("arguments[0].click();", elem)

    # Colocando o nome do projeto
    element = driver.find_element(By.CSS_SELECTOR, 'input#layout-project-name')
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.send_keys('Lotofácil em Análise')

    # Colocando os detalhes do slide
    element = driver.find_element(By.ID, "layout-details")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.send_keys("""
Introdução:

A Lotofácil é uma das loterias mais populares do Brasil devido à sua simplicidade e altas chances de ganhar. O jogo consiste em escolher 15 números dentre os 25 possíveis e, se todos estiverem corretos, o jogador ganha o prêmio principal.

A Lotofácil da Independência:

O concurso mais famoso da Lotofácil é a Lotofácil da Independência, que é realizado anualmente em setembro para comemorar o Dia da Independência do Brasil. Este concurso é altamente aguardado pelos apostadores devido ao alto valor do prêmio oferecido, que geralmente é muito maior do que o valor regular da Lotofácil. Além disso, a arrecadação é destinada exclusivamente para o prêmio principal, o que significa que não há acumulação do valor para os próximos concursos. Em 2021, o prêmio da Lotofácil da Independência foi de R$ 150 milhões.

Estatísticas:

Os jogadores podem usar as estatísticas da Lotofácil para ajudá-los a escolher seus números da sorte. As bolas mais sorteadas na história da Lotofácil são a bola 20, que foi sorteada 1752 vezes, a bola 10, que foi sorteada 1743 vezes, e a bola 11, que foi sorteada 1739 vezes. No entanto, é importante lembrar que a loteria é um jogo de azar, e as estatísticas não garantem a vitória.

As 3 bolas que mais saem em cada mês:

As estatísticas mostram que há três bolas que têm mais chances de serem sorteadas em cada mês. Em janeiro, as bolas mais sorteadas são a 11, 20 e 10, enquanto em fevereiro, são a 18, 8 e 2. Em março, as bolas mais sorteadas são a 11, 20 e 25. Conhecer essas estatísticas pode ser útil para aqueles que desejam aumentar suas chances de ganhar.

Conclusão:

Em resumo, a Lotofácil é uma loteria popular no Brasil com altas chances de ganhar e a Lotofácil da Independência é um dos concursos mais aguardados do ano devido ao alto valor do prêmio oferecido. É importante lembrar que a loteria é um jogo de azar e que as estatísticas não garantem a vitória, mas podem ser úteis para aqueles que desejam aumentar suas chances de ganhar.""""")

    # O objetivo
    element = driver.find_element(By.ID, "layout-purpose")
    driver.execute_script("arguments[0].scrollIntoView();", element)
    element.send_keys('Apresentação das análises que fiz do banco de dados da lotofácil')

    #     Gerando o slide
    botao = driver.find_element(By.ID, ":r3:")
    botao.click()

    #
    # registre a função para ser chamada quando a tecla "Esc" for pressionada
    keyboard.on_press(on_right_press)

    # aguarde a tecla "Esc" ser pressionada
    while True:
        if keyboard.is_pressed('right'):
            break

    # Iniciar a ultima analise
    bolas_thread = threading.Thread(target=play_audio, args=("apresentacao.mp3",))
    bolas_thread.start()

    # imprimindo
    pyautogui.moveTo(1800, 410)
    pyautogui.click()

    time.sleep(4)

    # abrindo slides
    pyautogui.moveTo(119, 1045)
    pyautogui.click()

    time.sleep(10)

#     Dando play nos slides
    pyautogui.moveTo(455, 34)
    pyautogui.click()
    time.sleep(1)
    pyautogui.moveTo(30, 78)
    pyautogui.click()

    keyboard.on_press(on_up_press)

    while True:
        if keyboard.is_pressed('up'):
            break

    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://brandonsaraiva.github.io/devportfolio/")
    while True:
        if keyboard.is_pressed('up'):
            break
    driver.get("https://github.com/BrandonSaraiva/data_science_bot")

    input("Pressione Enter para finalizar o driver...")
    driver.quit()
    