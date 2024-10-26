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

## Variáveis Agregadas (2010-2017)

| Modelo                            | Precision (Não Reconhecido) | Recall (Não Reconhecido) | F1-score (Não Reconhecido) | Precision (Reconhecido) | Recall (Reconhecido) | F1-score (Reconhecido) | Weighted Avg Recall | Weighted F1  |
|------------------------------------|-----------------------------|---------------------------|----------------------------|--------------------------|----------------------|-------------------------|---------------------|--------------|
| Sem Balanceamento                  | 0.714286                    | 0.020747                  | 0.040323                   | 0.884540                 | 0.998895             | 0.938246                | 0.883959            | 0.832737     |
| SMOTE                              | 0.187970                    | 0.207469                  | 0.197239                   | 0.892997                 | 0.880663             | 0.886787                | 0.801560            | 0.805763     |
| Balanceado por Pesos               | 1.000000                    | 0.004149                  | 0.008264                   | 0.882927                 | 1.000000             | 0.937824                | **0.882984**        | 0.828597     |
| Balanceado com Variáveis Selecionadas | 0.000000                    | 0.000000                  | 0.000000                   | 0.882496                 | 1.000000             | 0.937581                | **0.882496**        | 0.827412     |

## Variáveis Agregadas (2018-2024)

| Modelo                            | Precision (Não Reconhecido) | Recall (Não Reconhecido) | F1-score (Não Reconhecido) | Precision (Reconhecido) | Recall (Reconhecido) | F1-score (Reconhecido) | Weighted Avg Recall | Weighted F1  |
|------------------------------------|-----------------------------|---------------------------|----------------------------|--------------------------|----------------------|-------------------------|---------------------|--------------|
| Sem Balanceamento                  | 0.442308                    | 0.110048                  | 0.176245                   | 0.925241                 | 0.987559             | 0.955385                | 0.915354            | 0.891275     |
| SMOTE                              | 0.279412                    | 0.272727                  | 0.276029                   | 0.934932                 | 0.936937             | 0.935933                | 0.882283            | 0.881634     |
| Balanceado por Pesos               | 0.000000                    | 0.000000                  | 0.000000                   | 0.917717                 | 1.000000             | 0.957093                | **0.917717**        | 0.878340     |
| Balanceado com Variáveis Selecionadas | 0.428571                    | 0.014354                  | 0.027778                   | 0.918674                 | 0.998284             | 0.956826                | **0.917323**        | 0.880380     |

## Variáveis Desagregadas (2010-2017)

| Modelo                            | Precision (Não Reconhecido) | Recall (Não Reconhecido) | F1-score (Não Reconhecido) | Precision (Reconhecido) | Recall (Reconhecido) | F1-score (Reconhecido) | Weighted Avg Recall | Weighted F1  |
|------------------------------------|-----------------------------|---------------------------|----------------------------|--------------------------|----------------------|-------------------------|---------------------|--------------|
| Sem Balanceamento                  | 0.818182                    | 0.060403                  | 0.112500                   | 0.896831                 | 0.998359             | 0.944876                | **0.896199**        | 0.854215     |
| SMOTE                              | 0.336842                    | 0.214765                  | 0.262295                   | 0.908091                 | 0.948318             | 0.927769                | 0.868421            | 0.855287     |
| Balanceado por Pesos               | 0.413043                    | 0.127517                  | 0.194872                   | 0.901664                 | 0.977851             | 0.938213                | **0.885234**        | 0.857250     |
| Balanceado com Variáveis Selecionadas | 1.000000                    | 0.020134                  | 0.039474                   | 0.893040                 | 1.000000             | 0.943498                | **0.893275**        | 0.845034     |

## Variáveis Desagregadas (2018-2024)

