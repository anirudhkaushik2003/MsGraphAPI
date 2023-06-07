import os
import requests
from graph import generate_access_token, GRAPH_API_ENDPOINT
APP_ID = r'INSERT_API_HERE'
SCOPES = ['Files.ReadWrite']

access_token = generate_access_token(APP_ID, SCOPES)
headers = {
    'Authorization': 'Bearer ' + access_token['access_token']
}

file_path = input("Enter File path (Absolute): ")
file_path.encode('unicode_escape')
file_name = os.path.basename(file_path)

with open(file_path, 'rb') as upload:
    media_content = upload.read()

option = input("What do you want to do with the file?\n(1)Upload to home directory\n(2)Upload file by folder id\n(3)Upload file based on folder path\nEnter choice:")
# upload file to home directory

if(option == '1'):
    response = requests.put(
        GRAPH_API_ENDPOINT + f'/me/drive/items/root:/{file_name}:/content',
        headers=headers,
        data=media_content
    )

elif (option == '2'):
    folder_id = input("Enter Folder ID: ")
    response = requests.put(
        GRAPH_API_ENDPOINT + f'/me/drive/items/{folder_id}:/{file_name}:/content',
        headers=headers,
        data=media_content
    )

else:
    folder_path = input("Enter Folder Path: ")
    folder_path.encode('unicode_escape')
    response = requests.put(
        GRAPH_API_ENDPOINT + f'/me/drive/root:/{folder_path}/{file_name}:/content',
        headers=headers,
        data=media_content
    )
print(response.json())