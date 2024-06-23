import os
import json
from dobby_storage.storage import LocalStorage, S3Storage, FTPStorage, GoogleDriveStorage, StorageConfig, FileStorage
import pytest
from unittest.mock import MagicMock
from unittest.mock import patch

@pytest.fixture
def config_path(tmp_path):
    config_data = {
        "default": "local",
        "disks": {
            "local": {
                "driver": "local",
                "root": str(tmp_path)
            }
        }
    }
    config_file = tmp_path / "test_storage.json"
    with open(config_file, "w") as f:
        json.dump(config_data, f)
    return config_file

def test_storage_config(config_path):
    storage_config = StorageConfig(config_path)
    assert storage_config.get_default_disk() == storage_config.get_disk("local")

def test_file_storage(config_path):
    file_storage = FileStorage(config_path)
    assert isinstance(file_storage._storage, LocalStorage)

    file_path = os.path.join(os.path.dirname(__file__), "test.txt")
    destination = "destination.txt"
    saved_path = file_storage.save(file_path, destination)
    assert os.path.exists(saved_path)

def test_local_storage_save(tmp_path):
    root_dir = tmp_path
    file_path = os.path.join(root_dir, "test.txt")
    with open(file_path, "w") as f:
        f.write("test content")

    local_storage = LocalStorage(root_dir)
    destination = "destination.txt"
    saved_path = local_storage.save(file_path, destination)

    assert os.path.exists(saved_path)

def test_s3_storage_save(tmp_path):
    key = "test_key"
    secret = "test_secret"
    region = "test_region"
    bucket = "test_bucket"

    s3 = MagicMock()
    with patch("dobby_storage.storage.boto3.client", return_value=s3):
        s3_storage = S3Storage(key, secret, region, bucket)
        file_path = os.path.join(tmp_path, "test.txt")
        with open(file_path, "w") as f:
            f.write("test content")

        object_name = "test_object"
        saved_path = s3_storage.save(file_path, object_name, bucket_name=bucket)

        assert saved_path.startswith(f"https://{bucket}.s3.amazonaws.com/")

def test_ftp_storage_save(tmp_path):
    server = "test_server"
    user = "test_user"
    password = "test_password"

    ftp = MagicMock()
    with patch("dobby_storage.storage.FTP", return_value=ftp):
        ftp_storage = FTPStorage(server, user, password)
        file_path = os.path.join(tmp_path, "test.txt")
        with open(file_path, "w") as f:
            f.write("test content")

        ftp_path = "test_ftp_path"
        saved_path = ftp_storage.save(file_path, ftp_path)

        assert saved_path == f"ftp://{user}@{server}/{ftp_path}"

def test_google_drive_storage_save(tmp_path):
    auth_path = "test_auth_path"

    gauth = MagicMock()
    gdrive = MagicMock()
    with patch("dobby_storage.storage.GoogleAuth", return_value=gauth):
        with patch("dobby_storage.storage.GoogleDrive", return_value=gdrive):
            google_drive_storage = GoogleDriveStorage(auth_path)
            file_path = os.path.join(tmp_path, "test.txt")
            with open(file_path, "w") as f:
                f.write("test content")

            saved_url = google_drive_storage.save(file_path)

            assert saved_url.startswith("https://drive.google.com/uc?id=")