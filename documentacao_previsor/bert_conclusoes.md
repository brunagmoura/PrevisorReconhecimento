# Resultados BERTopics

No projeto de reconhecimento federal de desastres, aplicamos o BERTopic para descobrir automaticamente os principais temas presentes nas descrições de desastres fornecidas pelos municípios.

## O que foi feito

O passo a passo foi:

- Preparação das descrições: Primeiro, pegamos as descrições dos desastres que estavam no banco de dados, tanto para os eventos reconhecidos quanto para os não reconhecidos. Essas descrições incluem informações sobre os danos causados pelos desastres, como prejuízos materiais e impactos ambientais.
- Transformação das descrições em números: Para que o modelo BERTopic pudesse entender o conteúdo dos textos, transformamos essas descrições em números que representam o significado das palavras e frases. Essa etapa permite que o modelo "compreenda" o que está sendo dito em cada descrição.
- Agrupamento por temas: Com as descrições transformadas, o BERTopic conseguiu identificar quais textos falavam sobre temas parecidos e os agrupou. Cada grupo formado representa um tópico, ou seja, um conjunto de descrições que tratam de assuntos similares.
- Identificação das palavras mais importantes: Para cada grupo (ou tópico), o modelo destacou as palavras que mais aparecem e que ajudam a definir o tema principal do grupo. Isso nos permitiu ver quais palavras eram mais frequentes nas descrições de desastres.
- Comparação entre desastres reconhecidos e não reconhecidos: Aplicamos essa mesma análise para dois grupos de eventos: os que foram reconhecidos pelo governo federal e os que não foram reconhecidos. Dessa forma, pudemos comparar os tópicos mais comuns em cada grupo e entender se havia diferenças importantes nos temas tratados.

## Agrupamento por temas

### Eventos reconhecidos

| **Tópico**    | **Palavras Principais**                                      | **Count** | **Descrição Principal**                                                                 | **Conclusão**                                                                                                                                                               |
|---------------|--------------------------------------------------------------|----------|------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -1 (outliers) | rio, ponte, bairro, rua                                       | 47.736   | Outliers - menciona locais como rio, ponte, bairro, rua.                                 | Muitos documentos foram classificados como outliers, indicando que são muito variados ou genéricos. Pode ser necessário revisar os conteúdos desses tópicos.                |
| 0             | houvexd, hiuve, xd                                            | 1.070    | Palavras como "houvexd" sugerem ruído ou erro de processamento.                          | Este tópico parece conter erros no texto. Pode ser necessário revisar os conteúdos desses tópicos.                                 |
| 1             | telhados, telhas, telhado, fibrocimento                       | 971      | Relacionado a telhados e telhas de fibrocimento.                                          | Tópico claro sobre danos a telhados, provavelmente devido a tempestades ou vendavais. Relevante para desastres que afetam infraestruturas residenciais.                     |
| 2             | materiais, danos, hove, reparties                             | 569      | Danos materiais em geral.                                                                | Esse tópico abrange uma variedade de desastres com relatos sobre danos materiais, mas sem especificar detalhes. Pode incluir diversos tipos de eventos.                     |
| 3             | combustível, motorista, motoristas, manutenção                | 555      | Logística de veículos e combustível.                                                     | Relacionado a dificuldades logísticas, como motoristas e combustível, o que pode afetar a resposta a desastres ou a recuperação após o evento.                              |
| 4             | aplicam, diapessoa, abastecia, prolongado                     | 533      | Situações prolongadas de falta de serviços ou abastecimento.                             | Refere-se a eventos que causaram interrupção prolongada de serviços essenciais, como abastecimento de água ou energia, indicando impactos prolongados.                      |
| 5             | contaminação, fossas, coliformes, poluição                    | 419      | Contaminação e poluição relacionadas ao saneamento (fossas, coliformes).                 | Este tópico destaca problemas com saneamento, especialmente a contaminação de fossas sépticas, um problema comum em desastres que afetam áreas residenciais.                |
| 6             | plantações, plantio, plantão, irrigação                       | 412      | Agricultura - impactos em plantações e irrigação.                                        | Descreve o impacto de desastres no setor agrícola, como perda de plantações. Pode indicar desastres climáticos que afetam diretamente a produção agrícola.                  |
| 7             | desastres, hidrometeorológico, fomentando, consu...           | 387      | Desastres hidrometeorológicos (chuvas, enchentes, secas).                                | Tópico amplo que agrupa desastres causados por eventos meteorológicos extremos, como enchentes e secas. Relevante para reconhecer padrões em eventos severos.               |
| 8             | pontilhões, estradas, bueiros, pontes                         | 356      | Infraestrutura de transporte danificada (pontes, estradas, bueiros).                     | Desastres que causam danos à infraestrutura de transporte, dificultando o acesso a áreas. Esse tipo de dano é crucial para justificar reconhecimento federal.               |
| 9             | correspondente, ton, referente, quinhentos                    | 352      | Relacionado a perdas agrícolas, com menção a toneladas e quantidades de sacas perdidas.   | Este tópico envolve descrições de prejuízos econômicos associados à produção agrícola, destacando perdas de safra, o que pode influenciar pedidos de ajuda.                 |
| 10            | hectares, hectare, sacas, plantada                            | 347      | Descrição de áreas afetadas em hectares e quantidade de sacas perdidas.                   | Relacionado à área plantada e perdas associadas à agricultura. Este tópico reflete o impacto dos desastres em terras produtivas, um fator importante para o reconhecimento. |

