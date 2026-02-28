from pydantic import BaseModel
from spectral_guard.core.proposed_edge import ProposedEdge

class ValidationResult(BaseModel):
    is_wormhole: bool
    stretch: float
    correction_prompt: str

class SpectralGuard:
    """The main O(1) topological circuit breaker for Agentic AI workflows."""
    
    def __init__(self, cheeger_h: float, tau: float = 0.45):
        self.cheeger_h = cheeger_h
        self.tau = tau

    def validate(self, edge: ProposedEdge) -> ValidationResult:
        stretch = edge.spectral_stretch()
        is_wormhole = stretch > self.tau
        
        prompt = "✅ Edge accepted."
        if is_wormhole:
            prompt = (
                f"🚨 SYSTEM CORRECTION: Rejecting proposed edge from '{edge.source_id}' "
                f"to '{edge.target_id}'. The degree-weighted Spectral Stretch ({stretch:.2f}) "
                f"exceeds the safety threshold of {self.tau}. This is an ontological wormhole."
            )
        
        return ValidationResult(
            is_wormhole=is_wormhole,
            stretch=stretch,
            correction_prompt=prompt
        )