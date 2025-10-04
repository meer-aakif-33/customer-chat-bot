import streamlit as st
from datetime import datetime
from qa_chain import chain

st.set_page_config(page_title="Customer Service Chatbot", page_icon="🤖")
st.title("🤖 Customer Service Chatbot (Gemini + FAISS)")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# CSS for chat bubbles
st.markdown("""
<style>
.user-bubble {
    background-color:#DCF8C6; padding:10px; border-radius:15px;
    max-width:70%; margin-bottom:5px; float:right; color:black; clear:both;
}
.bot-bubble {
    background-color:#F1F0F0; padding:10px; border-radius:15px;
    max-width:70%; margin-bottom:5px; float:left; color:black; clear:both;
}
.chat-container {
    max-height: 500px; overflow-y: auto; padding: 10px;
    border: 1px solid #ccc; border-radius: 10px; margin-bottom: 10px;
}
</style>
""", unsafe_allow_html=True)

# Display chat container
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    timestamp = msg.get("timestamp", "")
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">🧑 {msg["content"]} <br><small>{timestamp}</small></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble">🤖 {msg["content"]} <br><small>{timestamp}</small></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)

# Chat input
user_input = st.chat_input("Type your message...")

# If user types something
if user_input:
    ts = datetime.now().strftime("%H:%M")
    # Append user message first
    st.session_state.messages.append({"role": "user", "content": user_input, "timestamp": ts})

    with st.spinner("Thinking..."):
        response = chain.invoke({"query": user_input})

    answer = response["result"]
    ts_bot = datetime.now().strftime("%H:%M")
    # Append bot response
    st.session_state.messages.append({"role": "bot", "content": answer, "timestamp": ts_bot})

# Display chat container AFTER appending
st.markdown('<div class="chat-container">', unsafe_allow_html=True)
for msg in st.session_state.messages:
    timestamp = msg.get("timestamp", "")
    if msg["role"] == "user":
        st.markdown(f'<div class="user-bubble">🧑 {msg["content"]} <br><small>{timestamp}</small></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="bot-bubble">🤖 {msg["content"]} <br><small>{timestamp}</small></div>', unsafe_allow_html=True)
st.markdown('</div>', unsafe_allow_html=True)
