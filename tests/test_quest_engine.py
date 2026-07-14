from app.optimizer.quest_engine import QuestEngine
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


def build_engine() -> QuestEngine:
    return QuestEngine(build_graph())


# ---------------------------------------------------------------------
# Available
# ---------------------------------------------------------------------


def test_available():

    engine = build_engine()

    quests = engine.available(set())

    assert len(quests) == 1
    assert quests[0].quest_id == 1


def test_available_after_completion():

    engine = build_engine()

    quests = engine.available({1})

    ids = {quest.quest_id for quest in quests}

    assert ids == {2, 4}


# ---------------------------------------------------------------------
# Blocked
# ---------------------------------------------------------------------


def test_blocked():

    engine = build_engine()

    quests = engine.blocked(set())

    ids = {quest.quest_id for quest in quests}

    assert ids == {2, 3, 4}


# ---------------------------------------------------------------------
# Completion
# ---------------------------------------------------------------------


def test_is_completed():

    engine = build_engine()

    assert engine.is_completed(1, {1, 2})
    assert not engine.is_completed(3, {1, 2})


# ---------------------------------------------------------------------
# Unlocks
# ---------------------------------------------------------------------


def test_unlocks():

    engine = build_engine()

    quests = engine.unlocks(1)

    ids = {quest.quest_id for quest in quests}

    assert ids == {2, 4}


def test_unlock_tree():

    engine = build_engine()

    quests = engine.unlock_tree(1)

    ids = {quest.quest_id for quest in quests}

    assert ids == {2, 3, 4}


# ---------------------------------------------------------------------
# Progress
# ---------------------------------------------------------------------


def test_completion_rate():

    engine = build_engine()

    assert engine.completion_rate(set()) == 0.0
    assert engine.completion_rate({1, 2}) == 50.0
    assert engine.completion_rate({1, 2, 3, 4}) == 100.0


def test_remaining():

    engine = build_engine()

    assert engine.remaining(set()) == 4
    assert engine.remaining({1}) == 3
    assert engine.remaining({1, 2, 3, 4}) == 0