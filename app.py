import os
import streamlit as st

from utils.pdf_processor import process_pdf
from utils.chroma_store import store_chunks
from utils.retriever import retrieve_chunks

from utils.rag import build_prompt
from utils.llm import generate_answer


# ---------------------------
# PAGE
# ---------------------------

st.title("🤖 AI Research Assistant")

st.write(
    "Upload a PDF and ask questions."
)

st.divider()


# ---------------------------
# SESSION STATE
# ---------------------------

if "pdf_loaded" not in st.session_state:

    st.session_state.pdf_loaded = False


# ---------------------------
# PDF UPLOAD
# ---------------------------

uploaded_file = st.file_uploader(
    "Upload PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    save_path = os.path.join(
        "data",
        uploaded_file.name
    )

    with open(
        save_path,
        "wb"
    ) as f:

        f.write(
            uploaded_file.getbuffer()
        )

    with st.spinner(
        "Processing PDF..."
    ):

        text, chunks = process_pdf(
            save_path
        )

        count = store_chunks(
            chunks
        )

    st.success(
        f"PDF processed successfully."
    )

    st.info(
        f"{count} chunks stored in ChromaDB."
    )

    st.session_state.pdf_loaded = True


# ---------------------------
# QUESTION SECTION
# ---------------------------

if st.session_state.pdf_loaded:

    question = st.text_input(
        "Ask a Question"
    )

    ask_button = st.button(
        "Ask"
    )

    if ask_button and question:

        with st.spinner(
            "Generating answer..."
        ):

            retrieved_chunks = retrieve_chunks(
                question
            )

            prompt = build_prompt(
                question,
                retrieved_chunks
            )

            answer = generate_answer(
                prompt
            )

        st.subheader(
            "Answer"
        )

        st.write(
            answer
        )

        with st.expander(
            "Retrieved Chunks"
        ):

            for i, chunk in enumerate(
                retrieved_chunks
            ):

                st.markdown(
                    f"### Chunk {i+1}"
                )

                st.write(
                    chunk
                )