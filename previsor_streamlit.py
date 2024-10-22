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
st.set_page_config(page_title="Previsor de Reconhecimento Federal de Desastres", page_icon="🚨", layout="wide")

# Carregar o modelo preditivo
modelo_dict = carregar_modelo()

# Obter o modelo e a lista de features do dicionário
if modelo_dict is not None:
    best_model = modelo_dict['model']
    colunas_modelo = modelo_dict['features']
else:
    best_model = None
    colunas_modelo = []

# Seção explicativa
st.header("Previsor de Reconhecimento Federal de Desastres")
st.markdown(
    """
    Este aplicativo permite prever se um desastre declarado por um município será **reconhecido federalmente** como Situação de Emergência ou Estado de Calamidade Pública.

    **Preencha as informações abaixo para obter uma previsão.**
    """
)

# Seção de entrada de dados
st.subheader("Informações sobre o desastre e o município")

# Danos Humanos
st.markdown("#### Danos Humanos")
col1, col2, col3 = st.columns(3)

with col1:
    dh_outros_afetados = st.number_input('Outros Afetados', min_value=0, step=1)
    dh_feridos_enfermos = st.number_input('Feridos e Enfermos Totais', min_value=0, step=1)
    dh_desabrigados_desalojados = st.number_input('Desabrigados e Desalojados Totais', min_value=0, step=1)

# Danos Materiais
st.markdown("#### Danos Materiais")
col4, col5 = st.columns(2)

with col4:
    dm_uni_habita_danificadas_destruidas = st.number_input('Unidades Habitacionais Danificadas e Destruídas', min_value=0, step=1)
    dm_uni_habita_valor = st.number_input('Valor das Unidades Habitacionais (R$)', min_value=0, step=1000)
    dm_inst_saude_danificadas_destruidas = st.number_input('Instalações de Saúde Danificadas e Destruídas', min_value=0, step=1)
    dm_inst_saude_valor = st.number_input('Valor das Instalações de Saúde (R$)', min_value=0, step=1000)
    dm_inst_ensino_danificadas_destruidas = st.number_input('Instalações de Ensino Danificadas e Destruídas', min_value=0, step=1)
    dm_inst_ensino_valor = st.number_input('Valor das Instalações de Ensino (R$)', min_value=0, step=1000)

with col5:
    dm_inst_servicos_danificadas_destruidas = st.number_input('Instalações de Serviços Danificadas e Destruídas', min_value=0, step=1)
    dm_inst_servicos_valor = st.number_input('Valor das Instalações de Serviços (R$)', min_value=0, step=1000)
    dm_inst_comuni_danificadas_destruidas = st.number_input('Instalações de Comunicação Danificadas e Destruídas', min_value=0, step=1)
    dm_inst_comuni_valor = st.number_input('Valor das Instalações de Comunicação (R$)', min_value=0, step=1000)
    dm_obras_infra_danificadas_destruidas = st.number_input('Obras de Infraestrutura Danificadas e Destruídas', min_value=0, step=1)
    dm_obras_infra_valor = st.number_input('Valor das Obras de Infraestrutura (R$)', min_value=0, step=1000)

# Prejuízos Públicos
st.markdown("#### Prejuízos Públicos (R$)")
col6, col7 = st.columns(2)

with col6:
    pepl_assis_med_emerg = st.number_input('Assistência Médica e Emergencial', min_value=0, step=1000)
    pepl_abast_agua_pot = st.number_input('Abastecimento de Água Potável', min_value=0, step=1000)
    pepl_sist_esgotos_sanit = st.number_input('Sistemas de Esgotos Sanitários', min_value=0, step=1000)
    pepl_sis_limp_rec_lixo = st.number_input('Sistemas de Limpeza e Reciclagem de Lixo', min_value=0, step=1000)
    pepl_sis_cont_pragas = st.number_input('Sistemas de Controle de Pragas', min_value=0, step=1000)
    pepl_distrib_energia = st.number_input('Distribuição de Energia', min_value=0, step=1000)

with col7:
    pepl_telecomunicacoes = st.number_input('Telecomunicações', min_value=0, step=1000)
    pepl_tran_loc_reg_curso = st.number_input('Transporte Local/Regional/Longo Curso', min_value=0, step=1000)
    pepl_distrib_combustiveis = st.number_input('Distribuição de Combustíveis', min_value=0, step=1000)
    pepl_seguranca_publica = st.number_input('Segurança Pública', min_value=0, step=1000)
    pepl_ensino = st.number_input('Ensino', min_value=0, step=1000)

