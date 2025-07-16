import pandas as pd
import streamlit as st
import calendar
import re # Importar a biblioteca de expressões regulares

# --- 1. Preparando os Dados (com Pandas) ---
@st.cache_data
def carregar_dados():
    dados_vendas = {
        'Produto': [
            'Camiseta', 'Calça', 'Boné', 'Camiseta', 'Calça', 'Boné',
            'Camiseta', 'Calça', 'Boné', 'Camiseta', 'Calça', 'Boné',
            'Camiseta', 'Calça', 'Boné', 'Camiseta', 'Calça', 'Boné',
            'Camiseta', 'Calça', 'Boné', 'Camiseta', 'Calça', 'Boné',
            'Camiseta', 'Calça', 'Boné', 'Camiseta', 'Calça', 'Boné',
            'Camiseta', 'Calça', 'Boné', 'Camiseta', 'Calça', 'Boné',
            'Camiseta', 'Calça', 'Boné', 'Camiseta', 'Calça', 'Boné',
            # 42 elementos
        ], 
        'Quantidade': [
            10, 5, 3, 12, 7, 6,
            8, 4, 11, 9, 10, 5,
            7, 9, 4, 6, 8, 10,
            11, 5, 7, 9, 6, 12,
            4, 8, 10, 5, 7, 9,
            12, 6, 8, 10, 5, 11,
            7, 9, 4, 6, 8, 10,
             # 42 elementos
        ], 
        'Valor Unitario': [
            100.50, 150.25, 50.00, 100.75, 150.00, 50.50,
            100.00, 150.80, 50.20, 100.10, 150.40, 50.60,
            100.90, 150.30, 50.70, 100.05, 150.15, 50.35,
            100.45, 150.65, 50.85, 100.20, 150.70, 50.95,
            100.30, 150.55, 50.10, 100.80, 150.90, 50.25,
            100.60, 150.00, 50.40, 100.70, 150.10, 50.30,
            100.95, 150.05, 50.15, 100.25, 150.35, 50.45,
            # 42 elementos
        ], 
        'Regiao': [
            'Norte', 'Sul', 'Leste', 'Oeste', 'Norte', 'Sul',
            'Leste', 'Oeste', 'Norte', 'Sul', 'Leste', 'Oeste',
            'Norte', 'Sul', 'Leste', 'Oeste', 'Norte', 'Sul',
            'Leste', 'Oeste', 'Norte', 'Sul', 'Leste', 'Oeste',
            'Norte', 'Sul', 'Leste', 'Oeste', 'Norte', 'Sul',
            'Leste', 'Oeste', 'Norte', 'Sul', 'Leste', 'Oeste',
            'Norte', 'Sul', 'Leste', 'Oeste', 'Norte', 'Sul'
            # 42 elementos
        ], 
        'Data Compra': [
            '01/01/2023', '05/01/2023', '10/01/2023', '15/02/2023', '20/02/2023', '25/02/2023',
            '01/03/2023', '07/03/2023', '14/03/2023', '20/04/2023', '25/04/2023', '30/04/2023',
            '05/05/2023', '10/05/2023', '15/05/2023', '20/06/2023', '25/06/2023', '30/06/2023',
            '01/07/2023', '08/07/2023', '16/07/2023', '24/08/2023', '01/09/2023', '09/09/2023',
            '17/09/2023', '25/10/2023', '02/11/2023', '10/11/2023', '18/11/2023', '26/12/2023',
            '04/01/2024', '12/01/2024', '20/01/2024', '28/02/2024', '05/03/2024', '13/03/2024',
            '21/04/2022', '29/04/2022', '07/05/2022', '15/05/2024', '23/06/2024', '15/03/2024' # 42 elementos
        ] 
    }

    print("\n--- Conteúdo e Comprimento das Listas em dados_vendas ---")
    for chave, lista in dados_vendas.items():
        print(f"{chave}: {len(lista)} elementos")
    print("------------------------------------------------------\n")

    df = pd.DataFrame(dados_vendas)

    df['Data Compra'] = pd.to_datetime(df['Data Compra'], format='%d/%m/%Y')
    df['Total Venda'] = df['Quantidade'] * df['Valor Unitario']

    df['Ano'] = df['Data Compra'].dt.year
    df['Mes_Num'] = df['Data Compra'].dt.month
    df['Mes'] = df['Mes_Num'].apply(lambda x: calendar.month_name[x].capitalize())
    
    df = df.sort_values(by=['Data Compra', 'Regiao', 'Produto']).reset_index(drop=True)
    return df

