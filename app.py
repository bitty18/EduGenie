import streamlit as st

st.title("EduGenie")
st.write("Your AI Learning Assistant")

question = st.text_input("Ask your question:")

if st.button("Ask EduGenie"):
    if question:
        st.write("Your question:", question)
        st.success("EduGenie received your question!")
        st.write("Demo answer: Inheritance allows one Java class to acquire properties and methods from another class.")
    else:
        st.warning("Please enter a question.")

