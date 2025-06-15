import streamlit as st
import openai

# Set your OpenAI API key from Streamlit Secrets
client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# Page setup
st.set_page_config(page_title="Bible AI Chatbot", layout="centered")
st.title("📖 Bible AI Chatbot")
st.write("Ask anything based on the Bible and receive AI-powered answers with scripture references.")

# Input field
question = st.text_input("Ask a Bible question:")

# If the user submits a question
if st.button("Get Answer") and question:
    with st.spinner("Searching the Scriptures..."):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",  # Or "gpt-3.5-turbo"
                messages=[
                    {"role": "system", "content": "You are a helpful assistant who answers only using the Bible and always includes scripture references."},
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

