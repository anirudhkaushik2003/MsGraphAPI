import os
import requests
import glob
import re
from graph import generate_access_token, GRAPH_API_ENDPOINT


APP_ID = r'5de8d1a6-9972-406f-b375-3a4664118841'
SCOPES = ['Files.ReadWrite']

access_token = generate_access_token(APP_ID, SCOPES)
headers = {
    'Authorization': 'Bearer ' + access_token['access_token']
}

file_path = input("Enter File path (Absolute): ")
file_path.encode('unicode_escape')
# input can be regex, convert to appropriate format for glob

option = input("What do you want to do with the file?\n(1)Upload to home directory\n(2)Upload file by folder id\n(3)Upload file based on folder path\nEnter choice:")
for file in glob.glob(file_path):
    file_name = os.path.basename(file)
    print(f"Uploading {file_name}...")

    with open(file, 'rb') as upload:
        media_content = upload.read()

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