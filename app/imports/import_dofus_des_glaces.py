from pathlib import Path

from sqlalchemy import select

from app.database.models import Campaign, Quest
from app.database.session import SessionLocal
from app.imports.json_importer import JsonImporter


def run():

    db = SessionLocal()

    data = JsonImporter.load(
        Path("data/campaigns/dofus_des_glaces.json")
    )

    campaign = db.scalar(
        select(Campaign).where(Campaign.code == "DG")
    )

    if campaign is None:
        raise RuntimeError("Campaign DG not found.")

    imported = 0

    for row in data:

        exists = db.scalar(
            select(Quest).where(
                Quest.ankama_id == row["ankama_id"]
            )
        )

        if exists:
            continue

        db.add(
            Quest(
                ankama_id=row["ankama_id"],
                name=row["name"],
                level=row["level"],
                campaign_id=campaign.id,
            )
        )

        imported += 1

    db.commit()

    db.close()

    print(f"{imported} quests imported.")


if __name__ == "__main__":
    run()