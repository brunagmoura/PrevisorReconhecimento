## Base de dados

A base de dados utilizada neste projeto reúne informações provenientes de diferentes fontes relevantes. Os dados sobre desastres foram disponibilizados pela Secretaria Nacional de Proteção e Defesa Civil (SEDEC/MIDR) e estão organizados no Atlas Digital de Desastres. Além disso, as informações sobre famílias em situação de vulnerabilidade social foram obtidas a partir do Cadastro Único (CadÚnico), enquanto os dados sobre os municípios brasileiros foram fornecidos pelo IBGE.

<style>
table {
  table-layout: fixed;
  width: 100%;
}

td, th {
  font-size: 8px;
  word-wrap: break-word; /* Para quebrar o texto */
}

th:nth-child(1), td:nth-child(1) {
  width: 100px; /* Tamanho da primeira coluna */
}

th:nth-child(2), td:nth-child(2) {
  width: 150px; /* Tamanho da segunda coluna */
}
</style>

| Variável | Descrição | Tipo de variável | Período | Resumo metodologia | Fonte | Observação |
| --- | --- | --- | --- | --- | --- | --- |
| Protocolo_S2iD | Protocolo de identificação do evento | Str | 2010-2024 | - | Atlas digital de desastres | - |
| Nome_Municipio | Nome do município | Str | 2010-2024 | - | - | - |
| Sigla_UF | Unidade da federação do município | Str | 2010-2024 | - | - | - |
| regiao | Região do município | Str | 2010-2024 | - | - | - |
| Data_Registro | Data de registro do evento | Data | 2010-2024 | - | - | - |
| Data_Evento | Data do evento | Data | 2010-2024 | - | - | - |
| codigo_ibge | Código IBGE identificador do município | Str | 2010-2024 | - | - | - |
| Setores Censitários | - | - | 2010-2024 | - | Atlas digital de desastres | - |
| Status | Reconhecido / Não reconhecido | Texto | 2010-2024 | - | - | - |
| DH_Descricao | Descrição dos danos humanos | Texto | 2010-2024 | - | Atlas digital de desastres | - |
| DH_MORTOS | Qtde. mortos | Int | 2010-2024 | Pessoas que perderam suas vidas em decorrência direta dos efeitos do desastre | Atlas digital de desastres | - |
| DH_FERIDOS | Qtde. feridos | Int | 2010-2024 | Pessoas que sofreram lesões em decorrência direta dos efeitos do desastre e necessitam de intervenção médico-hospitalar, materiais e insumos de saúde (medicamentos, médicos, etc.) | Atlas digital de desastres | - |
| DH_ENFERMOS | Qtde. enfermos | Int | 2010-2024 | Pessoas que desenvolveram processos patológicos em decorrência direta dos efeitos do desastre. | Atlas digital de desastres | - |
| DH_DESABRIGADOS | Qtde. desabrigados | Int | 2010-2024 | Pessoas que necessitam de abrigo público, como habitação temporária, em função de danos ou ameaça de danos causados em decorrência direta dos efeitos do desastre. | Atlas digital de desastres | - |
| DH_DESALOJADOS | Qtde. desalojados | Int | 2010-2024 | Pessoas que, em decorrência dos efeitos do desastre, desocuparam seus domicílios, mas não necessitam de abrigo público. | Atlas digital de desastres | - |
| DH_DESAPARECIDOS | Qtde. desaprecidos | Int | 2010-2024 | Pessoas que necessitam ser encontradas, pois, em decorrência direta dos efeitos do desastre, estão em situação de risco de morte iminente e em locais inseguros/perigosos. | Atlas digital de desastres | - |
| DH_OUTROS AFETADOS | Qtde. outros afetados | Int | 2010-2024 | Pessoas afetadas diretamente pelo desastre (excetuando as já informadas acima) | Atlas digital de desastres | - |
| DH_total_danos_humanos | Total de danos humanos reportados no evento | Int | 2010-2024 | Danos humanos reportados pelos municípios ao Ministério da Integração e Desenvolvimento Regional em situações de desastres com o objetivo de solicitar recursos para as ações de resposta e reconstrução. Os dados são coletados no Sistema Integrado de Informações sobre Desastres (S2ID). Os danos humanos correspondem ao quantitativo de pessoas mortas, feridas, enfermas, desabrigadas, desalojadas, desaparecidas e outras diretamente afetadas. Mais informações: https://atlasdigital.mdr.gov.br/arquivos/Atlas_Digital_Desastres_Manual_Aplicacao.pdf | Atlas digital de desastres | - |
| DM_Descricao | Descrição dos danos materiais | Str | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Uni Habita Danificadas | Qtde. unidades habitacionais danificadas | Int | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Uni Habita Destruidas | Qtde. unidades habitacionais destruídas | Int | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Uni Habita Valor | Valor estimado das unidades habitacionais atingidas | Int (R$) | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Inst Saúde Danificadas | Qtde. instalações de saúde danificadas | Int | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Inst Saúde Destruidas | Qtde. instalações de saúde destruídas | Int | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Inst Saúde Valor | Valor estimado das instituições de saúde atingidas | Int (R$) | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Inst Ensino Danificadas | Qtde. instituições de ensino danificadas | Int | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Inst Ensino Destruidas | Qtde. instituições de ensino destruídas | Int | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Inst Ensino Valor | Valor estimado das instituições de ensino atingidas | Int (R$) | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Inst Serviços Danificadas | Qtde. instituições de serviços públicos danificadas | Int | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Inst Serviços Destruidas | Qtde. instituições de serviços públicos destruídas | Int | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Inst Serviços Valor | Valor estimado das instituições de serviços públicos atingidas | Int (R$) | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Inst Comuni Danificadas | Qtde. instituições comunitárias danificadas | Int | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Inst Comuni Destruidas | Qtde. instituições comunitárias destruídas | Int | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Inst Comuni Valor | Valor estimado das instituições comunitárias de serviços públicos | Int (R$) | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Obras de Infra Danificadas | Qtde. obras de infraestrutura danificadas | Int | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Obras de Infra Destruidas | Qtde. obras de infraestrutura destruídas | Int | 2010-2024 | - | Atlas digital de desastres | - |
| DM_Obras de Infra Valor | Valor estimado das obras de infraestrutura atingidas | Int (R$) | 2010-2024 | - | Atlas digital de desastres | - |
| DM_total_danos_materiais | Danos materiais reportados no evento | Int | 2010-2024 | Danos materiais reportados pelos municípios ao Ministério da Integração e Desenvolvimento Regional em situações de desastres com o objetivo de solicitar recursos para as ações de resposta e reconstrução. Os dados são coletados no Sistema Integrado de Informações sobre Desastres (S2ID). Os danos materiais correspondem ao valor estimado de danos às unidades habitacionais, instalações públicas de saúde, instalações públicas de ensino, instalações públicas prestadoras de outros serviços, instalações públicas de uso comunitário e obras de infraestrutura pública danificadas ou destruídas pelo desastre. Mais informações: https://atlasdigital.mdr.gov.br/arquivos/Atlas_Digital_Desastres_Manual_Aplicacao.pdf | Atlas digital de desastres | - |
| DA_Descricao | Descrição dos danos ambientais | Str | 2010-2024 | Descrição dos danos ambientais e sua relação direta com os efeitos do desastre | Atlas digital de desastres | - |
| DA_Polui/cont da água | Poluição ou contaminação da água | Str | 2010-2024 | - | Atlas digital de desastres | - |
| DA_Polui/cont do ar | Poluição ou contaminação do ar | Str (faixa de valor) | 2010-2024 | - | Atlas digital de desastres | - |
| DA_Polui/cont do solo | Poluição ou contaminação do solo | Str (faixa de valor) | 2010-2024 | - | Atlas digital de desastres | - |
| DA_Dimi/exauri hídrico | Diminuição ou exaurimento hídrico | Str (faixa de valor) | 2010-2024 | - | Atlas digital de desastres | - |
| DA_Incêndi parques/APAs/APPs | Incêndios em parques, APA's ou APP's | Str (faixa de valor) | 2010-2024 | - | Atlas digital de desastres | - |
| PEPL_Descricao | Descrição dos prejuízos econômicos públicos | Str | 2010-2024 | Descrição dos serviços essenciais públicos prejudicados ou interrompidos. | Atlas digital de desastres | - |
| PEPL_Assis_méd e emergên(R$) | Prejuízo econômico público em assistência médica | Float (R$) | 2010-2024 | Valor estimado do prejuízo econômico público com assistência médica, saúde pública e atendimento de emergências médicas. | Atlas digital de desastres | - |
| PEPL_Abast de água pot(R$) | Prejuízo econômico público em assistência médica | Float (R$) | 2010-2024 | Valor estimado do prejuízo econômico público com abastecimento de água potável | Atlas digital de desastres | - |
| PEPL_sist de esgotos sanit(R$) | Prejuízo econômico público em esgoto | Float (R$) | 2010-2024 | Valor estimado do prejuízo econômico público com esgoto de águas pluviais e sistema de esgotos sanitários | Atlas digital de desastres | - |
| PEPL_Sis limp e rec lixo (R$) | Prejuízo econômico público em limpeza urbana | Float (R$) | 2010-2024 | Valor estimado do prejuízo econômico público com sistema de limpeza urbana e de recolhimento e destinação do lixo | Atlas digital de desastres | - |
| PEPL_Sis cont pragas (R$) | Prejuízo econômico público em controle de pragas | Float (R$) | 2010-2024 | Valor estimado do prejuíuzo econômico público com sistema de desinfestação e controle de pregas e vetores | Atlas digital de desastres | - |
| PEPL_distrib energia (R$) | Prejuízo econômico público em distribuição de energia | Float (R$) | 2010-2024 | Valor estimado do prejuízo econômico público com geração e distribuição de energia elétrica | Atlas digital de desastres | - |
| PEPL_Telecomunicações (R$) | Prejuízo econômico público em telecomunicações | Float (R$) | 2010-2024 | Valor estimado do prejuízo econômico público com telecomunicações | Atlas digital de desastres | - |
| PEPL_Tran loc/reg/l_curso (R$) | Prejuízo econômico público em transportes | Float (R$) | 2010-2024 | Valor estimado do prejuízo econômico público com transportes locais, regionais e de longo curso | Atlas digital de desastres | - |
| PEPL_Distrib combustíveis(R$) | Prejuízo econômico público em distribuição de combustíveis | Float (R$) | 2010-2024 | Valor estimado do prejuízo econômico público com distribuição de combustíveis, especialmente de uso doméstico | Atlas digital de desastres | - |
| PEPL_Segurança pública (R$) | Prejuízo econômico público em segurança púb;ica | Float (R$) | 2010-2024 | Valor estimado do prejuízo econômico público com segurança pública | Atlas digital de desastres | - |
| PEPL_Ensino (R$) | Prejuízo econômico público em ensino | Float (R$) | 2010-2024 | Valor estimado do prejuízo econômico público com esnino | Atlas digital de desastres | - |
| PEPL_total_publico | Prejuízos públicos totais | Float (R$) | 2010-2024 | Valor total dos prejuízos econômicos públicos. O valor é informado pelo município a partir do prejuízo econômico público estimado com os serviços essenciais prejudicados. | Atlas digital de desastres | - |
| PEPR_Descricao | Descrição dos prejuízos econômicos privados | Str | 2010-2024 | Descrição dos setores econômicos prejudicados pelo evento | Atlas digital de desastres | - |
| PEPR_Agricultura (R$) | Prejuízo econômico privado em agricultura | Valor (R$) | 2010-2024 | Valor estimado do prejuízo econômico privado do setor da agricultura em decorrência direta dos efeitos do desastre | Atlas digital de desastres | - |
| PEPR_Pecuária (R$) | Prejuízo econômico privado em pecuária | Valor (R$) | 2010-2024 | Valor estimado do prejuízo econômico privado do setor da pecuária  em decorrência direta dos efeitos do desastre | Atlas digital de desastres | - |
| PEPR_Indústria (R$) | Prejuízo econômico privado em indústria | Valor (R$) | 2010-2024 | Valor estimado do prejuízo econômico privado do setor da indústria  em decorrência direta dos efeitos do desastre | Atlas digital de desastres | - |
| PEPR_Comércio (R$) | Prejuízo econômico privado em comércio | Valor (R$) | 2010-2024 | Valor estimado do prejuízo econômico privado do setor de comércio  em decorrência direta dos efeitos do desastre | Atlas digital de desastres | - |
| PEPR_Serviços (R$) | Prejuízo econômico privado em serviços | Valor (R$) | 2010-2024 | Valor estimado do prejuízo econômico privado do setor de serviços  em decorrência direta dos efeitos do desastre | Atlas digital de desastres | - |
| PEPR_total_privado | Prejuízos privados totais | Valor acumulado (R$) | 2010-2024 | Descrição dos efeitos do desastre sobre os prejuízos econômicos privados. | Atlas digital de desastres | - |
| PE_PLePR | Prejuízos públicos e privados totais | Valor (R$) | 2010-2024 | Valor total dos prejuízos econômicos públicos e privados | Atlas digital de desastres | - |
| Ano_Evento | Ano do desastre | Numérica | 2010-2024 | - | - | - |
| Empenhado | Valor empenhado em gestão de riscos e desastres | Valor (R$) | 2010-2024 | - | - | - |
| DensidadePop | Densidade populacional | Float (índice) | 2010-2024 | População / Área | - | - |
| Area | Área | Int (km2) | 2010-2024 | - | Censo IBGE 2022 | Cada município tem apenas um valor de área. E esse valor tem como fonte o Censo IBGE 2022. |
| Municipio - UF | Município - Unidade da Federação | Str | 2010-2024 | - | - | - |
| PIB | Produto Interno Bruto | Float (R$) | 2010-2021 | - | PIB Municipal. IBGE. | - |
| DOMICILIO_AREARURAL | Qtde. domicílios na área rural | Int | 2018-2024 | - | CadÚnico (CGUData) | - |
| PDEFAGUA | Participação percentual de pessoas inscritas no Cadastro Único residentes em domicílios sem abastecimento de água adequado no total de pessoas inscritas no Cadastro Único. Considera-se adequado o abastecimento de água por meio de rede geral de distribuição e canalização interna. Foram excluídas as pessoas pertencentes a famílias com mais de 2 anos sem atualização do cadastro. A referência deste indicador é o mês de dezembro de cada ano. | Int | 2018-2024 | Razão entre o número de pessoas inscritas no Cadastro Único residentes em domicílios sem abastecimento de água adequado e o total de pessoas inscritas no Cadastro Único, multiplicado por 100. Considera-se adequado o abastecimento de água por meio de rede geral de distribuição e canalização interna. | CadÚnico (CGUData) | - |
| PDEFESGOTO | Participação percentual de pessoas inscritas no Cadastro Único residentes em domicílios sem banheiro ou com banheiro mas sem esgotamento sanitário adequado no total de pessoas inscritas no Cadastro Único. Considera-se adequado o esgotamento sanitário através de rede coletora de esgoto ou pluvial ou de fossa séptica. Foram excluídas as pessoas pertencentes a famílias com mais de 2 anos sem atualização do cadastro. A referência deste indicador é o mês de dezembro de cada ano. | Int | 2018-2024 | Razão entre o número de pessoas inscritas no Cadastro Único residentes em domicílios sem banheiro ou com banheiro mas sem esgotamento sanitário adequado e o total de pessoas inscritas no Cadastro Único, multiplicado por 100. Considera-se adequado o esgotamento sanitário através de rede coletora de esgoto ou pluvial ou de fossa séptica. | CadÚnico (CGUData) | - |
| PDEFLIXO | Participação percentual de pessoas inscritas no Cadastro Único residentes em domicílios sem coleta de lixo adequada no total de pessoas inscritas no Cadastro Único. Considera-se adequada a coleta de lixo direta ou indireta. Foram excluídas as pessoas pertencentes a famílias com mais de 2 anos sem atualização do cadastro. A referência deste indicador é o mês de dezembro de cada ano. | Int | 2018-2024 | Razão entre o número de pessoas inscritas no Cadastro Único residentes em domicílios sem coleta de lixo adequada e o total de pessoas inscritas no Cadastro Único, multiplicado por 100. Considera-se adequada a coleta de lixo direta ou indireta. | CadÚnico (CGUData) | - |
| PDEFSAN | Participação percentual de pessoas inscritas no Cadastro Único sem abastecimento de água, esgotamento sanitário e coleta de lixo adequados no total de pessoas inscritas no Cadastro Único. Consideram-se adequados: abastecimento de água por meio de rede geral de distribuição e canalização interna; esgotamento sanitário através de rede coletora de esgoto ou pluvial ou de fossa séptica; e coleta de lixo direta ou indireta. Foram excluídas as pessoas pertencentes a famílias com mais de 2 anos sem atualização do cadastro. A referência deste indicador é o mês de dezembro de cada ano. | Int | 2018-2024 | Razão entre o número de pessoas inscritas no Cadastro Único sem abastecimento de água, esgotamento sanitário e coleta de lixo adequados e o total de pessoas inscritas no Cadastro Único, multiplicado por 100. | CadÚnico (CGUData) | - |
| QTDE_FAMILIAS_ATUALIZADA | Qtde. famílias inscritas no CadÚnico | Int | 2018-2024 | - | CadÚnico (CGUData) | - |
| Cod_Cobrade | Classificação e Codificação Brasileira de Desastres | Str | 2010-2024 | O código Cobrade se divide em "Categoria", "Grupo", "Subgrupo" e "Tipo" | Classificação e Codificação Brasileira de Desastres | - |
| Categoria | Categoria do desastre | Str | 2010-2024 | - | - | - |
| Grupo | Grupo do desastre | Str | 2010-2024 | - | - | - |
| Subgrupo | Subgrupo do desastre | Str | 2010-2024 | - | - | - |
| Tipo | Tipo do desastre | Str | 2010-2024 | - | - | - |
| Pop | População residente | Int | 2010-2024 | - | Censo IBGE 2010. Censo IBGE 2022. Para os demais anos: estimativa IBGE. | - |
</p>
A tabela a seguir apresenta os códigos da Classificação e Codificação Brasileira de Desastres (COBRADE), juntamente com seus respectivos significados, facilitando a compreensão dos tipos e categorias de desastres catalogados.

