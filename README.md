# 🤖 LSTM NLP Intent Classification Chatbot

An end-to-end NLP Intent Classification Chatbot using LSTM, TensorFlow, and Deep Learning with preprocessing, tokenization, padding, visualization, and real-time intent prediction.

---

# 🚀 Kaggle Notebook

## 📘 Open Notebook

[Kaggle Notebook - LSTM NLP Chatbot](https://www.kaggle.com/code/kanhapatidar/lstm-nlp-chatbot?utm_source=chatgpt.com)

---

# 🚀 Features

✅ NLP Text Preprocessing  
✅ Intent Classification using LSTM  
✅ TensorFlow / Keras Deep Learning  
✅ Real-Time Chatbot Prediction  
✅ Tokenization & Sequence Padding  
✅ Label Encoding  
✅ Accuracy & Loss Visualization  
✅ Frontend Chat Interface  
✅ Flask Backend Integration  
✅ JSON-Based Response System  

---

# 🧠 Deep Learning Architecture

The chatbot uses:

- Embedding Layer
- LSTM Layer
- Dropout Layer
- Dense Output Layer

The model learns conversational patterns and predicts user intents from messages.

---

# 📂 Project Structure

```bash
LSTM-NLP-Intent-Chatbot/
│
├── static/
│   ├── script.js
│   └── style.css
│
├── template/
│   └── index.html
│
├── app.py
├── chatbot_data.csv
├── create_json.ipynb
├── label_encoder.pkl
├── lstm_chatbot_model.h5
├── tokenizer.pkl
├── responses.json
├── Untitled.ipynb
│
└── README.md
```

---

# 📊 Dataset

The dataset contains conversational chatbot messages with intent labels.

### Dataset Columns

| Column | Description |
|---|---|
| conversation_id | Unique conversation ID |
| turn | Conversation order |
| role | User/Bot |
| intent | Intent category |
| message | User message |

---

# ⚠️ Important Note

The complete dataset responses and `responses.json` file were not uploaded to GitHub because of large file size limitations.

You can access the complete notebook and dataset workflow from Kaggle.

---

# 📥 Kaggle Notebook Link

[Open Kaggle Notebook](https://www.kaggle.com/code/kanhapatidar/lstm-nlp-chatbot?utm_source=chatgpt.com)

---

# 🧹 NLP Preprocessing

The following preprocessing steps were performed:

- Lowercasing
- Removing special characters
- Removing extra spaces
- Tokenization
- Sequence Padding
- Label Encoding

---

# 🔢 Tokenization & Padding

Text messages are converted into numerical sequences using Keras Tokenizer and padded for fixed-length input processing.

---

# 🏗️ Model Training

The model is trained using:

- TensorFlow/Keras
- Sparse Categorical Crossentropy
- Adam Optimizer
- LSTM Networks

---

# 📈 Visualizations

The notebook includes:

- Intent Distribution
- Message Length Distribution
- WordCloud
- Accuracy Graph
- Loss Graph
- Confusion Matrix

---

# 💾 Saved Files

| File | Description |
|---|---|
| lstm_chatbot_model.h5 | Trained LSTM model |
| tokenizer.pkl | Saved tokenizer |
| label_encoder.pkl | Saved label encoder |

---

# 🌐 Frontend

The project includes a simple chatbot frontend using:

- HTML
- CSS
- JavaScript

---

# ⚙️ Backend

The backend is developed using:

- Flask
- TensorFlow
- Pickle
- JSON

---

# ▶️ How to Run the Project

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/LSTM-NLP-Intent-Chatbot.git
```

---

## 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install tensorflow flask pandas numpy matplotlib seaborn scikit-learn
```

---

## 3️⃣ Add Required Files

Download or create:

- chatbot_data.csv
- responses.json

inside the project folder.

---

## 4️⃣ Run Flask App

```bash
python app.py
```

---

## 5️⃣ Open Browser

```bash
http://127.0.0.1:5000
```

---

# 🧪 Example Predictions

| User Input | Predicted Intent |
|---|---|
| best phone deals | shopping |
| what is llm | ai |
| good habits | habits |

---

# 📚 Technologies Used

| Technology | Usage |
|---|---|
| Python | Core Programming |
| TensorFlow | Deep Learning |
| Keras | LSTM Model |
| Flask | Backend |
| HTML/CSS/JS | Frontend |
| Pandas | Data Processing |
| Matplotlib | Visualization |

---

# 🔥 Future Improvements

- Transformer Models (BERT/GPT)
- Attention Mechanism
- Multi-turn Conversation Memory
- FastAPI Deployment
- Docker Deployment
- Voice Assistant Integration

---

# 📸 Screenshots

Add screenshots here:

- Chat Interface
- Model Training
- Accuracy Graph
- Confusion Matrix

---

# 👨‍💻 Author

## Kanha Patidar

Deep Learning | NLP | AI Enthusiast

---

# ⭐ If You Like This Project

Give this repository a ⭐ on GitHub!

---

# 📄 License

This project is open-source and available under the MIT License.
