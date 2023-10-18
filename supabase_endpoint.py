#FastAPI packages
from fastapi import Request, APIRouter
from fastapi import status
import os
from dotenv import load_dotenv
from supabase import create_client, Client

router = APIRouter()

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
sup: Client = create_client(url, key)
# Cargar las variables de entorno desde el archivo .env

@router.get("/products_ids")
def get_users():
    response = sup.table('product').select("id").execute()
    return response

@router.get("/name_and_price_with_id")
def get_users(product_id):
    response = sup.table('product').select("name,price").eq("id",product_id).execute()
    return response