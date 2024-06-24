from ragbuilder.langchain_module.common import setup_logging
import logging
from langchain_chroma import Chroma
from langchain_community.vectorstores import FAISS
from langchain_community.vectorstores import SingleStoreDB
import uuid
setup_logging()
logger = logging.getLogger("ragbuilder")

def getVectorDB(splits, embedding, db_type):
    """
    Initialize and return a vector database object based on the specified db_type.

    Args:
    - splits (list): List of documents or splits to be indexed.
    - embedding: Embedding model instance or configuration needed for initialization.
    - db_type (str): Type of vector database to initialize. Supported values: "CHROMA", "FAISS".

    Returns:
    - Vector database object (Chroma or FAISS).

    Raises:
    - ValueError: If db_type is not supported.
    """
    if db_type == "CHROMA":
        logger.info("Chroma DB Loaded")
        return Chroma.from_documents(documents=splits, embedding=embedding, collection_name="collection_"+str(uuid.uuid4().int),)
    elif db_type == "FAISS":
        logger.info("FAISS DB Loaded")
        return FAISS.from_documents(documents=splits, embedding=embedding)
    elif db_type == "SINGELSTORE":
        logger.info("SINGELSTORE DB Loaded")
        return SingleStoreDB.from_documents(documents=splits, embedding=embedding,  table_name="table_"+str(uuid.uuid4().int))
    else:
        raise ValueError(f"Unsupported db_type: {db_type}. Supported types are 'CHROMA' and 'FAISS'.")

