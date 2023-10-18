#FastAPI packages
from fastapi import APIRouter
from fastapi import status
from starlette.responses import RedirectResponse

router = APIRouter()


# IT WORKS EVEN FOR NESTED IMAGES INSIDE FOLDERS
@router.get("/get_image/")
async def get_image(img_id):
    # Reemplaza 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' con el ID de tu imagen en Google Drive
    google_drive_url = f"https://drive.google.com/uc?export=view&id={img_id}"
    print(google_drive_url)
    return RedirectResponse(url=google_drive_url)
