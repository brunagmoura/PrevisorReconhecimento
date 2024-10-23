# Resultados do modelo XGBoost

Com base nas especificidades identificadas na base de dados, foram realizados testes utilizando quatro conjuntos de dados distintos:

1. Features agregadas com eventos ocorridos entre 2010 e 2017.
2. Features agregadas com eventos ocorridos entre 2018 e 2024.
3. Features desagregadas com eventos ocorridos entre 2010 e 2017.
4. Features desagregadas com eventos ocorridos entre 2018 e 2024.

> **Nota**: Mais detalhes sobre o pré-processamento dos dados podem ser verificados no capítulo "Pré-processamento".

## Modelos com features agregadas

- **Modelo com features agregadas**:
  - Weighted avg F1-score: **86,59%** no período 2010-2017 e **90,1%** no período 2018-2024
  - Baixo desempenho para a classe 'Não reconhecido'.

## Modelos com features desagregadas

### 2010-2017

| Modelo                              | Precisão (Não reconhecido) | Recall (Não reconhecido) | F1-score (Não reconhecido) | Precisão (Reconhecido) | Recall (Reconhecido) | F1-score (Reconhecido) | Macro avg F1-score | Weighted avg F1-score |
|--------------------------------------|----------------------------|--------------------------|----------------------------|------------------------|-----------------------|------------------------|---------------------|----------------------------------------|
| Sem balanceamento                    | 0.687500                   | 0.152778                 | 0.250000                   | 0.908683               | 0.991830              | 0.948438               | 0.599219            | **0.874918**                         |
| Com SMOTE                            | 0.524590                   | 0.222222                 | 0.312195                   | 0.914308               | 0.976307              | 0.944291               | 0.628243            | **0.877754**                         |
| Com SMOTE e variáveis > -0,01        | 0.634146                   | 0.167742                 | 0.265306                   | 0.923169               | 0.990415              | 0.955610               | 0.610458            | **0.893403**                         |
| Com SMOTE e correlação < 0,5         | 0.543860                   | 0.200000                 | 0.292453                   | 0.925436               | 0.983387              | 0.953532               | 0.622992            | **0.893958**                         |


- **Uso do SMOTE**: A técnica de balanceamento melhorou o recall e o F1-score da classe 'Não reconhecido', mas a precisão caiu.
- **Seleção de Variáveis por Importância**: A exclusão de variáveis com importância < -0,01 não alterou significativamente o desempenho.
- **Remoção de Variáveis Correlacionadas**: A remoção de variáveis altamente correlacionadas beneficiou o recall da classe minoritária, com uma pequena redução na precisão.

### 2018-2024

| Modelo                              | Precisão (Não reconhecido) | Recall (Não reconhecido) | F1-score (Não reconhecido) | Precisão (Reconhecido) | Recall (Reconhecido) | F1-score (Reconhecido) | Macro avg F1-score | Weighted avg F1-score |
|--------------------------------------|----------------------------|--------------------------|----------------------------|------------------------|-----------------------|------------------------|---------------------|---------------------------------------|
| Sem balanceamento                    | 0.766667                   | 0.194915                 | 0.310811                   | 0.939258               | 0.995257              | 0.966447               | 0.638629            | **0.917912**                        |
| Com SMOTE                            | 0.648148                   | 0.296610                 | 0.406977                   | 0.946104               | 0.987127              | 0.966180               | 0.686579            | **0.924784**                        |
| Com SMOTE e variáveis > -0,01        | 0.648148                   | 0.296610                 | 0.406977                   | 0.946104               | 0.987127              | 0.966180               | 0.686579            | **0.924784**                        |
| Com SMOTE e correlação < 0,5         | 0.568966                   | 0.279661                 | 0.375000                   | 0.944661               | 0.983062              | 0.963479               | 0.669240            | **0.919916**                        |

- **Uso do SMOTE**: A técnica de balanceamento melhorou o recall e o F1-score da classe 'Não reconhecido', apesar de uma leve redução na precisão.
- **Seleção de Variáveis por Importância**: Não houve impacto perceptível no desempenho ao usar apenas variáveis com importância maior que -0,01.
- **Remoção de Variáveis Correlacionadas**: A remoção de variáveis altamente correlacionadas beneficiou o recall da classe minoritária, mas com uma redução significativa na precisão.

### Primeiras conclusões

- Impacto do SMOTE: Melhorou o recall e F1-score da classe 'Não reconhecido'.
- Seleção de Variáveis por Importância: Simplificação do modelo aumentou o recall e F1-score.
- Remoção de Variáveis Correlacionadas: Também melhorou o desempenho da classe minoritária, mantendo uma precisão ligeiramente maior.
- Os modelos de 2018-2024 mostraram melhor desempenho geral na classe minoritária.
- As técnicas de balanceamento e seleção de variáveis foram mais eficazes nos dados mais recentes.
- 
## Modelos adicionais 2018-2024

Considerando os melhores resultados obtidos nos modelos testados com as variáveis desagregadas e com os dados 2018-2024, foram realizados testes adicionais.

Nesses testes adicionais, as seguintes variáveis foram agregadas:

