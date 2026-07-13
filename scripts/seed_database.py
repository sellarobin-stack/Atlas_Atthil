from app.database.base_model import Base
from app.database.models import Campaign, Quest
from app.database.session import SessionLocal, engine

# Création des tables
Base.metadata.create_all(bind=engine)

db = SessionLocal()

# -------------------------
# Campaigns
# -------------------------

campaigns = [
    {
        "code": "DG",
        "name": "Dofus des Glaces",
        "description": "Campagne du Dofus des Glaces",
    },
    {
        "code": "DT",
        "name": "Dofus Turquoise",
        "description": "Campagne du Dofus Turquoise",
    },
    {
        "code": "DV",
        "name": "Dofus Vulbis",
        "description": "Campagne du Dofus Vulbis",
    },
]

for data in campaigns:

    campaign = (
        db.query(Campaign)
        .filter(Campaign.code == data["code"])
        .first()
    )

    if campaign is None:
        db.add(Campaign(**data))

db.commit()

# -------------------------
# Quests
# -------------------------



db.commit()

db.close()

print("Database seeded successfully.")