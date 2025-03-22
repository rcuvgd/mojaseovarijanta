import os

def create_client_folder(client_id: str) -> str:
    base_path = os.path.join("clients", client_id)
    os.makedirs(base_path, exist_ok=True)
    return base_path
