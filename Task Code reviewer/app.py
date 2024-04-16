import streamlit as st
import openai

with open("keys/.openai_api_key.txt") as f:
    key = f.read().strip()
    
openai.api_key = key
def review_code(code):
    try:
        response = openai.ChatCompletion.create(
          model="gpt-3.5-turbo-0125",
          messages=[
              {"role": "system", "content": "You are a helpful AI trained to review and suggest improvements for Python code."},
              {"role": "user", "content": f"Review the following Python code:\n{code}"}
          ]
        )
        return response.choices[0].message['content']
    except Exception as e:
        return f"An error occurred: {str(e)}"

def main():
    st.title('GenAI App - AI Code Reviewer')

    with st.form(key='code_review_form'):
        user_code = st.text_area("Paste your Python code here:", height=300)
        submit_button = st.form_submit_button(label='Review Code')

    if submit_button and user_code:
        review_result = review_code(user_code)
        st.subheader("Review Results")
        st.text_area("Suggestions:", value=review_result, height=300)

if __name__ == "__main__":
    main()
