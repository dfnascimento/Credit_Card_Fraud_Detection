# 🚨 API de Detecção de Fraudes em Transações de Cartão de Crédito

## 📄 Descrição do Projeto

Este projeto implementa uma **API RESTful** desenvolvida com **Flask** para disponibilizar um **modelo de Machine Learning** treinado para **detectar fraudes em transações de cartão de crédito**.

O objetivo é oferecer um endpoint simples e eficiente para realizar previsões em tempo real, podendo ser integrado a sistemas de monitoramento de pagamentos, dashboards de risco ou pipelines de decisão automatizada.

---

## 💾 Fonte dos Dados

* **Dataset:** [Kaggle - Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)
* **Acessado em:** 01/10/2025
* **Descrição:**

  * Contém **284.807 transações** reais realizadas em **setembro de 2013** por titulares de cartões de crédito europeus.
  * Apenas **492 transações** são classificadas como fraude (≈ 0,172% do total).
  * As variáveis **V1 a V28** foram transformadas via **PCA (Análise de Componentes Principais)** para proteger dados confidenciais.
  * As únicas variáveis não transformadas são:

    * `Time`: segundos decorridos desde a primeira transação.
    * `Amount`: valor da transação.
    * `Class`: variável alvo (1 = fraude, 0 = não fraude).

---

## 🧩 Estrutura do Projeto

```
credit-card-fraud-api/
│
├── data/
│   └── creditcard.csv                # Dataset original (não versionado)
│
├── model/
│   └── best_model.pkl               # Modelo treinado (serializado com pickle)
│   └── scaker.pkl                   # Scaler para normalização dos dados (serializado com pickle)
│
├── notebooks/
│   └── Credit_Card_Fraud_Detection.ipynb          # Notebook de treinamento e avaliação
│
├── api/
│   ├── __init__.py
│   ├── predict.py                        # Implementação do Endpoint API Flask
│   └── transaction_features.py           # Classe Transaction Features para geração do DataFrame
│
├── requirements.txt                  # Dependências do projeto
├── README.md                         # Este arquivo
└── run.py                            # Script principal para executar a API
└── Tests.ipynb                       # Notebook para geração de dados para testar API
```

---

## ⚙️ Tecnologias Utilizadas

* **Python 3.10+**
* **Flask**
* **scikit-learn**
* **pandas**
* **matplotlib**
* **seaborn**
* **joblib / pickle**

---

## 🧪 Treinamento do Modelo

1. **Pré-processamento:**

   * Remoção de dados duplicados
   * Engenharia de Features: criação das Features `Hour` e `Day`
   * Normalização da variável `Amount` e `Hour`.
   * Divisão em treino e teste.
   * Eleição das Features mais significaticas com base das de maior e menor correlação com a classe alvo.

2. **Modelos testados:**

   * Regressão Logística
   * Random Forest
   * XGBoost
   * LightGBM

3. **Métricas avaliadas:**

   * AUPRC - Área sob a Curva de Precisão-Recall 
   * Precisão
   * Recall
   * F1-Score


4. **Modelo escolhido:**
   `RandomForestClassifier` com ajuste de hiperparâmetros via **GridSearchCV**, apresentando melhor equilíbrio entre precisão e recall.

---

## 🚀 API Flask

### **Endpoint Principal**

**URL:** `/predict`
**Método:** `POST`
**Descrição:** Recebe os dados de uma transação e retorna a probabilidade de fraude.

#### 📥 Exemplo de Requisição

```bash
POST /predict
Content-Type: application/json

{
  "Time": 472.0,
  "Amount": 529.0,
  "V1": -3.0435406239976,
  "V2": -3.15730712090228,
  "V3": 1.08846277997285,
  "V4": 2.2886436183814,
  "V5": 1.35980512966107,
  "V6": -1.06482252298131,
  "V7": 0.325574266158614,
  "V8": -0.0677936531906277,
  "V9": -0.270952836226548,
  "V10": -0.838586564582682,
  "V11": -0.414575448285725,
  "V12": -0.503140859566824,
  "V13": 0.676501544635863,
  "V14": -1.69202893305906,
  "V15": 2.00063483909015,
  "V16": 0.666779695901966,
  "V17": 0.599717413841732,
  "V18": 1.72532100745514,
  "V19": 0.283344830149495,
  "V20": 2.10233879259444,
  "V21": 0.661695924845707,
  "V22": 0.435477208966341,
  "V23": 1.37596574254306,
  "V24": -0.293803152734021,
  "V25": 0.279798031841214,
  "V26": -0.145361714815161,
  "V27": -0.252773122530705,
  "V28": 0.0357642251788156
}
```

#### 📤 Exemplo de Resposta

```json
{
    "prediction": 1,
    "timestamp": "2025-10-06T23:40:39.026880"
}
```

---

## 🧱 Executando o Projeto Localmente

### 1. Clonar o repositório

```bash
git clone https://github.com/dfnascimento/Credit_Card_Fraud_Detection.git
cd Credit_Card_Fraud_Detection
```

### 2. Criar e ativar ambiente virtual

```bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
```

### 3. Instalar dependências

```bash
pip install -r requirements.txt
```

### 4. Executar a API

```bash
python run.py
```

Acesse:
👉 `http://127.0.0.1:5000/predict`


## 📈 Resultados do Modelo

| Métrica  | Valor  |
| -------- | -----  |
| AUPRC    | 0.8119 |
| Precisão | 0.93   |
| Recall   | 0.76   |
| F1-Score | 0.84   |

*(valores aproximados obtidos no dataset original)*

---

## 🔐 Considerações Éticas

A detecção de fraudes é uma aplicação sensível e deve ser usada **como ferramenta de apoio à decisão**, não como critério automático de bloqueio. O modelo deve ser constantemente **reavaliado e re-treinado** com dados atualizados para evitar **vieses e falsos positivos**.

---

## 📚 Autor

Diego de Faria do Nascimento
🔗 [LinkedIn](https://www.linkedin.com/in/diego-de-faria-do-nascimento-4926b628/) | [GitHub](https://github.com/dfnascimento)



