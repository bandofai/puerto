#!/usr/bin/env python3
"""
Cloud Storage Synchronization Script
Supports Google Drive, Dropbox, and OneDrive
"""

import argparse
import os
import sys
import json
from pathlib import Path
from typing import Optional, Dict, Any

# Cloud provider clients (install with: pip install google-api-python-client dropbox requests)
try:
    from google.oauth2.credentials import Credentials
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
    GOOGLE_AVAILABLE = True
except ImportError:
    GOOGLE_AVAILABLE = False

try:
    import dropbox
    from dropbox.files import WriteMode
    DROPBOX_AVAILABLE = True
except ImportError:
    DROPBOX_AVAILABLE = False

try:
    import requests
    ONEDRIVE_AVAILABLE = True
except ImportError:
    ONEDRIVE_AVAILABLE = False


class CloudSyncManager:
    """Manages cloud storage synchronization"""

    def __init__(self, config_path: str = "~/.backup-manager/config.json"):
        self.config_path = Path(config_path).expanduser()
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load configuration file"""
        if not self.config_path.exists():
            raise FileNotFoundError(f"Config not found: {self.config_path}")

        with open(self.config_path) as f:
            return json.load(f)

    def upload(self, provider: str, source: str, destination: str) -> bool:
        """Upload file/folder to cloud storage"""
        if provider == "gdrive":
            return self._upload_google_drive(source, destination)
        elif provider == "dropbox":
            return self._upload_dropbox(source, destination)
        elif provider == "onedrive":
            return self._upload_onedrive(source, destination)
        else:
            print(f"Unsupported provider: {provider}")
            return False

    def _upload_google_drive(self, source: str, destination: str) -> bool:
        """Upload to Google Drive"""
        if not GOOGLE_AVAILABLE:
            print("Google Drive libraries not available. Install: pip install google-api-python-client")
            return False

        try:
            # Load credentials
            creds_path = Path(self.config['destinations']['google_drive']['credentials']).expanduser()
            if not creds_path.exists():
                print(f"Google Drive credentials not found: {creds_path}")
                print("Run authentication first: python cloud_auth.py --provider gdrive")
                return False

            creds = Credentials.from_authorized_user_file(str(creds_path))
            service = build('drive', 'v3', credentials=creds)

            # Create folder if needed
            folder_id = self._get_or_create_folder(service, destination)

            # Upload file
            source_path = Path(source)
            if source_path.is_file():
                file_metadata = {
                    'name': source_path.name,
                    'parents': [folder_id]
                }
                media = MediaFileUpload(str(source_path), resumable=True)
                file = service.files().create(
                    body=file_metadata,
                    media_body=media,
                    fields='id'
                ).execute()

                print(f"✓ Uploaded to Google Drive: {source_path.name} (ID: {file.get('id')})")
                return True
            else:
                # Upload directory (recursive)
                return self._upload_directory_gdrive(service, source_path, folder_id)

        except Exception as e:
            print(f"✗ Google Drive upload failed: {e}")
            return False

    def _get_or_create_folder(self, service, path: str) -> str:
        """Get or create folder in Google Drive"""
        # Search for folder
        query = f"name='{path}' and mimeType='application/vnd.google-apps.folder'"
        results = service.files().list(q=query, fields='files(id)').execute()
        files = results.get('files', [])

        if files:
            return files[0]['id']

        # Create folder
        folder_metadata = {
            'name': path,
            'mimeType': 'application/vnd.google-apps.folder'
        }
        folder = service.files().create(body=folder_metadata, fields='id').execute()
        return folder['id']

    def _upload_directory_gdrive(self, service, directory: Path, parent_id: str) -> bool:
        """Recursively upload directory to Google Drive"""
        for item in directory.iterdir():
            if item.is_file():
                file_metadata = {
                    'name': item.name,
                    'parents': [parent_id]
                }
                media = MediaFileUpload(str(item), resumable=True)
                service.files().create(body=file_metadata, media_body=media).execute()
                print(f"  ✓ {item.name}")
            elif item.is_dir():
                # Create subfolder
                folder_metadata = {
                    'name': item.name,
                    'parents': [parent_id],
                    'mimeType': 'application/vnd.google-apps.folder'
                }
                folder = service.files().create(body=folder_metadata, fields='id').execute()
                self._upload_directory_gdrive(service, item, folder['id'])

        return True

    def _upload_dropbox(self, source: str, destination: str) -> bool:
        """Upload to Dropbox"""
        if not DROPBOX_AVAILABLE:
            print("Dropbox library not available. Install: pip install dropbox")
            return False

        try:
            # Load token
            token_path = Path(self.config['destinations']['dropbox']['credentials']).expanduser()
            if not token_path.exists():
                print(f"Dropbox token not found: {token_path}")
                return False

            with open(token_path) as f:
                token_data = json.load(f)

            dbx = dropbox.Dropbox(token_data['access_token'])

            # Upload file
            source_path = Path(source)
            dest_path = f"{destination}/{source_path.name}"

            CHUNK_SIZE = 4 * 1024 * 1024  # 4MB chunks

            with open(source_path, 'rb') as f:
                file_size = source_path.stat().st_size

                if file_size <= CHUNK_SIZE:
                    # Small file - single upload
                    dbx.files_upload(f.read(), dest_path, mode=WriteMode('overwrite'))
                else:
                    # Large file - chunked upload
                    upload_session_start = dbx.files_upload_session_start(f.read(CHUNK_SIZE))
                    cursor = dropbox.files.UploadSessionCursor(
                        session_id=upload_session_start.session_id,
                        offset=f.tell()
                    )
                    commit = dropbox.files.CommitInfo(path=dest_path, mode=WriteMode('overwrite'))

                    while f.tell() < file_size:
                        chunk = f.read(CHUNK_SIZE)
                        if f.tell() < file_size:
                            dbx.files_upload_session_append_v2(chunk, cursor)
                            cursor.offset = f.tell()
                        else:
                            dbx.files_upload_session_finish(chunk, cursor, commit)

            print(f"✓ Uploaded to Dropbox: {dest_path}")
            return True

        except Exception as e:
            print(f"✗ Dropbox upload failed: {e}")
            return False

    def _upload_onedrive(self, source: str, destination: str) -> bool:
        """Upload to OneDrive"""
        if not ONEDRIVE_AVAILABLE:
            print("OneDrive libraries not available. Install: pip install requests")
            return False

        try:
            # Load token
            token_path = Path(self.config['destinations']['onedrive']['credentials']).expanduser()
            if not token_path.exists():
                print(f"OneDrive token not found: {token_path}")
                return False

            with open(token_path) as f:
                token_data = json.load(f)

            access_token = token_data['access_token']
            headers = {'Authorization': f'Bearer {access_token}'}

            source_path = Path(source)
            filename = f"{destination}/{source_path.name}"

            file_size = source_path.stat().st_size

            if file_size < 4 * 1024 * 1024:  # < 4MB
                # Small file upload
                url = f'https://graph.microsoft.com/v1.0/me/drive/root:/{filename}:/content'
                with open(source_path, 'rb') as f:
                    response = requests.put(url, headers=headers, data=f)
                    response.raise_for_status()
            else:
                # Large file upload session
                url = f'https://graph.microsoft.com/v1.0/me/drive/root:/{filename}:/createUploadSession'
                session = requests.post(url, headers=headers).json()
                upload_url = session['uploadUrl']

                # Upload in chunks
                chunk_size = 10 * 1024 * 1024  # 10MB
                with open(source_path, 'rb') as f:
                    offset = 0
                    while True:
                        chunk = f.read(chunk_size)
                        if not chunk:
                            break

                        chunk_headers = {
                            'Content-Length': str(len(chunk)),
                            'Content-Range': f'bytes {offset}-{offset + len(chunk) - 1}/{file_size}'
                        }
                        response = requests.put(upload_url, headers=chunk_headers, data=chunk)
                        response.raise_for_status()
                        offset += len(chunk)

            print(f"✓ Uploaded to OneDrive: {filename}")
            return True

        except Exception as e:
            print(f"✗ OneDrive upload failed: {e}")
            return False

    def check_quota(self, provider: str) -> Dict[str, Any]:
        """Check storage quota for provider"""
        if provider == "gdrive":
            return self._check_quota_gdrive()
        elif provider == "dropbox":
            return self._check_quota_dropbox()
        elif provider == "onedrive":
            return self._check_quota_onedrive()
        else:
            return {}

    def _check_quota_gdrive(self) -> Dict[str, Any]:
        """Check Google Drive quota"""
        try:
            creds_path = Path(self.config['destinations']['google_drive']['credentials']).expanduser()
            creds = Credentials.from_authorized_user_file(str(creds_path))
            service = build('drive', 'v3', credentials=creds)

            about = service.about().get(fields='storageQuota').execute()
            quota = about['storageQuota']

            total = int(quota['limit'])
            used = int(quota['usage'])
            available = total - used
            percent = (used / total) * 100

            print(f"Google Drive:")
            print(f"  Total: {total / (1024**3):.2f} GB")
            print(f"  Used: {used / (1024**3):.2f} GB ({percent:.1f}%)")
            print(f"  Available: {available / (1024**3):.2f} GB")

            return {
                'total': total,
                'used': used,
                'available': available,
                'percent': percent
            }

        except Exception as e:
            print(f"✗ Failed to check Google Drive quota: {e}")
            return {}

    def _check_quota_dropbox(self) -> Dict[str, Any]:
        """Check Dropbox quota"""
        try:
            token_path = Path(self.config['destinations']['dropbox']['credentials']).expanduser()
            with open(token_path) as f:
                token_data = json.load(f)

            dbx = dropbox.Dropbox(token_data['access_token'])
            space = dbx.users_get_space_usage()

            total = space.allocation.get_individual().allocated
            used = space.used
            available = total - used
            percent = (used / total) * 100

            print(f"Dropbox:")
            print(f"  Total: {total / (1024**3):.2f} GB")
            print(f"  Used: {used / (1024**3):.2f} GB ({percent:.1f}%)")
            print(f"  Available: {available / (1024**3):.2f} GB")

            return {
                'total': total,
                'used': used,
                'available': available,
                'percent': percent
            }

        except Exception as e:
            print(f"✗ Failed to check Dropbox quota: {e}")
            return {}

    def _check_quota_onedrive(self) -> Dict[str, Any]:
        """Check OneDrive quota"""
        try:
            token_path = Path(self.config['destinations']['onedrive']['credentials']).expanduser()
            with open(token_path) as f:
                token_data = json.load(f)

            headers = {'Authorization': f'Bearer {token_data["access_token"]}'}
            url = 'https://graph.microsoft.com/v1.0/me/drive'
            response = requests.get(url, headers=headers)
            response.raise_for_status()

            data = response.json()
            quota = data['quota']

            total = quota['total']
            used = quota['used']
            available = quota['remaining']
            percent = (used / total) * 100

            print(f"OneDrive:")
            print(f"  Total: {total / (1024**3):.2f} GB")
            print(f"  Used: {used / (1024**3):.2f} GB ({percent:.1f}%)")
            print(f"  Available: {available / (1024**3):.2f} GB")

            return {
                'total': total,
                'used': used,
                'available': available,
                'percent': percent
            }

        except Exception as e:
            print(f"✗ Failed to check OneDrive quota: {e}")
            return {}


def main():
    parser = argparse.ArgumentParser(description="Cloud storage synchronization")
    parser.add_argument('--provider', required=True, choices=['gdrive', 'dropbox', 'onedrive'],
                        help='Cloud storage provider')
    parser.add_argument('--action', default='upload', choices=['upload', 'quota', 'verify'],
                        help='Action to perform')
    parser.add_argument('--source', help='Source file or directory')
    parser.add_argument('--destination', help='Destination path in cloud')
    parser.add_argument('--log', help='Log file path')

    args = parser.parse_args()

    # Initialize manager
    try:
        manager = CloudSyncManager()
    except FileNotFoundError as e:
        print(f"✗ {e}")
        sys.exit(1)

    # Perform action
    if args.action == 'upload':
        if not args.source or not args.destination:
            print("✗ --source and --destination required for upload")
            sys.exit(1)

        success = manager.upload(args.provider, args.source, args.destination)
        sys.exit(0 if success else 1)

    elif args.action == 'quota':
        manager.check_quota(args.provider)
        sys.exit(0)

    elif args.action == 'verify':
        # Verification logic would go here
        print(f"Verifying {args.provider} backups...")
        sys.exit(0)


if __name__ == '__main__':
    main()
