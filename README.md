# Castanhal Crime Analytics

Uma aplicação web interativa desenvolvida com **Streamlit** para visualização e análise de dados de segurança pública da cidade de Castanhal, Pará. O objetivo deste projeto é fornecer um panorama detalhado sobre as ocorrências criminais no município, permitindo a exploração de tendências históricas e padrões específicos.

## 📊 Análises Disponíveis

A aplicação é organizada em páginas de navegação que oferecem análises detalhadas por tipo de ocorrência, utilizando o sistema de navegação do Streamlit.

### Panorama Geral (Home)

* Visão geral da quantidade de ocorrências por categoria criminal.

### Análises Detalhadas por Categoria

Cada página de análise detalhada (como a de Homicídio) inclui visualizações específicas, como:

* Bairros com maior ocorrência.
* Frequência ao longo do tempo (anual, mensal e semanal).
* Horários mais frequentes das ocorrências.
* Características das vítimas (distribuição de idade por sexo).

As categorias de crime analisadas são:

* Roubos
* Furtos
* Latrocínio
* Homicídio
* Lesão Corporal
* Mortes no Trânsito
* Tráfico de Drogas
* Estupros

## 📜 Fonte de Dados

Os dados utilizados são provenientes de registros de boletins de ocorrência disponibilizados publicamente pela [Secretaria de Segurança Pública e Defesa Social (SEGUP)](https://codec.segup.pa.gov.br) do Pará, abrangendo o período de 2010 a 2025.

O carregamento dos dados (`base_de_dados.csv`) é feito utilizando a função `load_data` que trata a leitura do arquivo no formato CSV com separador `;` e define os tipos de colunas, como `categoria`, `bairro`, `latitude`, `longitude` e a coluna temporal `data_hora`.

## 💻 Tecnologias Utilizadas

O projeto foi desenvolvido em Python e utiliza as seguintes bibliotecas principais:

* **Streamlit**: Framework para criação da aplicação web e do dashboard.
* **Pandas**: Para manipulação e análise dos dados.

A lista completa de dependências pode ser encontrada no arquivo `requirements.txt`.

## 🚀 Como Executar Localmente

Siga os passos abaixo para configurar e rodar o projeto em sua máquina:

### Pré-requisitos

* Python 3.x
* Git (opcional, para clonar o repositório)

### 1. Instalação das Dependências

Crie um ambiente virtual (recomendado) e instale as bibliotecas listadas no `requirements.txt`:

```bash
# Crie um ambiente virtual
python -m venv venv
source venv/bin/activate  # No Linux/macOS
.\venv\Scripts\activate   # No Windows

# Instale as dependências
pip install -r requirements.txt
```

### 2. Execução da Aplicação
Após a instalação, execute o arquivo principal (`main.py`) utilizando o comando `streamlit run`:

```bash
streamlit run main.py
```

A aplicação será iniciada e o painel de visualização será aberto automaticamente no seu navegador padrão (geralmente em `http://localhost:8501`).