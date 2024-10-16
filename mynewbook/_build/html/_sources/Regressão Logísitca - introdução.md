## Resultados da regressão logística

Tendo em vista as especificidades identificadas na base de dados, foram realizados testes para quatro bases de dados diferentes:

1. Features agregadas com eventos ocorridos entre 2010 e 2017;
2. Features agregadas com eventos ocorridos entre 2018 e 2024;
3. Features desagregadas com eventos ocorridos entre 2010 e 2017;
4. Features desagregadas com eventos ocorridos entre 2018 e 2024.

```{note}
Mais detalhes sobre o pré-processamento dos dados podem ser verificados no capítulo "Pré processamento".
```

## Eventos ocorridos entre 2010 e 2017

Nos testes dos eventos ocorridos entre 2010 e 2017 observou-se os seguintes resultados em relação às métricas de avaliação dos modelos:

|                         | Variáveis agregadas | Variáveis agregadas c/ SMOTE | Variáveis desagregadas | Variáveis desagregadas c/ SMOTE |
|-------------------------|---------------------|------------------------------|------------------------|---------------------------------|
| **Reconhecido**          |                     |                              |                        |                                 |
| Precision                | 0.913793            | **0.947808**                 | 0.915284               | 0.951181                        |
| Recall                   | 0.986881            | 0.768515                     | 0.987220               | 0.771885                        |
| F1-Score                 | 0.948932            | 0.848796                     | 0.949892               | 0.852205                        |
| Support                  | 2363                | 2363                         | 1565                   | 1565                            |
| **Não reconhecido**       |                     |                              |                        |                                 |
| Precision                | **0.465517**        | 0.211816                     | 0.375000               | 0.206667                        |
| Recall                   | 0.109312            | 0.595142                     | 0.077419               | 0.600000                        |
| F1-Score                 | 0.177049            | 0.312434                     | 0.128342               | 0.307438                        |
| Support                  | 247                 | 247                          | 155                    | 155                             |
| **Métricas gerais**       |                     |                              |                        |                                 |
| Accuracy                 | **0.903831**        | 0.752107                     | 0.905233               | 0.756395                        |
| Macro Avg Precision       | 0.689655            | 0.579812                     | 0.645142               | 0.578924                        |
| Macro Avg Recall          | 0.548096            | 0.681828                     | 0.532320               | 0.685942                        |
| Macro Avg F1-Score        | 0.562991            | 0.580615                     | 0.539117               | 0.579821                        |
| Weighted Avg Precision    | 0.871370            | 0.878157                     | 0.866596               | 0.884088                        |
| Weighted Avg Recall       | 0.903831            | 0.752107                     | **0.905233**           | 0.756395                        |
| Weighted Avg F1-Score     | **0.875884**        | 0.798037                     | **0.875857**           | 0.803112                        |
| Total Support             | 2610                | 2610                         | 1720                   | 1720                            |

### Precision (Precisão)

*Definição*: A precisão mede a proporção de previsões positivas que estão corretas. Ou seja, quantos dos exemplos classificados como "positivos" realmente pertencem à classe positiva.

*Interpretação*:

Para a classe Reconhecido, a precisão é consistentemente alta em todos os cenários. Isso significa que quando o modelo prevê que um evento será reconhecido, ele geralmente está correto.
Para a classe Não reconhecido, a precisão é muito menor. Isso sugere que quando o modelo prevê que um evento não será reconhecido, ele erra mais frequentemente, o que é esperado considerando a natureza desequilibrada dos dados.

### Recall (Sensibilidade ou Revocação)

*Definição*: O recall mede a proporção de exemplos verdadeiramente positivos que foram corretamente identificados. Em outras palavras, o quanto o modelo consegue capturar todos os exemplos positivos.

*Interpretação*:
Reconhecido: O recall é muito alto para a classe "Reconhecido", principalmente nos cenários sem SMOTE (0.986881 no primeiro cenário e 0.987220 no modelo 2). Isso significa que o modelo é capaz de identificar quase todos os eventos que deveriam ser reconhecidos.
Não reconhecido: O recall para "Não reconhecido" é extremamente baixo nos cenários sem SMOTE (0.109312 e 0.077419), indicando que o modelo raramente identifica corretamente essa classe. No entanto, após aplicar SMOTE, o recall melhora drasticamente (0.595142 e 0.600000). Isso mostra que o SMOTE está ajudando o modelo a capturar mais exemplos da classe minoritária.

### F1-Score

*Definição*: O F1-Score é a média harmônica da precisão e do recall. Ele equilibra os dois aspectos e é especialmente útil quando se trabalha com dados desbalanceados.

*Interpretação*:
Reconhecido: O F1-Score para a classe "Reconhecido" é sempre muito alto (acima de 0.84), refletindo o bom desempenho do modelo para essa classe majoritária.
Não reconhecido: O F1-Score para "Não reconhecido" é muito baixo sem SMOTE (0.177049 e 0.128342), mas melhora com SMOTE (0.312434 e 0.307438). Isso ocorre porque o SMOTE ajuda a balancear os dados, melhorando a identificação de exemplos dessa classe.

