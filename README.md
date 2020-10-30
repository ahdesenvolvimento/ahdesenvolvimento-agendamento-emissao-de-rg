# Aplicação Web como forma de facilitar a emissão de RG no estado do Piauí

## Descrição
-  Devido à demora e à dificuldade que algumas pessoas tem de tirar seu RG (principalmente as que moram em locais situados longe de postos de emissão), esse projeto tem como objetivo 
apresentar uma solução que reduza o tempo desse processo, por meio de um site de agendamento de atendimentos.

## Público alvo
- Qualquer pessoa que deseje fazer a emissão do documento

## Problema a ser resolvido
- Permitir que cidadões possam agendar atedimentos para evitar deslocamento desnecessário a SSP

## Funcionalidades básicas que o sistema deveria contemplar
1. Realizar agendamento
2. Confirmar agendamento
3. Visualizar agendamentos do dia
4. Cadastrar datas e horários para agendamento
5. Excluir datas e horários
6. Alterar datas e horários
7. Alterar dados cadastrais
8. Visualizar perfil
9. Cadastrar funcionário
10. Excluir funcionário
11. Visualizar funcionários
12. Visualizar status do agendamento
13. Alterar agendamento
14. Excluir agendamento
15. Visualizar datas e horários disponíveis

## Justificativa
- Apesar da existência de postos para emitir o RG, ainda há regiões que não os possuem, fazendo assim, habitantes se deslocarem grandes distancias para enfrentar filas e disputar uma média de cerca de 70 senhas por dia para serem atendidos. A justificativa se dá através da criação de um site de agendamento multiplataforma, que fará a entrada de dados, agendamento do atendimento e notificação da carteira quando estiver pronta, buscando agilizar o processo de emissão do RG.

## Fundamentação teórica
- Nesse tópico, são apresentados os conceitos e as definições dos elementos fundamentais que contextualizam tecnologicamente o tema, com o objetivo de dar uma breve introdução sobre cada.
1.	Sistema Gerenciador de Banco de Dados
- De acordo com Laudon e Laudon, SGBD é um software especifico usado para criar, armazenar, organizar e acessar dados a partir de um banco de dados[2], é o conjunto de softwares responsáveis pelo gerenciamento de um banco de dados. Existem vários tipos de SGBDs no mercado, gratuitos e pagos, o que será utilizado nesse projeto será o PostgreSQL.
2.	Python
- Para Borges[3], Python é uma linguagem de altíssimo nível orientada a obejto, de tipagem dinâmica e forte, interpretada e interativa. Este se diferencia por ter uma sintaxe mais clara e simples, que favorece na legibilade do código fonte, tornando a linguagem mais produtiva.
3.	Framework Django de desenvolvimento python
- Framework é um conjunto de classes que incorpora um projeto abstrato para soluções de famílias de problemas associados. Em outras palavras framework é um projeto e uma implementação parcial de uma aplicação para um dado domínio do problema. O framework para o desenvolvimento é a base de onde se pode desenvolver algo maior ou mais específico. É uma coleção de códigos-fonte, classes, funções, técnicas e metodologias que facilitam o desenvolvimento de novos softwares, afirma Minetto[4].
4.	Metodologia Scrum
- A abordagem Scrum(SCHWABER, 2004; SCHWABER e BEEDLE, 2001) é um método ágil geral, mas seu foco está no gerenciamento do desenvolvimento iterativo, ao invés das abordagens técnicas específicas da engenharia de software ágil. Consiste em um projeto que será divido em fases, os sprints, do qual dentro de cada fase será executada uma etapa do projeto.

## Ojetivo geral
- Apresentar uma proposta de site de agendamento de atendimentos, com o propósito de agilizar o processo de emissão de RG e diminuir sua burocracia.

## Ojetivos específicos
- Aumentar o número de atendimentos diários
- Maior praticidade na execução da rotina
- Gerar satisfação dos usuários

## Metodologia de execução do projeto
- Levantamento de requisitos
- Modelagem do banco de dados
- Para construção do site, será utilizado o SGBD PostgreSQL, com auxilio do pgAdmin e as ferramentas de desenvolvimento web serão o HTML, CSS (Bootstrap), JavaScript e Django.

## Resultados esperados e disseminação dos resultados
-Após a conclusão do projeto, espera-se que ocorra um aumento na velocidade de emissão do RG e do número de pessoas atendidas em postos de emissão por dia, além de uma satisfação por parte dos que utilizaram o site. Em relação à divulgação, pode ser feita por meio de propagandas e panfletos.

## Acompanhamento e Avaliação do Projeto Durante a Execução
- O projeto foi divido, primeiramente, em cinco sprints, com duração em torno de uma semana, cada, sendo avaliado diretamente pelo professor Ely por relatórios e pela própria equipe durante todo o projeto, por meio de reuniões.

## Referências
1. [1]	"Conheça todos os postos para emitir 1ª e 2ª via do RG e evite filas em Teresina",
https://www.oitomeia.com.br/noticias/2019/01/21/conheca-todos-os-postos-para-emitir-1a-e2a-via-do-rg-e-evite-filas-em-teresina/, Acessado em 25/02/2019.

2. [2]	Kenneth Laudon Jane Laudon, "Sistemas de Informação Gerenciais", Pearson Companion Website, 1991.

3. [3]	Luiz Eduardo Borges, "Python para Desenvolvedores", novatec, 2014.

4. [4]	Minetto Elton Luís. "Frameworks para Desenvolvimento em PHP", novatec, 2007.

