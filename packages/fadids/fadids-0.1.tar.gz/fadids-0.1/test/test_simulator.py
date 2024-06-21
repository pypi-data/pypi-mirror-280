import pytest
import numpy as np
from unittest.mock import MagicMock
from fadids.utils.simulator import StreamSimulator
import time

N_POINTS = 100


@pytest.fixture
def sample_data():
    # Create sample data to pass to the simulator
    return np.random.rand(N_POINTS)


@pytest.fixture
def mock_model():
    # Create a mock model with mock methods for fit, get_anomalies, and get_scores.
    model = MagicMock()
    model.fit = MagicMock()
    model.get_anomalies = MagicMock(return_value=[4, 5])
    model.get_scores = MagicMock(return_value={4: "0.8", 5: "0.85"})
    return model


def test_stream_simulation_with_no_delay(mock_model, sample_data):
    start = time.perf_counter_ns()
    simulator = StreamSimulator(
        model=mock_model, data=sample_data, timesleep=0)
    simulator()
    end = time.perf_counter_ns()
    elapsed_time_ms = (end - start) / 1e6  # milliseconds
    assert elapsed_time_ms <= 100


def test_stream_simulation_with_delay(mock_model, sample_data):
    start = time.perf_counter_ns()
    simulator = StreamSimulator(
        model=mock_model, data=sample_data, timesleep=0.05)
    simulator()
    end = time.perf_counter_ns()
    elapsed_time_ms = (end - start) / 1e6  # milliseconds
    assert elapsed_time_ms > 100


STEPS = [1, 10, 50]


@pytest.mark.parametrize("step", STEPS)
def test_stream_simulation_with_differents_steps(mock_model, sample_data, step):
    simulator = StreamSimulator(
        model=mock_model, data=sample_data, step=step)
    simulator()

    # Ensure fit is called the correct number of times
    assert mock_model.fit.call_count == N_POINTS / step
    expected_results = ([4, 5], {4: "0.8", 5: "0.85"})
    expected_short_results = [4, 5]
    results = simulator.get_results(return_scores=True)
    # Should return anomalies and scores as a tuple
    assert results == expected_results
    simulator.model.get_anomalies.assert_called_once()
    simulator.model.get_scores.assert_called_once()
    short_results = simulator.get_results(return_scores=False)
    # Should return only anomalies
    assert short_results == expected_short_results
