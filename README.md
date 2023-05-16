# Projeto Automação da Análise de Dados
Este projeto tem como objetivo automatizar grande parte do processo da análise de dados. Foram utilizadas diversas bibliotecas, incluindo threading, time, pyautogui, keyboard, pygame, os, getpass, selenium, pandas, sqlite3, calendar e matplotlib.

# Passo a Passo
O bot começa pegando as configurações do usuário do Chrome para acessar recursos que precisam de login, como o Jupyter Notebook. Em seguida, ele abre duas abas. Uma acessa o site https://peach.self.team/ para gerar slides com base nas informações fornecidas, enquanto a outra aba faz o download do banco de dados, cria um dataframe e cria gráficos.

Na parte dos slides, são fornecidas informações como o título do slide, as informações que ele deve conter e seu objetivo. Na outra aba, o bot acessa o site https://asloterias.com.br/download-todos-resultados-lotofacil, faz scroll até encontrar o botão de download do arquivo .csv e, durante esse processo, um áudio é tocado explicando cada passo do que está sendo feito.

Após baixar o csv, o bot abre um notebook no Google Colab e digita o código necessário utilizando a biblioteca keyboard.write. O usuário deve inserir o caminho do arquivo csv no código para criar um dataframe com a biblioteca pandas. Em seguida, o bot cria um banco de dados utilizando a biblioteca sqlite3.

A partir daí, o bot analisa os dados e cria gráficos. O primeiro gráfico mostra as 15 bolas que mais saíram na história da Lotofácil. Para criar esse gráfico, o bot executa o seguinte código:

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

Eu adicionei uma função que quando vc aperta P ele para o codigo, caso algo de errado no processo.

**Slides**

Depois de pressionar "Esc", o navegador será fechado e uma nova aba será aberta, onde o slide estará pronto para ser baixado. Ao pressionar a seta para a direita, os comandos para baixar, abrir e executar o slide serão executados automaticamente. No áudio, é explicado que a IA responsável por gerar os slides ainda está "aprendendo" e que esta é uma versão gratuita. Como resultado, os slides podem não ter uma qualidade excelente e a formatação do texto pode ser bastante simples. Além disso, podem ser adicionadas imagens que não estejam relacionadas com o conteúdo e informações curiosas e irrelevantes. Antes, este projeto utilizava a extensão paga do Google chamada Slides.Ai.io, que produzia slides incríveis. Infelizmente, devido ao fato de ser uma ferramenta paga, não foi possível continuar utilizando-a.

**Apresentação**

Após a geração dos slides pelo bot, fica a meu encargo apresentá-los e fornecer informações adicionais sobre a loteria lotofácil.

# Conclusão

Este projeto pode ser otimizado de diversas maneiras para torná-lo mais adaptável a outras análises e bancos de dados. Escolhi essa forma de trabalhar para aprimorar minhas habilidades em automação e obter ideias para futuros projetos.

# Vídeo para ver o bot funcionando:


https://drive.google.com/file/d/14DQf63hvocHKhdQBuuV8w09UfFmcINOE/view
