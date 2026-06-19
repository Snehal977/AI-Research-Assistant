def build_prompt(
        question,
        chunks):

    context = "\n\n".join(
        chunks
    )

    prompt = f"""
You are an AI Research Assistant.

Answer ONLY using
the provided context.

If answer is not present,
say:

'I could not find
that information
in the document.'

Context:
{context}

Question:
{question}

Answer:
"""

    return prompt