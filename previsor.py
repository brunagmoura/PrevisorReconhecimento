import pandas as pd
import joblib
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from imblearn.over_sampling import SMOTE
from sklearn.metrics import classification_report
from xgboost import XGBClassifier
from skopt import BayesSearchCV


# Carregar o dataset
df_eventos_2018_2024_modelo1 = pd.read_csv(
    "https://raw.githubusercontent.com/brunagmoura/PrevisorReconhecimento/refs/heads/main/df_eventos_2018_2024_modelo1.csv",
    sep=';',
    decimal=',',
)

# Remover linhas com dados ausentes
df_eventos_2018_2024_modelo1 = df_eventos_2018_2024_modelo1.dropna()

# Separar variáveis independentes (X) e dependentes (y)
X = df_eventos_2018_2024_modelo1.drop('Status', axis=1)
y = df_eventos_2018_2024_modelo1['Status']

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

# Salvar o modelo treinado
joblib.dump(best_xgb_model, 'previsor_desastres.pkl')