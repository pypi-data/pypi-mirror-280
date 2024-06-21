from fadids.models.univariate import MeanDeviationAD
from fadids.utils import simulator
import random


def generate_data(size=1000):
    # Générer 1000 valeurs normales entre 10 et 20
    data = [random.uniform(10, 20) for _ in range(size)]

    # Sélectionner 5 indices aléatoires pour les anomalies
    indices_anomalies = random.sample(range(1000), 5)

    # Insérer les anomalies avec des valeurs entre 30 et 40
    for indice in indices_anomalies:
        data[indice] = random.uniform(30, 40)

    return data, indices_anomalies


def test_anomaly_detection_with_high_threshold():
    data, indices_anomalies = generate_data()
    model = MeanDeviationAD(window_len=50, threshold=5)

    # Créer et exécuter le simulateur
    test_simulator = simulator.StreamSimulator(model=model, data=data)
    test_simulator()
    # Obtenir les résultats
    anomalies_detected, _ = test_simulator.get_results(return_scores=True)
    assert len(anomalies_detected) == 0
    # check if anomalies are detected
    assert test_simulator.model.check_anomalies() == False


def test_anomaly_detection_with_low_threshold():
    data, indices_anomalies = generate_data()
    model = MeanDeviationAD(window_len=50, threshold=0.1)

    # Créer et exécuter le simulateur
    test_simulator = simulator.StreamSimulator(model=model, data=data)
    test_simulator()
    anomalies_detected = test_simulator.get_results(return_scores=False)
    assert len(anomalies_detected) > 0
    # check if anomalies are detected
    assert test_simulator.model.check_anomalies() == True
