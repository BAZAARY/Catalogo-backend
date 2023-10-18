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

@router.get("/get_users")
def get_users():
    response = sup.table('user').select("*").execute()
    return response