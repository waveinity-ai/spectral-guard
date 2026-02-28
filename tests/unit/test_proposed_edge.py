from spectral_guard.core.proposed_edge import ProposedEdge

def test_wormhole_detected():
    """Opposite Fiedler signs -> wormhole"""
    edge = ProposedEdge(
        source_id="A", target_id="B",
        v2_source=0.8, v2_target=-0.7,
        current_cheeger_h=0.12
    )
    assert edge.is_wormhole(tau=0.45) is True

def test_valid_edge_accepted():
    """Same community -> accepted"""
    edge = ProposedEdge(
        source_id="C", target_id="D",
        v2_source=0.3, v2_target=0.35,
        current_cheeger_h=0.12
    )
    assert edge.is_wormhole(tau=0.45) is False