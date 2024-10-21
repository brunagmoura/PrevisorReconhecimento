import streamlit as st
import pandas as pd
import joblib
import requests
from io import BytesIO

# Função para carregar o modelo do Hugging Face
@st.cache_resource
def carregar_modelo():
    url = "https://huggingface.co/brunagmoura/previsor-reconhecimento/resolve/main/previsor_desastres.pkl"
    response = requests.get(url)
    if response.status_code == 200:
        modelo = joblib.load(BytesIO(response.content))
        return modelo
    else:
        st.error('Erro ao carregar o modelo do Hugging Face.')
        return None

# Carregar o modelo preditivo
modelo = carregar_modelo()

# Obter o melhor estimador do modelo BayesSearchCV
if modelo is not None:
    best_model = modelo.best_estimator_
    # Obter a lista de features
    colunas_modelo = best_model.feature_names_in_.tolist()
else:
    colunas_modelo = []

# Interface do Streamlit
st.title('Previsão de Reconhecimento Federal de Desastres')

st.markdown("""
Este aplicativo permite prever se um desastre declarado por um município será reconhecido federalmente como Situação de Emergência ou Estado de Calamidade Pública.
Insira as informações abaixo para obter uma previsão.
""")

# Campos para os dados de entrada
dh_total_danos_humanos = st.number_input('Danos Humanos Totais', min_value=0, step=1)
dm_total_danos_materiais = st.number_input('Danos Materiais Totais', min_value=0, step=1)
pepl_total_publico = st.number_input('Prejuízos Públicos Totais', min_value=0, step=1)
pepr_total_privado = st.number_input('Prejuízos Privados Totais', min_value=0, step=1)
domicilio_arearural = st.number_input('Domicílios na Área Rural', min_value=0, step=1)
pdefagua = st.number_input('Pessoas sem Água Adequada (%)', min_value=0.0)
pdefesgoto = st.number_input('Pessoas sem Esgoto Adequado (%)', min_value=0.0)
pdeflixo = st.number_input('Pessoas sem Coleta de Lixo Adequada (%)', min_value=0.0)
pdefsan = st.number_input('Pessoas sem Saneamento Básico (%)', min_value=0.0)
qtde_familias_atualizadas = st.number_input('Quantidade de Famílias no Cadastro Único', min_value=0, step=1)

# Seleção de Região e COBRADE
regiao = st.selectbox('Região', ['Centro-oeste', 'Nordeste', 'Norte', 'Sudeste', 'Sul'])
cobrade = st.selectbox('COBRADE', [
    '11110', '11120', '11311', '11312', '11313', '11321', '11331', '11332',
    '11340', '11410', '11420', '11431', '11432', '11433', '12100', '12200',
    '12300', '13111', '13112', '13120', '13211', '13212', '13213', '13214',
    '13215', '13310', '13321', '13322', '14110', '14120', '14131', '14132',
    '14140', '15110', '15120', '15130', '15210', '15230', '22210', '22220',
    '23120', '24100', '24200', '25100', '25500'
])

# Converter as variáveis categóricas em dummies
dados = {
    'DH_total_danos_humanos': [dh_total_danos_humanos],
    'DM_total_danos_materiais': [dm_total_danos_materiais],
    'PEPL_total_publico': [pepl_total_publico],
    'PEPR_total_privado': [pepr_total_privado],
    'DOMICILIO_AREARURAL': [domicilio_arearural],
    'PDEFAGUA': [pdefagua],
    'PDEFESGOTO': [pdefesgoto],
    'PDEFLIXO': [pdeflixo],
    'PDEFSAN': [pdefsan],
    'QTDE_FAMILIAS_ATUALIZADAS': [qtde_familias_atualizadas],
    f'regiao_{regiao}': [1],
    f'COBRADE_{cobrade}': [1]
}

# Criar um DataFrame e preencher as colunas faltantes com 0
df_dados = pd.DataFrame(dados)

# Preencher colunas faltantes e garantir a ordem correta
for coluna in colunas_modelo:
    if coluna not in df_dados.columns:
        df_dados[coluna] = 0

df_dados = df_dados[colunas_modelo]

# Prever com base nos dados fornecidos
if st.button('Prever'):
    if modelo is not None:
        try:
            predicao = modelo.predict(df_dados)
            resultado = 'Reconhecido' if predicao == 1 else 'Não reconhecido'
            st.success(f'A previsão para o desastre declarado é: {resultado}')
        except ValueError as e:
            st.error(f"Erro ao prever: {str(e)}")
    else:
        st.error('Não foi possível carregar o modelo. Verifique a conexão ou o link.')
