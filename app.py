from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

import tensorflow as tf
import numpy as np
import pickle
import json

from tensorflow.keras.preprocessing.sequence import pad_sequences

# =========================================
# LOAD MODEL
# =========================================

model = tf.keras.models.load_model(
    "lstm_chatbot_model.h5"
)

# =========================================
# LOAD TOKENIZER
# =========================================

with open("tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# =========================================
# LOAD LABEL ENCODER
# =========================================

with open("label_encoder.pkl", "rb") as f:
    lbl_encoder = pickle.load(f)

# =========================================
# LOAD RESPONSES
# =========================================

with open("responses.json", "r") as file:
    data = json.load(file)

# =========================================
# FASTAPI APP
# =========================================

app = FastAPI(
    title="LSTM NLP Chatbot API"
)

# =========================================
# CORS
# =========================================

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================================
# STATIC FILES
# =========================================

app.mount(
    "/static",
    StaticFiles(directory="static"),
    name="static"
)

# =========================================
# HTML TEMPLATE
# =========================================

templates = Jinja2Templates(
    directory="template"
)

# =========================================
# HOME ROUTE
# =========================================

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request
        }
    )

# =========================================
# CHATBOT API
# =========================================

@app.get("/chat")
async def chatbot(message: str):

    max_len = 20

    # TEXT TO SEQUENCE

    result = tokenizer.texts_to_sequences(
        [message]
    )

    # PADDING

    result = pad_sequences(
        result,
        truncating='post',
        maxlen=max_len
    )

    # PREDICTION

    prediction = model.predict(result)

    tag = lbl_encoder.inverse_transform(
        [np.argmax(prediction)]
    )[0]

    # FIND RESPONSE

    for intent in data['intents']:

        if intent['tag'] == tag:

            response = np.random.choice(
                intent['responses']
            )

            return {
                "message": message,
                "tag": tag,
                "response": response
            }

    return {
        "response": "Sorry, I didn't understand."
    }

# =========================================
# RUN:
# uvicorn app:app --reload
# =========================================