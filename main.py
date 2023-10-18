from fastapi import FastAPI
import upload_endpoint, get_image_endpoint, get_file_ids_endpoint, get_folder_ids_endpoint

app = FastAPI()

# Include the routes from individual endpoint files
app.include_router(upload_endpoint.router)
app.include_router(get_image_endpoint.router)
app.include_router(get_file_ids_endpoint.router)
app.include_router(get_folder_ids_endpoint.router)