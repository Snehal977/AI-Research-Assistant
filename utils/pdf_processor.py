from utils.pdf_loader import load_pdf
from utils.chunking import clean_text
from utils.chunking import create_chunk


def process_pdf(pdf_path):
    
    text = load_pdf(pdf_path)

    
    text = clean_text(text)

    # Create chunks
    chunks = create_chunk(
        text=text,
        chunk_size=1000,
        overlap=200
    )

    return text, chunks