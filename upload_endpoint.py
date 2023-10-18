#FastAPI packages
from fastapi import APIRouter
from fastapi import status
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

router = APIRouter()

def uploadByPath(path):
    # Below code does the authentication 
    gauth = GoogleAuth()
    # Try to load saved client credentials
    gauth.LoadCredentialsFile("mycreds.txt")
    if gauth.credentials is None:
        # Authenticate if they're not there

        # This is what solved the issues:
        gauth.GetFlow()
        gauth.flow.params.update({'access_type': 'offline'})
        gauth.flow.params.update({'approval_prompt': 'force'})

        # Usa el cliente_secrets.json file
        gauth.LocalWebserverAuth()
    elif gauth.access_token_expired:
        # Refresh them if expired
        gauth.Refresh()
    else:
        # Initialize the saved creds
        gauth.Authorize()
        # Save the current credentials to a file
    gauth.SaveCredentialsFile("mycreds.txt")
   
    drive = GoogleDrive(gauth) 
   

    # Replace this with the absolute path to the image you want to upload
    

    # Create a PyDrive file for the image
    file_title = path
   
    f = drive.CreateFile({'title': file_title}) 
    f.SetContentFile(path) 
    f.Upload() 
  
    # Due to a known bug in pydrive if we  
    # don't empty the variable used to 
    # upload the files to Google Drive the 
    # file stays open in memory and causes a 
    # memory leak, therefore preventing its  
    # deletion 
    f = None

@router.get("/upload_image/")
async def upload_image(img_path):
    # Extract parameters and call uploadByPath function
    uploadByPath(img_path)
    return {"message": "File uploaded successfully"}