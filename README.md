# Workshop - Projeto de API com FastAPI, Nginx, PostgreSQL e Docker

Este projeto tem como objetivo criar uma API web escalável utilizando Docker, Nginx como balanceador de carga, e PostgreSQL como banco de dados.

## Estrutura
Todo projeto deve ter um Dockerfile e um docker-compose.yml

`nginx` - É o tirador de pidido

`Dockerfile` - Arquivo com instruções para rodar a aplicação
`docker-compose.yml` - O arquivo é uma "mine-infraestrutura"

## Arquitetura
O projeto é composto por várias partes:

API: A aplicação principal, construída em Python utilizando o framework FastAPI. A API será dividida em duas instâncias para garantir alta disponibilidade e escalabilidade. Cada instância é independente e capaz de lidar com requisições de forma independente, o que melhora a capacidade de resposta e a tolerância a falhas do sistema.

Nginx: Servidor proxy que atua como um balanceador de carga distribuindo as requisições entre as duas instâncias da API. Ele gerencia o tráfego de entrada e saída, melhorando o desempenho, a confiabilidade e a segurança do sistema. O Nginx permite uma distribuição uniforme do tráfego entre as instâncias da API, garantindo uma utilização eficiente dos recursos disponíveis.

PostgreSQL: Banco de dados relacional utilizado para armazenar os dados da aplicação. O PostgreSQL oferece recursos avançados de gerenciamento de dados e é altamente confiável e escalável, tornando-o uma escolha ideal para aplicativos web.

Docker: Utilizado para encapsular cada componente da aplicação em contêineres isolados, garantindo que a aplicação seja executada de maneira consistente em diferentes ambientes. O Docker simplifica o processo de desenvolvimento, implantação e escalabilidade da aplicação.

## Configuração
Para executar o projeto, você precisará ter o Docker instalado na sua máquina. Depois de clonar este repositório, siga as etapas abaixo:

No terminal, navegue até o diretório do projeto.

Execute o comando docker-compose up --build para construir e iniciar os contêineres.

Após a construção dos contêineres, você poderá acessar a API através do endereço http://localhost.

O banco de dados PostgreSQL estará disponível na porta 5432.

O servidor Nginx estará disponível na porta 80.

## Utilização
Para interagir com a API, você pode enviar requisições HTTP para os endpoints fornecidos pela aplicação. Consulte a documentação da API para obter informações detalhadas sobre os endpoints disponíveis.

Você pode monitorar os logs dos contêineres para depurar possíveis problemas ou acompanhar o desempenho da aplicação.

Para encerrar a execução dos contêineres, pressione Ctrl + C no terminal e execute o comando docker-compose down.