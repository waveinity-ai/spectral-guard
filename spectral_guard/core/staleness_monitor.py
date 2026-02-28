from dataclasses import dataclass
from enum import Enum

DELTA_TOL = 0.05  # Configurable drift tolerance

class StaleStatus(Enum):
    FRESH = "FRESH"
    STALE = "STALE"
    CRITICAL = "CRITICAL"

@dataclass
class CacheMeta:
    lambda1: float
    lambda2: float
    max_edge_weight: float
    edges_since_recal: int

class StalenessMonitor:
    """Monitors Fiedler vector cache validity using Davis-Kahan drift bounds."""
    
    def check(self, meta: CacheMeta) -> StaleStatus:
        spectral_gap = meta.lambda2 - meta.lambda1
        
        if spectral_gap < 1e-8:
            return StaleStatus.CRITICAL
            
        drift = (meta.edges_since_recal * meta.max_edge_weight) / spectral_gap
        
        if drift > 2 * DELTA_TOL:
            return StaleStatus.CRITICAL
        elif drift > DELTA_TOL:
            return StaleStatus.STALE
            
        return StaleStatus.FRESH