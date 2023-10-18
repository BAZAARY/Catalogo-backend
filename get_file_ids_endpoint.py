#FastAPI packages
from fastapi import APIRouter
from fastapi import status
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth


router = APIRouter()


def get_file_ids(folder_id):
    file_ids = []
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

    # Obtén la lista de archivos y carpetas en la carpeta raíz (folder_id = 'root')
    file_list = drive.ListFile({'q': f"'{folder_id}' in parents"}).GetList()

    for file in file_list:
        file_ids.append({'id': file['id'], 'title': file['title']})

    return file_ids

@router.get("/get_files_ids_of_folder_with_id/")
async def getFilesIdsOfFolderWithId(folderId):
    file_ids = get_file_ids(folderId)
    return file_ids
