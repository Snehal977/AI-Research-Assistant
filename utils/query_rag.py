from utils.retriever import retrieve_chunks
from utils.rag import build_prompt
from utils.llm import generate_answer

while True:

    question = input(
        "\nAsk Question (type exit to quit): "
    )

    if question.lower() == "exit":
        break

    retrieved_chunks = retrieve_chunks(
        question)
        
    #for i,chunk in enumerate(retrieved_chunks):
            #print(f"\nChunk {i+1}")
            #print("-"*80)
            #print(chunk)
    

    prompt = build_prompt(
        question,
        retrieved_chunks
    )

    answer = generate_answer(
        prompt
    )

    print("\nAnswer:\n")
    print(answer)