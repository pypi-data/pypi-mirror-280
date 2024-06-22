from abc import abstractmethod

class BaseEModel:
    @abstractmethod
    def embed(): ... 

class BaseCModel:
    @abstractmethod
    def cluster(): ... 