### Support (Suporte)

*Definição*: O suporte é o número de ocorrências reais de cada classe nos dados. Ele mostra a distribuição do número de exemplos entre as classes.

*Interpretação*:
Reconhecido: A classe "Reconhecido" tem muito mais suporte (2363 no primeiro cenário e 1565 no modelo 2). Isso confirma que os dados estão desbalanceados, com muito mais exemplos de eventos reconhecidos do que não reconhecidos.
Não reconhecido: A classe "Não reconhecido" tem muito menos suporte (247 no primeiro cenário e 155 no modelo 2), o que faz com que os modelos tenham mais dificuldade em prever essa classe corretamente.

### Accuracy (Acurácia)

*Definição*: A acurácia é a proporção de previsões corretas em relação ao total de exemplos.

*Interpretação*:
A acurácia é alta nos cenários sem SMOTE (acima de 0.90), indicando que o modelo está correto na maioria das previsões. No entanto, como os dados estão desbalanceados, a alta acurácia pode estar inflada pela boa performance na classe majoritária (Reconhecido).
Após aplicar SMOTE, a acurácia diminui para cerca de 0.75. Isso acontece porque o modelo passa a focar mais na classe minoritária (Não reconhecido), mas ainda não consegue identificar perfeitamente os dois grupos.

### Macro Avg (Média Macro)
*Definição*: A média macro calcula a média simples das métricas para todas as classes, tratando cada classe igualmente, independentemente do número de exemplos.

*Interpretação*:
A média macro de precisão e F1-score é consistentemente menor com SMOTE, o que indica que o SMOTE melhora o recall da classe minoritária às custas da precisão geral do modelo.
Sem SMOTE, o modelo favorece a classe "Reconhecido", o que leva a médias macro mais baixas, especialmente para o recall.

### Weighted Avg (Média Ponderada)

*Definição*: A média ponderada calcula a média das métricas levando em conta o suporte (número de exemplos) de cada classe.

*Interpretação*
A média ponderada de precisão e F1-score é alta nos quatro cenários, mas cai ligeiramente após o uso de SMOTE. Isso ocorre porque, embora o modelo melhore o desempenho para a classe minoritária, ele ainda tem dificuldade em prever corretamente essa classe, o que afeta o desempenho geral.

## Eventos ocorridos entre 2018 e 2024

|                         |  Variáveis agregadas | Variáveis agregadas c/ SMOTE | Variáveis desagregadas | Variáveis desagregadas c/ SMOTE |
|-------------------------|------------------------|----------------------------------|------------------------|---------------------------------|
| **Reconhecido**          |                        |                                  |                        |                                 |
| Precision                | 0.924403               | 0.947368                         | 0.933333               | **0.965458**                    |
| Recall                   | 0.981697               | 0.726290                         | 0.992053               | 0.740397                        |
| F1-Score                 | 0.952189               | 0.822227                         | 0.961798               | 0.838081                        |
| Support                  | 2404                   | 2404                             | 1510                   | 1510                            |
| **Não reconhecido**       |                        |                                  |                        |                                 |
| Precision                | 0.456790               | 0.168142                         | **0.760000**           | 0.211268                        |
| Recall                   | 0.160870               | 0.578261                         | 0.262069               | 0.724138                        |
| F1-Score                 | 0.237942               | 0.260529                         | 0.389744               | 0.327103                        |
| Support                  | 230                    | 230                              | 145                    | 145                             |
| **Métricas gerais**       |                        |                                  |                        |                                 |
| Accuracy                 | 0.910023               | 0.713364                         | 0.928097               | 0.738973                        |
| Macro Avg Precision       | 0.690596               | 0.557755                         | 0.846667               | 0.588363                        |
| Macro Avg Recall          | 0.571283               | 0.652275                         | 0.627061               | 0.732268                        |
| Macro Avg F1-Score        | 0.595065               | 0.541378                         | 0.675771               | 0.582592                        |
| Weighted Avg Precision    | 0.883571               | 0.879327                         | 0.918147               | 0.899381                        |
| Weighted Avg Recall       | 0.910023               | 0.713364                         | **0.928097**           | 0.738973                        |
| Weighted Avg F1-Score     | 0.889821               | 0.773180                         | **0.911678**           | 0.793312                        |
| Total Support             | 2634                   | 2634                             | 1655                   | 1655                            |


## Conclusão

Modelos sem SMOTE têm uma excelente performance para a classe "Reconhecido", mas sofrem ao prever a classe "Não reconhecido".

Modelos com SMOTE melhoram significativamente o recall para a classe "Não reconhecido", mas isso vem à custa de uma redução na precisão e acurácia geral.

O Modelo com variáveis desagregadas (2018-2024) sem SMOTE apresenta o melhor desempenho geral, com uma boa acurácia e um bom equilíbrio entre precisão e recall.

No entanto, se o objetivo é melhorar o recall da classe "Não reconhecido", o uso de SMOTE no modelo com variáveis desagregadas se destaca, embora com uma leve queda na acurácia.