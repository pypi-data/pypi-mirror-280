import os

from dotenv import load_dotenv
from neo4j import GraphDatabase

from graph_store.base import GraphStore

load_dotenv()
NEO4J_PASSWORD = os.environ.get('NEO4J_PASSWORD')
NEO4J_URI  = os.environ.get('NEO4J_URI')
NEO4J_USERNAME = os.environ.get('NEO4J_USERNAME')
class Neo4jStore(GraphStore):

    def get_connection(self):
        # Define the connection details for your Neo4j database
        uri = NEO4J_URI
        username = "neo4j"
        password = NEO4J_PASSWORD  # Change this to your actual Neo4j password

        # Create a Neo4j driver instance
        driver = GraphDatabase.driver(uri, auth=(username, password))

        return driver

    def create_node(self,session, label, properties):
        """
        Create a node with the given label and properties.
        """
        properties_string = ', '.join(f'{key}: ${key}' for key in properties.keys())
        query = f"CREATE (n:{label} {{{properties_string}}})"
        session.run(query, **properties)

    def create_relationship(self,session, node1_label, node1_properties, relationship, node2_label, node2_properties):
        """
        Create a relationship between two nodes.
        """
        match_node1 = ' AND '.join(f'n1.{key} = ${key}1' for key in node1_properties.keys())
        match_node2 = ' AND '.join(f'n2.{key} = ${key}2' for key in node2_properties.keys())
        query = f"""
        MATCH (n1:{node1_label}), (n2:{node2_label})
        WHERE {match_node1} AND {match_node2}
        CREATE (n1)-[:{relationship}]->(n2)
        """
        params = {f'{key}1': value for key, value in node1_properties.items()}
        params.update({f'{key}2': value for key, value in node2_properties.items()})
        session.run(query, **params)

    def create_nodes_and_relationships(self,nodes, relationships):
        """
        Create nodes and relationships in the Neo4j database.
        :param nodes: List of tuples containing node label and properties dictionary.
        :param relationships: List of tuples containing two nodes and relationship type.
        """
        driver = self.get_connection()
        with driver.session() as session:
            for label, properties in nodes:
                self.create_node(session, label, properties)

            for (node1_label, node1_properties), relationship, (node2_label, node2_properties) in relationships:
                self.create_relationship(session, node1_label, node1_properties, relationship, node2_label, node2_properties)
        driver.close()

if __name__=="__main__":
    graph_store = Neo4jStore()
    nodes = [
        ('TajMahal', {'name': 'Taj Mahal', 'location': 'Agra, India, on the banks of the Yamuna River'}),
        ('Country', {'name': 'India'})
    ]

    relationships = [
        (('TajMahal', {'name': 'Taj Mahal'}), 'LOCATED_IN', ('Country', {'name': 'India'}))
    ]

    graph_store.create_nodes_and_relationships(nodes, relationships)

    # Close the driver connection


    print("Nodes and relationships created successfully.")