import math
from pydantic import BaseModel

class ProposedEdge(BaseModel):
    """
    Pydantic model representing a proposed edge from a neuro-symbolic agent.
    Contains cached Fiedler coordinates for O(1) validation.
    """
    source_id: str
    target_id: str
    v2_source: float     # Cached combinatorial Fiedler coord
    v2_target: float
    edge_weight: float = 1.0
    current_cheeger_h: float
    cache_stale: bool = False
    source_degree: int = 1
    target_degree: int = 1

    def spectral_stretch(self) -> float:
        """Computes the degree-weighted first-order Fiedler perturbation."""
        degree_factor = 1.0 / (1 + math.log1p(
            min(self.source_degree, self.target_degree)))
        
        return self.edge_weight * degree_factor * \
               (self.v2_source - self.v2_target) ** 2

    def is_wormhole(self, tau: float) -> bool:
        """Evaluates if the proposed edge violates the topological threshold."""
        return self.spectral_stretch() > tau