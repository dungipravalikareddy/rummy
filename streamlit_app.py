import streamlit as st
from query_engine import ask_query

st.set_page_config(page_title="Customer Support Bot", page_icon="💬")
st.title("💬 Customer Support Bot (SQL + LangChain)")

query = st.text_input("Ask me something about your order:")

if query:
    with st.spinner("Thinking..."):
        try:
            response = ask_query(query)
            st.success(response)
        except Exception as e:
            st.error(f"Error: {str(e)}")
