from app.optimizer.quest_graph import QuestGraph
from app.optimizer.quest_node import QuestNode


def build_graph() -> QuestGraph:
    """
        1
       / \
      ▼   ▼
      2   4
      │
      ▼
      3
    """

    graph = QuestGraph()

    graph.add_node(QuestNode(1, "Quest 1", 1))
    graph.add_node(QuestNode(2, "Quest 2", 10))
    graph.add_node(QuestNode(3, "Quest 3", 20))
    graph.add_node(QuestNode(4, "Quest 4", 15))

    graph.add_dependency(1, 2)
    graph.add_dependency(2, 3)
    graph.add_dependency(1, 4)

    return graph


# ---------------------------------------------------------------------
# Nodes
# ---------------------------------------------------------------------


def test_add_node():

    graph = QuestGraph()

    graph.add_node(
        QuestNode(
            1,
            "Quest 1",
            1,
        )
    )

    assert len(graph) == 1


# ---------------------------------------------------------------------
# Dependencies
# ---------------------------------------------------------------------


def test_add_dependency():

    graph = QuestGraph()

    graph.add_node(QuestNode(1, "A", 1))
    graph.add_node(QuestNode(2, "B", 1))

    graph.add_dependency(1, 2)

    assert graph.get_node(1).children == {2}
    assert graph.get_node(2).parents == {1}


# ---------------------------------------------------------------------
# Roots / Leaves
# ---------------------------------------------------------------------


def test_roots():

    graph = build_graph()

    roots = graph.roots()

    assert len(roots) == 1
    assert roots[0].quest_id == 1


def test_leaves():

    graph = build_graph()

    leaves = graph.leaves()

    assert len(leaves) == 2

    ids = {quest.quest_id for quest in leaves}

    assert ids == {3, 4}


# ---------------------------------------------------------------------
# Available
# ---------------------------------------------------------------------


def test_available_without_completed():

    graph = build_graph()

    quests = graph.available(set())

    assert len(quests) == 1
    assert quests[0].quest_id == 1


def test_available_after_first_quest():

    graph = build_graph()

    quests = graph.available({1})

    ids = {quest.quest_id for quest in quests}

    assert ids == {2, 4}


# ---------------------------------------------------------------------
# Blocked
# ---------------------------------------------------------------------


def test_blocked():

    graph = build_graph()

    quests = graph.blocked(set())

    ids = {quest.quest_id for quest in quests}

    assert ids == {2, 3, 4}


# ---------------------------------------------------------------------
# Ancestors
# ---------------------------------------------------------------------


def test_ancestors():

    graph = build_graph()

    ancestors = graph.ancestors(3)

    ids = {quest.quest_id for quest in ancestors}

    assert ids == {1, 2}


# ---------------------------------------------------------------------
# Descendants
# ---------------------------------------------------------------------


def test_descendants():

    graph = build_graph()

    descendants = graph.descendants(1)

    ids = {quest.quest_id for quest in descendants}

    assert ids == {2, 3, 4}