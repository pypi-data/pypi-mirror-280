import os

from dotenv import load_dotenv
from langchain_community.graphs import Neo4jGraph
from langchain_core.documents import Document
from langchain_experimental.graph_transformers import LLMGraphTransformer
from langchain_openai import ChatOpenAI

from memory.memory_base import MemoryBase

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
NEO4J_URI = os.environ.get('NEO4J_URI')
NEO4J_USERNAME = os.environ.get("NEO4J_USERNAME")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD")

graph = Neo4jGraph(url=NEO4J_URI,
                   username=NEO4J_USERNAME,
                   password=NEO4J_PASSWORD)


class EntityMemory(MemoryBase):
    class Config:
        arbitrary_types_allowed = True

    def retrieve_memory_item(self, mem_key: str, kwargs=None):
        pass

    def add_memory_item(self, mem_key: str, mem_val: str):
        graph_documents = self.extract_entities(mem_key,mem_val)
        graph.add_graph_documents(
            graph_documents,
            baseEntityLabel=True,
            include_source=True
        )

    def extract_entities(self,mem_key: str, mem_val: str):
        llm = ChatOpenAI(temperature=0, model_name="gpt-4")
        llm_transformer = LLMGraphTransformer(llm=llm)
        documents=[Document(page_content=mem_val)]

        graph_documents = llm_transformer.convert_to_graph_documents(documents)
        return graph_documents


# if __name__ == "__main__":
#     llm = ChatOpenAI()
#     em = EntityMemory()
#     sm = SemanticMemory()
#     generation_prompt = ChatPromptTemplate.from_messages([
#         (
#             "system",
#             "You will answer based on a question asked."
#             " Please ensure to add all necessary details."
#             "If you receive a critique, respond with a modified version of your response that incorporates the "
#             "critique comments.",
#         ),
#         MessagesPlaceholder(variable_name="messages"), ])
#     generate = generation_prompt | ChatOpenAI()
#     while True:
#         user_input = input("User: ")
#         messages = generate.invoke({"messages": [user_input]})
#         em.add_memory_item(
#             mem_key=user_input,
#             mem_val=messages.content,
#         )
#         sm.add_memory_item(mem_key=user_input,
#             mem_val=messages.content)

