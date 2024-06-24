from ragbuilder  import parse_config
import os

# def parse_config():
#     #print(config)
#     config= {}
#     # path= "https://python.langchain.com/v0.2/docs/how_to/custom_tools/"  #url
#     # path = "/Users/ashwinaravind/DEsktop/working_autorag/autorag/InputFiles" #directoy
#     path = "/Users/ashwinaravind/DEsktop/working_autorag/autorag/InputFiles/arxiv.pdf" #File
#     test_data="/Users/ashwinaravind/Desktop/working_autorag/autorag/arxiv.783857.csv"
#     # path="/Users/ashwinaravind/Desktop/working_autorag/autorag/langchain_for_ragas/docs-get_started-quickstart.md"
#     config["compare_templates"] = True
#     config['include_granular_combos'] = False
#     src_data={ 1 : {'source':'file','input_path': path}}
#     print(f"src_data = {src_data}")
#     compare_templates=config["compare_templates"]
#     include_granular_combos=config['include_granular_combos']
#     return rag_builder(compare_templates=compare_templates, include_granular_combos=include_granular_combos,src_data=src_data,test_data=test_data,disabled_opts=[])

# import generate_data
# config = {
#     "compareTemplates": True,
#     "generateSyntheticData": True,
#     "sourceData": "/Users/ashwinaravind/Desktop/working_autorag/autorag/InputFiles",
#     "syntheticDataGeneration": {
#         "testSize": 5,
#         "criticLLM": {
#             "model": "gpt-3.5-turbo-16k",
#             "temperature": 0.2
#         },
#         "generatorLLM": {
#             "model": "gpt-3.5-turbo-16k",
#             "temperature": 0.2
#         },
#         "embedding": {
#             "model": "text-embedding-3-large"
#         }
#     }

# }
# def parse_config():
#     #print(config)
#     compareTemplates=config["compareTemplates"]
#     gen_synthetic_data=config["generateSyntheticData"]
#     path=config["sourceData"]

#     src_data={ 1 : {'source':'url','input_path': path}}
#     if gen_synthetic_data:
#         # test_size=config["syntheticDataGeneration"]["testSize"]
#         # critic_llm=config["syntheticDataGeneration"]["criticLLM"]
#         # generator_llm=config["syntheticDataGeneration"]["generatorLLM"]
#         # embeddings=config["syntheticDataGeneration"]["embedding"]
#         # TODO: Add Distribution
#         # event_loop=asyncio.get_event_loop()
#         f_name=generate_data.generate_data(
#             src_data=path
#             # test_size=test_size,
#             # generator_llm=generator_llm,
#             # critic_llm=critic_llm,
#             # embeddings=OpenAIEmbeddings()
#         )
#     else:
#         f_name=config["testDataPath"]

#     # return rag_builder(compareTemplates=compareTemplates, src_data=src_data, test_data=f_name)


parse_config()



