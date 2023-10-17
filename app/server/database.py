from beanie import init_beanie
import motor.motor_asyncio

from app.server.models.product_review import ProductReview
 

async def init_db():
    print("initalizing db")
    client = motor.motor_asyncio.AsyncIOMotorClient(
        # "mongodb+srv://admin:LbenH1jDn9igKqZa@cluster0.0qizfif.mongodb.net/?retryWrites=true&w=majority"
        "mongodb+srv://oparadivinefavour2:Uta3TpbdRFZ2b2Ij@cluster0.ixzsezu.mongodb.net/?retryWrites=true&w=majority"
    )

    await init_beanie(database=client.db_name, document_models=[ProductReview])
#  uvicorn app.server.app:app --reload