| Nova Variável                               | Agregação                                                                                         |
|---------------------------------------------|---------------------------------------------------------------------------------------------------|
| DH_FERIDOS_ENFERMOS                         | DH_FERIDOS + DH_ENFERMOS                                                        |
| DH_DESABRIGADOS_DESALOJADOS                 | DH_DESABRIGADOS + DH_DESALOJADOS                                               ||
| DM_Uni_Habita_Danificadas_Destruidas        | DM_Uni Habita Danificadas + DM_Uni Habita Destruidas                           ||
| DM_Inst_Saude_Danificadas_Destruidas        | DM_Inst Saúde Danificadas + DM_Inst Saúde Destruidas                           ||
| DM_Inst_Ensino_Danificadas_Destruidas       | DM_Inst Ensino Danificadas + DM_Inst Ensino Destruidas                         | |
| DM_Inst_Servicos_Danificadas_Destruidas     | DM_Inst Serviços Danificadas + DM_Inst Serviços Destruidas                     ||
| DM_Inst_Comuni_Danificadas_Destruidas       | DM_Inst Comuni Danificadas + DM_Inst Comuni Destruidas                       | |
| DM_Obras_Infra_Danificadas_Destruidas       | DM_Obras de Infra Danificadas + DM_Obras de Infra Destruidas                  | |

As métricas analisadas nessa nova rodada de testes foram:

- Accuracy (Acurácia): Proporção de previsões corretas (tanto positivas quanto negativas) em relação ao total de casos.
- Recall (Revocação): Proporção de casos positivos corretamente identificados pelo modelo. Importante quando queremos capturar todos os casos positivos. É o nosso caso!
- Precision (Precisão): Proporção de previsões positivas que realmente são positivas. Importante quando queremos minimizar falsos positivos.
- F1 Score: Média harmônica entre precisão e recall. Útil para balancear ambos quando há desbalanceamento de classes.
- AUC-ROC (Área Sob a Curva ROC): Mede a capacidade do modelo em distinguir entre classes. Valores mais próximos de 1 indicam melhor desempenho.
- AUC-PR (Área Sob a Curva de Precisão-Revocação): Similar ao AUC-ROC, mas é mais informativa em conjuntos de dados desbalanceados.

Os resultados são apresentados na tabela abaixo:

| model                                                                | accuracy_train | accuracy_test | recall_train | recall_test | precision | f1     | auc_roc | auc_pr |
|----------------------------------------------------------------------|----------------|---------------|--------------|-------------|-----------|--------|---------|--------|
| XGBoost Base                                                         | 0.997          | 0.934         | 1.000        | 0.990       | 0.941     | 0.965  | 0.829   | 0.976  |
| XGBoost com hiperparâmetros de Thakur (2020)                         | 0.979          | 0.934         | 1.000        | 0.998       | 0.931     | 0.963  | 0.825   | 0.975  |
| XGBoost com hiperparâmetros de Thakur (2020) e Features Selecionadas | 0.931          | 0.930         | 0.996        | 0.997       | 0.931     | 0.965  | 0.825   | 0.975  |
| XGBoost com hiperparâmetros de Thakur (2020) e Feature Engineering   | 0.953          | 0.934         | 0.999        | 0.999       | 0.933     | 0.965  | 0.842   | 0.978  |
| XGBoost com hiperparâmetros de Thakur (2020) e scale_pos_weight=1    | 0.917          | 0.915         | 1.000        | 1.000       | 0.915     | 0.956  | 0.812   | 0.973  |
| XGBoost com hiperparâmetros de Thakur (2020) e scale_pos_weight=5    | 0.939          | 0.930         | 1.000        | 1.000       | 0.929     | 0.963  | 0.838   | 0.977  |
| XGBoost com hiperparâmetros de Thakur (2020) e scale_pos_weight=10   | 0.936          | 0.930         | 1.000        | 1.000       | 0.929     | 0.963  | 0.839   | 0.978  |
| XGBoost com scale_pos_weight=20                                      | 0.933          | 0.928         | 1.000        | 1.000       | 0.927     | 0.962  | 0.835   | 0.977  |
| XGBoost com scale_pos_weight=30                                      | 0.932          | 0.929         | 1.000        | 1.000       | 0.928     | 0.962  | 0.832   | 0.977  |


### Análise dos Resultados

1. XGBoost Base
Acurácia de treino muito alta (0.997) comparada com a de teste (0.934), o que pode indicar overfitting (quando o modelo se ajusta muito bem aos dados de treino, mas não generaliza tão bem para novos dados).

2XGBoost com scale_pos_weight 1, 5, 10 e 20
O scale_pos_weight é um parâmetro que ajuda o modelo a lidar com desbalanceamento de classes, dando mais peso à classe minoritária.

Como o recall é 1.000 em todos os casos, o modelo não está deixando escapar nenhum caso positivo.

3. XGBoost Tunado

O AUC-ROC diminuiu um pouco, sugerindo que a capacidade do modelo em distinguir entre as classes não melhorou.

4. XGBoost com Features Selecionadas

A seleção de features reduziu um pouco a acurácia de treino, aproximando-a da de teste. Isso pode ajudar a reduzir overfitting.

As outras métricas permanecem similares, indicando que a remoção de features não prejudicou o desempenho.

5. XGBoost com Feature Engineering

A criação de novas features (feature engineering) melhorou o AUC-ROC, indicando que o modelo está melhor em distinguir entre as classes.
A acurácia de treino diminuiu um pouco, o que pode ajudar a evitar overfitting.

#### Overfitting

Modelos com scale_pos_weight ajustado: A acurácia de treino e teste são próximas, indicando baixo overfitting.
XGBoost Base: A acurácia de treino muito alta comparada à de teste sugere algum overfitting.
XGBoost com hiperparâmetros e com Feature Engineering: A diferença entre acurácia de treino e teste diminuiu, sugerindo que os ajustes ajudaram a reduzir overfitting.

### Resultados

- Com o objetivo de maximizar o recall sem overfitting, os modelos com ajuste de scale_pos_weight ou com feature engineering são boas opções.

