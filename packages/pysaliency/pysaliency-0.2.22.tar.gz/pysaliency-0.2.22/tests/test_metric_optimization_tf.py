import numpy as np
import pytest


# from pysaliency.metric_optimization_tf import maximize_expected_sim


@pytest.mark.skip("tensorflow <2.0 not available for new python versions, need to upgrade to tensorflow 2 in pysaliency")
def test_maximize_expected_sim_decay_1overk():
    density = np.ones((20, 20))
    density[6:17, 8:12] = 20
    density[2:4, 18:18] = 30
    density /= density.sum()
    log_density = np.log(density)

    saliency_map, score = maximize_expected_sim(
        log_density=log_density,
        kernel_size=1,
        train_samples_per_epoch=1000,
        val_samples=1000,
        max_iter=100
    )

    np.testing.assert_allclose(score, -0.8202789932489393, rtol=5e-7)  # need bigger tolerance to handle differences between CPU and GPU


@pytest.mark.skip("tensorflow <2.0 not available for new python versions, need to upgrade to tensorflow 2 in pysaliency")
def test_maximize_expected_sim_decay_on_plateau():
    density = np.ones((20, 20))
    density[6:17, 8:12] = 20
    density[2:4, 18:18] = 30
    density /= density.sum()
    log_density = np.log(density)

    saliency_map, score = maximize_expected_sim(
        log_density=log_density,
        kernel_size=1,
        train_samples_per_epoch=1000,
        val_samples=1000,
        max_iter=100,
        backlook=1,
        min_iter=10,
        learning_rate_decay_scheme='validation_loss',
    )

    np.testing.assert_allclose(score, -0.8203513294458387, rtol=5e-7)  # need bigger tolerance to handle differences between CPU and GPU
