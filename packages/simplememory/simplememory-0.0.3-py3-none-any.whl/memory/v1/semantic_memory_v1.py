import os
import logging

from dotenv import load_dotenv
from langchain_openai import OpenAIEmbeddings
from pinecone import Pinecone

from graph_store.neo4j_store import Neo4jStore
from memory.memory_base import MemoryBase

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
NEO4J_URI = os.environ.get('NEO4J_URI')
NEO4J_USERNAME = os.environ.get("NEO4J_USERNAME")
NEO4J_PASSWORD = os.environ.get("NEO4J_PASSWORD")

logger = logging.getLogger(__name__)


class SemanticMemory(MemoryBase):
    graph_store = Neo4jStore()

    class Config:
        arbitrary_types_allowed = True

    def _embed_memory(self, mem_key):
        client = OpenAIEmbeddings(model="text-embedding-3-large")
        semantic_value = client.embed_query(mem_key)

        return semantic_value

    def retrieve_memory_value(self, mem_key: str, kwargs=None):
        memory_value = self.graph_store.get_item_from_memory(mem_key=mem_key)
        return memory_value

    def retrieve_memory_item(self, mem_key: str, kwargs=None):
        semantic_mem_val = self._embed_memory(mem_key)
        memory_items = self.graph_store.query_memory_vector(input_vector=semantic_mem_val)
        # memory_item = memory_index.query(vector=semantic_mem_val, top_k=1, include_metadata=True)

        return memory_items

    def return_node_relations(self, mem_key: str, mem_val: str):
        try:
            nodes = [('input', {'name': mem_key}), ('output', {'name': mem_val})]
            relationships = [
                (('input', {'name': mem_key}), 'LEADS_TO', ('output', {'name': mem_val}))
            ]
            logger.info("Successfully returned node and relations")
            return nodes, relationships
        except Exception as e:
            logger.error("Failed to return node and relationships")
            print(e)

    def add_memory_item(self, mem_key: str, mem_val: str):
        try:
            nodes, relationships = self.return_node_relations(mem_key, mem_val)
            vector = self._embed_memory(mem_key)
            self._insert_to_mem_store(mem_key, mem_val, nodes, relationships, vector)
            logger.info("Successfuly inserted to memory store, memory key: ", mem_key)
            return nodes, relationships
        except Exception as e:
            logger.error("Adding to memory failed for key: ", mem_key)
            print(e)

    def _insert_to_mem_store(self, mem_key, mem_val, nodes, relationships, vector):
        try:
            logger.info("Adding memory key: ", mem_key)
            self.graph_store.create_nodes_and_relationships(mem_key, mem_val, nodes, relationships, vector)
        except Exception as e:
            logger.error("Failed to insert memory key: ", mem_key)
            print(e)

    def clean_up_memory_item(self):
        pass


if __name__=="__main__":
    sm = SemanticMemory()
    question = "What is blockchain?"
    memory = sm.retrieve_memory_item(mem_key=question)
    memory_key = memory[0]['name']
    print(memory[0]['name'])
    memory_value = sm.retrieve_memory_value(memory_key)
    print(memory_value)