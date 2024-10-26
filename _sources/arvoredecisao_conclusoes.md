# Resultados dos Modelos de Árvores de Decisão

## Conjuntos de Dados Testados:
- **Features agregadas** com eventos de 2010 a 2017.
- **Features agregadas** com eventos de 2018 a 2024.
- **Features desagregadas** com eventos de 2010 a 2017.
- **Features desagregadas** com eventos de 2018 a 2024.

## Métricas Analisadas:
- **Precision**: Proporção de previsões positivas que realmente são positivas.
- **Recall**: Proporção de casos positivos corretamente identificados.
- **F1 Score**: Média harmônica entre precisão e recall.
- **Weighted Avg Recall**: Recall ponderado considerando o desbalanceamento das classes.

## Comparação de Modelos

### Variáveis Agregadas (2010-2017)
| Modelo                            | Precision (Não Reconhecido) | Recall (Não Reconhecido) | F1-score (Não Reconhecido) | Precision (Reconhecido) | Recall (Reconhecido) | F1-score (Reconhecido) | Weighted Avg Recall | Weighted F1  |
|------------------------------------|-----------------------------|---------------------------|----------------------------|--------------------------|----------------------|-------------------------|----------------|--------------|
| Sem Balanceamento                  | 0.714286                    | 0.020747                  | 0.040323                   | 0.884540                 | 0.998895             | 0.938246                | 0.883959       | 0.832737     |
| SMOTE                              | 0.187970                    | 0.207469                  | 0.197239                   | 0.892997                 | 0.880663             | 0.886787                | 0.801560       | 0.805763     |
| Balanceado por Pesos               | 0.000000                    | 0.000000                  | 0.000000                   | 0.882496                 | 1.000000             | 0.937581                | **0.882496**   | 0.827412     |
| Balanceado com Variáveis Selecionadas | 0.000000                    | 0.000000                  | 0.000000                   | 0.882496                 | 1.000000             | 0.937581                | **0.882496**   | 0.827412     |

### Variáveis Agregadas (2018-2024)
| Modelo                            | Precision (Não Reconhecido) | Recall (Não Reconhecido) | F1-score (Não Reconhecido) | Precision (Reconhecido) | Recall (Reconhecido) | F1-score (Reconhecido) | Weighted Avg Recall | Weighted F1  |
|------------------------------------|-----------------------------|---------------------------|----------------------------|--------------------------|----------------------|-------------------------|---------------------|--------------|
| Sem Balanceamento                  | 0.442308                    | 0.110048                  | 0.176245                   | 0.925241                 | 0.987559             | 0.955385                | **0.915354**            | 0.891275     |
| SMOTE                              | 0.279412                    | 0.272727                  | 0.276029                   | 0.934932                 | 0.936937             | 0.935933                | 0.882283            | 0.881634     |
| Balanceado por Pesos               | 0.428571                    | 0.100478                  | 0.162791                   | 0.924528                 | 0.987988             | 0.955205                | **0.914961**            | 0.890003     |
| Balanceado com Variáveis Selecionadas | 0.391892                    | 0.138756                  | 0.204947                   | 0.927007                 | 0.980695             | 0.953096                | 0.911417            | 0.891535     |

### Variáveis Desagregadas (2010-2017)
| Modelo                            | Precision (Não Reconhecido) | Recall (Não Reconhecido) | F1-score (Não Reconhecido) | Precision (Reconhecido) | Recall (Reconhecido) | F1-score (Reconhecido) | Weighted Avg Recall | Weighted F1  |
|------------------------------------|-----------------------------|---------------------------|----------------------------|--------------------------|----------------------|-------------------------|---------------------|--------------|
| Sem Balanceamento                  | 0.818182                    | 0.060403                  | 0.112500                   | 0.896831                 | 0.998359             | 0.944876                | 0.896199            | 0.854215     |
| SMOTE                              | 0.336842                    | 0.214765                  | 0.262295                   | 0.908091                 | 0.948318             | 0.927769                | 0.868421            | 0.855287     |
| Balanceado por Pesos               | 0.413043                    | 0.127517                  | 0.194872                   | 0.901664                 | 0.977851             | 0.938213                | **0.885234**            | 0.857250     |
| Balanceado com Variáveis Selecionadas | 0.413043                    | 0.127517                  | 0.194872                   | 0.901664                 | 0.977851             | 0.938213                | **0.885234**            | 0.857250     |

### Variáveis Desagregadas (2018-2024)
| Modelo                            | Precision (Não Reconhecido) | Recall (Não Reconhecido) | F1-score (Não Reconhecido) | Precision (Reconhecido) | Recall (Reconhecido) | F1-score (Reconhecido) | Weighted Avg Recall | Weighted F1  |
|------------------------------------|-----------------------------|---------------------------|----------------------------|--------------------------|----------------------|-------------------------|---------------------|--------------|
| Sem Balanceamento                  | 0.958333                    | 0.184000                  | 0.308725                   | 0.935032                 | 0.999319             | 0.966107                | **0.935383**            | 0.914556     |
| SMOTE                              | 0.319728                    | 0.376000                  | 0.345588                   | 0.946095                 | 0.931926             | 0.938957                | 0.888331            | 0.892426     |
| Balanceado por Pesos               | 0.411215                    | 0.352000                  | 0.379310                   | 0.945528                 | 0.957114             | 0.951286                | 0.909661            | 0.906432     |
| Balanceado com Variáveis Selecionadas | 0.405660                    | 0.344000                  | 0.372294                   | 0.944892                 | 0.957114             | 0.950964                | 0.909034            | 0.905585     |

## Análise e Conclusões:

1. **Baixo Desempenho na Classe "Não Reconhecido"**:
   - **Em todos os casos**, os modelos apresentaram dificuldades em prever corretamente a classe "Não Reconhecido" (baixo *recall*), especialmente com o balanceamento por pesos e seleção de variáveis.
   - O **SMOTE** trouxe uma leve melhoria no *recall* para a classe "Não Reconhecido", mas ainda assim, o desempenho nessa classe foi muito inferior ao da classe "Reconhecido".

2. **Impacto do Balanceamento por Pesos**:
   - Nos modelos com **variáveis selecionadas**, o desempenho foi similar ao do modelo balanceado por pesos sem seleção de variáveis.

3. **Melhor Desempenho Geral com SMOTE**:
   - O **SMOTE** trouxe uma melhoria geral no desempenho para a classe "Não Reconhecido" em termos de *recall*, com um impacto menor nas outras métricas, tornando-se a técnica mais balanceada entre precisão e recall.