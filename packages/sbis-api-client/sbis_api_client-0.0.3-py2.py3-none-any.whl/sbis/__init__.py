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

    def get_points(self, *, pointId: int=None, product: str=None, withPhones: bool=None, withPrices: bool=None, withSchedule: bool=None, page: int=None, pageSize: int=None):
        """
        Запрос возвращает информацию о точках продаж.

        Parameters:
            pointId (int, optional): Идентификатор точки продаж.
            product (str, optional): Название продукта точки продаж.
            withPhones (bool, optional): Флаг передачи всех или одного номера телефона по точке продаж. По умолчанию False.
            withPrices (bool, optional): Флаг передачи идентификаторов всех прайсов по точке продаж. По умолчанию False.
            withSchedule (bool, optional): Флаг передачи подробного режима работы точки продаж. По умолчанию False.
            page (int, optional): Номер страницы результата. Если не указан, вернутся все результаты.
            pageSize (int, optional): Размер страницы. Если не указан, вернутся все результаты.

        Returns:
            dict: Список точек продаж в формате JSON.

        Raises:
            Exception: Если произошла ошибка при выполнении запроса.

        """
        url = 'https://api.sbis.ru/retail/point/list'
        headers = {
            "X-SBISAccessToken": self.token
        }
        parameters = {
            'pointId': pointId,
            'product': product,
            'withPhones': withPhones,
            'withPrices': withPrices, 
            'withSchedule': withSchedule,
            'page': page,
            'pageSize': pageSize
        }

        parameters = {k: v for k, v in parameters.items() if v is not None}
        
        try:
            response = requests.get(url, params=parameters, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ошибка при выполнении запроса: {e}")

    def get_priceList(self, *, pointId: int, actualDate: str, searchString: str = None, page: int=None, pageSize: int=None):
        """
        Запрос возвращает информацию о действующих прайс-листах. Чтобы запрос работал корректно, настройте прайс-лист с типом «Выбранные наименования».

        Parameters:
            pointId (int): Идентификатор точки продаж, который возвращается в результате запроса «Получить точку продаж».
            actualDate (str): Дата в формате ГГГГ-ММ-ДД.
            searchString (str, optional): Название прайса, который требуется найти.
            page (int, optional): Номер страницы результата. Если не указан, вернутся все результаты.
            pageSize (int, optional): Количество записей на странице. Если не указан, вернутся все результаты.

        Returns:
            dict: Прайс-лист товаров в формате JSON.

        Raises:
            Exception: Если произошла ошибка при выполнении запроса.

        """
        url = 'https://api.sbis.ru/retail/nomenclature/price-list'
        headers = {
            "X-SBISAccessToken": self.token
        }
        parameters = {
            'pointId': pointId,
            'actualDate': actualDate,
            'searchString': searchString,
            'page': page,
            'pageSize': pageSize
        }

        parameters = {k: v for k, v in parameters.items() if v is not None}
        
        try:
            response = requests.get(url, params=parameters, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ошибка при выполнении запроса: {e}")

    def get_nomenclatureList(self, *, pointId: int, priceListId: int, withBalance: bool=None, withBarcode: bool=None, onlyPublished: bool=None, page: int=None, pageSize: int=None):
        """
        Запрос возвращает информацию о товарах и услугах по действующему прайс-листу.

        Parameters:
            pointId (int): Идентификатор точки продаж, который вернулся в результате запроса «Получить точку продаж».
            priceListId (int): Идентификатор прайс-листа, который вернулся в результате запроса «Получить прайс-лист».
            withBalance (bool, optional): Признак передачи остатков.
            withBarcode (bool, optional): Признак передачи штрихкодов товара.
            onlyPublished (bool, optional): Признак возврата только опубликованных позиций.
            page (int, optional): Номер страницы
            pageSize (int, optional): Количество записей на странице.

        Returns:
            dict: Словарь с результатом запроса в формате JSON.

        Raises:
            Exception: Если произошла ошибка при выполнении запроса.
        """
        url = 'https://api.sbis.ru/retail/nomenclature/list?'
        headers = {
            "X-SBISAccessToken": self.token
        }
        parameters = {
            'pointId': pointId,
            'priceListId': priceListId,
            'withBalance': withBalance,
            'withBarcode': withBarcode,
            'onlyPublished': onlyPublished,
            'page': page,
            'pageSize': pageSize
        }

        parameters = {k: v for k, v in parameters.items() if v is not None}

        try:
            response = requests.get(url, params=parameters, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ошибка при выполнении запроса: {e}")

    def get_nomenclature_balances(self, *, nomenclatures=None, priceListIds=None, warehouses, companies):
        """
        Запрос возвращает информацию об остатках товаров на складе.

        Parameters:
            nomenclatures (list of int, optional): Массив идентификаторов товаров.
            priceListIds (list of int, optional): Массив идентификаторов товаров из прайс-листа.
            warehouses (list of int): Идентификаторы складов, на которых проверяются остатки.
            companies (list of int): Идентификаторы организаций.

        Returns:
            dict: Словарь с результатом запроса в формате JSON.

        Raises:
            Exception: Если произошла ошибка при выполнении запроса.
        """
        url = 'https://api.sbis.ru/retail/nomenclature/balances'
        headers = {
            "X-SBISAccessToken": self.token
        }
        
        parameters = {
            'nomenclatures': nomenclatures, 
            'priceListIds':priceListIds,
            'warehouses': warehouses,
            'companies': companies
        }
        
        parameters = {k: v for k, v in parameters.items() if v is not None}
        
        try:
            response = requests.get(url, params=parameters, headers=headers)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            raise Exception(f"Ошибка при выполнении запроса: {e}")

    def get_bonus_client(self, phone:int, pointId:int):
        """
        Возвращает список документов пользователя.

        Parameters:
            phone (int): Номер телефона клиента.
            pointId (int): Идентификатор точки продаж

        Returns:
            bonusBalance: Баланс бонусов, доступный для списания в точке продаж. Состоит из персональных бонусов и бонусов по всем картам, действительным в точке продаж. Если оплата бонусами в точке продаж отключена, вернется «null»

        Raises:
            Exception: Если произошла ошибка при выполнении запроса.

        """
        
        externalId = requests.get(f"https://api.sbis.ru/retail/customer/find?phone={phone}")
        

        url = f"https://api.sbis.ru/retail/customer/{externalId}/bonus-balance"
        headers = {
            'Content-Type': 'charset=utf-8',
            'X-SBISAccessToken': self.token
        }
        params = {
            'pointId': pointId
        }
        try:
            response = requests.get(url, headers=headers, params=params)
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Ошибка при выполнении запроса. Код ответа: {response.status_code}")
                return None
        except Exception as e:
            print(f"Ошибка при выполнении запроса: {str(e)}")
            return None
