import os
import pygame
import sys

def play_audio(mp3_filename):
    # Verifique se o script está sendo executado pelo PyInstaller
    if getattr(sys, 'frozen', False):
        # Se sim, o diretório do executável é armazenado em sys._MEIPASS
        current_dir = sys._MEIPASS
    else:
        # Caso contrário, o diretório atual é usado
        current_dir = os.path.dirname(os.path.abspath(__file__))

    # Constrói o caminho completo para o arquivo MP3 dentro da pasta "audios"
    mp3_path = os.path.join(current_dir, "audios", mp3_filename)

    # Inicializa o mixer de áudio do pygame
    pygame.mixer.init()

    # Carrega o arquivo de áudio MP3
    pygame.mixer.music.load(mp3_path)

    # Toca o arquivo de áudio MP3
    pygame.mixer.music.play()

    # Espera até que a reprodução do arquivo de áudio termine
    while pygame.mixer.music.get_busy():
        pass

    # Retorne o objeto de áudio
    return pygame.mixer.music
