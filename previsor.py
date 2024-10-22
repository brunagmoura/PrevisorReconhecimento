import pandas as pd
from sklearn.metrics import ConfusionMatrixDisplay
from sklearn.inspection import permutation_importance
import matplotlib.pyplot as plt
from sklearn.metrics import make_scorer, recall_score
import numpy as np
from sklearn.model_selection import StratifiedKFold, train_test_split
from imblearn.over_sampling import SMOTE
from sklearn.pipeline import Pipeline
import xgboost as xgb
from skopt import BayesSearchCV
from sklearn.preprocessing import RobustScaler
from sklearn import metrics
import joblib

# Carregar o dataset
df_eventos_2018_2024_modelo2 = pd.read_csv(
    "https://raw.githubusercontent.com/brunagmoura/PrevisorReconhecimento/refs/heads/main/df_eventos_2018_2024_modelo2.csv",
    sep=';',
    decimal=',',
)

# Inclusão de features derivadas, tratando dados ausentes como 0
df_eventos_2018_2024_modelo2['DH_FERIDOS_ENFERMOS'] = df_eventos_2018_2024_modelo2['DH_FERIDOS'].fillna(0) + df_eventos_2018_2024_modelo2['DH_ENFERMOS'].fillna(0)
df_eventos_2018_2024_modelo2['DH_DESABRIGADOS_DESALOJADOS'] = df_eventos_2018_2024_modelo2['DH_DESABRIGADOS'].fillna(0) + df_eventos_2018_2024_modelo2['DH_DESALOJADOS'].fillna(0)
df_eventos_2018_2024_modelo2['DH_DESAPARECIDOS'] = df_eventos_2018_2024_modelo2['DH_DESAPARECIDOS'].fillna(0)
df_eventos_2018_2024_modelo2['DH_MORTOS'] = df_eventos_2018_2024_modelo2['DH_MORTOS'].fillna(0)
df_eventos_2018_2024_modelo2['DM_Uni_Habita_Danificadas_Destruidas'] = df_eventos_2018_2024_modelo2['DM_Uni Habita Danificadas'].fillna(0) + df_eventos_2018_2024_modelo2['DM_Uni Habita Destruidas'].fillna(0)
df_eventos_2018_2024_modelo2['DM_Uni_Habita_Valor'] = df_eventos_2018_2024_modelo2['DM_Uni Habita Valor'].fillna(0)
df_eventos_2018_2024_modelo2['DM_Inst_Saude_Danificadas_Destruidas'] = df_eventos_2018_2024_modelo2['DM_Inst Saúde Danificadas'].fillna(0) + df_eventos_2018_2024_modelo2['DM_Inst Saúde Destruidas'].fillna(0)
df_eventos_2018_2024_modelo2['DM_Inst_Saude_Valor'] = df_eventos_2018_2024_modelo2['DM_Inst Saúde Valor'].fillna(0)
df_eventos_2018_2024_modelo2['DM_Inst_Ensino_Danificadas_Destruidas'] = df_eventos_2018_2024_modelo2['DM_Inst Ensino Danificadas'].fillna(0) + df_eventos_2018_2024_modelo2['DM_Inst Ensino Destruidas'].fillna(0)
df_eventos_2018_2024_modelo2['DM_Inst_Ensino_Valor'] = df_eventos_2018_2024_modelo2['DM_Inst Ensino Valor'].fillna(0)
df_eventos_2018_2024_modelo2['DM_Inst_Servicos_Danificadas_Destruidas'] = df_eventos_2018_2024_modelo2['DM_Inst Serviços Danificadas'].fillna(0) + df_eventos_2018_2024_modelo2['DM_Inst Serviços Destruidas'].fillna(0)
df_eventos_2018_2024_modelo2['DM_Inst_Servicos_Valor'] = df_eventos_2018_2024_modelo2['DM_Inst Serviços Valor'].fillna(0)
df_eventos_2018_2024_modelo2['DM_Inst_Comuni_Danificadas_Destruidas'] = df_eventos_2018_2024_modelo2['DM_Inst Comuni Danificadas'].fillna(0) + df_eventos_2018_2024_modelo2['DM_Inst Comuni Destruidas'].fillna(0)
df_eventos_2018_2024_modelo2['DM_Inst_Comuni_Valor'] = df_eventos_2018_2024_modelo2['DM_Inst Comuni Valor'].fillna(0)
df_eventos_2018_2024_modelo2['DM_Obras_Infra_Danificadas_Destruidas'] = df_eventos_2018_2024_modelo2['DM_Obras de Infra Danificadas'].fillna(0) + df_eventos_2018_2024_modelo2['DM_Obras de Infra Destruidas'].fillna(0)
df_eventos_2018_2024_modelo2['DM_Obras_Infra_Valor'] = df_eventos_2018_2024_modelo2['DM_Obras de Infra Valor'].fillna(0)

