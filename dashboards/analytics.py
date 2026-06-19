def document_statistics(
        text,
        chunks):

    chunk_lengths = [
        len(chunk)
        for chunk in chunks
    ]

    stats = {

        "characters":
            len(text),

        "words":
            len(text.split()),

        "chunks":
            len(chunks),

        "average_chunk_length":
            sum(chunk_lengths)
            / len(chunk_lengths),

        "largest_chunk":
            max(chunk_lengths),

        "smallest_chunk":
            min(chunk_lengths)
    }

    return stats