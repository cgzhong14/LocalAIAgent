This project demonstrates a cli application that will read in inputs and will answer questions regarding a list of pizza places
and recommend spots that.

main.py - uses OllamaLLM model 'llama3.2' we feed the model our template with reveiws and the actual quesiton from the cli prompt. we use vector.py to import the information found from the document to our LLM.

vector.py - we use vecotr search and use the ollamaembedding model 'mxbai-embed-large' and create a chroma db that inputs all the data entries form the csv file realisitc_restuarant_reviews.csv. We only create this once, if there isn't one then we used the one we created. We then add the documents to the retriever

Technologies used: Ollama, LangChain, Python, Chroma DB as storage for documents