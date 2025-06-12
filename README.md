# 🌎💨 Air Quality Data Pipeline

[🇬🇧 English](#english) | [🇧🇷 Português](#português)

---

## English

### 🌟 Project Overview
This project is a **data pipeline** designed to collect, process, and analyze air quality data from the [OpenAQ](https://openaq.org/) platform. The pipeline focuses on gathering sensor data from various locations and countries, using **Apache Airflow** for workflow orchestration and data processing.

---

### 🚀 Current Features
- 📥 Data ingestion from OpenAQ API
- 🌍 Collection of sensor information by country
- 📊 Measurement data collection for each sensor
- 💾 Data storage in CSV format
- 🔄 Automated data pipeline with Apache Airflow
- 🔎 Basic data exploration capabilities

---

### 🗂️ Project Structure

```
air_quality_pipeline/
├── .astro/              # Astronomer configuration
├── config/             # Configuration files
├── data/
│   └── raw/           # Raw data storage
├── dags/              # Airflow DAGs
│   └── extract.py     # Data extraction and transformation DAG
├── include/           # Additional Airflow files
├── plugins/           # Custom Airflow plugins
├── src/
│   ├── ingestion/     # Data ingestion scripts
│   └── explore_data.py # Data exploration utilities
├── tests/             # Test files
├── notebooks/         # Jupyter notebooks for analysis
├── .venv/            # Virtual environment
├── airflow_settings.yaml # Airflow configuration
├── Dockerfile        # Container configuration
└── requirements.txt  # Python dependencies
```

---

### ⚙️ Setup and Installation

1. **Create a virtual environment:**
    ```
    python -m venv .venv
    source .venv/bin/activate  # On Unix/macOS
    ```

2. **Install dependencies:**
    ```
    pip install -r requirements.txt
    ```

3. **Create a `.env` file in the `.venv` directory with your OpenAQ API key:**
    ```
    OPENAQ_API_KEY=your_api_key_here
    ```

4. **Configure Airflow:**
    ```
    export AIRFLOW_HOME=~/airflow
    airflow db init
    airflow users create \
        --username admin \
        --firstname Admin \
        --lastname User \
        --role Admin \
        --email admin@example.com \
        --password admin
    ```

5. **Start Airflow services:**
    ```
    airflow webserver -p 8080
    airflow scheduler
    ```

6. **Docker Setup (Optional):**
    The project includes Docker support for containerized deployment. To use Docker:
    ```
    docker build -t air-quality-pipeline .
    ```

---

### 🌱 Future Enhancements
- ☁️ Cloud database implementation for scalable data storage
- 🧠 Advanced data processing and analytics
- 🛰️ Real-time monitoring capabilities
- 📈 Data visualization dashboard
- 🔍 Data quality monitoring and validation
- 📊 Advanced analytics and reporting

---

## Português

### 🌟 Visão Geral do Projeto
Este projeto é um **pipeline de dados** projetado para coletar, processar e analisar dados de qualidade do ar da plataforma [OpenAQ](https://openaq.org/). O pipeline foca na coleta de dados de sensores de várias localidades e países, utilizando **Apache Airflow** para orquestração de workflows e processamento de dados.

---

### 🚀 Funcionalidades Atuais
- 📥 Ingestão de dados da API OpenAQ
- 🌍 Coleta de informações de sensores por país
- 📊 Coleta de dados de medição para cada sensor
- 💾 Armazenamento de dados em formato CSV
- 🔄 Pipeline de dados automatizado com Apache Airflow
- 🔎 Capacidades básicas de exploração de dados

---

### 🗂️ Estrutura do Projeto

```
air_quality_pipeline/
├── .astro/              # Configuração do Astronomer
├── config/             # Arquivos de configuração
├── data/
│   └── raw/           # Armazenamento de dados brutos
├── dags/              # DAGs do Airflow
│   └── extract.py     # DAG de extração e transformação de dados
├── include/           # Arquivos adicionais do Airflow
├── plugins/           # Plugins personalizados do Airflow
├── src/
│   ├── ingestion/     # Scripts de ingestão de dados
│   └── explore_data.py # Utilitários de exploração de dados
├── tests/             # Arquivos de teste
├── notebooks/         # Notebooks Jupyter para análise
├── .venv/            # Ambiente virtual
├── airflow_settings.yaml # Configuração do Airflow
├── Dockerfile        # Configuração do container
└── requirements.txt  # Dependências Python
```

---

### ⚙️ Configuração e Instalação

1. **Criar um ambiente virtual:**
    ```
    python -m venv .venv
    source .venv/bin/activate  # No Unix/macOS
    ```

2. **Instalar dependências:**
    ```
    pip install -r requirements.txt
    ```

3. **Criar um arquivo `.env` no diretório `.venv` com sua chave de API OpenAQ:**
    ```
    OPENAQ_API_KEY=sua_chave_api_aqui
    ```

4. **Configurar o Airflow:**
    ```
    export AIRFLOW_HOME=~/airflow
    airflow db init
    airflow users create \
        --username admin \
        --firstname Admin \
        --lastname User \
        --role Admin \
        --email admin@example.com \
        --password admin
    ```

5. **Iniciar serviços do Airflow:**
    ```
    airflow webserver -p 8080
    airflow scheduler
    ```

6. **Configuração Docker (Opcional):**
    O projeto inclui suporte a Docker para implantação containerizada. Para usar Docker:
    ```
    docker build -t air-quality-pipeline .
    ```

---

### 🌱 Melhorias Futuras
- ☁️ Implementação de banco de dados em nuvem para armazenamento escalável
- 🧠 Processamento avançado de dados e análises
- 🛰️ Capacidades de monitoramento em tempo real
- 📈 Dashboard de visualização de dados
- 🔍 Monitoramento e validação de qualidade dos dados
- 📊 Análises avançadas e relatórios

---

     Feito para a engenharia de dados!

