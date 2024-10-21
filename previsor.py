import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
from skopt import BayesSearchCV
from sklearn import metrics
from sklearn.metrics import ConfusionMatrixDisplay

# Carregar o dataset
df_eventos_2018_2024_modelo2 = pd.read_csv(
    "https://raw.githubusercontent.com/brunagmoura/PrevisorReconhecimento/refs/heads/main/df_eventos_2018_2024_modelo2.csv",
    sep=';',
    decimal=',',
)

# Remover linhas com dados ausentes

df_eventos_2018_2024_modelo2 = df_eventos_2018_2024_modelo2.dropna()

# Remover linhas com todos os dados informados = 0.

colunas_informados = [
    'DH_MORTOS', 'DH_FERIDOS', 'DH_ENFERMOS', 'DH_DESABRIGADOS', 'DH_DESALOJADOS',
    'DH_DESAPARECIDOS', 'DH_OUTROS AFETADOS',
    'DM_Uni Habita Danificadas', 'DM_Uni Habita Destruidas', 'DM_Uni Habita Valor',
    'DM_Inst Saúde Danificadas', 'DM_Inst Saúde Destruidas', 'DM_Inst Saúde Valor',
    'DM_Inst Ensino Danificadas', 'DM_Inst Ensino Destruidas', 'DM_Inst Ensino Valor',
    'DM_Inst Serviços Danificadas', 'DM_Inst Serviços Destruidas', 'DM_Inst Serviços Valor',
    'DM_Inst Comuni Danificadas', 'DM_Inst Comuni Destruidas', 'DM_Inst Comuni Valor',
    'DM_Obras de Infra Danificadas', 'DM_Obras de Infra Destruidas', 'DM_Obras de Infra Valor',
    'PEPL_Assis_méd e emergên(R$)', 'PEPL_Abast de água pot(R$)',
    'PEPL_sist de esgotos sanit(R$)', 'PEPL_Sis limp e rec lixo (R$)', 'PEPL_Sis cont pragas (R$)',
    'PEPL_distrib energia (R$)', 'PEPL_Telecomunicações (R$)', 'PEPL_Tran loc/reg/l_curso (R$)',
    'PEPL_Distrib combustíveis(R$)', 'PEPL_Segurança pública (R$)', 'PEPL_Ensino (R$)',
    'PEPR_Agricultura (R$)', 'PEPR_Pecuária (R$)', 'PEPR_Indústria (R$)', 'PEPR_Comércio (R$)',
    'PEPR_Serviços (R$)'
]

df_eventos_2018_2024_modelo2 = df_eventos_2018_2024_modelo2[
    ~(df_eventos_2018_2024_modelo2[colunas_informados] == 0).all(axis=1)
]

# Remover colunas que agrgeam pouco ao modelo
colunas_manter = [ 'Status',
    'DH_FERIDOS', 'DH_ENFERMOS',
    'DM_Inst Saúde Destruidas', 'DM_Inst Saúde Danificadas',
    'DM_Inst Ensino Danificadas', 'DM_Inst Ensino Destruidas',
    'DM_Uni Habita Danificadas', 'DM_Uni Habita Destruidas',
    'DM_Obras de Infra Danificadas', 'DM_Obras de Infra Destruidas',
    'PEPR_Comércio (R$)', 'PEPR_Agricultura (R$)',
    'PEPL_Sis cont pragas (R$)', 'PEPL_Segurança pública (R$)',
    'PEPL_sist de esgotos sanit(R$)', 'PEPL_Tran loc/reg/l_curso (R$)'
]

# Selecionar colunas que começam por 'COBRADE' ou 'Sigla_UF' e adicionar à lista de colunas a manter
colunas_manter.extend([col for col in df_eventos_2018_2024_modelo2.columns if col.startswith('COBRADE') or col.startswith('Sigla_UF')])

# Manter apenas as colunas desejadas no dataset original
df_eventos_2018_2024_modelo2 = df_eventos_2018_2024_modelo2[colunas_manter]

# Separar variáveis independentes (X) e dependentes (y)
X = df_eventos_2018_2024_modelo2.drop('Status', axis=1)
y = df_eventos_2018_2024_modelo2['Status']

# Dividir os dados em treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Aplicar o SMOTE para balancear as classes no conjunto de treino
smote = SMOTE(random_state=1)
X_train_smote, y_train_smote = smote.fit_resample(X_train, y_train)

# Definir o modelo XGBoost
xgb = XGBClassifier(use_label_encoder=False, eval_metric='logloss')

# Definir os hiperparâmetros para a busca bayesiana
param_grid = {
    'n_estimators': (50, 500),
    'max_depth': (3, 30),
    'learning_rate': (0.01, 0.3, 'log-uniform'),
    'subsample': (0.6, 1.0),
    'colsample_bytree': (0.6, 1.0),
    'alpha': (0, 1.0),
    'lambda': (0, 1.0)
}

# Definir a busca bayesiana
bayes_search_xgb_smote = BayesSearchCV(
    estimator=xgb,
    search_spaces=param_grid,
    n_iter=32,
    cv=3,
    n_jobs=-1,
    random_state=42
)

# Ajustar o modelo com os dados
best_xgb_model = bayes_search_xgb_smote.fit(X_train, y_train)

# Fazer previsões com o conjunto de teste original
y_pred_xgb = best_xgb_model.predict(X_test)

# Relatório de classificação
classification_report_xgb_smote = metrics.classification_report(
    y_test, y_pred_xgb, digits=6, target_names=['Reconhecido', 'Não reconhecido']
)

print('Classification report para XGBoost com SMOTE: \n')
print(classification_report_xgb_smote)

ConfusionMatrixDisplay.from_estimator(bayes_search_xgb_smote, X_test, y_test,
                                      values_format='d', cmap='Blues', display_labels=['Reconhecido', 'Não reconhecido'])

# Salvar o modelo treinado
joblib.dump(best_xgb_model, 'previsor_desastres.pkl')