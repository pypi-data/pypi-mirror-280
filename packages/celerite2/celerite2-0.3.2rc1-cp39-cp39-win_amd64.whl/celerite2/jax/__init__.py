# -*- coding: utf-8 -*-

import logging

logger = logging.getLogger(__name__)

from jax import config  # noqa isort:skip

if not config.read("jax_enable_x64"):
    logger.warning(
        "celerite2.jax only works with dtype float64. "
        "We're enabling x64 now, but you might run into issues if you've "
        "already run some jax code.\n"
        "You can squash this warning by setting the environment variable "
        "'JAX_ENABLE_X64=True' or by running:\n"
        ">>> from jax import config\n"
        ">>> config.update('jax_enable_x64', True)"
    )
    config.update("jax_enable_x64", True)


__all__ = ["terms", "GaussianProcess", "CeleriteNormal"]

from celerite2.jax import terms  # noqa isort:skip
from celerite2.jax.celerite2 import GaussianProcess  # noqa isort:skip
