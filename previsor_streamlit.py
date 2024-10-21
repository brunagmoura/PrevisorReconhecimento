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

# Configurações de estilo
st.set_page_config(page_title="Previsor de Reconhecimento Federal de Desastres", page_icon="🚨", layout="centered")

# Carregar o modelo preditivo
modelo = carregar_modelo()

# Obter o melhor estimador do modelo BayesSearchCV
if modelo is not None:
    best_model = modelo.best_estimator_
    # Obter a lista de features
    colunas_modelo = best_model.feature_names_in_.tolist()
else:
    colunas_modelo = []

# Seção explicativa
st.header("Sobre o Projeto")
st.markdown(
    """
    O reconhecimento federal de Situação de Emergência ou Estado de Calamidade Pública permite ao município acessar recursos federais para resposta e reconstrução. 
    Este aplicativo permite prever se um desastre declarado por um município será reconhecido federalmente como Situação de Emergência ou Estado de Calamidade Pública.
    Insira as informações abaixo para obter uma previsão.
    """
)

# Seção de entrada de dados
st.header("Informações sobre o desastre e o município")

st.subheader("Danos e prejuízos registrados")

col1, col2 = st.columns(2)

with col1:
    dh_feridos = st.number_input('Feridos Totais', min_value=0, step=1)
    dh_enfermos = st.number_input('Enfermos Totais', min_value=0, step=1)
    dm_inst_saude_danificadas = st.number_input('Instalações de Saúde Danificadas', min_value=0, step=1)
    dm_inst_saude_destruidas = st.number_input('Instalações de Saúde Destruídas', min_value=0, step=1)
    dm_uni_habita_danificadas = st.number_input('Unidades Habitacionais Danificadas', min_value=0, step=1)
    dm_uni_habita_destruidas = st.number_input('Unidades Habitacionais Destruídas', min_value=0, step=1)

with col2:
    dm_inst_ensino_danificadas = st.number_input('Instalações de Ensino Danificadas', min_value=0, step=1)
    dm_inst_ensino_destruidas = st.number_input('Instalações de Ensino Destruídas', min_value=0, step=1)
    dm_obras_infra_danificadas = st.number_input('Obras de Infraestrutura Danificadas', min_value=0, step=1)
    dm_obras_infra_destruidas = st.number_input('Obras de Infraestrutura Destruídas', min_value=0, step=1)
    pepr_comercio = st.number_input('Prejuízos no Comércio (R$)', min_value=0, step=1)
    pepr_agricultura = st.number_input('Prejuízos na Agricultura (R$)', min_value=0, step=1)

# Seleção de Região e COBRADE