# Prejuízos Privados
st.markdown("#### Prejuízos Privados (R$)")
col8, col9 = st.columns(2)

with col8:
    pepr_agricultura = st.number_input('Agricultura', min_value=0, step=1000)
    pepr_pecuaria = st.number_input('Pecuária', min_value=0, step=1000)
    pepr_industria = st.number_input('Indústria', min_value=0, step=1000)

with col9:
    pepr_comercio = st.number_input('Comércio', min_value=0, step=1000)
    pepr_servicos = st.number_input('Serviços', min_value=0, step=1000)

# Dados do Município
st.markdown("### Dados do Município")
col10, col11 = st.columns(2)

with col10:
    densidade_pop = st.number_input('Densidade Populacional (hab/km²)', min_value=0.0)
    domicilio_area_rural = st.number_input('Número de Domicílios na Área Rural', min_value=0, step=1)
    qtde_familias_atualizadas = st.number_input('Quantidade de Famílias Atualizadas', min_value=0, step=1)

with col11:
    pdefagua = st.number_input('Deficiência de Abastecimento de Água (%)', min_value=0.0, max_value=100.0)
    pdefesgoto = st.number_input('Deficiência de Esgotamento Sanitário (%)', min_value=0.0, max_value=100.0)
    pdeflixo = st.number_input('Deficiência de Coleta de Lixo (%)', min_value=0.0, max_value=100.0)
    pdefsan = st.number_input('Deficiência de Saneamento (%)', min_value=0.0, max_value=100.0)

