import os
from google.oauth2 import service_account
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload, MediaFileUpload
import io
from googleapiclient.errors import HttpError
from config import SCOPES, SERVICE_ACCOUNT_FILE, BASE_PARENT_ID, MAP_TYPE 

class ClientAPI:

    def __init__(self):
        # Create credentials using the service account file
        self.credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        # Build the Google Drive service
        self.service = build('drive', 'v3', credentials=self.credentials)

    def listFolder(self, parent_folder_id : str = BASE_PARENT_ID, show_info : bool = False) -> list[dict[str, str]]:
        """List folders and files in Google Drive."""
        results = self.service.files().list(
            q=f"'{parent_folder_id}' in parents and trashed=false",
            pageSize=1000,
            fields="nextPageToken, files(id, name, mimeType)"
        ).execute()
        items = results.get('files', [])

        if show_info:
            if not items:
                print("No folders or files found in Google Drive.")
            else:
                print("Folders and files:")
                for item in items:
                    print(f"Name: {item['name']}, Type: {item['mimeType']}, ID: {item['id']}")

        return results.get('files', [])

    def findFile(self, file_name: str, parentId: str | None = None) -> dict[str, str] | None:
        file_path = file_name.split('/')
        if file_path[-1] == '':
            file_path.pop()
        if not file_path:
            return None
        parentId = parentId if parentId is not None else BASE_PARENT_ID
        subDirs = file_path[:-1]
        fileName = file_path[-1]

        # search for the file in every subdirectory
        for subDir in subDirs:
            files = self.listFolder(parentId)
            previousParentId = parentId
            for file in files:
                if file['name'] == subDir:
                    parentId = file['id']
                    break
            # did not found the subdirectory
            if previousParentId == parentId:
                return None

        files = self.listFolder(parentId)
        print(files)

        for file in files:
            if file['name'] == fileName:
                return file
        return None # file not found

    def getFolderId(self, folder_path: str) -> str:
        folder = self.findFile(folder_path)
        if folder is None or folder.get('mimeType') != MAP_TYPE['folder']:
            raise ValueError(f"Invalid destination path: {folder_path}, you must pass a folder path.")

        return folder['id']

    def createFile(self, file_name: str, mime_type: str, file_path : str | None = None, parent_id: str = BASE_PARENT_ID) -> str:
        """Create a file in Google Drive and return its ID."""

        if mime_type not in MAP_TYPE:
            raise ValueError(f"Invalid mime type: {mime_type}")
        if file_path is not None and os.path.exists(file_path) == False:
            raise ValueError(f"File not found: {file_path}")
        if file_path is not None and mime_type == 'folder':
            raise ValueError(f"Invalid mime type: {mime_type} for a file path.")

        file_metadata = {'name': file_name, 'mime_type' : MAP_TYPE[mime_type], 'parents' : [parent_id]}
        media = None
        if file_path is not None:
            media = MediaFileUpload(file_path, mimetype=MAP_TYPE[mime_type])
        file = self.service.files().create(body=file_metadata, media_body=media, fields='id').execute()
        return file.get('id')

    def makeDir(self, folder_name: str, parent_path: str = '') -> str:
        parent_id = BASE_PARENT_ID
        if parent_path:
            parent_id = self.getFolderId(parent_path)
        return self.createFile(folder_name, 'folder', parent_id=parent_id)

    def uploadFile(self, file_path: str, dest_path: str, mime_type: str) -> str:
        if mime_type not in MAP_TYPE:
            raise ValueError(f"Invalid mime type: {mime_type}")

        # Get the folder ID of the destination path, in Google Drive
        folder_id = self.getFolderId(dest_path)

        # Check if the file to upload exists
        if os.path.exists(file_path) == False:
            raise ValueError(f"File not found: {file_path}")

        fileName = os.path.basename(file_path)

        return self.createFile(fileName, mime_type, file_path, folder_id)

def create_folder(folder_name, parent_folder_id=None):
    """Create a folder in Google Drive and return its ID."""
    folder_metadata = {
        'name': folder_name,
        "mimeType": "application/vnd.google-apps.folder",
        'parents': [parent_folder_id] if parent_folder_id else []
    }

    created_folder = drive_service.files().create(
        body=folder_metadata,
        fields='id'
    ).execute()

    print(f'Created Folder ID: {created_folder["id"]}')
    return created_folder["id"]

def delete_files(file_or_folder_id):
    """Delete a file or folder in Google Drive by ID."""
    try:
        drive_service.files().delete(fileId=file_or_folder_id).execute()
        print(f"Successfully deleted file/folder with ID: {file_or_folder_id}")
    except Exception as e:
        print(f"Error deleting file/folder with ID: {file_or_folder_id}")
        print(f"Error details: {str(e)}")

def download_file(file_id, destination_path):
    """Download a file from Google Drive by its ID."""
    request = drive_service.files().get_media(fileId=file_id)
    fh = io.FileIO(destination_path, mode='wb')
    # 
    downloader = MediaIoBaseDownload(fh, request)
    
    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")

if __name__ == '__main__':
    # Example usage:

    # Create a new folder
    # create_folder("MyNewFolder", '1Cb1NMDh7HrlTTyycck_cRDDrv-0Rgqd-')
    # file_metadata = {'name': 'my_test.csv'}
    #
    # media = MediaFileUpload('./test.csv',
    #                         mimetype='text/csv')
    #
    # file = drive_service.files().create(body=file_metadata, media_body=media,
    #                               fields='id').execute()
    api = ClientAPI()
    # api.listFolder(BASE_PARENT_ID, show_info=True)
    print(api.makeDir("newFolder"))

    # file_id  = '1bQFHDiJclvQfD1NnQyhqVXWv5xDj1ZLp'
    # request_body = {
    #     'role': 'reader',
    #     'type': 'anyone'
    # }
    # response_permission = drive_service.permissions().create(
    #     fileId=file_id,
    #     body=request_body
    # ).execute()
    # response_share_link = drive_service.files().get(
    #     fileId=file_id,
    #     fields='webViewLink'
    # ).execute()
    # print(response_share_link)


    
    # Delete a file or folder by ID
    # delete_files("your_file_or_folder_id")

    # Download a file by its ID
    # download_file("your_file_id", "destination_path/file_name.extension")
