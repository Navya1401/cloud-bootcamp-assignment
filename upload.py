from azure.storage.blob import BlobServiceClient
import os

def upload_file(connection_string, container_name, file_path):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)

        file_name = os.path.basename(file_path)
        blob_client = blob_service_client.get_blob_client(container=container_name, blob=file_name)

        with open(file_path, "rb") as data:
            blob_client.upload_blob(data, overwrite=True)

        print(f"✅ File '{file_name}' uploaded successfully!")

    except Exception as e:
        print("Error:", e)


def list_files(connection_string, container_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        container_client = blob_service_client.get_container_client(container_name)

        print("\n Files in container:")
        for blob in container_client.list_blobs():
            print("-", blob.name)

    except Exception as e:
        print("Error listing files:", e)


if __name__ == "__main__":
    conn = input("Enter connection string: ")
    container = input("Enter container name: ")
    path = input("Enter file path: ")

    upload_file(conn, container, path)
    list_files(conn, container)