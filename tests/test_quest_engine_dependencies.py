from app.optimizer.quest_engine import QuestEngine
from app.optimizer.quest_graph import QuestGraph
from app.optimizer.quest_node import QuestNode


def build_graph() -> QuestGraph:
    """
    Graphe utilisé pour tous les tests.

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


def test_missing_requirements_no_completion():

    engine = QuestEngine(build_graph())

    missing = engine.missing_requirements(3, set())

    ids = {quest.quest_id for quest in missing}

    assert ids == {1, 2}

def test_missing_requirements_after_first_quest():
    engine = QuestEngine(build_graph())

    missing = engine.missing_requirements(3, {1})

    assert len(missing) == 1
    assert missing[0].quest_id == 2


def test_missing_requirements_after_second_quest():
    engine = QuestEngine(build_graph())

    missing = engine.missing_requirements(3, {1, 2})

    assert missing == []


def test_unlocks_first_quest():
    engine = QuestEngine(build_graph())

    unlocked = engine.unlocks(1)

    assert len(unlocked) == 2

    ids = {quest.quest_id for quest in unlocked}

    assert ids == {2, 4}


def test_unlocks_second_quest():
    engine = QuestEngine(build_graph())

    unlocked = engine.unlocks(2)

    assert len(unlocked) == 1
    assert unlocked[0].quest_id == 3


def test_unlocks_leaf():
    engine = QuestEngine(build_graph())

    unlocked = engine.unlocks(3)

    assert unlocked == []


def test_is_completed_true():
    engine = QuestEngine(build_graph())

    assert engine.is_completed(2, {1, 2})


def test_is_completed_false():
    engine = QuestEngine(build_graph())

    assert not engine.is_completed(3, {1, 2})