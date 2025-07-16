# 📊 Chatbot de Análise de Vendas com Streamlit

Este projeto demonstra a evolução de um chatbot básico de análise de vendas baseado em terminal para um **aplicativo web interativo e robusto**, construído com **Python** e **Streamlit**. Ele oferece uma interface amigável para consultar e visualizar dados de vendas, integrando Processamento de Linguagem Natural (PNL) com recursos de manipulação e exibição de dados.

É um recurso valioso para desenvolvedores que desejam entender como transformar scripts de análise de dados em **aplicações web completas e conversacionais**, com foco na experiência do usuário e na flexibilidade das consultas.

---

## ✨ Jornada de Evolução do Projeto

Este projeto passou por uma significativa evolução, transformando um script simples de terminal em uma aplicação web interativa:

### Versão Inicial (Terminal)

* **Foco:** Demonstrar conceitos básicos de PNL e análise de dados em um ambiente de terminal.
* **Dados:** `DataFrame` pequeno e estático com `Produto`, `Vendas` e `Regiao`.
* **Análises:** Apenas `total_vendas` e `media_vendas` por produto.
* **PNL:** Detecção simples de palavras-chave (`"vendas"`, nomes de produtos) e loop básico de interação.
* **Experiência do Usuário:** Interação por linha de comando (`input()`, `print()`).

### Versão Atual (Streamlit - Aprimorada)

* **Foco:** Construir uma aplicação web completa e interativa para análise de vendas com foco na usabilidade e visualização.
* **Dados Expandidos:** `DataFrame` maior e mais rico, incluindo `Quantidade`, `Valor Unitario`, `Data Compra`, além de colunas derivadas como `Total Venda`, `Ano`, `Mes`.
* **Funcionalidades de Dados:**
    * Carga de dados otimizada com `@st.cache_data`.
    * Cálculo de `Total Venda`.
    * Extração de `Ano` e `Mes` da `Data Compra`.
    * Formatação de valores monetários para padrão brasileiro (`R$ X.XXX,XX`).
* **Análises Abrangentes:**
    * `analisar_vendas_produto`: Total de vendas por produto.
    * `mes_que_mais_vendeu`: Identifica o mês de maior faturamento.
    * `regiao_que_mais_vendeu_produto`: Encontra a região líder de vendas para um produto específico.
    * `total_vendas_no_ano`: Sumariza as vendas por cada ano registrado.
    * `total_vendas_no_mes`: Permite consultar o total de vendas para qualquer mês específico.
* **Lógica de Chatbot (PNL Aprimorada):**
    * Migração para **Streamlit Chat Elements** para uma interface de chat moderna e com histórico de mensagens.
    * Uso de **Expressões Regulares (`re`)** para um reconhecimento de intenção e extração de entidades muito mais robusto e flexível, permitindo variações na formulação das perguntas.
    * Priorização inteligente das intenções do usuário.
* **Interface e Visualização (Streamlit):**
    * **Aplicação Web:** Experiência completa em navegador.
    * **Layout:** `st.set_page_config` configurando título, ícone e layout `wide`.
    * **Tabela de Dados Detalhados:** Exibição interativa do `DataFrame` de vendas com `st.dataframe`.
    * **Estilização Personalizada:** Utilização de `.streamlit/config.toml` para definir um tema visual (`primaryColor`, `backgroundColor`, `textColor`, etc.), garantindo uma experiência de usuário mais agradável.
    * **Alinhamento de Colunas:** Aplicação de `st.column_config.TextColumn` para alinhar a coluna 'Quantidade' à esquerda, melhorando a legibilidade.

---

## 🚀 Funcionalidades Atuais

O chatbot oferece análises aprofundadas sobre dados de vendas de forma conversacional:

-   **Análise por Produto:** Total de vendas de um produto específico.
-   **Melhor Mês de Vendas:** Identifica o mês com o maior faturamento geral.
-   **Vendas Anuais:** Exibe o total de vendas para cada ano presente nos dados.
-   **Vendas por Mês Específico:** Permite consultar o faturamento de um determinado mês.
-   **Desempenho por Região (por produto):** Mostra qual região mais vendeu um produto específico.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi desenvolvido com as seguintes ferramentas e bibliotecas:

-   **Python (Core):** Para a lógica de programação e backend.
-   **Pandas:** Essencial para manipulação, agregação e análise de dados.
-   **Streamlit:** Framework para construção rápida e eficiente da interface web e componentes interativos.
-   **`re` (Regex):** Biblioteca para processamento de linguagem natural, permitindo o reconhecimento de padrões nas perguntas dos usuários.
-   **`calendar`:** Utilizado para manipulação de nomes de meses.

