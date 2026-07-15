from pathlib import Path
import json

from app.data_pipeline.sources.dofusdb import DofusDbSource


RAW_DIRECTORY = Path("data/raw")


def save_json(filename: str, data: dict | list) -> None:
    """
    Sauvegarde une réponse JSON dans le dossier data/raw.
    """

    RAW_DIRECTORY.mkdir(
        parents=True,
        exist_ok=True,
    )

    filepath = RAW_DIRECTORY / filename

    with filepath.open(
        "w",
        encoding="utf-8",
    ) as file:

        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4,
        )


def inspect() -> None:

    source = DofusDbSource()

    print("=" * 60)
    print("Downloading quests...")
    print("=" * 60)

    quests = source.get_quests()

    save_json(
        "quests.json",
        quests,
    )

    print()
    print("Type retourné :")
    print(type(quests))

    print()

    if isinstance(quests, dict):

        print("Clés du dictionnaire :")

        for key in quests.keys():
            print(f" - {key}")

    elif isinstance(quests, list):

        print(f"Nombre d'éléments : {len(quests)}")

        if len(quests) > 0:

            print()

            print("Clés du premier élément :")

            for key in quests[0].keys():
                print(f" - {key}")

    print()

    print("Aperçu de la réponse :")

    print()

    print(
        json.dumps(
            quests,
            indent=4,
            ensure_ascii=False,
        )[:5000]
    )

    print()

    print("=" * 60)
    print("Inspection terminée")
    print("=" * 60)


if __name__ == "__main__":
    inspect()