st.subheader("Região e classificação do desastre")
regiao = st.selectbox('Região', ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'])
cobrade_tipo = st.selectbox('Tipo de Desastre (COBRADE)', [
    'Geológico - Terremoto - Tremor de terra (11110)',
    'Geológico - Terremoto - Tsunami (11120)',
    'Geológico - Movimento de massa - Quedas, Tombamentos e rolamentos - Blocos (11311)',
    'Geológico - Movimento de massa - Quedas, Tombamentos e rolamentos - Lascas (11312)',
    'Geológico - Movimento de massa - Quedas, Tombamentos e rolamentos - Matacões (11313)',
    'Geológico - Movimento de massa - Quedas, Tombamentos e rolamentos - Lajes (11314)',
    'Geológico - Movimento de massa - Deslizamentos - Deslizamentos de solo e ou rocha (11321)',
    'Geológico - Movimento de massa - Corridas de Massa - Solo/Lama (11331)',
    'Geológico - Movimento de massa - Corridas de Massa - Rocha/Detrito (11332)',
    'Geológico - Movimento de massa - Subsidências e colapsos (11340)',
    'Geológico - Erosão - Erosão Costeira/Marinha (11410)',
    'Geológico - Erosão - Erosão de Margem Fluvial (11420)',
    'Geológico - Erosão - Erosão Continental - Laminar (11431)',
    'Geológico - Erosão - Erosão Continental - Ravinas (11432)',
    'Geológico - Erosão - Erosão Continental - Boçorocas (11433)',
    'Hidrológico - Inundações (12100)',
    'Hidrológico - Enxurradas (12200)',
    'Hidrológico - Alagamentos (12300)',
    'Meteorológico - Sistemas de Grande Escala/Escala Regional - Ciclones - Ventos Costeiros (Mobilidade de Dunas) (13111)',
    'Meteorológico - Sistemas de Grande Escala/Escala Regional - Ciclones - Marés de Tempestade (Ressacas) (13112)',
    'Meteorológico - Sistemas de Grande Escala/Escala Regional - Frentes Frias/Zonas de Convergência (13120)',
    'Meteorológico - Tempestades - Tempestade Local/Convectiva - Tornados (13211)',
    'Meteorológico - Tempestades - Tempestade Local/Convectiva - Tempestade de Raios (13212)',
    'Meteorológico - Tempestades - Tempestade Local/Convectiva - Granizo (13213)',
    'Meteorológico - Tempestades - Tempestade Local/Convectiva - Chuvas Intensas (13214)',
    'Meteorológico - Tempestades - Tempestade Local/Convectiva - Vendaval (13215)',
    'Meteorológico - Temperaturas Extremas - Onda de Calor (13310)',
    'Meteorológico - Temperaturas Extremas - Onda de Frio - Friagem (13321)',
    'Meteorológico - Temperaturas Extremas - Onda de Frio - Geadas (13322)',
    'Climatológico - Seca - Estiagem (14110)',
    'Climatológico - Seca - Seca (14120)',
    'Climatológico - Seca - Incêndio Florestal - Incêndios em Parques, Áreas de Proteção Ambiental e Áreas de Preservação Permanente (14131)',
    'Climatológico - Seca - Incêndio Florestal - Incêndios em áreas não protegidas, com reflexos na qualidade do ar (14132)',
    'Climatológico - Seca - Baixa Umidade do Ar (14140)',
    'Biológico - Epidemias - Doenças infecciosas virais (15110)',
    'Biológico - Epidemias - Doenças infecciosas bacterianas (15120)',
    'Biológico - Epidemias - Doenças infecciosas parasíticas (15130)',
    'Biológico - Epidemias - Doenças infecciosas fúngicas (15140)',
    'Biológico - Infestações/Pragas - Infestações de animais (15210)',
    'Biológico - Infestações/Pragas - Outras Infestações (15230)',
    'Produtos Perigosos - Desastres relacionados à contaminação da água - Liberação de produtos químicos nos sistemas de água potável (22210)',
    'Produtos Perigosos - Desastres relacionados à contaminação da água - Derramamento de produtos químicos em ambiente lacustre, fluvial, marinho e aquíferos (22220)',
    'Produtos Perigosos - Incêndios Urbanos - Incêndios em aglomerados residenciais (23120)',
    'Obras Civis - Colapso de edificações (24100)',
    'Obras Civis - Rompimento/colapso de barragens (24200)',
    'Transporte de Passageiros e Cargas - Transporte rodoviário (25100)',
    'Transporte de Passageiros e Cargas - Transporte aquaviário (25500)'
])

# Verificar se o usuário selecionou algo
if cobrade_tipo:
    cobrade = cobrade_tipo.split('(')[-1][:-1]
else:
    st.error("Por favor, selecione um tipo de desastre válido.")

# Converter as variáveis categóricas em dummies
dados = {
    'DH_FERIDOS': [dh_feridos],
    'DH_ENFERMOS': [dh_enfermos],
    'DM_Inst Saúde Danificadas': [dm_inst_saude_danificadas],
    'DM_Inst Saúde Destruidas': [dm_inst_saude_destruidas],
    'DM_Inst Ensino Danificadas': [dm_inst_ensino_danificadas],
    'DM_Inst Ensino Destruidas': [dm_inst_ensino_destruidas],
    'DM_Uni Habita Danificadas': [dm_uni_habita_danificadas],
    'DM_Uni Habita Destruidas': [dm_uni_habita_destruidas],
    'DM_Obras de Infra Danificadas': [dm_obras_infra_danificadas],
    'DM_Obras de Infra Destruidas': [dm_obras_infra_destruidas],
    'PEPR_Comércio (R$)': [pepr_comercio],
    'PEPR_Agricultura (R$)': [pepr_agricultura],
    f'Sigla_UF_{regiao}': [1],
    f'COBRADE_{cobrade}': [1] if cobrade_tipo else [0]
}

# Criar DataFrame
df_dados = pd.DataFrame(dados)

# Preencher colunas faltantes com 0
for coluna in colunas_modelo:
    if coluna not in df_dados.columns:
        df_dados[coluna] = 0

df_dados = df_dados[colunas_modelo]

st.write("Entrada do modelo:")
st.write(df_dados)

# Prever com base nos dados fornecidos
if st.button('Prever'):
    if modelo is not None:
        try:
            predicao = modelo.predict(df_dados)
            if predicao == 1:
                resultado = 'Reconhecido'
                st.success(f'A previsão para o desastre declarado é: {resultado}')
            else:
                resultado = 'Não reconhecido'
                st.error(f'A previsão para o desastre declarado é: {resultado}')
        except ValueError as e:
            st.error(f"Erro ao prever: {str(e)}")
    else:
        st.error('Não foi possível carregar o modelo. Verifique a conexão ou o link.')
