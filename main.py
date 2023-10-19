from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import upload_endpoint, get_image_endpoint, get_file_ids_endpoint, get_folder_ids_endpoint, supabase_endpoint

app = FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routes from individual endpoint files
app.include_router(upload_endpoint.router) #
app.include_router(get_image_endpoint.router) #http://localhost:8000/get_image/?img_id=1pVF1w9xsZvtY3DwC5G3nQ9NpgGPjG4b0
app.include_router(get_file_ids_endpoint.router) #http://localhost:8000/get_files_ids_of_folder_with_id/?folderId=11R1q-5qBjAmb7RJauz0bk-YrekEWFWys
app.include_router(get_folder_ids_endpoint.router) #http://localhost:8000/get_folder_ids/
app.include_router(supabase_endpoint.router) #http://localhost:8000/get_users/
