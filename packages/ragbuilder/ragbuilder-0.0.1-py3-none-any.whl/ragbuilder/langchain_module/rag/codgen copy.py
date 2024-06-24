import os
import logging

# Set up logger
logger = logging.getLogger(__name__)

def getHuggingFaceLLM(retrieval_model, return_text=False):
    logger.info(f"model={retrieval_model} Invoked")
    
    if return_text:
        return f'HuggingFaceEndpoint(repo_id={retrieval_model}, huggingfacehub_api_token=os.environ.get("HUGGINGFACEHUB_API_TOKEN"))'
    
    return HuggingFaceEndpoint(
        repo_id=retrieval_model,
        huggingfacehub_api_token=os.environ.get("HUGGINGFACEHUB_API_TOKEN"),
    )

# Example usage
# Uncomment to test
print(getHuggingFaceLLM("some-model", return_text=True))  # Should return string representation
# print(getHuggingFaceLLM("some-model", return_text=False)) # Should return HuggingFaceEndpoint object
