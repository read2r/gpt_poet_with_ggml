from langchain.llms import CTransformers
import streamlit as st

llm = CTransformers(
    model="llama-2-7b-chat.ggmlv3.q2_K.bin",
    model_type="llama"
)

st.title("GPT Poet")
poem_topic = st.text_input("Your poem's topic")

if st.button("Write Poem"):
    if len(poem_topic) == 0:
        st.write("No Topic")
    else:
        with st.spinner("Now writing poem..."):
            result = llm.predict(f"Write poem about {poem_topic}")
            st.write(result)