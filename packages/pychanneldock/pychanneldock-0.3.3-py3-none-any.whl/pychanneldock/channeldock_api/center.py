from pychanneldock.constants.center_constants import Constants
import requests
import os
import base64
import json


class ChannelDockAPI:
    """
    Official documentation: https://documenter.getpostman.com/view/16435285/2s9XxsUbPy

    """

    def __init__(self):
        self.headers = Constants.HEADERS

    @staticmethod
    def save_json(path, json_obj):
        """
        Save a JSON object to a file.

        :param path: The path of the file where the JSON object will be saved.
        :param json_obj: The JSON object to save.
        """
        with open(path, 'w') as f:
            f.write(json.dumps(json_obj, indent=4))

    def check_credentials(self):
        """
        Check if the credentials are correct
        :return: The response from the GET request.
        """
        return requests.get(Constants.HOME_URL, headers=self.headers)

    def get_product(self, page=1, **kwargs):
        """
        Get products from ChannelDock API
        :param page: page number - mandatory
        :param kwargs: id, seller_id, center_id, ean, sku, product_reference, location, sort_attr, sort_dir, include_stock_location_data
        id: the product id
        seller_id: the seller id
        center_product_status: the center product status
        ean: the product ean
        sku: the product sku
        product_reference: the product reference
        location: free input - location of the product
        sort_attr: the attribute to sort by (updated_at, id)
        sort_dir: the direction to sort by (ASC, DESC)
        include_stock_location_data: include stock location data (true or false)

        :return: The response from the GET request.
        """

        url = f'{Constants.PRODUCTS_URL}?page={page}'
        for key, value in kwargs.items():
            url = f'{url}&{key}={value}'
        return requests.get(url, headers=self.headers)

    def get_all_products(self, **kwargs):
        """
        Get all products from ChannelDock API
        :param kwargs: id, ean, sku, tittle, supplier_id, sort_attr, sort_dir, include_stock_location_data
        id: the product id
        ean: the product ean
        sku: the product sku
        title: the product title
        supplier_id: the supplier id
        sort_attr: the attribute to sort by (updated_at, id)
        sort_dir: the direction to sort by (ASC, DESC)
        include_stock_location_data: include stock location data (true or false)
        :return: List of all products
        """
        page = 0
        products = []
        while True:
            page += 1
            response = self.get_product(page, **kwargs)
            if response.status_code == 200:
                response = response.json()
                if response['response'] == 'success' and len(response['products']) > 0:
                    products.extend(response['products'])
                else:
                    break
            else:
                break
        return products

    def update_product(self, data):
        """
        For more details on the data format, check the official documentation
        Post product to ChannelDock API
        :param data: product data
        :return: The response from the POST request.
        """

        url = Constants.PRODUCTS_URL
        data = json.dumps(data, indent=4)
        return requests.post(url, headers=self.headers, data=data)

    def update_stock_amount_bulk(self, data):
        """
        For more details on the data format, check the official documentation
        Post product to ChannelDock API
        :param data: product data
        :return: The response from the POST request.
        """

        url = Constants.PRODUCTS_STOCK_UPDATE_URL
        data = json.dumps(data, indent=4)
        return requests.post(url, headers=self.headers, data=data)

    def get_orders(self, page=1, **kwargs):
        """
        Get orders from ChannelDock API
        :param page: page number - mandatory
        :param kwargs: id, seller_id, order_status, order_id, shipping_country_code, sort_attr, sort_dir, start_date,
                        end_date, include_raw_order_data
        id: the order id in the system
        seller_id: the seller id
        order_status: the order status
        order_id: the order id
        shipping_country_code: the shipping country code
        sort_attr: the attribute to sort by (updated_at, default: order_date, sync_date, updated_at)
        sort_dir: the direction to sort by (ASC, DESC)
        shipping_address_accurate: the shipping address accurate (default:1, 0, 'ALL')
        start_date: the start date
        end_date: the end date
        include_raw_order_data: include raw order data (true or false)
        :return: The response from the GET request.
        """

        url = f'{Constants.ORDERS_URL}?page={page}'
        for key, value in kwargs.items():
            url = f'{url}&{key}={value}'
        return requests.get(url, headers=self.headers)

    def get_all_orders(self, **kwargs):
        """
        Get all orders from ChannelDock API
        :param kwargs: order_status, order_id, shipping_country_code, sort_attr, sort_dir, start_date, end_date, id,
                        include_raw_order_data
        order_status: the order status
        order_id: the order id
        shipping_country_code: the shipping country code
        sort_attr: the attribute to sort by (updated_at, default: order_date, sync_date, updated_at)
        sort_dir: the direction to sort by (ASC, DESC)
        start_date: the start date
        end_date: the end date
        id: the order id
        include_raw_order_data: include raw order data (true or false)
        :return: List of all orders
        """

        page = 0
        orders = []
        while True:
            page += 1
            response = self.get_orders(page, **kwargs)
            if response.status_code == 200:
                response = response.json()
                if len(response['orders']) > 0 and response['response'] == 'success':
                    orders.extend(response['orders'])
                else:
                    break
            else:
                break
        return orders

    def create_order(self, data):
        """
        For more details on the data format, check the official documentation
        Post order to ChannelDock API
        :param data: order data
        :return: The response from the POST request.
        """

        url = Constants.ORDERS_URL
        data = json.dumps(data, indent=4)
        return requests.post(url, headers=self.headers, data=data)

    def create_stock_location(self, data):
        """
        For more details on the data format, check the official documentation
        Post stock location to ChannelDock API
        :param data: stock location data
        :return: The response from the POST request.
        """

        url = Constants.CREATE_STOCK_LOCATION_URL
        data = json.dumps(data, indent=4)
        return requests.post(url, headers=self.headers, data=data)

    def update_stock_location(self, data):
        """
        For more details on the data format, check the official documentation
        Update stock location to ChannelDock API
        :param data: stock location data
        :return: The response from the PUT request.
        """

        url = Constants.CREATE_STOCK_LOCATION_URL
        data = json.dumps(data, indent=4)
        return requests.put(url, headers=self.headers, data=data)

    def delete_stock_location(self, data):
        """
        For more details on the data format, check the official documentation
        Delete stock location to ChannelDock API
        :param data: stock location data
        :return: The response from the DELETE request.
        """

        url = Constants.CREATE_STOCK_LOCATION_URL
        data = json.dumps(data, indent=4)
        return requests.delete(url, headers=self.headers, data=data)

    def get_shipments(self, page=1, **kwargs):
        """
        Get shipments from ChannelDock API
        :param page: page number - mandatory
        :param kwargs: id, seller_id, status, order_id, sort_attr, sort_dir, start_date, end_date, include_pdf_label
        id: the shipment id in the system
        seller_id: the seller id
        status: the shipment status (registered, distribution, delivered, return)
        order_id: the order id
        sort_attr: the attribute to sort by (updated_at, default: created_at, updated_at)
        sort_dir: the direction to sort by (ASC, DESC)
        start_date: the start date
        end_date: the end date
        include_pdf_label: include pdf label (true or false)
        :return: The response from the GET request.
        """

        url = f'{Constants.SHIPMENTS_URL}?page={page}'
        for key, value in kwargs.items():
            url = f'{url}&{key}={value}'
        return requests.get(url, headers=self.headers)

    def get_all_shipments(self, **kwargs):
        """
        Get all shipments from ChannelDock API
        :param kwargs: id, seller_id, status, order_id, sort_attr, sort_dir, start_date, end_date, include_pdf_label
        id: the shipment id in the system
        seller_id: the seller id
        status: the shipment status (registered, distribution, delivered, return)
        order_id: the order id
        sort_attr: the attribute to sort by (updated_at, default: created_at, updated_at)
        sort_dir: the direction to sort by (ASC, DESC)
        start_date: the start date
        end_date: the end date
        include_pdf_label: include pdf label (true or false)
        :return: List of all shipments
        """

        page = 0
        shipments = []
        while True:
            page += 1
            response = self.get_shipments(page, **kwargs)
            if response.status_code == 200:
                response = response.json()
                if len(response['shipments']) > 0 and response['response'] == 'success':
                    shipments.extend(response['shipments'])
                else:
                    break
            else:
                break
        return shipments

    @staticmethod
    def create_labels(dir_path, shipments):
        """
        Create labels from shipments
        :param dir_path: Path to save the labels
        :param shipments: Shipments to create labels
        :return:
        """
        directories = os.path.abspath(dir_path)
        if not os.path.exists(directories):
            os.makedirs(directories)
        labels = []
        for shipment in shipments:
            file_name = f'{directories}/label_{shipment["id"]}.pdf'
            encoded_pdf = base64.b64decode(shipment["base64_label_pdf"])
            labels.append(encoded_pdf)
            with open(file_name, 'wb') as f:
                f.write(encoded_pdf)

    def update_shipment(self, data):
        """
        For more details on the data format, check the official documentation
        Update shipment to ChannelDock API
        :param data: shipment data
        :return: The response from the PUT request.
        """

        url = Constants.SHIPMENTS_URL
        data = json.dumps(data, indent=4)
        return requests.put(url, headers=self.headers, data=data)

    def create_shipment(self, data):
        """
        For more details on the data format, check the official documentation
        Post shipment to ChannelDock API
        :param data: shipment data
        :return: The response from the POST request.
        """

        url = Constants.SHIPMENTS_URL
        data = json.dumps(data, indent=4)
        return requests.post(url, headers=self.headers, data=data)

    def list_carriers(self):
        """
        Get carriers from ChannelDock API
        :return: The response from the GET request.
        """

        return requests.get(Constants.CARRIERS_URL, headers=self.headers)

    def get_sellers(self, page=1, **kwargs):
        """
        Get sellers from ChannelDock API
        :param page: page number - mandatory
        :param kwargs: seller_id, sort_attr, sort_dir
        seller_id: the seller id
        sort_attr: the attribute to sort by
        sort_dir: the direction to sort by (ASC, DESC)
        :return: The response from the GET request.
        """

        url = f'{Constants.SELLERS_URL}?page={page}'
        return requests.get(url, headers=self.headers)

    def get_all_sellers(self, **kwargs):
        """
        Get all sellers from ChannelDock API
        :param kwargs: seller_id, sort_attr, sort_dir
        seller_id: the seller id
        sort_attr: the attribute to sort by
        sort_dir: the direction to sort by (ASC, DESC)
        :return: List of all sellers
        """

        page = 0
        sellers = []
        while True:
            page += 1
            response = self.get_sellers(page, **kwargs)
            if response.status_code == 200:
                response = response.json()
                if len(response['sellers']) > 0 and response['response'] == 'success':
                    sellers.extend(response['sellers'])
                else:
                    break
            else:
                break
        return sellers

    def get_administration(self, page=1, **kwargs):
        """
        Get administration from ChannelDock API
        :param page: page number - mandatory
        :param kwargs: start_date, end_date, seller_id
        start_date: the start date
        end_date: the end date
        seller_id: the seller id
        :return: The response from the GET request.
        """
        url = f'{Constants.ADMINISTRATION_URL}?page={page}'
        for key, value in kwargs.items():
            url = f'{url}&{key}={value}'
        return requests.get(url, headers=self.headers)

    def get_all_administration(self, **kwargs):
        """
        Get all administration from ChannelDock API
        :param kwargs: start_date, end_date, seller_id
        start_date: the start date
        end_date: the end date
        seller_id: the seller id
        :return: List of all administration
        """
        page = 0
        administration = []
        while True:
            page += 1
            response = self.get_administration(page, **kwargs)
            if response.status_code == 200:
                response = response.json()
                if len(response['sellers']) > 0 and response['sellers'] == 'success':
                    administration.extend(response['sellers'])
                else:
                    break
            else:
                break
        return administration

    def get_inbounds(self, page=1, **kwargs):
        """
        Get inbounds from ChannelDock API
        :param page: page number - mandatory
        :param kwargs: id, seller_id, status, sort_attr, sort_dir, start_date, end_date
        id: the inbound id
        seller_id: the seller id
        status: the inbound status (new, confirmed, stocked)
        sort_attr: the attribute to sort by (updated_at, default: created_at, updated_at)
        sort_dir: the direction to sort by (ASC, DESC)
        delivery_type: the delivery type (default: outbound, bol_outbound, amazon_outbound)
        :return: The response from the GET request.
        """
        url = f'{Constants.INBOUNDS_URL}?page={page}'
        for key, value in kwargs.items():
            url = f'{url}&{key}={value}'
        return requests.get(url, headers=self.headers)

    def get_all_inbounds(self, **kwargs):
        """
        Get all inbounds from ChannelDock API
        :param kwargs: id, seller_id, status, sort_attr, sort_dir, start_date, end_date
        id: the inbound id
        seller_id: the seller id
        status: the inbound status (new, confirmed, stocked)
        sort_attr: the attribute to sort by (updated_at, default: created_at, updated_at)
        sort_dir: the direction to sort by (ASC, DESC)
        delivery_type: the delivery type (default: outbound, bol_outbound, amazon_outbound)
        :return: List of all inbounds
        """
        page = 0
        inbounds = []
        while True:
            page += 1
            response = self.get_inbounds(page, **kwargs)
            if response.status_code == 200:
                response = response.json()
                if len(response['inbounds']) > 0 and response['response'] == 'success':
                    inbounds.extend(response['inbounds'])
                else:
                    break
            else:
                break
        return inbounds

    def create_inbound(self, data):
        """
        For more details on the data format, check the official documentation
        Post inbound to ChannelDock API
        :param data: inbound data
        :return: The response from the POST request.
        """

        url = Constants.INBOUNDS_URL
        data = json.dumps(data, indent=4)
        return requests.post(url, headers=self.headers, data=data)

    def update_inbound(self, data):
        """
        For more details on the data format, check the official documentation
        Update inbound to ChannelDock API
        :param data: inbound data
        :return: The response from the PUT request.
        """

        url = Constants.INBOUNDS_URL
        data = json.dumps(data, indent=4)
        return requests.put(url, headers=self.headers, data=data)

    def delete_inbound(self, data):
        """
        For more details on the data format, check the official documentation
        Delete inbound to ChannelDock API
        :param data: inbound data
        :return: The response from the DELETE request.
        """

        url = Constants.INBOUNDS_URL
        data = json.dumps(data, indent=4)
        return requests.delete(url, headers=self.headers, data=data)

    def stock_inbound_item(self, data):
        """
        For more details on the data format, check the official documentation
        :param data:
        :return: The response from the POST request.
        """
        url = Constants.STOCK_INBOUND_ITEM_URL
        data = json.dumps(data, indent=4)
        return requests.post(url, headers=self.headers, data=data)

    def get_returns(self, page=1, **kwargs):
        """
        Get returns from ChannelDock API
        :param page: page number - mandatory
        :param kwargs: id, order_id, sort_attr, sort_dir, remote_order_id, remote_return_id, is_handled,
                start_handled_date, end_handled_date
        id: the return id
        order_id: the order id
        sort_attr: the attribute to sort by (order_id)
        sort_dir: the direction to sort by (ASC, DESC)
        remote_order_id: the remote order id (from r.g. Amazon or bol.com)
        remote_return_id: the remote return id (from r.g. Amazon or bol.com)
        is_handled: the return is handled (1 or 0)
        start_handled_date: the start handled date
        end_handled_date: the end handled date
        :return: The response from the GET request.
        """
        url = f'{Constants.RETURNS_URL}?page={page}'
        for key, value in kwargs.items():
            url = f'{url}&{key}={value}'
        return requests.get(url, headers=self.headers)

    def get_all_returns(self, **kwargs):
        """
        Get all returns from ChannelDock API
        :param kwargs: id, order_id, sort_attr, sort_dir, remote_order_id, remote_return_id, is_handled,
                start_handled_date, end_handled_date
        id: the return id
        order_id: the order id
        sort_attr: the attribute to sort by (order_id)
        sort_dir: the direction to sort by (ASC, DESC)
        remote_order_id: the remote order id (from r.g. Amazon or bol.com)
        remote_return_id: the remote return id (from r.g. Amazon or bol.com)
        is_handled: the return is handled (1 or 0)
        start_handled_date: the start handled date
        end_handled_date: the end handled date
        :return: List of all returns
        """
        page = 0
        returns = []
        while True:
            page += 1
            response = self.get_returns(page, **kwargs)
            if response.status_code == 200:
                response = response.json()
                if len(response['returns']) > 0 and response['response'] == 'success':
                    returns.extend(response['returns'])
                else:
                    break
            else:
                break
        return returns

    def handle_return(self, data):
        """
        For more details on the data format, check the official documentation
        Handle return to ChannelDock API
        :param data: return data
        :return: The response from the PUT request.
        """

        url = Constants.RETURNS_URL
        data = json.dumps(data, indent=4)
        return requests.put(url, headers=self.headers, data=data)
