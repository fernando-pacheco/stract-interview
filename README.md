# API de Relatórios - Processo Seletivo Stract

Bem-vindo à minha resolução do desafio da Stract! Este repositório contém um servidor em `Python + Flask` que consome os dados da API de contas de anúncio de clientes imaginários e gera relatórios em formato CSV.

## 📌 Instalação e Configuração

##### 1. Clonar o Repositório

```bash
git clone https://github.com/fernando-pacheco/stract-interview
cd stract-interview
```

##### 2. Criar e Ativar um Ambiente Virtual

```bash
python -m venv venv
source venv/bin/activate  # Para Linux/macOS
venv\Scripts\activate     # Para Windows
```

##### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

##### 4. Definir Variáveis de Ambiente

* Crie um arquivo `.env` e defina o token de acesso:

```bash
API_TOKEN=ProcessoSeletivoStract2025
API_URL=https://sidebar.stract.to
FLASK_APP=main.py
IMAGE=stract-api
```

##### 5. Exportar as variáveis
* Terminal bash
```bash
source .env
```

* Obs: em caso de não uso do `bash`, as variáveis deverão ser exportada manualmente

##### 6. Executar o Servidor

```bash
flask run
```

##### 7. Uso do docker (Opcional)
* Configurar o arquivo .env da mesma forma
* Exportar as variáveis para o terminal
* Executar o build da imagem: `docker build -t $IMAGE .`
* Executar a composição da imagem: `docker compose up`

#### O servidor estará rodando em http://localhost:5000/

## 🚀 Endpoints Disponíveis

#### Informações do Desenvolvedor

<b>GET /</b>

* Retorna nome, e-mail e LinkedIn do desenvolvedor.

```bash
curl -X GET "http://localhost:5000/"
```

#### Relatórios por Plataforma

<b>GET /{plataforma}</b>

* Retorna uma tabela CSV com todos os anúncios veiculados na plataforma informada.

```bash
curl -X GET "http://localhost:5000/<plataforma>"
```

<b>GET /{plataforma}/resumo</b>

* Retorna um resumo agregando os dados de todas as contas da plataforma informada.

```bash
curl -X GET "http://localhost:5000/<plataforma>/resumo"
```

#### Relatórios Gerais

<b>GET /geral</b>

* Retorna uma tabela CSV com todos os anúncios de todas as plataformas.

```bash
curl -X GET "http://localhost:5000/geral"
```

<b>GET /geral/resumo</b>

* Retorna um resumo agregando os dados de todas as plataformas.

```bash
curl -X GET "http://localhost:5000/geral/resumo"
```

## 📊 Exemplo de Saída

<b>/facebook</b>

```bash
Platform,Ad Name,Clicks,Impressions,Spend
Facebook,Ad1,10,1000,50
Facebook,Ad2,20,2000,100
```

<b>/facebook/resumo</b>

```bash
Platform,Ad Name,Clicks,Impressions,Spend
Facebook,,30,3000,150
```

📌 Observações

O campo "Cost per Click" para Google Analytics será calculado como spend / clicks.

A API utiliza paginação; a navegação é feita via parâmetro page.

📫 Contato

Desenvolvido por Seu Nome.