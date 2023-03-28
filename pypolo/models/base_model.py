from abc import ABC, abstractmethod
from typing import Tuple

import numpy as np


class BaseModel(ABC):
    """Interface of a probabilistic model."""

    @abstractmethod
    def learn(self,
              x_new: np.ndarray,
              y_new: np.ndarray,
              num_iter: int,
              verbose: bool = True) -> None:
        r"""Optimizes the model parameters.

        Args:
            x_new (np.ndarray): New training inputs of shape
                (num_inputs, dim_inputs).
            y_new (np.ndarray): New training outputs of shape
                (num_outputs, dim_outputs).
            num_iter (int): Number of optimization/training iterations.
            verbose (bool): Print the optimization information or not?

        Raises:
            NotImplementedError: This is an abstract method and must be
                implemented by derived classes.
        """
        raise NotImplementedError

    @abstractmethod
    def predict(self, x_test: np.ndarray) -> Tuple[np.ndarray, np.ndarray]:
        """Makes predictions.

        Args:
            x_test (np.ndarray): Test inputs of shape (num_inputs, dim_inputs).

        Returns:
            Tuple[np.ndarray, np.ndarray]: A tuple containing predictive mean
                and predictive standard deviation of shape (num_inputs, 1).

        Raises:
            NotImplementedError: This is an abstract method and must be
                implemented by derived classes.
        """
        raise NotImplementedError
