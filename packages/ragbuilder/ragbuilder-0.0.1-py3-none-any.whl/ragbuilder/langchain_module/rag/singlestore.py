import openai
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores.singlestoredb import SingleStoreDB
import os
import pandas as pd
import requests

# URL of the public .txt file you want to use
file_url = "https://sherlock-holm.es/stories/plain-text/stud.txt"

# Send a GET request to the file URL
response = requests.get(file_url)

# Proceed if the file was successfully downloaded
if response.status_code == 200:
    file_content = response.text

    # Save the content to a file
    file_path = 'downloaded_example.txt'
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(file_content)

    # Now, you can proceed with your original code using 'downloaded_example.txt'
    # Load and process documents
    loader = TextLoader(file_path)  # Use the downloaded document

    documents = loader.load()
    text_splitter = CharacterTextSplitter(chunk_size=2000, chunk_overlap=0)
    docs = text_splitter.split_documents(documents)

    # Generate embeddings and create a document search database
    OPENAI_KEY = "sk-kruxai-service-account-q8k4AHfwNjmrDBAaxLgLT3BlbkFJg2SHm2K2UTqydtZPGmip" 
# Replace with your OpenAI API key
    embeddings = OpenAIEmbeddings(api_key=OPENAI_KEY)

    # Create Vector Database
    os.environ["SINGLESTOREDB_URL"] = "ashwin-81163:KonzOO77Qwnsh6k4aaJ9ZtqnPukazCQ4@svc-3482219c-a389-4079-b18b-d50662524e8a-shared-dml.aws-virginia-6.svc.singlestore.com:3333/db_ashwin_ce684"
    vector_database = SingleStoreDB.from_documents(docs, embeddings, table_name="newdb")  # Replace "your_table_name" with your actual table name

    query = "which university did he study?"
    docs = vector_database.similarity_search(query)
    print(docs[0].page_content)

else:
    print("Failed to download the file. Please check the URL and try again.")