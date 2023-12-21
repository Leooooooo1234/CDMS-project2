import requests
import simplejson
from urllib.parse import urljoin
from fe.access.auth import Auth


class Buyer:
    def __init__(self, url_prefix, user_id, password):
        self.url_prefix = urljoin(url_prefix, "buyer/")
        self.user_id = user_id
        self.password = password
        self.token = ""
        self.terminal = "my terminal"
        self.auth = Auth(url_prefix)
        code, self.token = self.auth.login(self.user_id, self.password, self.terminal)
        assert code == 200

    def new_order(self, store_id: str, book_id_and_count: [(str, int)]) -> (int, str):
        books = []
        for id_count_pair in book_id_and_count:
            books.append({"id": id_count_pair[0], "count": id_count_pair[1]})
        json = {"user_id": self.user_id, "store_id": store_id, "books": books}
        #print(simplejson.dumps(json))
        url = urljoin(self.url_prefix, "new_order")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        response_json = r.json()
        return r.status_code, response_json.get("order_id")

    def payment(self,  order_id: str):
        json = {"user_id": self.user_id, "password": self.password, "order_id": order_id}
        url = urljoin(self.url_prefix, "payment")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        return r.status_code

    def add_funds(self, add_value: str) -> int:
        json = {"user_id": self.user_id, "password": self.password, "add_value": add_value}
        url = urljoin(self.url_prefix, "add_funds")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        return r.status_code

    def cancel_order(self, buyer_id: str, order_id: str):
        json = {
            "user_id": buyer_id,
            "order_id": order_id
        }
        url = urljoin(self.url_prefix, "cancel_order")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        return r.status_code

    def query_order(self, user_id):
        json = {"user_id": user_id}
        url = urljoin(self.url_prefix, "query_order")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        print('access')
        print(r)
        response_json = r.json()
        return r.status_code, response_json.get("order_list")

    def query_order_para(self, user_id, para):
        json = {"user_id": user_id,
                "para": para
        }
        url = urljoin(self.url_prefix, "query_order_para")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        print('access')
        print(r)
        response_json = r.json()
        return r.status_code, response_json.get("order_list")

    def query_order_state(self, order_id):
        json = {"order_id": order_id}
        url = urljoin(self.url_prefix, "query_order_state")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        # print(r)
        response_json = r.json()
        return r.status_code, response_json.get("order_state")

    def query_detail_order(self, order_id):
        json = {"order_id": order_id}
        url = urljoin(self.url_prefix, "query_detail_order")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        # print(r)
        response_json = r.json()
        return r.status_code, response_json.get("order_detail_list")

    def receive_book(self, buyer_id: str, order_id: str):
        json = {
            "user_id": buyer_id,
            "order_id": order_id
        }
        url = urljoin(self.url_prefix, "receive_book")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        return r.status_code

    # 全站搜索图书，默认搜索第一个
    def search_book_all(self, query: str, first:int = 1):
        json = {
            "query": query,
            "first": first
        }
        url = urljoin(self.url_prefix, "search_book_all")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        response_json = r.json()
        return r.status_code, response_json.get("pages"), response_json.get("book_list")

    # 店铺搜索
    def search_book_store(self, query: str, store_id: str, first: int = 1):
        json = {
            "query": query,
            "store_id": store_id,
            "first": first
        }
        url = urljoin(self.url_prefix, "search_book_store")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        response_json = r.json()
        return r.status_code, response_json.get("pages"), response_json.get("book_list")

    # 全站搜索图书，默认搜索第一个
    def search_book_all_tag(self, tag: str, first: int = 1):
        json = {
            "tag": tag,
            "first": first
        }
        url = urljoin(self.url_prefix, "search_book_all_tag")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        response_json = r.json()
        return r.status_code, response_json.get("pages"), response_json.get("book_list")

    # 店铺搜索
    def search_book_store_tag(self, tag: str, store_id: str, first: int = 1):
        json = {
            "tag": tag,
            "store_id": store_id,
            "first": first
        }
        url = urljoin(self.url_prefix, "search_book_store_tag")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        response_json = r.json()
        return r.status_code, response_json.get("pages"), response_json.get("book_list")

    # 全站搜索图书，默认搜索第一个
    def search_book_all_title(self, title: str, first: int = 1):
        json = {
            "title": title,
            "first": first
        }
        url = urljoin(self.url_prefix, "search_book_all_title")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        response_json = r.json()
        return r.status_code, response_json.get("pages"), response_json.get("book_list")

    # 店铺搜索
    def search_book_store_title(self, title: str, store_id: str, first: int = 1):
        json = {
                "title": title,
                "store_id": store_id,
                "first": first
            }
        url = urljoin(self.url_prefix, "search_book_store_title")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        response_json = r.json()
        return r.status_code, response_json.get("pages"), response_json.get("book_list")

    # 全站搜索图书，默认搜索第一个
    def search_book_all_author(self, author: str, first: int = 1):
        json = {
                "author": author,
                "first": first
            }
        url = urljoin(self.url_prefix, "search_book_all_author")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        response_json = r.json()
        return r.status_code, response_json.get("pages"), response_json.get("book_list")

    # 店铺搜索
    def search_book_store_author(self, author: str, store_id: str, first: int = 1):
        json = {
                "author": author,
                "store_id": store_id,
                "first": first
                }
        url = urljoin(self.url_prefix, "search_book_store_author")
        headers = {"token": self.token}
        r = requests.post(url, headers=headers, json=json)
        response_json = r.json()
        return r.status_code, response_json.get("pages"), response_json.get("book_list")