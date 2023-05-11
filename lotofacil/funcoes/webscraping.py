
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import getpass
from funcoes.tratamento import sqlCreation
from funcoes.playmp3 import play_audio
import os
import pygame
import threading

def scraping():
    username = getpass.getuser()
    # Inicializar o driver do Selenium
    options = webdriver.ChromeOptions()
    options.add_argument(
        f"user-data-dir=C:\\Users\\{username}\\AppData\\Local\\Google\\Chrome\\User Data\\".format(username))
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()

    # Iniciar a reprodução do primeiro áudio em uma thread separada
    audio_thread = threading.Thread(target=play_audio, args=("baixando_dados.mp3",))
    audio_thread.start()

    # Navegar até o site desejado
    driver.get("https://asloterias.com.br/download-todos-resultados-lotofacil")

    # Rolar a página para baixo em 1000 pixels
    driver.execute_script("window.scrollBy(0, 200);")

    # Encontrar o elemento e rolar a página para ele
    download_button = driver.find_element(By.CSS_SELECTOR,
                                          '[title="Download Todos resultados da Lotofacil em Excel por ordem crescente"]')
    driver.execute_script("arguments[0].scrollIntoView();", download_button)

    # Clicar no elemento
    download_button.click()

    time.sleep(1.5)

    # Esperar até que a reprodução do primeiro áudio termine antes de iniciar a reprodução do segundo áudio
    audio_thread.join()

    # Iniciar a reprodução do segundo áudio em uma thread separada
    slide_thread = threading.Thread(target=play_audio, args=("criandoSlides.mp3",))
    slide_thread.start()
    # Parte do jupyter colab
    sqlCreation(slide_thread)


    input("Pressione Enter para finalizar o driver...")
    driver.quit()
