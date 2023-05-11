import os
import pygame

def play_audio(mp3_filename):
    # Obtém o diretório atual do script
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Constrói o caminho para a pasta "audios" usando o diretório atual
    audios_dir = os.path.join(current_dir, "audios")

    # Constrói o caminho completo para o arquivo MP3 dentro da pasta "audios"
    mp3_path = os.path.join(audios_dir, mp3_filename)

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

