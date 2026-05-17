from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate #Lagnchain is framework that makes easier to work with LLM's
from vector import retriever

model = OllamaLLM(model = "llama3.2")

template = """
    You are a expert in Reviewing pizza restaurants
    Here are some relevant reviews: {reviews}

    Here is the question to answer: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

# keep asking questions until 'q' is entered
while True:
    print("\n\n------------------------------")
    question = input("Ask a question about pizza restaurants (q to quit): ")
    print("\n\n")
    if question.lower() == "q":
        break
    reviews = retriever.invoke(question)
    # pass revieew and questions into review chain to get answer. The review chain will use the reviews as context to answer the question.
    result = chain.invoke({"reviews": reviews, "question": question})
    print(result)