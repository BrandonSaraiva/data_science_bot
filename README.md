# Objetivo
O objetivo desse projeto foi automatizar grande parte do processo da analise de dados. Fiz esse trabalho dessa forma porque amo mecher com automação, por isso decidi não só baixar os dados utilizando webscraping, mas todo o caminho da analise de dados.
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
  Bom, primeiro eu faço o bot pegar as configurações do usuário do chrome para ele poder acessar alguns recursos que precisam de login, por exemplo o jupyer notebook. Depois ele abre 2 abas, uma vai entrar no site https://peach.self.team/ para poder gerar os slides (esse site é uma IA que gera slides com base nas informações que você der a ela) e a outra aba irá baixar o banco de dados, criar um dataframe e criar os gráficos. Na parte dos slides eu forneço informaçao como por exemplo o titulo do slide, as informações que vai conter, e o objetivo do slide. Na outra aba, ele entra no site https://asloterias.com.br/download-todos-resultados-lotofacil, scrola pra baixo até achar o botão de download do arquivo .csv, enquanto isso ocorre, um áudio explicando o que o bot está fazendo está sendo tocado, o projeto inteiro tem 9 audios durante o processo, explicando o passo a passo do que está sendo feito. 
  Depois dele baixar o csv, ele irá abrir 1 jupyter notebook no google colab, apertando a tecla *esc* ele irá digitar o código, esse código ele digita atraves da funçao keyboard.write, eu coloquei os codigos a serem digitados dentro dessa funçao e ele executa. Depois de voce subir o csv e colocar o caminho no código ele irá criar um dataframe utilizando a biblioteca pandas,com esse dataframe ele irá criar um banco de dado utilizando a biblioteca sqlite3. 
  Depois de criar o banco de dados começa a parte de **analisar** os dados, o primeiro gráfico q ele cria é mostrando as 15 bolas que mais sairam na história da lotofácil, eis o código para servir de exemplo:

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

Depois disso, ele irá criar um código que mostra as 3 bolas que mais saem cada mes, o resultado é esse:

![image](https://github.com/BrandonSaraiva/data_science_bot/assets/90096835/18cdfd1a-fdce-4241-96e0-2f2f2efd7d51)

E por último, ele produz um código que pega o dia atual, e depois vê quais as bolas que mais sairam nesse mesmo dia no passado, retornando o resultado:

![image](https://github.com/BrandonSaraiva/data_science_bot/assets/90096835/446b1585-d5d0-4618-8fba-3db70a5a4e6f)

Lembrando que durante todo esse processo ele está narrando as ações.

**Slides**

Após apertar esc, ele irá fechar o navegador e você irá abrir a outra aba que ele criou logo no início, lá o slide já estará pronto para ser baixado, apertando a seta *right* ele irá executar os comandos de baixar o slide, abrir ele e executar. No áudio ele explica que a IA que gerou os slides ainda está "aprendendo", é uma versão grátis então os slides não irão ser de uma qualidade muito boa, ela formata o texto de uma forma bem simples, coloca imagens que muitas vezes não tem haver com o texto e coloca algumas informações esquisitas kkk, o melhor gerador de slides atual é uma extensão do google chamada Slides.Ai.io, antes esse projeto era utilizando essa ferramenta, os slides ficavam incríveis, mas por ser uma ferramenta paga não deu para eu dar continuidade nesse projeto. 

**Apresentação**

A apresentação dos slides ficou comigo mesmo, depois do bot fazer maior parte do trabalho eu fico com a parte final de mostrar os slides que foram gerados e falar algumas informações a mais sobre a loteria lotofácil.

**Conclusão**

Existem diversas alterações possíveis nesse projeto para deixar ele mais otimizado, mais adaptável a outras análises e bancos de dados, o objetivo principal de eu ter escolhido essa forma de fazer foi para desenvolver mais minhas skills em automação e me ajudar a ter idéias para projetos futuros.