| Modelo                            | Precision (Não Reconhecido) | Recall (Não Reconhecido) | F1-score (Não Reconhecido) | Precision (Reconhecido) | Recall (Reconhecido) | F1-score (Reconhecido) | Weighted Avg Recall | Weighted F1  |
|------------------------------------|-----------------------------|---------------------------|----------------------------|--------------------------|----------------------|-------------------------|---------------------|--------------|
| Sem Balanceamento                  | 0.960000                    | 0.192000                  | 0.320000                   | 0.935628                 | 0.999319             | 0.966425                | **0.936010**        | 0.915733     |
| SMOTE                              | 0.319728                    | 0.376000                  | 0.345588                   | 0.946095                 | 0.931926             | 0.938957                | 0.888331            | 0.892426     |
| Balanceado por Pesos               | 0.944444                    | 0.136000                  | 0.237762                   | 0.931472                 | 0.999319             | 0.964204                | **0.931619**        | 0.907237     |
| Balanceado com Variáveis Selecionadas | 1.000000                    | 0.136000                  | 0.239437                   | 0.931516                 | 1.000000             | 0.964544                | **0.932246**        | 0.907681     |

## Importância das Variáveis (Modelos com definição de hiperparâmetros, Balanceamento por Pesos, Seleção de Variáveis)

| **Feature**                              | **Agregado 2010-2017** | **Agregado 2018-2024** | **Desagregado 2010-2017** | **Desagregado 2018-2024** |
|------------------------------------------|------------------------|------------------------|---------------------------|---------------------------|
| PEPR_total_privado                       | **0.419349**           | **0.267709**           | -                         | -                         |
| Rendapercapita                           | 0.219838               | -                      | 0.211740                  | -                         |
| DH_total_danos_humanos                   | **0.187282**           | **0.681237**           | -                         | -                         |
| PEPL_total_publico                       | 0.117049               | -                      | -                         | -                         |
| DM_total_danos_materiais                 | 0.056482               | 0.033385               | 0.041523                  | -                         |
| PDEFESGOTO                               | -                      | 0.017669               | -                         | -                         |
| PEPR_Agricultura (R$)                    | -                      | -                      | 0.344319                  | -                         |
| Sigla_UF_TO                              | -                      | -                      | 0.225400                  | -                         |
| PEPL_Abast de água pot(R$)               | -                      | -                      | 0.106759                  | -                         |
| DensidadePop                             | -                      | -                      | 0.070259                  | -                         |
| DM_Inst Saúde Destruidas                 | -                      | -                      | -                         | 0.581018                  |
| DM_Uni Habita Destruidas                 | -                      | -                      | -                         | 0.139474                  |
| DH_OUTROS AFETADOS                       | -                      | -                      | -                         | 0.106050                  |
| COBRADE_11410 (Erosão costeira)          | -                      | -                      | -                         | 0.075611                  |
| COBRADE_24100 (Queda de estrutura civil) | -                      | -                      | -                         | 0.068325                  |
| DM_Inst Saúde Valor                      | -                      | -                      | -                         | 0.029520                  |

Parece haver uma certa mudança de foco ao longo do tempo

- 2010-2017: O foco foi principalmente nas perdas econômicas, tanto no setor privado quanto no setor público. Em termos desagregados, as perdas no setor agrícola  foram importantes, sugerindo que o impacto econômico pesava nas decisões.
- 2018-2024: O foco passou a ser significativamente mais relacionado aos danos humanos, o que pode refletir uma mudança nos critérios de reconhecimento federal. Em termos desagregados, há especial atenção aos danos à infraestrutura de saúde e o impacto em habitações, indicando uma ênfase nas consequências sociais e humanas dos desastres.

## Árvore 2018-2024 com variáveis desagregadas e com poda



## Análise e Conclusões:

1. **Baixo Desempenho na Classe "Não Reconhecido"**:
   - **Em todos os casos**, os modelos apresentaram dificuldades em prever corretamente a classe "Não Reconhecido" (baixo *recall*), especialmente com o balanceamento por pesos e seleção de variáveis.
   - O **SMOTE** trouxe uma leve melhoria no *recall* para a classe "Não Reconhecido", mas ainda assim, o desempenho nessa classe foi muito inferior ao da classe "Reconhecido".

2. **Impacto do Balanceamento por Pesos**:
   - Nos modelos com **variáveis selecionadas**, o desempenho foi similar ao do modelo balanceado por pesos sem seleção de variáveis.

3. **Melhor Desempenho Geral com SMOTE**:
   - O **SMOTE** trouxe uma melhoria geral no desempenho para a classe "Não Reconhecido" em termos de *recall*, com um impacto menor nas outras métricas, tornando-se a técnica mais balanceada entre precisão e recall.