# This is a sample Python script.
from funcoes.webscraping import scraping
import threading
from funcoes.gerandoSlide import slides

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Web scraping pra fazer o donwload do excel
    thread = threading.Thread(target=slides)
    thread.start()
    scraping()
 
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
