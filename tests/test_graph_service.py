from app.services.graph_service import GraphService


def test_build_engine():

    service = GraphService()

    engine = service.build_engine()

    assert engine is not None

    assert len(engine.graph) > 0