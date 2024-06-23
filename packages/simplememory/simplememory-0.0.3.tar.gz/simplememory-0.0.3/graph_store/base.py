from abc import abstractmethod


class GraphStore():
    @abstractmethod
    def get_connection(self):
        pass