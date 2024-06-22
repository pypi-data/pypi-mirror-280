"""
overcluster: a library for generating overlapping cluster membership
"""

__version__ = "0.1.3"

from .utils import *
from .bisect_q_means import BisectingQMeans

__all__ = [
        "BisectingQmeans",
        "overcluster",
        "select_central_point",
        "slow_bisecting_kmeans"]
