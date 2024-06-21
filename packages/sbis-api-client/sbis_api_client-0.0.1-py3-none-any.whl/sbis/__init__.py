import requests

class SbisClient:
    def __init__(self, clientId, secret, secretKey):
        self.clientId = clientId
        self.secret = secret
        self.secretKey = secretKey
        self.token = None
        self.sid = None

    def authenticate(self):
        """
        Выполняет аутентификацию пользователя и сохраняет полученный токен и сессионный ID (sid).

        Raises:
            Exception: Если произошла ошибка при выполнении запроса.

        """
        json_payload = {
            "app_client_id": self.clientId,
            "app_secret": self.secret,
            "secret_key": self.secretKey
        }
        url = 'https://online.sbis.ru/oauth/service/'
        
        try:
            response = requests.post(url, json=json_payload)
            if response.status_code == 200:
                data = response.json()
                self.token = data.get('token')
                self.sid = data.get('sid')
                print("Аутентификация прошла успешно.")
            else:
                print(f"Ошибка при аутентификации. Код ответа: {response.status_code}")
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {str(e)}")

    def data(self):
        """
        Выводит данные текущего состояния клиента.
        """
        print(f"\nClient ID: {self.clientId}")
        print(f"Secret: {self.secret}")
        print(f"Secret Key: {self.secretKey}")
        print(f"Token: {self.token}")
        print(f"Session ID (SID): {self.sid}\n")

    def logout(self):
        """
        Выполняет выход пользователя из системы, завершая использование текущего токена доступа.

        Raises:
            Exception: Если произошла ошибка при выполнении запроса.

        """
        if not self.token:
            print("Не выполнена аутентификация. Вызовите метод authenticate() для получения токена.")
            return
        
        url = 'https://online.sbis.ru/oauth/service/'
        json_payload = {
            "event": "exit",
            "token": self.token
        }
        headers = {
            'Content-Type': 'application/json'
        }
        
        try:
            response = requests.post(url, json=json_payload, headers=headers)
            response.raise_for_status()  # Проверка на ошибки HTTP
            print("Выход из системы выполнен успешно.")
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при выполнении запроса: {str(e)}")

    def get_documents(self):
        """
        Возвращает список документов пользователя.

        Returns:
            list: Список документов, полученных от API СБИС.

        Raises:
            Exception: Если произошла ошибка при выполнении запроса.

        """
        if not self.token or not self.sid:
            print("Не выполнена аутентификация. Вызовите метод authenticate() для получения токена.")
            return []

        # Пример запроса к API СБИС для получения списка документов
        url = "https://online.sbis.ru/service/"
        headers = {
            'Authorization': f'Bearer {self.token}',
            'X-SBISSessionID': self.sid,
            'Content-Type': 'application/json'
        }
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                data = response.json()
                documents = data.get('documents', [])
                return documents
            else:
                print(f"Ошибка при получении списка документов. Код ответа: {response.status_code}")
                return []
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {str(e)}")
            return []

if __name__ == "__main__":
    client = SbisClient(
        clientId="7760676789310629",
        secret="RWHREDMVWJDHYFZO0CM83MHF",
        secretKey="B9PT47e2j3JGwsswHAzHaU5ssyzoqHsIYFHLjtZYQhlqV8U7eIkF5VIYluyrGwugVv7g1dWRcbSnoCzk10gq961GdzfpUD7INYZiS0wR8K1lrbVwkMjvqi"
    )
    client.authenticate() # Авторизация

    client.data()  # Данные клиента
    
    client.logout() # Выход