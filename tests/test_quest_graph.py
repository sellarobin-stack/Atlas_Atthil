from app.optimizer.quest_graph import QuestGraph
from app.optimizer.quest_node import QuestNode


def test_add_node():

    graph = QuestGraph()

    graph.add_node(
        QuestNode(
            quest_id=1,
            name="Quest 1",
            level=1,
        )
    )

    assert len(graph) == 1


def test_dependency():

    graph = QuestGraph()

    graph.add_node(QuestNode(1, "A", 1))
    graph.add_node(QuestNode(2, "B", 1))

    graph.add_dependency(1, 2)

    assert graph.get_node(1).children == {2}
    assert graph.get_node(2).parents == {1}


def test_roots():

    graph = QuestGraph()

    graph.add_node(QuestNode(1, "A", 1))
    graph.add_node(QuestNode(2, "B", 1))

    graph.add_dependency(1, 2)

    roots = graph.roots()

    assert len(roots) == 1
    assert roots[0].quest_id == 1


def test_leaves():

    graph = QuestGraph()

    graph.add_node(QuestNode(1, "A", 1))
    graph.add_node(QuestNode(2, "B", 1))

    graph.add_dependency(1, 2)

    leaves = graph.leaves()

    assert len(leaves) == 1
    assert leaves[0].quest_id == 2

def test_available():

    graph = QuestGraph()

    graph.add_node(QuestNode(1, "A", 1))
    graph.add_node(QuestNode(2, "B", 1))

    graph.add_dependency(1, 2)

    available = graph.available(set())

    assert len(available) == 1
    assert available[0].quest_id == 1

def test_available_after_completion():

    graph = QuestGraph()

    graph.add_node(QuestNode(1, "A", 1))
    graph.add_node(QuestNode(2, "B", 1))

    graph.add_dependency(1, 2)

    available = graph.available({1})

    assert len(available) == 1
    assert available[0].quest_id == 2

def test_blocked():

    graph = QuestGraph()

    graph.add_node(QuestNode(1, "A", 1))
    graph.add_node(QuestNode(2, "B", 1))

    graph.add_dependency(1, 2)

    blocked = graph.blocked(set())

    assert len(blocked) == 1
    assert blocked[0].quest_id == 2