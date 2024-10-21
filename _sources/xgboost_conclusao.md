# Resultados do modelo XGBoost

Com base nas especificidades identificadas na base de dados, foram realizados testes utilizando quatro conjuntos de dados distintos:

1. Features agregadas com eventos ocorridos entre 2010 e 2017.
2. Features agregadas com eventos ocorridos entre 2018 e 2024.
3. Features desagregadas com eventos ocorridos entre 2010 e 2017.
4. Features desagregadas com eventos ocorridos entre 2018 e 2024.

> **Nota**: Mais detalhes sobre o pré-processamento dos dados podem ser verificados no capítulo "Pré-processamento".

## Tabela Comparativa dos Modelos (2010-2017)

| Modelo                              | Precisão (Não reconhecido) | Recall (Não reconhecido) | F1-score (Não reconhecido) | Precisão (Reconhecido) | Recall (Reconhecido) | F1-score (Reconhecido) | Macro avg F1-score | Weighted avg F1-score (**destacado**) |
|--------------------------------------|----------------------------|--------------------------|----------------------------|------------------------|-----------------------|------------------------|---------------------|-----------------------------------------|
| Sem balanceamento                    | 0.612903                   | 0.122581                 | 0.204301                   | 0.919479               | 0.992332              | 0.954518               | 0.579409            | **0.886911**                          |
| Com SMOTE                            | 0.634146                   | 0.167742                 | 0.265306                   | 0.923169               | 0.990415              | 0.955610               | 0.610458            | **0.893403**                          |
| Com SMOTE e variáveis > -0,01        | 0.634146                   | 0.167742                 | 0.265306                   | 0.923169               | 0.990415              | 0.955610               | 0.610458            | **0.893403**                          |
| Com SMOTE e correlação < 0,5         | 0.543860                   | 0.200000                 | 0.292453                   | 0.925436               | 0.983387              | 0.953532               | 0.622992            | **0.893958**                          |

### Análise Comparativa dos Modelos (2010-2017)

- **Modelo sem balanceamento**:
  - Weighted avg F1-score: **88,69%**
  - Classe 'Não reconhecido': 
    - Precisão: 61,29%
    - Recall: 12,26%
    - F1-score: 20,43%
  - O modelo tem alta precisão para a classe majoritária, mas baixo desempenho na classe minoritária.

- **Modelo com SMOTE**:
  - Weighted avg F1-score: **89,34%**
  - Classe 'Não reconhecido': 
    - Precisão: 63,41%
    - Recall: 16,77%
    - F1-score: 26,53%
  - A aplicação do SMOTE aumentou tanto a precisão quanto o recall da classe minoritária.

- **Modelo com SMOTE e variáveis de importância > -0,01**:
  - Weighted avg F1-score: **89,34%**
  - Resultados idênticos ao modelo anterior. A seleção de variáveis com base na importância não trouxe impacto significativo.

- **Modelo com SMOTE e correlação < 0,5**:
  - Weighted avg F1-score: **89,39%**
  - Classe 'Não reconhecido': 
    - Precisão: 54,38%
    - Recall: 20,00%
    - F1-score: 29,25%
  - A remoção de variáveis correlacionadas aumentou o recall e o F1-score da classe minoritária, mas reduziu a precisão.

### Conclusões

- **Uso do SMOTE**: A técnica de balanceamento melhorou a detecção da classe minoritária, aumentando a precisão, recall e F1-score.
- **Seleção de Variáveis por Importância**: A exclusão de variáveis com importância < -0,01 não alterou o desempenho.
- **Remoção de Variáveis Correlacionadas**: A remoção de variáveis altamente correlacionadas beneficiou o recall da classe minoritária, mas com uma redução na precisão.

## Tabela Comparativa dos Modelos (2018-2024)

| Modelo                              | Precisão (Não reconhecido) | Recall (Não reconhecido) | F1-score (Não reconhecido) | Precisão (Reconhecido) | Recall (Reconhecido) | F1-score (Reconhecido) | Macro avg F1-score | Weighted avg F1-score (**destacado**) |
|--------------------------------------|----------------------------|--------------------------|----------------------------|------------------------|-----------------------|------------------------|---------------------|-----------------------------------------|
| Sem balanceamento                    | 0.859649                   | 0.337931                 | 0.485149                   | 0.939925               | 0.994702              | 0.966538               | 0.725843            | **0.924362**                          |
| Com SMOTE                            | 0.756757                   | 0.386207                 | 0.511416                   | 0.943707               | 0.988079              | 0.965383               | 0.738399            | **0.925610**                          |
| Com SMOTE e variáveis > -0,01        | 0.666667                   | 0.427586                 | 0.521008                   | 0.946863               | 0.979470              | 0.962891               | 0.741950            | **0.924176**                          |
| Com SMOTE e correlação < 0,5         | 0.677778                   | 0.420690                 | 0.519149                   | 0.946326               | 0.980795              | 0.963252               | 0.741200            | **0.924343**                          |

### Análise Comparativa dos Modelos (2018-2024)

- **Modelo sem balanceamento**:
  - Weighted avg F1-score: **92,43%**
  - Classe 'Não reconhecido': 
    - Precisão: 85,96%
    - Recall: 33,79%
    - F1-score: 48,51%
  - Alta precisão na classe 'Reconhecido', mas baixo recall na classe minoritária.

- **Modelo com SMOTE**:
  - Weighted avg F1-score: **92,56%**
  - Classe 'Não reconhecido': 
    - Precisão: 75,68%
    - Recall: 38,62%
    - F1-score: 51,14%
  - Melhorou o recall e F1-score da classe minoritária.

- **Modelo com SMOTE e variáveis de importância > -0,01**:
  - Weighted avg F1-score: **92,41%**
  - Precisão reduziu, mas recall e F1-score da classe minoritária aumentaram.

- **Modelo com SMOTE e correlação < 0,5**:
  - Weighted avg F1-score: **92,43%**
  - Precisão e recall se mantiveram estáveis em relação ao modelo anterior.

### Conclusões

- **Impacto do SMOTE**: Melhorou o recall e F1-score da classe 'Não reconhecido'.
- **Seleção de Variáveis por Importância**: Simplificação do modelo aumentou o recall e F1-score.
- **Remoção de Variáveis Correlacionadas**: Também melhorou o desempenho da classe minoritária, mantendo uma precisão ligeiramente maior.
- Os modelos de 2018-2024 mostraram melhor desempenho geral na classe minoritária.
- As técnicas de balanceamento e seleção de variáveis foram mais eficazes nos dados mais recentes.