"""
overcluster: a library for generating overlapping cluster membership
"""

__version__ = "0.1.2"

from .utils import *
from ._bisect_q_means import BisectingQMeans

__all__ = [
        "BisectingQmeans",
        "overcluster",
        "select_central_point",
        "slow_bisecting_kmeans"]