def formatar_moeda_br(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

df_vendas = carregar_dados()

# Mapeamento para nomes de meses em português (global para fácil acesso)
MESES_EN_PARA_PT = {
    'January': 'janeiro', 'February': 'fevereiro', 'March': 'março', 'April': 'abril',
    'May': 'maio', 'June': 'junho', 'July': 'julho', 'August': 'agosto',
    'September': 'setembro', 'October': 'outubro', 'November': 'novembro', 'December': 'dezembro'
}

# --- 2. Funções de Análise de Dados ---
def analisar_vendas_produto(produto_nome):
    vendas_do_produto = df_vendas[df_vendas['Produto'].str.lower() == produto_nome.lower()]
    if vendas_do_produto.empty:
        return f"Não encontrei dados para o produto **'{produto_nome}'**. Tem certeza que o nome está correto?"
    else:
        total_vendas = vendas_do_produto['Total Venda'].sum()
        if pd.isna(total_vendas):
            return f"Não foi possível calcular o total de vendas para '{produto_nome}' devido a dados inválidos."
        return f"O total de vendas do produto **'{produto_nome}'** no período registrado é de **{formatar_moeda_br(total_vendas)}**."

def mes_que_mais_vendeu():
    vendas_por_mes = df_vendas.groupby('Mes', observed=True)['Total Venda'].sum().reset_index()

    if vendas_por_mes.empty:
        return "Não há dados de vendas suficientes para determinar o mês que mais vendeu."

    vendas_por_mes_sorted = vendas_por_mes.sort_values(by='Total Venda', ascending=False)
    
    mes_max_en = vendas_por_mes_sorted.iloc[0]['Mes'] 
    mes_max_pt = MESES_EN_PARA_PT.get(mes_max_en, mes_max_en) 
    total_max = vendas_por_mes_sorted.iloc[0]['Total Venda']
    
    return f"O mês que mais vendeu foi **{mes_max_pt.capitalize()}**, com um total de **{formatar_moeda_br(total_max)}**."

def regiao_que_mais_vendeu_produto(produto_nome):
    df_produto = df_vendas[df_vendas['Produto'].str.lower() == produto_nome.lower()]
    if df_produto.empty:
        return f"Não encontrei dados para o produto **'{produto_nome}'**. Tem certeza que o nome está correto?"

    vendas_por_regiao = df_produto.groupby('Regiao')['Total Venda'].sum().reset_index()
    if vendas_por_regiao.empty:
        return f"Não há dados de vendas para o produto **'{produto_nome}'** por região."

    regiao_max = vendas_por_regiao.loc[vendas_por_regiao['Total Venda'].idxmax()]
    return (f"Para o produto **'{produto_nome}'**, a região que mais vendeu foi **{regiao_max['Regiao']}**, "
            f"com um total de **{formatar_moeda_br(regiao_max['Total Venda'])}**.")

def total_vendas_no_ano():
    vendas_por_ano = df_vendas.groupby('Ano')['Total Venda'].sum().reset_index()

    if vendas_por_ano.empty:
        return "Não há dados de vendas suficientes para calcular o total de vendas por ano."

    response = "O total de vendas por ano é:\n\n"
    for index, row in vendas_por_ano.iterrows():
        response += f"- Ano **{int(row['Ano'])}**: **{formatar_moeda_br(row['Total Venda'])}**\n"
    
    return response

def total_vendas_no_mes(nome_mes_input):
    meses_pt_para_en = {
        'janeiro': 'January', 'fevereiro': 'February', 'março': 'March', 'abril': 'April',
        'maio': 'May', 'junho': 'June', 'julho': 'July', 'agosto': 'August',
        'setembro': 'September', 'outubro': 'October', 'novembro': 'November', 'dezembro': 'December'
    }
    
    mes_para_comparar_en = meses_pt_para_en.get(nome_mes_input.lower(), nome_mes_input.capitalize())
    
    vendas_mes = df_vendas[df_vendas['Mes'] == mes_para_comparar_en]
    
    if vendas_mes.empty:
        meses_validos_lower = list(meses_pt_para_en.keys()) + [m.lower() for m in MESES_EN_PARA_PT.keys()]
        if nome_mes_input.lower() not in meses_validos_lower:
            return f"Mês **'{nome_mes_input}'** inválido. Por favor, use um nome de mês válido (ex: 'julho', 'janeiro')."
        else:
            mes_pt_display = MESES_EN_PARA_PT.get(nome_mes_input.capitalize(), nome_mes_input.capitalize())
            return f"Não encontrei dados de vendas para o mês de **{mes_pt_display}** no período registrado."
    
    total_mes = vendas_mes['Total Venda'].sum()
    if pd.isna(total_mes):
        return f"Não foi possível calcular o total de vendas para '{MESES_EN_PARA_PT.get(mes_para_comparar_en, mes_para_comparar_en)}' devido a dados inválidos."
    
    mes_pt_display = MESES_EN_PARA_PT.get(mes_para_comparar_en, mes_para_comparar_en)
    return f"O total de vendas no mês de **{mes_pt_display.capitalize()}** foi de **{formatar_moeda_br(total_mes)}**."


# --- 3. O "Cérebro" do Chatbot (Lógica Aprimorada com Regex) ---
def chatbot_resposta(pergunta_usuario):
    pergunta_usuario_lower = pergunta_usuario.lower()

    # SAUDAÇÕES E DESPEDIDAS - Estas devem ser as primeiras
    if "olá" in pergunta_usuario_lower or "oi" in pergunta_usuario_lower or "bom dia" in pergunta_usuario_lower:
        return ("Olá! Sou seu assistente de vendas. Posso te ajudar com perguntas como:\n"
                "- **Mês que mais vendeu**\n"
                "- **Total de vendas no ano**\n"
                "- **Total de vendas no mês de julho**\n"
                "- **Região que mais vendeu camiseta**\n"
                "- **Vendas da camiseta**")
    elif "sair" in pergunta_usuario_lower or "tchau" in pergunta_usuario_lower or "obrigado" in pergunta_usuario_lower:
        return "Até mais! Se precisar de mais insights, é só chamar."

    # PRIORIZAR: Mês que mais vendeu (ou faturou)
    padroes_mes_mais_vendeu = [
        r"m[eê]s que mais vendeu",
        r"qual (o|é o) m[eê]s (que|que mais) vendeu",
        r"melhor m[eê]s de vendas",
        r"m[eê]s com maior faturamento",
        r"m[eê]s mais faturou"
    ]
    for padrao in padroes_mes_mais_vendeu:
        if re.search(padrao, pergunta_usuario_lower):
            return mes_que_mais_vendeu()

    # PERGUNTAS GERAIS: Total de vendas no ano
    padroes_total_ano = [
        r"total de vendas no ano",
        r"vendas anuais",
        r"quanto vendeu no ano",
        r"faturamento anual",
        r"vendas por ano"
    ]
    for padrao in padroes_total_ano:
        if re.search(padrao, pergunta_usuario_lower):
            return total_vendas_no_ano()

    # PERGUNTAS SOBRE MESES ESPECÍFICOS
    meses_pt_regex = "|".join([
        'janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho',
        'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
    ])
    # Padrão flexível para "total de vendas no mês de [mês]"
    # Inclui variações como "vendas em julho", "quanto vendeu em março"
    match_mes = re.search(rf"(total de vendas no m[eê]s de|vendas no m[eê]s de|vendas em|quanto vendeu em)\s*({meses_pt_regex})\b", pergunta_usuario_lower)
    if match_mes:
        nome_mes = match_mes.group(2) 
        return total_vendas_no_mes(nome_mes)

    # PERGUNTAS SOBRE PRODUTOS E REGIÕES
    produtos_disponiveis = [p.lower() for p in df_vendas['Produto'].unique()]
    produtos_regex = "|".join(re.escape(p) for p in produtos_disponiveis) 

    match_regiao_produto = re.search(rf"(regi[aã]o que mais vendeu|qual regi[aã]o vendeu mais) ({produtos_regex})", pergunta_usuario_lower)
    if match_regiao_produto:
        produto_encontrado = match_regiao_produto.group(2)
        return regiao_que_mais_vendeu_produto(produto_encontrado)

    match_vendas_produto = re.search(rf"(vendas d[ao] |quanto vendeu d[eo] )({produtos_regex})", pergunta_usuario_lower)
    if match_vendas_produto:
        produto_encontrado = match_vendas_produto.group(2)
        return analisar_vendas_produto(produto_encontrado)

    return ("Desculpe, não entendi sua pergunta. Por favor, tente reformular ou use uma das sugestões:\n"
            "- **Mês que mais vendeu**\n"
            "- **Total de vendas no ano**\n"
            "- **Total de vendas no mês de julho** (ou o mês que desejar)\n"
            "- **Região que mais vendeu camiseta**\n"
            "- **Vendas da camiseta**")

# --- 4. Interface Gráfica com Streamlit ---
st.set_page_config(
    page_title="Chatbot de Análise de Vendas",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Chatbot de Análise de Vendas")
st.write("Olá! Sou seu assistente de vendas. Posso te dar insights e visualizações sobre suas vendas.")
st.write("Experimente perguntar no chat:")
st.markdown("""
- **Mês que mais vendeu** (ou "qual mês faturou mais?")
- **Total de vendas no ano** (ou "quanto vendemos no ano?")
- **Total de vendas no mês de julho** (ou qualquer mês, ex: "vendas em agosto")
- **Região que mais vendeu camiseta** (ou "qual região vendeu mais boné?")
- **Vendas da camiseta** (ou "quanto vendemos de calça?")
""")

st.markdown("---")

# Prepara o DataFrame para exibição na tabela, aplicando o alinhamento na coluna 'Quantidade'
if df_vendas.empty:
    st.warning("Nenhum dado de vendas disponível para exibição.")
else:
    st.subheader("Dados de Vendas Detalhados")
    
    # Cria uma cópia para modificação local, sem afetar df_vendas
    df_para_exibir_final = df_vendas.copy()
    
    df_para_exibir_final['Data Compra'] = df_para_exibir_final['Data Compra'].dt.strftime('%d/%m/%Y')
    
    # Excluir as colunas 'Ano', 'Mes_Num' e 'Mes' da exibição
    df_para_exibir_final = df_para_exibir_final.drop(columns=['Ano', 'Mes_Num', 'Mes'], errors='ignore')

    df_para_exibir_final['Valor Unitario'] = df_para_exibir_final['Valor Unitario'].apply(formatar_moeda_br)
    df_para_exibir_final['Total Venda'] = df_para_exibir_final['Total Venda'].apply(formatar_moeda_br)
    
    # ***** IMPORTANTE PARA O ALINHAMENTO *****
    # Converte a coluna 'Quantidade' para string para que possa ser alinhada à esquerda
    df_para_exibir_final['Quantidade'] = df_para_exibir_final['Quantidade'].astype(str)

    st.dataframe(
        df_para_exibir_final,
        column_config={
            "Quantidade": st.column_config.TextColumn( # Usa TextColumn para alinhar à esquerda
                "Quantidade",
                help="Número de itens vendidos",
                width="small",
            )
        },
        use_container_width=True # Opcional: faz a tabela ocupar toda a largura disponível
    )

st.markdown("---")

st.header("Chatbot de Perguntas e Respostas")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_prompt := st.chat_input("Pergunte-me algo sobre vendas..."):
    st.session_state.messages.append({"role": "user", "content": user_prompt})
    with st.chat_message("user"):
        st.markdown(user_prompt)

    response = chatbot_resposta(user_prompt)
    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)