| COBRADE | Categoria  | Grupo                                                      | Subgrupo                               | Tipo                                                | Subtipo                                              |
|---------|------------|------------------------------------------------------------|----------------------------------------|-----------------------------------------------------|-----------------------------------------------------|
| 11110   | Natural     | Geológico                                                  | Terremoto                              | Tremor de terra                                     |                                                     |
| 11120   | Natural     | Geológico                                                  | Terremoto                              | Tsunami                                             |                                                     |
| 11200   | Natural     | Geológico                                                  | Emanação vulcânica                      |                                                     |                                                     |
| 11311   | Natural     | Geológico                                                  | Movimento de massa                     | Quedas, Tombamentos e rolamentos                    | Blocos                                              |
| 11312   | Natural     | Geológico                                                  | Movimento de massa                     | Quedas, Tombamentos e rolamentos                    | Lascas                                              |
| 11313   | Natural     | Geológico                                                  | Movimento de massa                     | Quedas, Tombamentos e rolamentos                    | Matacões                                            |
| 11314   | Natural     | Geológico                                                  | Movimento de massa                     | Quedas, Tombamentos e rolamentos                    | Lajes                                               |
| 11321   | Natural     | Geológico                                                  | Movimento de massa                     | Deslizamentos                                       | Deslizamentos de solo e ou rocha                    |
| 11331   | Natural     | Geológico                                                  | Movimento de massa                     | Corridas de Massa                                   | Solo/Lama                                           |
| 11332   | Natural     | Geológico                                                  | Movimento de massa                     | Corridas de Massa                                   | Rocha/Detrito                                       |
| 11340   | Natural     | Geológico                                                  | Movimento de massa                     | Subsidências e colapsos                             |                                                     |
| 11410   | Natural     | Geológico                                                  | Erosão                                 | Erosão Costeira/Marinha                             |                                                     |
| 11420   | Natural     | Geológico                                                  | Erosão                                 | Erosão de Margem Fluvial                            |                                                     |
| 11431   | Natural     | Geológico                                                  | Erosão Continental                     | Laminar                                             |                                                     |
| 11432   | Natural     | Geológico                                                  | Erosão Continental                     | Ravinas                                             |                                                     |
| 11433   | Natural     | Geológico                                                  | Erosão Continental                     | Boçorocas                                           |                                                     |
| 12100   | Natural     | Hidrológico                                                | Inundações                             |                                                     |                                                     |
| 12200   | Natural     | Hidrológico                                                | Enxurradas                             |                                                     |                                                     |
| 12300   | Natural     | Hidrológico                                                | Alagamentos                            |                                                     |                                                     |
| 13111   | Natural     | Meteorológico                                              | Sistemas de Grande Escala/Escala Regional | Ciclones                                           | Ventos Costeiros (Mobilidade de Dunas)              |
| 13112   | Natural     | Meteorológico                                              | Sistemas de Grande Escala/Escala Regional | Ciclones                                           | Marés de Tempestade (Ressacas)                      |
| 13120   | Natural     | Meteorológico                                              | Sistemas de Grande Escala/Escala Regional | Frentes Frias/Zonas de Convergência                 |                                                     |
| 13211   | Natural     | Meteorológico                                              | Tempestades                            | Tempestade Local/Convectiva                         | Tornados                                            |
| 13212   | Natural     | Meteorológico                                              | Tempestades                            | Tempestade Local/Convectiva                         | Tempestade de Raios                                 |
| 13213   | Natural     | Meteorológico                                              | Tempestades                            | Tempestade Local/Convectiva                         | Granizo                                             |
| 13214   | Natural     | Meteorológico                                              | Tempestades                            | Tempestade Local/Convectiva                         | Chuvas Intensas                                     |
| 13215   | Natural     | Meteorológico                                              | Tempestades                            | Tempestade Local/Convectiva                         | Vendaval                                            |
| 13310   | Natural     | Meteorológico                                              | Temperaturas Extremas                  | Onda de Calor                                       |                                                     |
| 13321   | Natural     | Meteorológico                                              | Temperaturas Extremas                  | Onda de Frio                                        | Friagem                                             |
| 13322   | Natural     | Meteorológico                                              | Temperaturas Extremas                  | Onda de Frio                                        | Geadas                                              |
| 14110   | Natural     | Climatológico                                              | Seca                                   | Estiagem                                            |                                                     |
| 14120   | Natural     | Climatológico                                              | Seca                                   | Seca                                               |                                                     |
| 14131   | Natural     | Climatológico                                              | Seca                                   | Incêndio Florestal                                  | Incêndios em Parques, Áreas de Proteção Ambiental e Áreas de Preservação Permanente Nacionais, Estaduais ou Municipais |
| 14132   | Natural     | Climatológico                                              | Seca                                   | Incêndio Florestal                                  | Incêndios em áreas não protegidas, com reflexos na qualidade do ar |
| 14140   | Natural     | Climatológico                                              | Seca                                   | Baixa Umidade do Ar                                 |                                                     |
| 15110   | Natural     | Biológico                                                  | Epidemias                              | Doenças infecciosas virais                          |                                                     |
| 15120   | Natural     | Biológico                                                  | Epidemias                              | Doenças infecciosas bacterianas                    |                                                     |
| 15130   | Natural     | Biológico                                                  | Epidemias                              | Doenças infecciosas parasíticas                    |                                                     |
| 15140   | Natural     | Biológico                                                  | Epidemias                              | Doenças infecciosas fúngicas                       |                                                     |
| 15210   | Natural     | Biológico                                                  | Infestações/Pragas                     | Infestações de animais                             |                                                     |
| 15221   | Natural     | Biológico                                                  | Infestações/Pragas                     | Infestações de algas                               | Marés vermelhas                                     |
| 15222   | Natural     | Biológico                                                  | Infestações/Pragas                     | Infestações de algas                               | Ciano bactérias em reservatórios                    |
| 15230   | Natural     | Biológico                                                  | Infestações/Pragas                     | Outras Infestações                                 |                                                     |
| 21110   | Tecnológico | Desastres Relacionados a Substâncias radioativas           | Desastres siderais com riscos radioativos | Queda de satélite (radionuclídeos)                 |                                                     |
| 21210   | Tecnológico | Desastres Relacionados a Substâncias radioativas           | Desastres com substâncias e equipamentos radioativos de uso em pesquisas, indústrias e usinas nucleares | Fontes radioativas em processos de produção        |                                                     |
| 21310   | Tecnológico | Desastres Relacionados a Substâncias radioativas           | Desastres relacionados com riscos de intensa poluição ambiental provocada por resíduos radioativos | Outras fontes de liberação de radionuclídeos para o meio ambiente |
| 22110   | Tecnológico | Desastres Relacionados a Produtos Perigosos                | Desastres em plantas e distritos industriais, parques e armazenamentos com extravasamento de produtos perigosos | Liberação de produtos químicos para a atmosfera causada por explosão ou incêndio |
| 22210   | Tecnológico | Desastres Relacionados a Produtos Perigosos                | Desastres relacionados à contaminação da água     | Liberação de produtos químicos nos sistemas de água potável |
| 22220   | Tecnológico | Desastres Relacionados a Produtos Perigosos                | Desastres relacionados à contaminação da água     | Derramamento de produtos químicos em ambiente lacustre, fluvial, marinho e aquíferos |
| 22310   | Tecnológico | Desastres Relacionados a Produtos Perigosos                | Desastres Relacionados a Conflitos Bélicos        | Liberação produtos químicos e contaminação como consequência de ações militares |
| 22410   | Tecnológico | Desastres Relacionados a Produtos Perigosos                | Desastres relacionados a transporte de produtos perigosos | Transporte rodoviário                              |                                                     |
| 22420   | Tecnológico | Desastres Relacionados a Produtos Perigosos                | Desastres relacionados a transporte de produtos perigosos | Transporte ferroviário                             |                                                     |
| 22430   | Tecnológico | Desastres Relacionados a Produtos Perigosos                | Desastres relacionados a transporte de produtos perigosos | Transporte aéreo                                   |                                                     |
| 22440   | Tecnológico | Desastres Relacionados a Produtos Perigosos                | Desastres relacionados a transporte de produtos perigosos | Transporte dutoviário                              |                                                     |
| 22450   | Tecnológico | Desastres Relacionados a Produtos Perigosos                | Desastres relacionados a transporte de produtos perigosos | Transporte marítimo                                |                                                     |
| 22460   | Tecnológico | Desastres Relacionados a Produtos Perigosos                | Desastres relacionados a transporte de produtos perigosos | Transporte aquaviário                              |                                                     |
| 23110   | Tecnológico | Desastres Relacionados a Incêndios Urbanos                 | Incêndios urbanos                          | Incêndios em plantas e distritos industriais, parques e