colunas_a_remover = ['DH_FERIDOS', 'DH_ENFERMOS', 'DH_DESABRIGADOS', 'DH_DESALOJADOS',
                     'DH_DESAPARECIDOS', 'DH_MORTOS', 'DM_Uni Habita Danificadas', 'DM_Uni Habita Destruidas',
                     'DM_Uni Habita Valor', 'DM_Inst Saúde Danificadas', 'DM_Inst Saúde Destruidas',
                     'DM_Inst Saúde Valor', 'DM_Inst Ensino Danificadas', 'DM_Inst Ensino Destruidas',
                     'DM_Inst Ensino Valor', 'DM_Inst Serviços Danificadas', 'DM_Inst Serviços Destruidas',
                     'DM_Inst Serviços Valor', 'DM_Inst Comuni Danificadas', 'DM_Inst Comuni Destruidas',
                     'DM_Inst Comuni Valor', 'DM_Obras de Infra Danificadas', 'DM_Obras de Infra Destruidas',
                     'DM_Obras de Infra Valor']

df_eventos_2018_2024_modelo2 = df_eventos_2018_2024_modelo2.drop(columns=colunas_a_remover)

df_eventos_2018_2024_modelo2 = df_eventos_2018_2024_modelo2.dropna()

# Separar variáveis independentes (X) e dependentes (y)
X_2018_2024_modelo2 = df_eventos_2018_2024_modelo2.drop('Status', axis=1)

y_2018_2024_modelo2 = df_eventos_2018_2024_modelo2['Status']

# Dividir os dados em treino e teste
X_train_2018_2024_modelo2, X_test_2018_2024_modelo2, y_train_2018_2024_modelo2, y_test_2018_2024_modelo2 = train_test_split(X_2018_2024_modelo2, y_2018_2024_modelo2, test_size=0.2, random_state=1, stratify=y_2018_2024_modelo2)

# Definir hiperparâmetros para a busca bayesiana
param_grid_bayes = {
    'xgb__eta': [0.01, 0.015, 0.025, 0.05, 0.1],
    'xgb__gamma': [0.05, 0.1, 0.3, 0.5, 0.7, 0.9, 1.0],
    'xgb__max_depth': [3, 5, 7, 9, 12, 15, 17, 25],
    'xgb__min_child_weight': [1, 3, 5, 7],
    'xgb__subsample': [0.6, 0.7, 0.8, 0.9, 1.0],
    'xgb__colsample_bytree': [0.6, 0.7, 0.8, 0.9, 1.0],
    'xgb__lambda': [0.01, 0.1, 1.0],
    'xgb__alpha': [0, 0.1, 0.5, 1.0]
}

# Usar recall como métrica de scoring
scorer = make_scorer(recall_score)

# Definir scale_pos_weight
scale_pos_weight = np.sqrt(7549 / 726)

# Criar pipeline com RobustScaler e XGBoost Classifier
pipeline_xgb = Pipeline([
    ('scaler', RobustScaler()),
    ('xgb', xgb.XGBClassifier(
        random_state=1,
        eval_metric='logloss',
        scale_pos_weight=scale_pos_weight
    ))
])

# Realizar a busca bayesiana com validação cruzada
cv = StratifiedKFold(n_splits=10, shuffle=True, random_state=1)

bayes_search_xgb = BayesSearchCV(
    pipeline_xgb,
    search_spaces=param_grid_bayes,
    n_iter=30,
    cv=cv,
    scoring=scorer,
    n_jobs=-1,
    random_state=1
)

# Ajustar o modelo ao conjunto de treino balanceado
bayes_search_xgb.fit(X_train_2018_2024_modelo2, y_train_2018_2024_modelo2)

# Melhor modelo encontrado
best_xgb_model = bayes_search_xgb.best_estimator_

# Fazer previsões com o conjunto de teste original
y_pred_xgb_smote = best_xgb_model.predict(X_test_2018_2024_modelo2)

model_data = {
    'model': best_xgb_model,
    'features': X_2018_2024_modelo2.columns.tolist()  # Salvando as colunas utilizadas no treinamento
}

# Salvar o modelo e as features em um único arquivo
joblib.dump(model_data, 'previsor_desastres.pkl')