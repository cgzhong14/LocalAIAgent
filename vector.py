#vecotr search is  database ChromaDb. Look relevant information and model can use it to answer question.
#add relevant database and embedding model. Then create retriever to get relevant information based on question.
from langchain_ollama import OllamaEmbeddings
from langchain_chroma import Chroma #vector store
from langchain_core.documents import Document
import os
import pandas as pd

# bring in CSV file, define embedding model
df = pd.read_csv("realistic_restaurant_reviews.csv") #dataframe
embeddings = OllamaEmbeddings(model="mxbai-embed-large") #embedding model

# check if this location alrdy exists
db_location = './chrome_langchain_db'
add_documents = not os.path.exists(db_location) #check if db exists

# if db doesn't exist, then cook data into db
if add_documents:
    documents = []
    ids = []
    for i, row in df.iterrows():
        document = Document(
        page_content=row['Title'] + " " + row["Review"], 
            metadata={"rating": row["Rating"], "date": row["Date"]},
            id = str(i)
        )
        ids.append(str(i))
        documents.append(document)

#init vectore store and add documents if db doesn't exist. If db exists, then just init vector store and retriever.
vector_store = Chroma(
    collection_name="restaurant_reviews",
    persist_directory=db_location,
    embedding_function=embeddings
)

if add_documents:
    vector_store.add_documents(documents=documents, ids=ids)

retriever = vector_store.as_retriever(search_kwargs={"k":5}) # 5 reviews and pass it as llm context to answer question.