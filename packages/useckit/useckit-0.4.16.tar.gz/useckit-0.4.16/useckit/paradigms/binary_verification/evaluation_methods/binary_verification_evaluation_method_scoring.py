import json
from pathlib import Path

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from sklearn.metrics import auc

from useckit import Dataset
from useckit.paradigms.binary_verification.evaluation_methods.binary_verification_evaluation_method_base import \
    VerificationBaseEvaluationMethod
from useckit.paradigms.binary_verification.prediction_models.verification_prediction_model_base import \
    VerificationBasePredictionModel


class BinaryScoringVerification(VerificationBaseEvaluationMethod):
    def evaluate(self, dataset: Dataset, prediction_model: VerificationBasePredictionModel, **kwargs):
        # The `prediction_model` contains fitted classifiers.

        # Extract multiclass_classification_strategy from kwargs or set default to 'ovr'
        multiclass_classification_strategy = kwargs.get('multiclass_classification_strategy', 'ovr').lower()
        if multiclass_classification_strategy not in ["ovr", "ova", "ovo"]:
            raise ValueError(f'multiclass_classification_strategy must be in ["ovr", "ova", "ovo"], '
                             f'but {multiclass_classification_strategy} was provided.')
        if multiclass_classification_strategy == "ova":  # Align different spellings
            multiclass_classification_strategy = "ovr"

        # Unpack prediction_model
        classifs = prediction_model.classifs
        labels_per_classif = prediction_model.labels_per_classif
        self.output_dir = Path(prediction_model.output_dir).parent / "evaluation"
        self.verbose = prediction_model.verbose

        # Unpack dataset
        reject_label = dataset.reject_label
        matching_data = dataset.testset_matching_data
        matching_labels = dataset.testset_matching_labels

        # Prepare result storage
        if multiclass_classification_strategy == "ovr":
            results = self._run_ovr(classifs, labels_per_classif, matching_data, matching_labels,
                                    getattr(dataset, 'testset_enrollment_slicedsample_origin', None))
        elif multiclass_classification_strategy == "ovo":
            results = self._run_ovo(classifs, labels_per_classif, matching_data, matching_labels,
                                    getattr(dataset, 'testset_enrollment_slicedsample_origin', None))

        proba_metrics = self._calculate_proba_based_predictions(results)

        self.plot_eer(proba_metrics)
        self.plot_auc(proba_metrics)

    def _run_ovr(self, classifs, labels_per_classif, matching_data, matching_labels, slicedsample_origin_idx=None):
        results = []

        # Run matching data for all classifiers
        for label, classif in zip(labels_per_classif, classifs):
            y_scores = classif.predict_proba(matching_data)[:, 0]

            if slicedsample_origin_idx is not None:
                raise NotImplementedError("Majority-Voting is not implemented here, yet [1].")

            y_true = (matching_labels == label).astype(int)
            results.append({'clf_class one label': label,
                            'y_scores': y_scores,
                            'y_true': y_true,
                            'matching_labels': matching_labels,
                            'method': 'ovr'})

        return results

    def _run_ovo(self, classifs, labels_per_classif, matching_data, matching_labels, slicedsample_origin_idx=None):
        results = []

        # Iterate over all possible pairs of classifiers/labels
        for i, (label_one, classif_one) in enumerate(zip(labels_per_classif, classifs)):
            for j, (label_other, classif_other) in enumerate(zip(labels_per_classif, classifs)):
                if i >= j:
                    continue  # Skip same classifier comparisons and ensure each pair is only computed once

                # Select data where the matching label is either label_one or label_other
                data_indices = (matching_labels == label_one) | (matching_labels == label_other)
                selected_data = matching_data[data_indices]
                selected_labels = matching_labels[data_indices]

                # Compute probability scores for class corresponding to label_one
                y_scores = classif_one.predict_proba(selected_data)[:, 0]

                if slicedsample_origin_idx is not None:
                    raise NotImplementedError("Majority-Voting is not implemented here, yet [2].")

                # Create true labels array: 1 where the label matches label_one, otherwise 0
                y_true = (selected_labels == label_one).astype(int)

                # Append results
                results.append({
                    'clf_class one label': label_one,
                    'clf_class other label': label_other,
                    'y_scores': y_scores,
                    'y_true': y_true,
                    'matching_labels': selected_labels,
                    'method': 'ovo'
                })

        return results

    def _calculate_proba_based_predictions(self, results: list[dict]):
        all_y_scores = np.unique(np.concatenate([r['y_scores'] for r in results]))

        min_score = min(all_y_scores) - 0.000001
        max_score = max(all_y_scores) + 0.000001

        all_y_scores = np.concatenate([[min_score], all_y_scores, [max_score]])

        metric_results = []

        for threshold in all_y_scores:
            for r in results:  # for every identity
                current_class_label = r['clf_class one label']

                # init
                tp = fp = tn = fn = 0

                for matching_label, prediction_score in zip(r['matching_labels'], r['y_scores']):
                    if prediction_score <= threshold:  # ACCEPT
                        if current_class_label == matching_label:
                            # true positive
                            tp += 1
                        else:
                            # false positive
                            fp += 1
                    else:  # REJECT
                        if current_class_label == matching_label:
                            # false negative
                            fn += 1
                        else:
                            # true negative
                            tn += 1

                metric_results.append({'threshold': threshold, 'tp': tp, 'fp': fp, 'tn': tn, 'fn': fn})
        return metric_results

    def plot_eer(self, proba_metrics):
        df = pd.DataFrame(proba_metrics)

        df['fpr'] = df.apply(lambda row: self.calculate_fpr(row['fp'], row['tn']), axis=1)
        df['fnr'] = df.apply(lambda row: self.calculate_fnr(row['fn'], row['tp']), axis=1)

        # Calculate the point where FPR and FNR are closest (EER)
        df['eer_diff'] = np.abs(df['fpr'] - df['fnr'])
        eer_threshold = df.loc[df['eer_diff'].idxmin(), 'threshold']
        eer_value = df.loc[df['eer_diff'].idxmin(), 'fpr']

        # Plotting
        plt.figure(figsize=(10, 5))
        plt.plot(df['threshold'], df['fpr'], label='False Positive Rate (FPR / FAR)')
        plt.plot(df['threshold'], df['fnr'], label='False Negative Rate (FNR / FRR)')
        plt.axvline(x=eer_threshold, color='r', linestyle='--', label=f'EER at threshold {eer_threshold:.5f}')
        plt.title('Equal Error Rate (EER) Analysis')
        plt.xlabel('Threshold')
        plt.ylabel('Error Rate')
        plt.legend()
        plt.grid(True)
        plt.savefig(Path(self.output_dir) / 'eer.pdf', bbox_inches="tight")

        if self.verbose:
            print(f"The Equal Error Rate (EER) is approximately {eer_value:.2f} at threshold {eer_threshold:.5f}")

        # Write data to a JSON file
        with open(Path(self.output_dir) / 'eer.json', 'w') as file:
            json.dump({"eer_threshold": eer_threshold, "eer_value": eer_value}, file, indent=4)
        df.to_csv(Path(self.output_dir) / 'eer-data.tsv', sep='\t', index=False)


    def plot_auc(self, proba_metrics):
        df = pd.DataFrame(proba_metrics)

        # Calculate the ROC curve and AUC
        df["fpr"] = df.apply(lambda row: self.calculate_fpr(fp=row['fp'], tn=row['tn']), axis=1)
        df["tpr"] = df.apply(lambda row: self.calculate_tpr(tp=row['tp'], fn=row['fn']), axis=1)
        df_sorted = df.sort_values(by="fpr")
        roc_auc = auc(x=df_sorted["fpr"].values, y=df_sorted["tpr"].values)

        # Plotting
        plt.figure(figsize=(6, 5))
        plt.plot(df.fpr, df.tpr, color='darkorange', lw=2, label=f'ROC curve (AUC = {roc_auc:.2f})')
        plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--', label=f'Random Guess (AUC = 0.5)')
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('Receiver Operating Characteristic (ROC)')
        plt.legend(loc="lower right")
        plt.grid(True)
        plt.savefig(Path(self.output_dir) / 'roc_curve.pdf', bbox_inches="tight")

        if self.verbose:
            print(f"The Area Under the Curve (AUC) is {roc_auc:.2f}")

        # Write AUC to a JSON file
        with open(Path(self.output_dir) / 'auc.json', 'w') as file:
            json.dump({"auc_value": roc_auc}, file, indent=4)

    @staticmethod
    def calculate_fpr(fp, tn):
        try:
            return fp / (fp + tn)
        except ZeroDivisionError:
            print("useckit warning: Calculation of false positive rate lead resulted in division by zero, setting to 1.0.")
            return 1.0

    @staticmethod
    def calculate_fnr(fn, tp):
        try:
            return fn / (fn + tp)
        except ZeroDivisionError:
            print("useckit warning: Calculation of false negative rate resulted in division by zero, setting to 1.0.")
            return 1.0

    @staticmethod
    def calculate_tpr(tp, fn):
        try:
            return tp / (tp + fn)
        except ZeroDivisionError:
            print("useckit warning: Calculation of true positive rate lead to division by zero, setting to 0.0.")
            return 0.0
