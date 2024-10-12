## Sobre o projeto

O projeto **Previsor de reconhecimento federal** tem como objetivo prever se um desastre registrado no sistema **S2ID** (Sistema Integrado de Informações sobre Desastre) resultará no reconhecimento federal de um estado de calamidade pública ou situação de emergência.

Este projeto foi desenvolvido no âmbito do *bootcamp* em *Machine Learning* promovido pela Escola Nacional de Administração Pública (Enap), turma de outubro de 2024.

## Principais conceitos

### Sistema S2ID

Os municípios ou estados afetados por um desastre registram estes eventos no Sistema Integrado de Informações sobre Desastres (S2ID). O registro é obrigatório para a solicitação de reconhecimento federal e a solicitação de recursos para as ações de resposta e para obras de reconstrução.

### Desastre e reconhecimento federal

A Portaria nº 3.646, de 20 de dezembro de 2022 do Ministério da Integração e Desenvolvimento Regional (MIDR) e o Decreto nº 10.593, de 24 de dezembro de 2020, estabelecem as principais diretrizes sobre o Sistema Nacional de Proteção e Defesa Civil e o Sistema Nacional de Informações sobre Desastres.

Os seguintes conceitos são relevantes para compreender os testes realizados ao longo deste projeto:

| Conceito        | Descrição                                                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Desastre        | Evento adverso, natural ou antrópico, que provoca danos humanos, materiais ou ambientais, e prejuízos econômicos e sociais.                                       |
| Estado de Calamidade Pública (ECP)| Situação provocada por desastre que compromete substancialmente a capacidade de resposta do Poder Público, exigindo medidas administrativas excepcionais.          |
| Situação de Emergência (SE)| Situação anormal causada por desastre que compromete parcialmente a capacidade de resposta do ente federativo, também demandando medidas excepcionais.             |
| Dano            | Impacto direto do evento adverso, deteriorando as condições humanas, materiais ou ambientais.                                                                     |
| Prejuízo Econômico | Perda econômica resultante dos danos, impactando a renda, infraestrutura e setores produtivos do território afetado.                                              |
| Prejuízo Social | Alteração na normalidade social causada pelo desastre, provocando mudanças na rotina, mobilidade e convivência das pessoas.                                        |

Para que seja realizado o reconhecimento federal do ECP ou da SE, o seguinte fluxo deve ser seguido.

```{figure} ./figures/fluxo_reconhecimento.png
:name: fluxo-reconhecimento

Fluxo para o reconhecimento federal de ECP e SE
```

Conforme ilustrado na imagem acima, a análise do processo passa por diferentes níveis de avaliação, envolvendo o analista, coordenador, diretor e, por fim, o secretário, que decide pelo reconhecimento ou indeferimento do Estado de Calamidade Pública (ECP) ou da Situação de Emergência (SE).

Nesse contexto, a aplicação de técnicas de machine learning pode contribuir para agilizar a análise, reduzindo custos e aumentando a eficiência do processo de tomada de decisão.

## Base de dados

A base de dados utilizada neste projeto foi extraída de diversas fontes de dados.

A tabela a seguir apresenta a origem de cada variável e a sua descrição.

## Conteúdo deste livro

```{tableofcontents}
```
