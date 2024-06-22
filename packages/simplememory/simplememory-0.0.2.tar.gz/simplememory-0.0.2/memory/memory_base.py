import math
from abc import abstractmethod

from pydantic.v1 import BaseModel


class MemoryBase(BaseModel):

    @abstractmethod
    def retrieve_memory_item(self,mem_key:str,kwargs=None):
        pass

    @abstractmethod
    def add_memory_item(self,mem_key:str,mem_val:str):
        pass

    def clean_up_memory(self):
        pass

    def get_retention_score(self, strength:int,days_elapsed_since_last_used:int):
        """
        strength: This parameter denotes the strength of the memory.The strenght of the memory
        is equivalent to the number of times the memory item has been accessed. In case of entity,
        this will be the number of times(count), the entity has been used
        days_elapsed_since_last_used: This is the duration in days that has elapsed from today till the
        memory was last accessed.
        """
        score = math.exp(-days_elapsed_since_last_used / strength)

        return score

