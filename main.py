import streamlit as st
from query_engine import ask_query

st.title("🧠 Customer Support Chatbot")

user_question = st.text_input("Ask me anything about your orders, refunds, or general help:")

if st.button("Ask"):
    if user_question:
        with st.spinner("Thinking..."):
            response = ask_query(user_question)
            st.success(response)
    else:
        st.warning("Please enter a question.")
