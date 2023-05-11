import time
import pyautogui
import keyboard
from funcoes.continuar import on_esc_press
import threading
from funcoes.playmp3 import play_audio

def sqlCreation(slide_thread):
    # Abrindo site
    pyautogui.hotkey('ctrl','l')
    keyboard.write('https://colab.research.google.com')
    pyautogui.press('Enter')
    # criando slides enquanto isso
    time.sleep(5)

 # Abrindo o notebook
    pyautogui.moveTo(1161, 820)
    pyautogui.click()
    time.sleep(7)

    # Iniciar a reprodução do terceiro áudio em uma thread separada
    note_thread = threading.Thread(target=play_audio, args=("abrindoNote.mp3",))
    note_thread.start()

    # Abrindo arquivos
    pyautogui.moveTo(15, 340)
    pyautogui.click()
    # registre a função para ser chamada quando a tecla "Esc" for pressionada
    keyboard.on_press(on_esc_press)

    # aguarde a tecla "Esc" ser pressionada
    while True:
        if keyboard.is_pressed('esc'):
            break

    # importações
    keyboard.write("""
#importacoes necessarias para oq iremos fazer:
import pandas as pd
import sqlite3
import calendar
from datetime import datetime
import matplotlib.pyplot as plt
    """)
    pyautogui.hotkey('ctrl', 'enter')
    pyautogui.hotkey('ctrl', 'm', 'b')

    # escrevendo o codigo do df
    keyboard.write("""
# escreva o caminho do seu arquivo xlsx, ele irá ser lido a partir da linha 7 devido ser texto antes
df = pd.read_excel('caminho/do/arquivo.xlsx', skiprows=6, header=0)

df""")

    # aguarde a tecla "Esc" ser pressionada
    while True:
        if keyboard.is_pressed('esc'):
            break

    pyautogui.hotkey('ctrl', 'enter')
    time.sleep(3)
    pyautogui.hotkey('ctrl', 'm', 'b')
    time.sleep(1)

    # Iniciar a reprodução do audio do banco de dados
    banco_thread = threading.Thread(target=play_audio, args=("bancoDados.mp3",))
    banco_thread.start()

    # Criando banco de dados baseado no df
    keyboard.write("""
# Cria uma conexo com o banco de dados
conn = sqlite3.connect('lotoFacil.db')

# Nome da tabela
nome_tabela = 'numerosSorteados'

# Renomeia as colunas com o padrao solicitado
df.columns = ['Concurso', 'Data', 'bola_1', 'bola_2', 'bola_3', 'bola_4', 'bola_5',
'bola_6', 'bola_7', 'bola_8', 'bola_9', 'bola_10', 'bola_11', 'bola_12',
'bola_13', 'bola_14', 'bola_15']

# Insere os dados do DataFrame na tabela do banco de dados
df.to_sql(nome_tabela, conn, if_exists='replace', index=False)""")
    pyautogui.press('del')
    pyautogui.hotkey('ctrl', 'a')
    for c in range(5):
        pyautogui.hotkey('shift', 'tab')
    pyautogui.hotkey('ctrl', 'enter')

    time.sleep(5)
    pyautogui.scroll(-350)

    pyautogui.hotkey('ctrl', 'm', 'b')
    time.sleep(1)

    # Iniciar a reprodução do audio sobre o grafico
    grafico_thread = threading.Thread(target=play_audio, args=("grafico.mp3",))
    grafico_thread.start()
    # Fazendo grafico com as bolas que mais sairam:
    keyboard.write("""
sql_query = f'''
SELECT ball, COUNT(ball) as count
FROM (SELECT Bola_1 as ball FROM {nome_tabela} UNION ALL
SELECT Bola_2 as ball FROM {nome_tabela} UNION ALL
SELECT Bola_3 as ball FROM {nome_tabela} UNION ALL
SELECT Bola_4 as ball FROM {nome_tabela} UNION ALL
SELECT Bola_5 as ball FROM {nome_tabela} UNION ALL
SELECT Bola_6 as ball FROM {nome_tabela} UNION ALL
SELECT Bola_7 as ball FROM {nome_tabela} UNION ALL
SELECT Bola_8 as ball FROM {nome_tabela} UNION ALL
SELECT Bola_9 as ball FROM {nome_tabela} UNION ALL
SELECT Bola_10 as ball FROM {nome_tabela} UNION ALL
SELECT Bola_11 as ball FROM {nome_tabela} UNION ALL
SELECT Bola_12 as ball FROM {nome_tabela} UNION ALL
SELECT Bola_13 as ball FROM {nome_tabela} UNION ALL
SELECT Bola_14 as ball FROM {nome_tabela} UNION ALL
SELECT Bola_15 as ball FROM {nome_tabela})

GROUP BY ball
ORDER BY count DESC
LIMIT 15
'''

result = conn.execute(sql_query).fetchall()

fig, ax = plt.subplots(figsize=(12, 5))

# Define os rótulos do eixo y como "Ball 1", "Ball 2", etc.
y_labels = [f"Ball {row[0]}" for row in result][::-1]

# Define os valores do eixo x como as contagens de cada bola
x_values = [row[1] for row in result][::-1]

# Define as cores de cada barra como uma lista de tuplas RGBA
bar_colors = [(0, 0, 1, i/18 + 0.2) for i in range(15)]

# Plota o gráfico de barras horizontal
ax.barh(y_labels, x_values, color=bar_colors)


ax.set_xlabel('Numero de vezes que saiu')
ax.set_ylabel('Numero da bola')
ax.set_title('Top 15 bolas que mais sairam na história da LotoFácil')

# Remove white space in the chart
plt.tight_layout()

plt.show()""")
    pyautogui.press('del')
    pyautogui.hotkey('ctrl', 'enter')
    time.sleep(9)
    pyautogui.scroll(-600)

    # registre a função para ser chamada quando a tecla "Esc" for pressionada
    keyboard.on_press(on_esc_press)

    # aguarde a tecla "Esc" ser pressionada
    while True:
        if keyboard.is_pressed('esc'):
            break

    pyautogui.hotkey('ctrl', 'm', 'b')
    # Bolas que mais sairam em cada mes
    keyboard.write("""
# Load data from database
df = pd.read_sql_query("SELECT * FROM numerosSorteados", conn)

# Convert 'Data' column to datetime format
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m/%Y')

# Extract month from 'Data' column
df['month'] = df['Data'].dt.month

# Melt the data frame to have one row per ball
melted_df = pd.melt(df, id_vars=['Concurso', 'Data', 'month'], value_vars=['bola_1', 'bola_2', 'bola_3', 'bola_4', 'bola_5', 'bola_6', 'bola_7', 'bola_8', 'bola_9', 'bola_10', 'bola_11', 'bola_12', 'bola_13', 'bola_14', 'bola_15'], var_name='ball', value_name='number')

# Group by month and number and count the occurrences of each number
result = melted_df.groupby(['month', 'number']).size().reset_index(name='count')

# Sort the result by month and count in descending order
result = result.sort_values(['month', 'count'], ascending=[True, False])

# Group by month and take the first 3 rows of each group (i.e. the 3 most frequent numbers)
result = result.groupby(['month']).head(3)

# Add a column with the month name
result['month_name'] = result['month'].apply(lambda x: calendar.month_name[x])

# Pivot the result to have one row per month and columns for the top 3 numbers
result = result.pivot_table(index=['month_name'], columns=result.groupby(['month_name']).cumcount().add(1), values='number', aggfunc='first')

# Rename columns
result.columns = ['Top 1', 'Top 2', 'Top 3']

# Sort the index to have months in order from January to December
result = result.sort_index(key=lambda x: [calendar.month_name[1:].index(month) for month in x])

# Format the index and columns in bold
result.index = result.index.map(lambda x: f'\\033[1m{x}\\033[0m')
result.columns = result.columns.map(lambda x: f'\\033[1m{x}\\033[0m')

# Display the result
print(result.to_markdown())""")
    for c in range(9):
        pyautogui.press('del')
    pyautogui.hotkey('ctrl', 'enter')

    # Iniciar a reprodução das bolas mes
    bolas_thread = threading.Thread(target=play_audio, args=("bolaSaem.mp3",))
    bolas_thread.start()

    time.sleep(1)
    pyautogui.scroll(-800)

    # registre a função para ser chamada quando a tecla "Esc" for pressionada
    keyboard.on_press(on_esc_press)

    # aguarde a tecla "Esc" ser pressionada
    while True:
        if keyboard.is_pressed('esc'):
            break

    # Iniciar a reprodução das bolas mes
    bolas_thread = threading.Thread(target=play_audio, args=("sorry.mp3",))
    bolas_thread.start()
    pyautogui.hotkey('ctrl', 'm', 'b')
    # Analisando dia e bolas q saem no dia
    keyboard.write("""
# Connect to the database
conn = sqlite3.connect('lotoFacil.db')

# Get the current date and extract the day
today = datetime.now().strftime('%d')

# Query to get the 15 most frequently drawn numbers on the current day
query = f'''
SELECT bola, COUNT(*) as frequency
FROM (
SELECT bola_1 as bola FROM numerosSorteados WHERE substr(Data, 1, 2) = '{today}'
UNION ALL SELECT bola_2 as bola FROM numerosSorteados WHERE substr(Data, 1, 2) = '{today}'
UNION ALL SELECT bola_3 as bola FROM numerosSorteados WHERE substr(Data, 1, 2) = '{today}'
UNION ALL SELECT bola_4 as bola FROM numerosSorteados WHERE substr(Data, 1, 2) = '{today}'
UNION ALL SELECT bola_5 as bola FROM numerosSorteados WHERE substr(Data, 1, 2) = '{today}'
UNION ALL SELECT bola_6 as bola FROM numerosSorteados WHERE substr(Data, 1, 2) = '{today}'
UNION ALL SELECT bola_7 as bola FROM numerosSorteados WHERE substr(Data, 1, 2) = '{today}'
UNION ALL SELECT bola_8 as bola FROM numerosSorteados WHERE substr(Data, 1, 2) = '{today}'
UNION ALL SELECT bola_9 as bola FROM numerosSorteados WHERE substr(Data, 1, 2) = '{today}'
UNION ALL SELECT bola_10 as bola FROM numerosSorteados WHERE substr(Data, 1, 2) = '{today}'
UNION ALL SELECT bola_11 as bola FROM numerosSorteados WHERE substr(Data, 1, 2) = '{today}'
UNION ALL SELECT bola_12 as bola FROM numerosSorteados WHERE substr(Data, 1, 2) = '{today}'
UNION ALL SELECT bola_13 as bola FROM numerosSorteados WHERE substr(Data, 1, 2) = '{today}'
UNION ALL SELECT bola_14 as bola FROM numerosSorteados WHERE substr(Data, 1, 2) = '{today}'
UNION ALL SELECT bola_15 as bola FROM numerosSorteados WHERE substr(Data, 1, 2) = '{today}'
)
GROUP BY bola
ORDER BY frequency DESC
LIMIT 15
'''

# Execute the query and store the result in a DataFrame
df = pd.read_sql_query(query, conn)

# Print the result
# Get the list of most frequently drawn numbers
num_list = df.sort_values('bola').iloc[:, 0].values.tolist()

# Format the output
print('-------------------------------------')
print('         \\033[1mLOTOFÁCIL - RESULTADO\\033[0m       ')
print('-------------------------------------')
print(f'Hoje é dia {today}, nesse dia costuma cair bastante as seguintes bolas:\\n')
print('   \\033[1mBolas Mais Sorteadas No Passado:\\033[0m       ')
print('-------------------------------------')
print(f"\\033[1m{num_list[0]:>6}\\033[0m \\033[1m{num_list[1]:>6}\\033[0m \\033[1m{num_list[2]:>6}\\033[0m \\033[1m{num_list[3]:>6}\\033[0m \\033[1m{num_list[4]:>6}\\033[0m")
print(f"\\033[1m{num_list[5]:>6}\\033[0m \\033[1m{num_list[6]:>6}\\033[0m \\033[1m{num_list[7]:>6}\\033[0m \\033[1m{num_list[8]:>6}\\033[0m \\033[1m{num_list[9]:>6}\\033[0m")
print(f"\\033[1m{num_list[10]:>6}\\033[0m \\033[1m{num_list[11]:>6}\\033[0m \\033[1m{num_list[12]:>6}\\033[0m \\033[1m{num_list[13]:>6}\\033[0m \\033[1m{num_list[14]:>6}\\033[0m")
print('-------------------------------------')""")
    for c in range(49):
        pyautogui.press('del')
    pyautogui.hotkey('ctrl','a')
    pyautogui.hotkey('shift','tab')

    # Iniciar a ultima analise
    bolas_thread = threading.Thread(target=play_audio, args=("ultimo.mp3",))
    bolas_thread.start()

    pyautogui.hotkey('ctrl', 'enter')
    pyautogui.scroll(-800)

    # registre a função para ser chamada quando a tecla "Esc" for pressionada
    keyboard.on_press(on_esc_press)

    # aguarde a tecla "Esc" ser pressionada
    while True:
        if keyboard.is_pressed('esc'):
            break

    pyautogui.hotkey('alt','f4')
    pyautogui.press('enter')


