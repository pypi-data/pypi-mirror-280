# simplememory
This will be the memory of the agents and agency

**To use this package:**

Ensure that a `.env` exists with below parameters.

```
OPENAI_API_KEY=sk-"ADD YOUR API KEY HERE"
PINECONE_API_KEY = "ADD YOUR API KEY HERE"
PINECONE_INDEX="ADD YOUR INDEX NAME HERE"
```
If using entity memory or v1 of semantic memory, below parameters are needed
```
OPENAI_API_KEY = "ADD YOUR API KEY HERE"
NEO4J_URI = "ADD YOUR NEO4J URI HERE"
NEO4J_USERNAME = "ADD YOUR NEO4J USERNAME HERE"
NEO4J_PASSWORD = "ADD YOUR NEO4J PASSWORD"

```

**How to add to semantic memory:**
- use v1 of semantic memory which uses NEO4J
```
# Below version will be deprecated use v1
from memory.semantic_memory import SemanticMemory
if __name__=="__main__":
    sc= SemanticMemory()
    semantic_val,memory_item = sc.add_memory_item(mem_key="What is the capital of india?",mem_val="The capital of India is New Delhi"
    print(semantic_val)
    print(memory_item)

```
```python
# V1 of semantic memory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_openai import ChatOpenAI
from memory.v1.semantic_memory_v1 import SemanticMemory

if __name__ == "__main__":
    llm = ChatOpenAI()
    sm = SemanticMemory()
    generation_prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "You will answer based on a question asked.",
        ),
        MessagesPlaceholder(variable_name="messages"), ])
    generate = generation_prompt | ChatOpenAI()
    while True:
        user_input = input("User: ")
        messages = generate.invoke({"messages": [user_input]})
        sm.add_memory_item(mem_key=user_input,
            mem_val=messages.content)
```

**How to retrieve semantic memory:**
- use V1 of sematic memory. It uses NEO4J.
```
# The below will be deprecated
from memory.semantic_memory import SemanticMemory
if __name__=="__main__":
    sc= SemanticMemory()
    result = sc.retrieve_memory_item(mem_key="what is the capital of India?")
    print(result['matches'][0]['metadata']['key'])
    print(result['matches'][0]['metadata']['value'])
    print(result['matches'][0]['score'])
```

```python
from memory.v1.semantic_memory_v1 import SemanticMemory

sm = SemanticMemory()
question = "What is blockchain?"
memory = sm.retrieve_memory_item(mem_key=question)
memory_key = memory[0]['name']
print(memory[0]['name'])
memory_value = sm.retrieve_memory_value(memory_key)
print(memory_value)
```


**How to add entity memory:**
```python
from memory.entity_memory import EntityMemory

if __name__=="__main__":
    sc= EntityMemory()
    sc.add_memory_item(mem_key="What is the capital of India?",mem_val="The capital of India is New Delhi")

```
