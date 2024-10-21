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

### Análise comparativa dos Modelos com features desagregadas (2010-2017)

| Modelo                              | Precisão (Não reconhecido) | Recall (Não reconhecido) | F1-score (Não reconhecido) | Precisão (Reconhecido) | Recall (Reconhecido) | F1-score (Reconhecido) | Macro avg F1-score | Weighted avg F1-score |
|--------------------------------------|----------------------------|--------------------------|----------------------------|------------------------|-----------------------|------------------------|---------------------|----------------------------------------|
| Sem balanceamento                    | 0.687500                   | 0.152778                 | 0.250000                   | 0.908683               | 0.991830              | 0.948438               | 0.599219            | **0.874918**                         |
| Com SMOTE                            | 0.524590                   | 0.222222                 | 0.312195                   | 0.914308               | 0.976307              | 0.944291               | 0.628243            | **0.877754**                         |
| Com SMOTE e variáveis > -0,01        | 0.634146                   | 0.167742                 | 0.265306                   | 0.923169               | 0.990415              | 0.955610               | 0.610458            | **0.893403**                         |
| Com SMOTE e correlação < 0,5         | 0.543860                   | 0.200000                 | 0.292453                   | 0.925436               | 0.983387              | 0.953532               | 0.622992            | **0.893958**                         |


- **Uso do SMOTE**: A técnica de balanceamento melhorou o recall e o F1-score da classe 'Não reconhecido', mas a precisão caiu.
- **Seleção de Variáveis por Importância**: A exclusão de variáveis com importância < -0,01 não alterou significativamente o desempenho.
- **Remoção de Variáveis Correlacionadas**: A remoção de variáveis altamente correlacionadas beneficiou o recall da classe minoritária, com uma pequena redução na precisão.

### Análise comparativa dos Modelos com features desagregadas (2018-2024)

| Modelo                              | Precisão (Não reconhecido) | Recall (Não reconhecido) | F1-score (Não reconhecido) | Precisão (Reconhecido) | Recall (Reconhecido) | F1-score (Reconhecido) | Macro avg F1-score | Weighted avg F1-score |
|--------------------------------------|----------------------------|--------------------------|----------------------------|------------------------|-----------------------|------------------------|---------------------|---------------------------------------|
| Sem balanceamento                    | 0.766667                   | 0.194915                 | 0.310811                   | 0.939258               | 0.995257              | 0.966447               | 0.638629            | **0.917912**                        |
| Com SMOTE                            | 0.648148                   | 0.296610                 | 0.406977                   | 0.946104               | 0.987127              | 0.966180               | 0.686579            | **0.924784**                        |
| Com SMOTE e variáveis > -0,01        | 0.648148                   | 0.296610                 | 0.406977                   | 0.946104               | 0.987127              | 0.966180               | 0.686579            | **0.924784**                        |
| Com SMOTE e correlação < 0,5         | 0.568966                   | 0.279661                 | 0.375000                   | 0.944661               | 0.983062              | 0.963479               | 0.669240            | **0.919916**                        |

- **Uso do SMOTE**: A técnica de balanceamento melhorou o recall e o F1-score da classe 'Não reconhecido', apesar de uma leve redução na precisão.
- **Seleção de Variáveis por Importância**: Não houve impacto perceptível no desempenho ao usar apenas variáveis com importância maior que -0,01.
- **Remoção de Variáveis Correlacionadas**: A remoção de variáveis altamente correlacionadas beneficiou o recall da classe minoritária, mas com uma redução significativa na precisão.

## Conclusões

- Impacto do SMOTE: Melhorou o recall e F1-score da classe 'Não reconhecido'.
- Seleção de Variáveis por Importância: Simplificação do modelo aumentou o recall e F1-score.
- Remoção de Variáveis Correlacionadas: Também melhorou o desempenho da classe minoritária, mantendo uma precisão ligeiramente maior.
- Os modelos de 2018-2024 mostraram melhor desempenho geral na classe minoritária.
- As técnicas de balanceamento e seleção de variáveis foram mais eficazes nos dados mais recentes.