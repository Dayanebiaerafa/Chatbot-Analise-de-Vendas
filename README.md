# 📊 Chatbot de Análise de Vendas com Streamlit

Este projeto evoluiu para um **aplicativo web interativo** construído em **Python** utilizando **Streamlit**, projetado para fornecer insights de análise de vendas através de uma interface de chatbot amigável. Ele demonstra a integração de funcionalidades de Processamento de Linguagem Natural (PNL) com capacidades de visualização e manipulação de dados.

É um excelente recurso para desenvolvedores que buscam entender como construir **aplicativos conversacionais interativos que analisam e exibem dados**.

---

## ✨ Novidades e Melhorias

Desde a versão anterior, o projeto foi significativamente aprimorado com as seguintes funcionalidades:

* **Interface Web com Streamlit:** O chatbot agora opera em um navegador, oferecendo uma experiência de usuário muito mais rica e intuitiva.
* **Visualização de Dados Interativa:** Adição de uma tabela dinâmica para exibir os dados de vendas detalhados diretamente na interface do aplicativo.
* **Estilização Personalizada:** Implementação de um tema visual coeso através do arquivo `config.toml`, permitindo controle sobre cores primárias, de fundo e de texto.
* **Alinhamento de Colunas na Tabela:** Aprimoramento da apresentação dos dados na tabela, com a coluna 'Quantidade' agora alinhada à esquerda para melhor legibilidade.
* **Lógica de PNL Aprimorada com Regex:** O "cérebro" do chatbot utiliza expressões regulares (`re`) para um reconhecimento de intenção e extração de entidades mais robusto e flexível.
* **Novas Análises de Vendas:**
    * **Mês que mais vendeu:** Identifica o período de maior faturamento.
    * **Total de vendas no ano:** Fornece um resumo anual.
    * **Total de vendas no mês específico:** Permite consultar vendas por qualquer mês.
    * **Região que mais vendeu por produto:** Ajuda a identificar o desempenho de produtos em diferentes locais.

---

## 🚀 Funcionalidades Principais

O chatbot oferece análises sobre dados de vendas, aplicando os seguintes princípios:

-   **Entendimento da Intenção e Extração de Entidades:** Reconhece as perguntas do usuário e extrai informações cruciais (como nomes de produtos, meses, etc.).
-   **Acesso e Processamento de Dados com Pandas:** Utiliza um DataFrame simulado para filtrar, agrupar e calcular métricas de vendas (totais, por produto, por região, por mês/ano).
-   **Geração de Insights Claras e Contextualizadas:** Apresenta os resultados da análise de forma compreensível e em formato de diálogo.
-   **Interatividade:** Mantém um fluxo de diálogo contínuo, com histórico de mensagens e sugestões de perguntas.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi desenvolvido com as seguintes ferramentas e bibliotecas:

-   **Python (Core):** Para a lógica de programação.
-   **Pandas:** Para manipulação e análise eficiente de dados tabulares.
-   **Streamlit:** Para a construção rápida da interface web interativa e do chatbot.
-   **`re` (Regex):** Para padrões de reconhecimento de texto na lógica do chatbot.

---

## 🏗️ Estrutura do Projeto

A estrutura do aplicativo é modular e didática:

-   **`app.py`:** Contém toda a lógica do aplicativo Streamlit, incluindo:
    * Carregamento e pré-processamento dos dados de vendas.
    * Funções para análises específicas de vendas (por produto, mês, ano, região).
    * A lógica principal do chatbot (`chatbot_resposta`) com uso de expressões regulares.
    * A interface do usuário do Streamlit, incluindo o chat e a tabela de dados.
-   **`.streamlit/config.toml`:** Arquivo de configuração que define o tema visual do aplicativo (cores de fundo, texto, primária, etc.).

---

## ⚙️ Como Rodar o Projeto

Siga os passos abaixo para executar o chatbot no seu ambiente local:

1.  **Clone o repositório:**

    ```bash
    git clone [https://github.com/Dayanebiaerafa/Chatbot-Analise-de-Vendas.git](https://github.com/Dayanebiaerafa/Chatbot-Analise-de-Vendas.git)
    ```

2.  **Navegue até o diretório do projeto:**

    ```bash
    cd Chatbot-Analise-de-Vendas
    ```

3.  **Crie e ative um ambiente virtual (recomendado):**

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

5.  **Verifique a configuração do tema:**
    Certifique-se de que a pasta `.streamlit` existe no mesmo nível do `app.py` e que o arquivo `config.toml` dentro dela contém as suas configurações de cores:

    ```toml
    # .streamlit/config.toml
    [theme]
    primaryColor="#3A0BE6"
    backgroundColor="#FFFFFF"
    secondaryBackgroundColor="#DEE0E4"
    textColor="#040610"
    # font="sans serif" # Opcional: descomente e mude se quiser uma fonte específica
    ```

6.  **Execute o aplicativo Streamlit:**

    ```bash
    streamlit run app.py
    ```

    Isso abrirá o aplicativo no seu navegador padrão.

---

## 🤝 Como Colaborar

Contribuições são **muito bem-vindas**! Se você tem ideias para melhorar o chatbot, adicionar funcionalidades, refatorar o código ou corrigir bugs:

1.  **Abra uma Issue:** Explique o problema ou sugestão.
2.  **Faça um Pull Request:**
    * Faça um fork deste repositório.
    * Crie uma nova branch:
        ```bash
        git checkout -b sua-nova-feature
        ```
    * Realize suas alterações, faça commits claros e organize seu código.
    * Envie suas alterações para o seu fork:
        ```bash
        git push origin sua-nova-feature
        ```
    * Abra um Pull Request explicando suas mudanças e o problema que ele resolve ou a funcionalidade que adiciona.

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

**#Python #Chatbot #Pandas #Streamlit #PNL #AnáliseDeDados #DataScience #AssistenteConversacional #OpenSource**
