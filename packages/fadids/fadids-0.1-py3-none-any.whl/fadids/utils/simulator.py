from abc import ABC
import time
from typing import Any, Dict
import numpy as np


class StreamSimulator(ABC):
    def __init__(self, model, data: np.ndarray, step: int = 30, timesleep: float = 0) -> None:
        """Initialize a stream simulator with a anomaly detection model 

        Args:
            model: model from streamad and embedded in an adaptator from this package 
            data (np.ndarray): data for training.
            step (int, optional):  number of values to skip between each iteration. Defaults to 30.
            timesleep (float, optional): Time to wait in second between each iteration. Defaults to 0.
        """
        self.model = model
        self.data = data
        self.step = step
        self.timesleep = timesleep

    def __call__(self) -> None:
        """Start the simulation. Loop on the whole data
        """
        current_index = 0
        last_index = 0
        while current_index < len(self.data):
            current_index += self.step
            sample = self.data[last_index:current_index]
            self.model.fit(sample)
            last_index = current_index
            time.sleep(self.timesleep)

    def get_results(self, return_scores=False) -> Dict[int, Any]:
        if return_scores:
            return self.model.get_anomalies(), self.model.get_scores()
        else:
            return self.model.get_anomalies()
