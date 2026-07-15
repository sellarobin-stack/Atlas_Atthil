from app.services.graph_service import GraphService


def test_build_engine():

    with GraphService() as service:

        engine = service.build_engine()

    assert engine is not None
    assert len(engine.graph) > 0


def test_engine_contains_roots():

    with GraphService() as service:

        engine = service.build_engine()

    roots = engine.graph.roots()

    assert len(roots) > 0


def test_engine_contains_leaves():

    with GraphService() as service:

        engine = service.build_engine()

    leaves = engine.graph.leaves()

    assert len(leaves) > 0


def test_available_returns_list():

    with GraphService() as service:

        engine = service.build_engine()

    available = engine.available(set())

    assert isinstance(available, list)


def test_blocked_returns_list():

    with GraphService() as service:

        engine = service.build_engine()

    blocked = engine.blocked(set())

    assert isinstance(blocked, list)