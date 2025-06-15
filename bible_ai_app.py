import streamlit as st
import openai

# Set your OpenAI API key here or use Streamlit secrets for security
openai.api_key = st.secrets["OPENAI_API_KEY"]

# Streamlit page config
st.set_page_config(page_title="Bible AI Chatbot", layout="centered")

# App title
st.title("📖 Bible AI Chatbot")
st.write("Ask any question based on the Bible and get AI-powered answers!")

# Input from the user
user_question = st.text_input("Type your Bible-related question here:")

# When user submits a question
if st.button("Get Answer") and user_question:
    with st.spinner("Thinking..."):
        try:
            prompt = (
                "You are a helpful assistant that answers questions strictly based on the Bible. "
                "If something is not found in the Bible, say 'The Bible does not mention that directly.'\n\n"
                f"Question: {user_question}\nAnswer:"
            )

            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",  # or "gpt-4" if you have access
                messages=[{"role": "user", "content": prompt}],
                max_tokens=500,
                temperature=0.7,
            )

            answer = response.choices[0].message.content.strip()
            st.success("Answer:")
            st.write(answer)

        except Exception as e:
            st.error(f"Something went wrong: {e}")
          
