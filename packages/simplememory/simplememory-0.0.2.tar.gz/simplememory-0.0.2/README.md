# simplememory
This will be the memory of the agents and agency

**To use this package:**

Ensure that a `.env` exists with below parameters.

```
OPENAI_API_KEY=sk-"ADD YOUR API KEY HERE"
PINECONE_API_KEY = "ADD YOUR API KEY HERE"
PINECONE_INDEX="ADD YOUR INDEX NAME HERE"
```
If using entity memory, below parameters are needed
```
OPENAI_API_KEY = "ADD YOUR API KEY HERE"
NEO4J_URI = "ADD YOUR NEO4J URI HERE"
NEO4J_USERNAME = "ADD YOUR NEO4J USERNAME HERE"
NEO4J_PASSWORD = "ADD YOUR NEO4J PASSWORD"

```

**How to add to semantic memory:**
```
from memory.semantic_memory import SemanticMemory
if __name__=="__main__":
    sc= SemanticMemory()
    semantic_val,memory_item = sc.add_memory_item(mem_key="What is the capital of india?",mem_val="The capital of India is New Delhi"
    print(semantic_val)
    print(memory_item)

```
**How to retrieve semantic memory:**
```
from memory.semantic_memory import SemanticMemory
if __name__=="__main__":
    sc= SemanticMemory()
    result = sc.retrieve_memory_item(mem_key="what is the capital of India?")
    print(result['matches'][0]['metadata']['key'])
    print(result['matches'][0]['metadata']['value'])
    print(result['matches'][0]['score'])
```

**How to add entity memory:**
```python
from memory.entity_memory import EntityMemory

if __name__=="__main__":
    sc= EntityMemory()
    sc.add_memory_item(mem_key="What is the capital of India?",mem_val="The capital of India is New Delhi")

```
