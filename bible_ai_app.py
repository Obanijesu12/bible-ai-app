import streamlit as st
import openai

# Load API key from Streamlit secrets
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

st.set_page_config(page_title="Bible AI Chatbot", layout="centered")
st.title("📖 Bible AI Chatbot")
st.write("Ask any Bible-related question and receive AI-powered answers with scripture references.")

question = st.text_input("Ask your question:")

if st.button("Get Answer") and question:
    with st.spinner("Searching the Scriptures..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # ✅ Updated to a model you have access to
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that answers questions strictly from the Bible and always includes scripture references."},
                    {"role": "user", "content": question}
                ],
                max_tokens=500,
                temperature=0.7
            )
            answer = response.choices[0].message.content.strip()
            st.success("Answer:")
            st.markdown(answer)
        except Exception as e:
            st.error(f"Something went wrong: {e}")
            
