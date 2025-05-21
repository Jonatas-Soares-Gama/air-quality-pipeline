# 🌎💨 Air Quality Data Pipeline

[🇬🇧 English](#english) | [🇧🇷 Português](#português)

---

## English

### 🌟 Project Overview
This project is a **data pipeline** designed to collect, process, and analyze air quality data from the [OpenAQ](https://openaq.org/) platform. The pipeline currently focuses on gathering sensor data from various locations and countries, with plans to expand its capabilities using **Apache Airflow** and cloud database solutions.

---

### 🚀 Current Features
- 📥 Data ingestion from OpenAQ API
- 🌍 Collection of sensor information by country
- 📊 Measurement data collection for each sensor
- 💾 Data storage in CSV format
- 🔎 Basic data exploration capabilities

---

### 🗂️ Project Structure

```
air_quality_pipeline/
├── data/
│   └── raw/              # Raw data storage
├── src/
│   └── ingestion/        # Data ingestion scripts
├── notebooks/            # Jupyter notebooks for analysis
└── .venv/               # Virtual environment
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

---

### 🌱 Future Enhancements
- ⏳ Integration with Apache Airflow for workflow orchestration
- ☁️ Cloud database implementation for scalable data storage
- 🧠 Advanced data processing and analytics
- 🛰️ Real-time monitoring capabilities
- 📈 Data visualization dashboard

---

## Português

### 🌟 Visão Geral do Projeto
Este projeto é um **pipeline de dados** projetado para coletar, processar e analisar dados de qualidade do ar da plataforma [OpenAQ](https://openaq.org/). Atualmente, o pipeline foca na coleta de dados de sensores de várias localidades e países, com planos de expansão para uso de **Apache Airflow** e soluções de banco de dados em nuvem.

---

### 🚀 Funcionalidades Atuais
- 📥 Ingestão de dados da API OpenAQ
- 🌍 Coleta de informações de sensores por país
- 📊 Coleta de dados de medição para cada sensor
- 💾 Armazenamento de dados em formato CSV
- 🔎 Capacidades básicas de exploração de dados

---

### 🗂️ Estrutura do Projeto

```
air_quality_pipeline/
├── data/
│   └── raw/              # Armazenamento de dados brutos
├── src/
│   └── ingestion/        # Scripts de ingestão de dados
├── notebooks/            # Notebooks Jupyter para análise
└── .venv/               # Ambiente virtual
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

---

### 🌱 Melhorias Futuras
- ⏳ Integração com Apache Airflow para orquestração de workflows
- ☁️ Implementação de banco de dados em nuvem para armazenamento escalável
- 🧠 Processamento avançado de dados e análises
- 🛰️ Capacidades de monitoramento em tempo real
- 📈 Dashboard de visualização de dados

---

     Feito para a engenharia de dados!

