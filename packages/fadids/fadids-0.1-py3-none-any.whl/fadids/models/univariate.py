import numpy as np
from typing import List
from streamad.model import SRDetector


class MeanDeviationAD():
    def __init__(self, window_len=50, threshold=1) -> None:
        """
        Initialize the MeanDeviationAD anomaly detection model.

        Args:
            window_len (int): The number of samples in the moving window.
            threshold (float): The number of standard deviations away from the mean
                               to consider an observation as an anomaly.

        Attributes:
            expected_low (float): Lower boundary for anomaly detection.
            expected_high (float): Upper boundary for anomaly detection.
            init_done (bool): Flag to check if the initialization is complete.
            predictions (list[bool]): List to store anomaly predictions.
            last_sample (list[float]): List to store the last window of observations.
        """
        self.window_len = window_len
        self.threshold = threshold
        self.expected_low: float = 0
        self.expected_high: float = 0
        self.init_done: bool = False
        self.predictions = []
        self.last_sample = []

    def fit(self, data: List[float]):
        """Fill a list of last data values, and predict if the list > window.size. Finally, reduct the list.

        Args:
            data (List[float]): values for fit and predict
        """
        current_sample = self.last_sample + data
        if len(current_sample) > self.window_len:
            for index in range(len(current_sample)):
                if index >= self.window_len:
                    self._predict(current_sample[index-self.window_len:index])
        try:
            self.last_sample = current_sample[-self.window_len:]
        except KeyError:
            self.last_sample = current_sample

    def _predict(self, data):
        means = np.mean(data)
        deviations = np.std(data)
        if self.init_done:  # initialize expected values before anomaly detection
            pred_tmp = (means > self.expected_high) | (
                means < self.expected_low)
            self.predictions.append(pred_tmp)
        else:
            for i in range(self.window_len + 1):
                self.predictions.append(False)
            self.init_done = True
        self.expected_high = means + self.threshold * deviations
        self.expected_low = means - self.threshold * deviations

    def check_anomalies(self):
        """check if anomalies are detected"""
        return np.array(self.predictions).any()

    def get_anomalies(self):
        '''return a list of anomalies indices'''
        indices_true = [index for index,
                        value in enumerate(self.predictions) if value]
        return indices_true

    def get_scores(self):
        """return scores anomalies scores for each prediction

        Returns:
            Dict[int, float]: dictionnaire score
        """
        idxs = [i for i in range(len(self.predictions))]
        scores = dict(zip(idxs, self.predictions))
        return scores


class AbstractContainer():
    def __init__(self, model, threshold: float, initialization: int, pca=False) -> None:
        """Initialize a model for anomaly detection in data stream

        Args:
            model (_type_): a streamad model
            threshold (float): threshold that will change the numbers of anomaly detected
            initialization (int): number of values to wait before the anomaly detection
        """
        self.model = model
        self.threshold = threshold
        self.initialization = initialization
        self.anomalies_scores = []
        self.predictions = []

    def update() -> None:
        """fit the model and calcul an anomaly score for each new point based on drift concept"""
        pass

    def check_anomalies(self) -> bool:
        """check if anomalies are detected"""

        return np.array(self.predictions).any()

    def get_anomalies(self) -> List[int]:
        '''return a list of anomalies indices'''
        indices_true = [index for index,
                        value in enumerate(self.predictions) if value]
        return indices_true


class UnivariateContainer(AbstractContainer):
    def __init__(self, model, threshold: float = 0.9, initialization: int = 600) -> None:
        super().__init__(model, threshold, initialization)

    def fit(self, data: np.ndarray):
        current_data = data.reshape(-1, 1)
        for x in current_data:
            score = self.model.fit_score(x)
            try:
                if (score > self.threshold) & (len(self.anomalies_scores) > self.initialization):
                    self.predictions.append(True)
                else:
                    self.predictions.append(False)
            except TypeError:
                self.predictions.append(False)
            self.anomalies_scores.append(score)
