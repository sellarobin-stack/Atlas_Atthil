from app.optimizer.quest_engine import QuestEngine
from app.optimizer.quest_graph import QuestGraph
from app.optimizer.quest_node import QuestNode


def build_graph():

    graph = QuestGraph()

    graph.add_node(QuestNode(1, "A", 1))
    graph.add_node(QuestNode(2, "B", 1))
    graph.add_node(QuestNode(3, "C", 1))

    graph.add_dependency(1, 2)
    graph.add_dependency(2, 3)

    return graph


def test_available():

    engine = QuestEngine(build_graph())

    quests = engine.available(set())

    assert len(quests) == 1
    assert quests[0].quest_id == 1


def test_available_after_first_quest():

    engine = QuestEngine(build_graph())

    quests = engine.available({1})

    assert len(quests) == 1
    assert quests[0].quest_id == 2


def test_blocked():

    engine = QuestEngine(build_graph())

    quests = engine.blocked(set())

    assert len(quests) == 2