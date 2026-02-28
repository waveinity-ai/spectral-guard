__version__ = "2.0.0"

from .core.proposed_edge import ProposedEdge
from .core.circuit_breaker import SpectralGuard, ValidationResult

__all__ = ["ProposedEdge", "SpectralGuard", "ValidationResult"]