### Eventos não reconhecidos

| **Tópico** | **Palavras Principais**                                      | **Count** | **Descrição Principal**                                                                  | **Conclusão**                                                                                                                                               |
|------------|--------------------------------------------------------------|----------|------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| -1         | rua, município, devido, pessoas                              | 4.666    | Outliers - menciona ruas e pessoas em municípios.                                         | Muitos documentos foram classificados como outliers, indicando que são diversos ou genéricos. Pode ser necessário revisar os conteúdos desses tópicos. |
| 0          | telhado, telhados, telhas, internet                          | 171      | Relacionado a telhados e possíveis danos por tempestades.                                 | Esse tópico trata de danos em telhados, com uma possível menção a serviços de internet. Relevante para desastres com impacto em infraestrutura doméstica.     |
| 1          | animal, humano, consumo, abasteciam                          | 166      | Relacionado ao abastecimento de água e consumo humano e animal.                           | Tópico relacionado à interrupção de abastecimento de água e consumo, afetando tanto humanos quanto animais. Isso pode indicar crises hídricas em áreas rurais. |
| 2          | rural, população, zona, iomer                                | 153      | Descreve impactos em áreas rurais.                                                        | Este tópico aborda desastres que afetam a população em áreas rurais, com impactos provavelmente associados a falta de recursos ou infraestrutura adequada.    |
| 3          | barragens, barragem, poços, cisternas                        | 121      | Relacionado a barragens, poços e cisternas.                                               | Tópico que se refere a desastres que impactam sistemas de abastecimento hídrico, como barragens e cisternas. Relevante para a gestão de água em áreas rurais. |
| 4          | escola, escolas, aulas, alunos                               | 119      | Impacto de desastres em escolas, com interrupção de aulas.                                | Este tópico está focado nos impactos sobre escolas e estudantes, indicando que os desastres resultaram na interrupção das atividades educacionais.             |
| 5          | casas, casa, alagadas, desalojadas                           | 116      | Descreve danos a casas, especialmente alagamentos e desalojados.                         | Tópico relacionado a casas alagadas e desalojamentos. Esses desastres parecem causar danos diretos a moradias, forçando as pessoas a saírem de suas casas.    |
| 6          | ambientais, ambiental, ambiente, danos                       | 104      | Relacionado a danos ambientais.                                                           | Esse tópico aborda danos ambientais, possivelmente relacionados à contaminação de solo, rios ou outros recursos naturais. Relevante para desastres ecológicos.|
| 7          | contaminação, solo, fossas, poluição                         | 103      | Relacionado à contaminação do solo e poluição.                                            | Problemas com contaminação de fossas e poluição do solo são destacados neste tópico, sugerindo que desastres podem ter impacto direto na saúde pública.       |
| 8          | famílias, parentes, família, casa                            | 102      | Descreve o impacto nas famílias e moradias.                                               | Tópico focado nos efeitos dos desastres sobre famílias e suas casas, possivelmente refletindo perdas materiais e deslocamento de famílias.                    |
| 9          | plantações, plantio, decorrente, agricultura                 | 98       | Impacto em plantações e agricultura.                                                      | Este tópico trata dos danos à agricultura, com menção a plantações e problemas decorrentes de desastres que afetam diretamente a produção agrícola.           |
| 10         | estradas, pontes, bueiros, estrada                           | 97       | Relacionado a danos em estradas, pontes e bueiros.                                        | Desastres que causaram danos à infraestrutura rodoviária, afetando estradas e pontes. Esse tipo de dano é importante para a mobilidade e resposta a emergências.|

## Visualização dos resultados

Intertopic Distance Map

| ![Intertopic Distance Map - Eventos Reconhecidos](../figures/bertTopic_reconhecidos.png) | ![Intertopic Distance Map - Eventos não reconhecidos](../figures/berTopic_naoreconhecidos.png) |
|:----------------------------------------------------------------------------------------:|:----------------------------------------------------------------------------------------------:|
|                      Intertopic Distance Map - Eventos Reconhecidos                      |                       Intertopic Distance Map - Eventos Não Reconhecidos                       |



## Conclusões

A análise dos tópicos identificados revelou algumas diferenças entre os eventos reconhecidos e não reconhecidos. 

Nos eventos reconhecidos, observou-se uma maior concentração de tópicos relacionados a temas como danos à infraestrutura, contaminação e impacto na agricultura, o que sugere padrões mais consistentes e previsíveis. 

Por outro lado, os eventos não reconhecidos apresentaram uma maior diversidade temática e menos consistência nos temas, o que pode indicar que esses desastres foram mais variados, dificultando o reconhecimento federal.

A maior diversidade e falta de consistência nos temas dos eventos não reconhecidos pode dificultar o desenvolvimento de um modelo de machine learning para identificar automaticamente esses casos. Essa falta de padrões claros torna mais difícil para o modelo aprender a diferenciar eventos reconhecidos de não reconhecidos.