from azure.storage.blob import BlobServiceClient
from io import BytesIO
import logging


class BlobStorageConnector():
    def __init__(self, connection_string: str):
        self.blob_service_client = BlobServiceClient.from_connection_string(connection_string)
        self.blob_container_client = None
        self.blob_client = None

    def does_container_exist(self, container_name: str) -> bool:
        for container in self.blob_service_client.list_containers(name_starts_with=container_name):
            if container.name == container_name:
                return True
            
        return False

    def does_blob_exist(self, blob_name: str) -> bool:
        if self.blob_container_client is not None:
            for blob in self.blob_container_client.list_blob_names(name_starts_with=blob_name):
                if blob == blob_name:
                    return True
            
            return False
        
        logging.error("Container connection was not established before searching for blob.")
        return False

    def create_upload_blob_client(self, container_name: str, blob_name: str) -> bool:
        if self.does_container_exist(container_name):
            self.blob_container_client = self.blob_service_client.get_container_client(container=container_name)

            if self.does_blob_exist(blob_name=blob_name):
                self.blob_client = self.blob_container_client.get_blob_client(blob=blob_name)
                logging.info(f"Blob client for file upload of {blob_name} in {container_name} created successfully.")
                
                return True

            else:
                logging.error(f"Blob {blob_name} does not exist in {container_name}.")

        else:
            logging.error(f"Container {container_name} was not found. Connection to storage was not established.")

        return False

    def create_download_blob_client(self, container_name: str, blob_name: str) -> bool:
        if self.does_container_exist(container_name):
            self.blob_container_client = self.blob_service_client.get_container_client(container=container_name)

            if not self.does_blob_exist(blob_name=blob_name):
                self.blob_client = self.blob_container_client.get_blob_client(blob=blob_name)
                logging.info(f"Blob client for file download of {blob_name} in {container_name} created successfully.")

                return True

            else:
                logging.error(f"Blob {blob_name} already exists in {container_name}. Cannot download a new one with the same name.")

        else:
            logging.error(f"Container {container_name} was not found. Connection to storage was not established.")

        return False
    
    def download_blob_from_file_stream_to_azure(self, file_stream: BytesIO) -> None:
        logging.info("Downloading blob from file stream to Azure...")
        self.blob_client.upload_blob(file_stream)
        logging.info("Download completed.")

    def get_blob_file_stream_from_azure(self) -> BytesIO:
        if self.blob_client is not None:
            return BytesIO(self.blob_client.download_blob().readall());
        else:
            return None
    
    def close(self) -> None:
        if self.blob_client is not None:
            self.blob_client.close()
        if self.blob_container_client is not None:
            self.blob_client.close()
        if self.blob_service_client is not None:
            self.blob_service_client.close()
