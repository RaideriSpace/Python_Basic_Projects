# Titulo
# Input do chat
# A cada mensagem enviada:

# streamlit - frontend e backend
# flask, django, fastapi

import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyCPm1gCh9SVjD6E7u9sll3gywsPudUyQDg") # Chave API

# Define as instruções do sistema. Isso não aparecerá no chat.
system_instructions = "Você é uma ia que fala de forma não formal, experiênte e bem sábia, sempre tendo um provérbio ou um ensinamento sobre qualquer coisa."

modelo = genai.GenerativeModel('gemini-1.5-flash', system_instruction = system_instructions) # Modelo da IA

st.write("### Chatbot com Gemini IA") # Texto no formato Markdown

# session_state = memoria do streamlit
if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

# Exibir o histórico de mensagens
for mensagem in st.session_state["lista_mensagens"]:
    st.chat_message(mensagem["role"]).write(mensagem["content"])

# Input do usuário
mensagem_usuario = st.chat_input("Escreva sua mensagem") 

if mensagem_usuario:
    
    # Mostrar a mensagem que o usuario enviou no chat
    st.chat_message('user').write(mensagem_usuario)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem) # Adiciona a mensagem a memória
    
    # Resposta da IA
    chat = modelo.start_chat(history=[
        {"role": "user" if m["role"] == "user" else "model", "parts": [m["content"]]} 
        for m in st.session_state["lista_mensagens"]
    ])
    
    try:
        resposta = chat.send_message(mensagem_usuario)
        resposta_texto = resposta.text
    except Exception as e:
        resposta_texto = f"Erro ao gerar resposta: {e}"
    
    #Exibir a resposta da IA
    st.chat_message('ai').write(resposta_texto)
    
    mensagem_ai = {"role": "ai", "content": resposta_texto}
    st.session_state["lista_mensagens"].append(mensagem_ai)
    
    #Para rodar: streamlit run ./python_dev/main.py