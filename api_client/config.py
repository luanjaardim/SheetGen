# Define the Google Drive API scopes and service account file path
SCOPES = ['https://www.googleapis.com/auth/drive']
# You need to add here the .json file that you downloaded
SERVICE_ACCOUNT_FILE = "./pythondrive-420212-4f325cdf0cd1.json"
BASE_PARENT_ID = '1Cb1NMDh7HrlTTyycck_cRDDrv-0Rgqd-'

MAP_TYPE = {
    'folder': 'application/vnd.google-apps.folder',
    'file'  : 'application/vnd.google-apps.file',
    'table' : 'text/csv',
}