# Seleção de Região e COBRADE
st.markdown("#### Região e Classificação do Desastre")
regiao = st.selectbox('Estado', ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT', 'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO'])
cobrade_tipo = st.selectbox('Tipo de Desastre (COBRADE)', [
    '11110 - Terremoto - Tremor de terra',
    '11120 - Terremoto - Tsunami',
    '11311 - Movimento de massa - Quedas - Blocos',
    '11312 - Movimento de massa - Quedas - Lascas',
    '11313 - Movimento de massa - Quedas - Matacões',
    '11321 - Movimento de massa - Deslizamentos',
    '11331 - Corridas de Massa - Solo/Lama',
    '11332 - Corridas de Massa - Rocha/Detrito',
    '11340 - Subsidências e colapsos',
    '11410 - Erosão Costeira/Marinha',
    '11420 - Erosão de Margem Fluvial',
    '11431 - Erosão Continental - Laminar',
    '11432 - Erosão Continental - Ravinas',
    '11433 - Erosão Continental - Boçorocas',
    '12100 - Inundações',
    '12200 - Enxurradas',
    '12300 - Alagamentos',
    '13111 - Ciclones - Ventos Costeiros',
    '13112 - Ciclones - Marés de Tempestade',
    '13120 - Frentes Frias/Zonas de Convergência',
    '13211 - Tornados',
    '13212 - Tempestade de Raios',
    '13213 - Granizo',
    '13214 - Chuvas Intensas',
    '13215 - Vendaval',
    '13310 - Onda de Calor',
    '13321 - Onda de Frio - Friagem',
    '13322 - Onda de Frio - Geadas',
    '14110 - Estiagem',
    '14120 - Seca',
    '14131 - Incêndios em Áreas Protegidas',
    '14132 - Incêndios em Áreas Não Protegidas',
    '14140 - Baixa Umidade do Ar',
    '15110 - Doenças infecciosas virais',
    '15120 - Doenças infecciosas bacterianas',
    '15130 - Doenças infecciosas parasíticas',
    '15210 - Infestações de animais',
    '15230 - Outras Infestações',
    '22210 - Contaminação da água - Produtos químicos',
    '22220 - Derramamento de produtos químicos',
    '23120 - Incêndios em aglomerados residenciais',
    '24100 - Colapso de edificações',
    '24200 - Rompimento/colapso de barragens',
    '25100 - Transporte rodoviário',
    '25500 - Transporte aquaviário'
])

# Extrair o código COBRADE
if cobrade_tipo:
    cobrade = cobrade_tipo.split(' - ')[0]
else:
    st.error("Por favor, selecione um tipo de desastre válido.")

# Preparar os dados para o modelo
dados = {
    'DH_OUTROS AFETADOS': [dh_outros_afetados],
    'DH_FERIDOS_ENFERMOS': [dh_feridos_enfermos],
    'DH_DESABRIGADOS_DESALOJADOS': [dh_desabrigados_desalojados],
    'DM_Uni_Habita_Danificadas_Destruidas': [dm_uni_habita_danificadas_destruidas],
    'DM_Uni_Habita_Valor': [dm_uni_habita_valor],
    'DM_Inst_Saude_Danificadas_Destruidas': [dm_inst_saude_danificadas_destruidas],
    'DM_Inst_Saude_Valor': [dm_inst_saude_valor],
    'DM_Inst_Ensino_Danificadas_Destruidas': [dm_inst_ensino_danificadas_destruidas],
    'DM_Inst_Ensino_Valor': [dm_inst_ensino_valor],
    'DM_Inst_Servicos_Danificadas_Destruidas': [dm_inst_servicos_danificadas_destruidas],
    'DM_Inst_Servicos_Valor': [dm_inst_servicos_valor],
    'DM_Inst_Comuni_Danificadas_Destruidas': [dm_inst_comuni_danificadas_destruidas],
    'DM_Inst_Comuni_Valor': [dm_inst_comuni_valor],
    'DM_Obras_Infra_Danificadas_Destruidas': [dm_obras_infra_danificadas_destruidas],
    'DM_Obras_Infra_Valor': [dm_obras_infra_valor],
    'PEPL_Assis_méd e emergên(R$)': [pepl_assis_med_emerg],
    'PEPL_Abast de água pot(R$)': [pepl_abast_agua_pot],
    'PEPL_sist de esgotos sanit(R$)': [pepl_sist_esgotos_sanit],
    'PEPL_Sis limp e rec lixo (R$)': [pepl_sis_limp_rec_lixo],
    'PEPL_Sis cont pragas (R$)': [pepl_sis_cont_pragas],
    'PEPL_distrib energia (R$)': [pepl_distrib_energia],
    'PEPL_Telecomunicações (R$)': [pepl_telecomunicacoes],
    'PEPL_Tran loc/reg/l_curso (R$)': [pepl_tran_loc_reg_curso],
    'PEPL_Distrib combustíveis(R$)': [pepl_distrib_combustiveis],
    'PEPL_Segurança pública (R$)': [pepl_seguranca_publica],
    'PEPL_Ensino (R$)': [pepl_ensino],
    'PEPR_Agricultura (R$)': [pepr_agricultura],
    'PEPR_Pecuária (R$)': [pepr_pecuaria],
    'PEPR_Indústria (R$)': [pepr_industria],
    'PEPR_Comércio (R$)': [pepr_comercio],
    'PEPR_Serviços (R$)': [pepr_servicos],
    'DensidadePop': [densidade_pop],
    'DOMICILIO_AREARURAL': [domicilio_area_rural],
    'PDEFAGUA': [pdefagua],
    'PDEFESGOTO': [pdefesgoto],
    'PDEFLIXO': [pdeflixo],
    'PDEFSAN': [pdefsan],
    'QTDE_FAMILIAS_ATUALIZADAS': [qtde_familias_atualizadas],
    f'Sigla_UF_{regiao}': [1],
    f'COBRADE_{cobrade}': [1]
}

# Criar DataFrame
df_dados = pd.DataFrame(dados)

# Preencher colunas faltantes com 0
for coluna in colunas_modelo:
    if coluna not in df_dados.columns:
        df_dados[coluna] = 0

df_dados = df_dados[colunas_modelo]

# Exibir os dados de entrada
st.markdown("### Dados de Entrada:")
st.dataframe(df_dados)

# Prever com base nos dados fornecidos
if st.button('Prever'):
    if best_model is not None:
        try:
            predicao = best_model.predict(df_dados)
            if predicao == 0:
                resultado = 'Reconhecido'
                st.success(f'🟢 **A previsão para o desastre declarado é: {resultado}**')
            else:
                resultado = 'Não Reconhecido'
                st.error(f'🔴 **A previsão para o desastre declarado é: {resultado}**')
        except ValueError as e:
            st.error(f"Erro ao prever: {str(e)}")
    else:
        st.error('Não foi possível carregar o modelo. Verifique a conexão ou o link.')
