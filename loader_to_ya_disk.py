import requests
import os


class YaUploader:
    url = 'https://cloud-api.yandex.net/'

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Accept': 'application/json','Authorization': f'OAuth {self.token}'}

    def get_files_list(self):
        files_url = f'{self.url}v1/disk/resources/files/'
        headers = self.get_headers()
        response = requests.get(files_url, headers)
        return response.json()

    def _get_upload_link(self, disk_file_path):
        upload_url = f'{self.url}v1/disk/resources/upload/'
        headers = self.get_headers()
        params = {'path': disk_file_path, 'overwrite': "true"}
        response = requests.get(url=upload_url, headers=headers, params=params)
        return response.json()

    def upload_file_to_disk(self, disk_file_path: str, filename: str):

        href = self._get_upload_link(disk_file_path=disk_file_path).get("href","")
        response = requests.put(url=href, data=open(filename, "rb"))
        response.raise_for_status()
        if response.status_code == 201:
            print('Success')


def start_loader():
    path_to_file = os.path.join(os.getcwd(), '1.txt')
    name = os.path.basename(path_to_file)
    token = input('Input your token: ')
    yandex_loader = YaUploader(token)
    yandex_loader.upload_file_to_disk(f'Загрузки/{name}', path_to_file)
