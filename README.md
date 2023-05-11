# Objetivo
O objetivo desse projeto foi automatizar grande parte do processo da analise de dados. 
# Bibliotecas utilizadas
- threading
- time
- pyautogui
- keyboard
- pygame
- os
- getpass
- selenium
- pandas
- sqlite3
- calendar
- datetime
- matplotlib
# Passo a Passo
Bom, primeiro eu faço o bot pegar as configurações do usuário do chrome para ele poder acessar alguns recursos que precisam de login, por exemplo o jupyer notebook. Depois ele abre 2 abas, uma vai entrar no site https://peach.self.team/ para poder gerar os slides (esse site é uma IA que gera slides com base nas informações que você der a ela) e a outra aba irá baixar o banco de dados, criar um dataframe e criar os gráficos. Na parte dos slides eu forneço informaçao como por exemplo o titulo do slide, as informações que vai conter, e o objetivo do slide. Na outra aba, ele entra no site https://asloterias.com.br/download-todos-resultados-lotofacil, scrola pra baixo até achar o botão de download do arquivo .csv, enquanto isso ocorre, um áudio explicando o que o bot está fazendo está sendo tocado, o projeto inteiro tem 9 audios durante o processo, explicando o passo a passo do que está sendo feito. Depois dele baixar o csv, ele irá abrir 1 jupyter notebook no google colab, apertando a tecla *esc* ele irá digitar o código, esse código ele digita atraves da funçao keyboard.write, eu coloquei os codigos a serem digitados dentro dessa funçao e ele executa. Depois de voce subir o csv e colocar o caminho no código ele irá criar um dataframe utilizando a biblioteca pandas,com esse dataframe ele irá criar um banco de dado utilizando a biblioteca sqlite3. Depois de criar o banco de dados começa a parte de analisar os dados, o primeiro gráfico q ele cria é mostrando as 15 bolas que mais sairam na história da lotofácil, eis o código para servir de exemplo:

```
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
```

O Gráfico que ele gera:


![image](https://github.com/BrandonSaraiva/data_science_bot/assets/90096835/d4244f45-b7a0-4afa-ba37-d1561e37cb74)

