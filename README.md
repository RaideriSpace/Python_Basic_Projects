# 🐍 Python Projects Hub

    Este repositório contém uma coleção de projetos práticos desenvolvidos com Python, aplicando conceitos de automação, inteligência artificial e desenvolvimento de interfaces com IA. Cada projeto foca em resolver um desafio específico do mundo real.

## 📁 Estrutura de Projetos

    python_IA/
    │
    ├── data/
    │   ├── clientes.csv
    │   ├── novos_clientes.csv
    │
    ├── notebooks/
    │   └── inicial.ipynb
    │
    ├── modelos/
    │   └── modelo_random_forest.pkl  ← (opcional, se for salvar)
    │
    ├── src/
    │   ├── preprocessamento.py       ← (transformações com LabelEncoder)
    │   └── modelo_credito.py         ← (treinamento e predição)
    │
    ├── requirements.txt
    ├── README.md
    └── .gitignore

### 📂 `automacao`

    Automatização de processos manuais com a biblioteca `pyautogui`.

    - 🛠️ Automatiza o login e o cadastro de produtos em um sistema web.
    - 📄 Lê dados de um arquivo `CSV` com 294 produtos.
    - 🔧 Utiliza cliques e preenchimento de campos com coordenadas da tela.

    **Bibliotecas:** `pyautogui`, `time`, `pandas`

---

### 📂 `python_dev`

    Mini chatbot com interface usando `Streamlit` e integração com a IA Gemini da Google.

    - 💬 Chat com memória de contexto usando `st.session_state`.
    - 🔑 Utiliza a API do modelo `gemini-1.5-flash` com uma chave da Google.
    - 🤖 IA com estilo de fala sábio e não formal (personalização via `system_instructions`).

    **Bibliotecas:** `streamlit`, `google.generativeai`

---

### 📂 `python_IA`

    Projeto de **Machine Learning** para prever o **score de crédito** de clientes de um banco.

    - 📊 Base com 100.001 registros históricos de clientes.
    - 🧠 Modelos usados: `RandomForestClassifier` e `KNeighborsClassifier`
    - 📈 Avaliação de desempenho com `accuracy_score`
    - 🔮 Aplicação em novos clientes com base em um segundo CSV.

    **Bibliotecas:** `pandas`, `scikit-learn`, `jupyter`

---

## 🚀 Como executar os projetos

### Pré-requisitos

    - Python 3.10 ou superior
    - Gerenciador de pacotes: `pip`

### Instalação

    ```bash
    git clone https://github.com/seuusuario/python_projects_hub.git
    cd python_projects_hub
    pip install -r requirements.txt

### Executar projetos

    Projeto	Comando

    automacao	python codigo.py
    python_dev	streamlit run python_dev/main.py
    python_IA	Rodar o Jupyter Notebook inicial.ipynb

## ✅ Tecnologias Usadas

    Python

    Pandas

    PyAutoGUI

    Streamlit

    Scikit-learn

    Google Generative AI

    Jupyter Notebook

## 💡 Próximos Passos

    Criar uma API para o projeto de IA com FastAPI

    Adicionar testes automatizados

    Criar interface gráfica para o projeto de automação

## 🧑‍💻 Sobre

    Este repositório foi criado com o objetivo de aprender e praticar Python de forma aplicada, com foco em automações, inteligência artificial e construção de interfaces simples. Cada pasta representa um tipo de problema real resolvido com Python.

