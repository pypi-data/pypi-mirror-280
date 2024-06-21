import requests

BASE_URL = 'https://intellihack-backend-rcbmvyttca-uc.a.run.app'

class IntelliBotAPI:
    def __init__(self):
        self.access_token = None
        self.user_id = None
        self.username = None

    def connect(self, username, password):
        headers = {'Content-Type': 'application/x-www-form-urlencoded'}
        data = {'username': username, 'password': password}
        response = requests.post(BASE_URL + '/login', data=data, headers=headers)
        if response.status_code == 200:
            auth_data = response.json()
            self.access_token = auth_data['access_token']
            self.user_id = auth_data['id']
            self.username = auth_data['email']
        return response

    def chat(self, message, history=None):
        if not self.access_token or not self.user_id or not self.username:
            raise Exception("User not authenticated. Please connect first.")
        
        headers = {
            'Content-Type': 'application/json',
            # 'Authorization': f'Bearer {self.access_token}'
        }
        json_data = {
            'user_id': self.user_id,
            'username': self.username,
            'message': message,
            'history': history if history else ''
        }
        return requests.post(BASE_URL + '/query/chat', json=json_data, headers=headers)
