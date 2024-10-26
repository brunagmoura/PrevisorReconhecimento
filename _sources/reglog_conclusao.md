# Resultados da Regressão Logística

Com base nas especificidades identificadas na base de dados, foram realizados testes utilizando quatro conjuntos de dados distintos:

1. Features agregadas com eventos ocorridos entre 2010 e 2017.
2. Features agregadas com eventos ocorridos entre 2018 e 2024.
3. Features desagregadas com eventos ocorridos entre 2010 e 2017.
4. Features desagregadas com eventos ocorridos entre 2018 e 2024.

> **Nota**: Mais detalhes sobre o pré-processamento dos dados podem ser verificados no capítulo "Pré-processamento".

## Tabela Comparativa dos Modelos (2010-2017)

| Métrica                  | Variáveis agregadas | Variáveis agregadas c/ SMOTE | Variáveis desagregadas | Variáveis desagregadas c/ SMOTE |
|--------------------------|---------------------|------------------------------|------------------------|---------------------------------|
| **Reconhecido**           |                     |                              |                        |                                 |
| Precision                 | 0.913793            | **0.947808**                 | 0.915284               | 0.951181                        |
| Recall                    | 0.986881            | 0.768515                     | 0.987220               | 0.771885                        |
| F1-Score                  | 0.948932            | 0.848796                     | 0.949892               | 0.852205                        |
| **Não Reconhecido**       |                     |                              |                        |                                 |
| Precision                 | **0.465517**        | 0.211816                     | 0.375000               | 0.206667                        |
| Recall                    | 0.109312            | 0.595142                     | 0.077419               | 0.600000                        |
| F1-Score                  | 0.177049            | 0.312434                     | 0.128342               | 0.307438                        |
| **Métricas gerais**       |                     |                              |                        |                                 |
| Weighted Avg Precision    | 0.871370            | 0.878157                     | 0.866596               | 0.884088                        |
| Weighted Avg Recall       | **0.903831**        | 0.752107                     | **0.905233**           | 0.756395                        |
| Weighted Avg F1-Score     | **0.875884**        | 0.798037                     | **0.875857**           | 0.803112                        |
| Total Support             | 2610                | 2610                         | 1720                   | 1720                            |

### Análise Comparativa dos Modelos (2010-2017)

- **Modelo sem SMOTE**:
  - Weighted avg F1-score: **87,58%**
  - Classe "Não reconhecido":
    - Precision: 46,55%
    - Recall: 10,93%
    - F1-score: 17,70%
  - O modelo apresenta alta precisão e recall para a classe majoritária, mas dificuldades em detectar a classe minoritária.

- **Modelo com SMOTE**:
  - Weighted avg F1-score: **79,80%**
  - Classe "Não reconhecido":
    - Precision: 21,18%
    - Recall: 59,51%
    - F1-score: 31,24%
  - A aplicação do SMOTE melhora significativamente o recall da classe minoritária, mas reduz a precisão geral.

- **Modelo com variáveis desagregadas e sem SMOTE**:
  - Weighted avg F1-score: **87,58%**
  - Classe "Não reconhecido":
    - Precision: 37,50%
    - Recall: 7,74%
    - F1-score: 12,83%
  - Embora o modelo tenha alta performance para a classe majoritária, o desempenho para a classe minoritária é baixo.

- **Modelo com variáveis desagregadas e com SMOTE**:
  - Weighted avg F1-score: **80,31%**
  - Classe "Não reconhecido":
    - Precision: 20,67%
    - Recall: 60,00%
    - F1-score: 30,74%
  - A remoção de variáveis correlacionadas com SMOTE melhorou o recall da classe minoritária, mas reduziu a precisão.

### Conclusões

- **Impacto do SMOTE**: A aplicação do SMOTE melhorou a capacidade de detecção da classe "Não reconhecido", aumentando o recall e o F1-score dessa classe. No entanto, reduziu a precisão geral do modelo.
- **Desempenho Geral**: Todos os modelos mantiveram um bom desempenho na classe majoritária "Reconhecido", com alta precisão e recall.

## Tabela Comparativa dos Modelos (2018-2024)

| Métrica                  | Variáveis agregadas | Variáveis agregadas c/ SMOTE | Variáveis desagregadas | Variáveis desagregadas c/ SMOTE |
|--------------------------|---------------------|------------------------------|------------------------|---------------------------------|
| **Reconhecido**           |                     |                              |                        |                                 |
| Precision                 | 0.924403            | 0.947368                     | 0.933333               | **0.965458**                    |
| Recall                    | 0.981697            | 0.726290                     | 0.992053               | 0.740397                        |
| F1-Score                  | 0.952189            | 0.822227                     | 0.961798               | 0.838081                        |
| **Não Reconhecido**       |                     |                              |                        |                                 |
| Precision                 | 0.456790            | 0.168142                     | **0.760000**           | 0.211268                        |
| Recall                    | 0.160870            | 0.578261                     | 0.262069               | 0.724138                        |
| F1-Score                  | 0.237942            | 0.260529                     | 0.389744               | 0.327103                        |
| **Métricas gerais**       |                     |                              |                        |                                 |
| Weighted Avg Precision    | 0.883571            | 0.879327                     | 0.918147               | 0.899381                        |
| Weighted Avg Recall       | **0.910023**        | 0.713364                     | **0.928097**           | 0.738973                        |
| Weighted Avg F1-Score     | **0.889821**        | 0.773180                     | **0.911678**           | 0.793312                        |
| Total Support             | 2634                | 2634                         | 1655                   | 1655                            |

### Análise Comparativa dos Modelos (2018-2024)

- **Modelo sem SMOTE**:
  - Weighted avg F1-score: **88,98%**
  - Classe "Não reconhecido":
    - Precision: 45,68%
    - Recall: 16,09%
    - F1-score: 23,79%
  - O modelo apresenta bom desempenho para a classe majoritária, mas desempenho limitado para a classe minoritária.

- **Modelo com SMOTE**:
  - Weighted avg F1-score: **77,31%**
  - Classe "Não reconhecido":
    - Precision: 16,81%
    - Recall: 57,83%
    - F1-score: 26,05%
  - O SMOTE melhora o recall da classe minoritária, mas afeta negativamente a precisão geral.

- **Modelo com variáveis desagregadas e sem SMOTE**:
  - Weighted avg F1-score: **91,16%**
  - Classe "Não reconhecido":
    - Precision: 76,00%
    - Recall: 26,21%
    - F1-score: 38,97%
  - O modelo melhora significativamente a precisão da classe minoritária ao custo de uma redução no recall.

- **Modelo com variáveis desagregadas e com SMOTE**:
  - Weighted avg F1-score: **79,33%**
  - Classe "Não reconhecido":
    - Precision: 21,13%
    - Recall: 72,41%
    - F1-score: 32,71%
  - O SMOTE combinado com variáveis desagregadas melhora o recall da classe "Não reconhecido", mas com uma precisão menor.

### Conclusões

- **Impacto do SMOTE**: O SMOTE melhorou o desempenho de recall para a classe "Não reconhecido", especialmente em combinações com variáveis desagregadas. Contudo, reduziu a precisão geral.
- **Desempenho Geral**: Assim como nos dados de 2010-2017, os modelos mostraram um bom desempenho na classe "Reconhecido", com alta precisão e recall.
