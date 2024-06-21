import os
import pickle

import numpy as np
from sklearn.svm import SVC

from useckit import Dataset
from useckit.paradigms.anomaly_detection.prediction_models.scikit_model_descriptions import ScikitBaseDescription
from useckit.paradigms.binary_verification.prediction_models.scikit_model_descriptions import ScikitClassif
from useckit.paradigms.binary_verification.prediction_models.verification_prediction_model_base import \
    VerificationBasePredictionModel


class VerificationSkLearnPredictionModel(VerificationBasePredictionModel):
    def __init__(self,
                 scikit_binary_classif: ScikitBaseDescription = ScikitClassif(),
                 output_dir: str = "scikit_pred_model_out",
                 verbose=False):
        super().__init__(output_dir=output_dir, verbose=verbose)
        self.build_description = scikit_binary_classif
        self.classifs = []
        self.labels_per_classif = []

    def persist_model_trainables(self, path_like: str = 'saved_trainable_values', **kwargs):
        classifs_file = os.path.join(self.output_dir, path_like)
        labels_per_classif_file = os.path.join(os.path.dirname(os.path.join(self.output_dir, path_like)),
                                                "labels_per_classif.persisted")
        with open(classifs_file, "wb") as file:
            pickle.dump(self.classifs, file)
        with open(labels_per_classif_file, "wb") as file:
            pickle.dump(self.labels_per_classif, file)

    def restore_model_trainables(self, path_like: str, **kwargs):
        classifs_file = os.path.join(self.output_dir, path_like)
        labels_per_classif_file = os.path.join(os.path.dirname(os.path.join(self.output_dir, path_like)),
                                                "labels_per_classif.persisted")
        with open(classifs_file, "rb") as file:
            self.classifs = pickle.load(file)
        with open(labels_per_classif_file, "rb") as file:
            self.labels_per_classif = pickle.load(file)

    def build_model(self, nb_classes):
        result = []
        for i in range(nb_classes):
            result.append(self.build_description.build_model())
        return result

    def fit(self, dataset: Dataset):
        x_train, y_train = dataset.trainset_data, dataset.trainset_labels
        x_train = x_train.reshape((x_train.shape[0], np.prod(x_train.shape[1:])))
        nb_classes = dataset.train_classes()
        assert nb_classes > 0
        classifs_built = self.build_model(nb_classes)
        for i, classif in zip(np.unique(y_train), classifs_built):
            # find the elements in the training data that belong to class `i`
            belonging_indexes = y_train == i
            y_train_clf = belonging_indexes.astype(int)

            classif.fit(x_train, y_train_clf)
            self.labels_per_classif.append(i)
        self.classifs = classifs_built

    def predict(self, x_test):
        x_test = x_test.reshape((x_test.shape[0], np.prod(x_test.shape[1:])))
        result_pred = []
        result_id = []
        for i, classif in zip(self.labels_per_classif, self.classifs):
            preds = classif.predict(x_test)
            result_pred.append(preds)
            result_id.append(i)
        return np.array(result_pred), np.array(result_id)