---

## 🏗️ Estrutura do Projeto

A estrutura atual do aplicativo é altamente modular e reflete as boas práticas de desenvolvimento de aplicações Streamlit:

-   **`app.py`:** É o coração da aplicação Streamlit, contendo:
    * Definição e carregamento dos dados de vendas (`carregar_dados`).
    * Funções especializadas para diferentes tipos de análise de dados.
    * A função `chatbot_resposta`, que interpreta as perguntas do usuário usando regex e aciona as funções de análise apropriadas.
    * Todo o código da interface do usuário do Streamlit, incluindo o cabeçalho, a exibição da tabela de dados e o componente de chat.
-   **`.streamlit/config.toml`:** Um arquivo de configuração chave para personalizar o tema visual do aplicativo (cores de fundo, texto, primária, etc.), garantindo uma experiência visual consistente e agradável.

---

## ⚙️ Como Rodar o Projeto

Siga os passos abaixo para configurar e executar o chatbot no seu ambiente local:

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/Dayanebiaerafa/Chatbot-Analise-de-Vendas.git](https://github.com/Dayanebiaerafa/Chatbot-Analise-de-Vendas.git)
    ```

2.  **Navegue até o diretório do projeto:**

    ```bash
    cd Chatbot-Analise-de-Vendas
    ```

3.  **Crie e ative um ambiente virtual (altamente recomendado):**

    ```bash
    python -m venv venv
    # No Windows:
    .\venv\Scripts\activate
    # No macOS/Linux:
    source venv/bin/activate
    ```

4.  **Instale as dependências:**

    ```bash
    pip install pandas streamlit
    ```

5.  **Verifique a configuração do tema (opcional, mas recomendado para o visual completo):**
    Crie uma pasta chamada `.streamlit` no mesmo diretório do `app.py` (se ela ainda não existir). Dentro dela, crie um arquivo chamado `config.toml` e adicione o seguinte conteúdo para definir o tema:

    ```toml
    # .streamlit/config.toml
    [theme]
    primaryColor="#3A0BE6"        # Cor principal (botões, links)
    backgroundColor="#FFFFFF"     # Cor de fundo da aplicação
    secondaryBackgroundColor="#DEE0E4" # Cor de fundo de elementos secundários (ex: sidebar, containers)
    textColor="#040610"           # Cor do texto principal
    # font="sans serif"           # Opcional: descomente e mude se quiser uma fonte específica
    ```

6.  **Execute o aplicativo Streamlit:**

    ```bash
    streamlit run app.py
    ```

    Após a execução, o Streamlit abrirá automaticamente o aplicativo no seu navegador padrão. Você poderá interagir com o chatbot e visualizar os dados.

---

## 🤝 Como Colaborar

Contribuições, ideias e sugestões são **muito bem-vindas**! Se você tem formas de aprimorar o chatbot, adicionar novas funcionalidades, refatorar o código ou corrigir bugs, sinta-se à vontade para:

1.  **Abrir uma Issue:** Descreva detalhadamente o problema encontrado ou a sugestão de melhoria.
2.  **Fazer um Pull Request:**
    * Faça um fork (ramificação) deste repositório para a sua conta GitHub.
    * Crie uma nova branch para suas alterações:
        ```bash
        git checkout -b sua-nova-feature-ou-correcao
        ```
    * Implemente suas alterações, faça commits com mensagens claras e concisas.
    * Envie suas alterações para o seu fork:
        ```bash
        git push origin sua-nova-feature-ou-correcao
        ```
    * No GitHub, abra um Pull Request do seu fork para o repositório original, explicando suas mudanças e o valor que elas agregam ao projeto.

Vamos construir algo ainda melhor juntos! 💡

---
<p>
    <img 
      align=left 
      margin=10 
      width=80 
      src="https://github.com/user-attachments/assets/430109f9-1127-4cf3-a823-c29d32ecea76"
    />
    <p>&nbsp&nbsp&nbspDayane Teodoro<br>
    &nbsp&nbsp&nbsp
    <a href="https://github.com/Dayanebiaerafa">
    GitHub</a>&nbsp;|&nbsp;
    <a href="https://www.linkedin.com/in/dayaneteodoro/">LinkedIn</a>
&nbsp;|&nbsp;
    <a href="https://www.instagram.com/dayane_cie/">
    Instagram</a>
&nbsp;|&nbsp;</p>
</p>
<br/><br/>
<p>
💞 Feito com amor por Dayane Teodoro 🚀

**#Python #Chatbot #Pandas #Streamlit #PNL #AnáliseDeDados #DataScience #AssistenteConversacional #OpenSource #DesenvolvimentoWeb**
