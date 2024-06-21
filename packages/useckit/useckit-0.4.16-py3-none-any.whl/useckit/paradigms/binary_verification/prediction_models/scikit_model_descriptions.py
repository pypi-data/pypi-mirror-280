from abc import ABC, abstractmethod

from sklearn.svm import SVC


class ScikitBaseDescription(ABC):

    @abstractmethod
    def build_model(self):
        pass


class ScikitClassif(ScikitBaseDescription):

    def __init__(self, scikit_classif_class=SVC, classif_kwargs: dict = None):
        self.classif_class = scikit_classif_class
        self.classif_kwargs = {'probability': True} if classif_kwargs is None else classif_kwargs

    def build_model(self):
        return self.classif_class(**self.classif_kwargs)
