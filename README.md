# 🤖 Chatbot de Análise de Vendas Simples

Este projeto apresenta um chatbot básico em **Python** projetado para demonstrar como integrar funcionalidades de **Processamento de Linguagem Natural (PNL)** e **análise de dados** para gerar insights a partir de conversas.

É um excelente ponto de partida para desenvolvedores juniores que desejam entender os princípios por trás da construção de **assistentes conversacionais que interagem com dados**.

---

## 🚀 Funcionalidades

O chatbot simula uma interação com dados de vendas, aplicando os seguintes princípios:

- **Entendimento da Intenção:** Reconhece que o usuário deseja informações sobre "vendas".
- **Extração de Entidades:** Identifica o "produto" específico sobre o qual o usuário está perguntando.
- **Acesso e Processamento de Dados:** Utiliza dados simulados para filtrar e calcular totais e médias.
- **Geração de Insights Claras:** Apresenta os resultados da análise de forma compreensível e conversacional.
- **Interatividade:** Mantém um fluxo de diálogo simples, pedindo esclarecimentos quando necessário.

---

## 🛠️ Tecnologias Utilizadas

Este projeto foi desenvolvido com as seguintes ferramentas e bibliotecas:

- **Python (Core):** Para lógica de programação e interação com o usuário.
- **Pandas:** Para manipulação de dados, estruturação em DataFrames, filtragem, soma e média de forma eficiente.

---

## 🏗️ Como Foi Construído

A estrutura do chatbot é **modular** e **didática**, composta por:

- **Dados de Exemplo (`df_vendas`):** Um `DataFrame` criado com Pandas contendo colunas como Produto, Vendas e Região.
- **Função de Análise (`analisar_vendas_produto`):** Recebe o nome do produto, filtra os dados e retorna vendas totais e médias.
- **Lógica do Chatbot (`chatbot_resposta`):** Recebe perguntas, identifica intenção e entidade, chama a função de análise e gera resposta.
- **Loop de Interação:** Um `while True` permite que o usuário interaja em tempo real, com opção de encerrar com "sair".

Esse design facilita a compreensão de como **PNL básica, análise de dados e lógica conversacional** se integram.

---

## ⚙️ Como Rodar o Projeto

Siga os passos abaixo para executar o chatbot:

1. **Clone o repositório:**

```bash
git clone https://github.com/Dayanebiaerafa/Chatbot-Analise-de-Vendas.git
```

2. **Navegue até o diretório do projeto:**

```bash
cd Chatbot-Analise-de-Vendas
```

3. **Instale as dependências:**

Se ainda não tiver o `pandas` instalado, execute:

```bash
pip install pandas
```

4. **Execute o chatbot:**

```bash
python seu_arquivo_chatbot.py
```

(Substitua `seu_arquivo_chatbot.py` pelo nome do arquivo Python onde você salvou o código do chatbot.)

O chatbot iniciará no terminal, pronto para responder às suas perguntas!

---

## 🤝 Como Colaborar

Contribuições são **muito bem-vindas**! Se você tem ideias para melhorar o chatbot, adicionar funcionalidades, refatorar o código ou corrigir bugs:

1. **Abra uma Issue:** Explique o problema ou sugestão.
2. **Faça um Pull Request:**
   - Faça um fork deste repositório
   - Crie uma nova branch:
     ```bash
     git checkout -b sua-nova-feature
     ```
   - Realize suas alterações:
     ```bash
     git commit -m "Adiciona nova feature"
     git push origin sua-nova-feature
     ```
   - Abra um Pull Request explicando suas mudanças.

Vamos construir algo ainda melhor juntos! 💡

---
<p>
    <img 
      align=left 
      margin=10 
      width=80 
      src="![WhatsApp Image 2023-01-31 at 10 52 47 (1)](https://github.com/user-attachments/assets/430109f9-1127-4cf3-a823-c29d32ecea76)"
    />
    <p>&nbsp&nbsp&nbspDayane Teodoro<br>
    &nbsp&nbsp&nbsp
    <a href="https://github.com/Dayanebiaerafa">
    GitHub</a>&nbsp;|&nbsp;
    <a href="https://www.linkedin.com/in/dayaneteodoro/
felipe-exe">LinkedIn</a>
&nbsp;|&nbsp;
    <a href="https://www.instagram.com/dayane_cie/">
    Instagram</a>
&nbsp;|&nbsp;</p>
</p>
<br/><br/>
<p>
💞 Feito com amor por Dayane Teodoro⁉ 

**#Python #Chatbot #Pandas #PNL #AnáliseDeDados #DataScience #AssistenteConversacional #OpenSource #AprendizadoDeMáquina**
