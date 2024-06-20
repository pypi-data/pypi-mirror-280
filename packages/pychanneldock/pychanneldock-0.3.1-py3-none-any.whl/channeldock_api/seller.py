from constants.seller_constants import Constants
import requests
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
        :param kwargs: id, ean, sku, tittle, supplier_id, sort_attr, sort_dir, include_stock_location_data
        id: the product id
        ean: the product ean
        sku: the product sku
        title: the product title
        supplier_id: the supplier id
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
        Get products from ChannelDock API
        :param kwargs: id, ean, sku, tittle, supplier_id, sort_attr, sort_dir, include_stock_location_data
        id: the product id
        ean: the product ean
        sku: the product sku
        title: the product title
        supplier_id: the supplier id
        sort_attr: the attribute to sort by (updated_at, id)
        sort_dir: the direction to sort by (ASC, DESC)
        include_stock_location_data: include stock location data (true or false)
        :return: The response from the GET request.
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
        return requests.put(url, headers=self.headers, data=data)

    def create_product(self, data):
        """
        For more details on the data format, check the official documentation
        Create product to ChannelDock API
        :param data: product data
        :return: The response from the POST request.
        """

        url = Constants.PRODUCTS_URL
        data = json.dumps(data, indent=4)
        return requests.post(url, headers=self.headers, data=data)

    def get_orders(self, page=1, **kwargs):
        """
        Get orders from ChannelDock API
        :param page: page number - mandatory
        :param kwargs: id, order_status, order_id, shipping_country_code, sort_attr, sort_dir, start_date,
                        end_date, include_raw_order_data
        id: the order id in the system
        order_status: the order status (default: order, shipment, cancelled, return)
        order_id: the order id
        shipping_country_code: the shipping country code
        sort_attr: the attribute to sort by (default: order_date, id, sync_date, updated_at)
        sort_dir: the direction to sort by (default: ASC, DESC)
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
        :param kwargs: id, order_status, order_id, shipping_country_code, sort_attr, sort_dir, start_date,
                        end_date, include_raw_order_data
        id: the order id in the system
        order_status: the order status (default: order, shipment, cancelled, return)
        order_id: the order id
        shipping_country_code: the shipping country code
        sort_attr: the attribute to sort by (default: order_date, id, sync_date, updated_at)
        sort_dir: the direction to sort by (default: ASC, DESC)
        start_date: the start date
        end_date: the end date
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

    def update_order(self, data):
        """
        For more details on the data format, check the official documentation
        Update order to ChannelDock API
        :param data: order data
        :return: The response from the PUT request.
        """

        url = Constants.ORDERS_URL
        data = json.dumps(data, indent=4)
        return requests.put(url, headers=self.headers, data=data)

    def get_shipments(self, page=1, **kwargs):
        """
        Get shipments from ChannelDock API
        :param page: page number - mandatory
        :param kwargs: id, status, order_id, sort_attr, sort_dir, start_date, end_date
        id: the shipment id in the system
        status: the shipment status (registered, distribution, delivered, return)
        order_id: the order id
        sort_attr: the attribute to sort by (id, default: created_at, order_id)
        sort_dir: the direction to sort by (ASC, DESC)
        start_date: the start date
        end_date: the end date
        :return: The response from the GET request.
        """

        url = f'{Constants.SHIPMENTS_URL}?page={page}'
        for key, value in kwargs.items():
            url = f'{url}&{key}={value}'
        return requests.get(url, headers=self.headers)

    def get_all_shipments(self, **kwargs):
        """
        Get all shipments from ChannelDock API
        :param kwargs: id, status, order_id, sort_attr, sort_dir, start_date, end_date
        id: the shipment id in the system
        status: the shipment status (registered, distribution, delivered, return)
        order_id: the order id
        sort_attr: the attribute to sort by (id, default: created_at, order_id)
        sort_dir: the direction to sort by (ASC, DESC)
        start_date: the start date
        end_date: the end date
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

    def get_deliveries(self, page=1, **kwargs):
        """
        Get deliveries from ChannelDock API
        :param page: page number - mandatory
        :param kwargs: id, status, supplier_id, sort_attr, sort_dir, delivery_type, ref, status, delivery_date
        id: the delivery id in the system
        status: the delivery status
        supplier_id: the order id
        sort_attr: the attribute to sort by (id, default: created_at, order_id)
        sort_dir: the direction to sort by (ASC, DESC)
        delivery_type: the delivery type (inbound, outbound, bol_outbound, amazaon_outbound)
        ref: the delivery reference
        status: the delivery status (new, confirmed, delivered, stocked, shipped, cancelled)
        delivery_date: the delivery date
        :return: The response from the GET request.
        """

        url = f'{Constants.DELIVERIES_URL}?page={page}'
        for key, value in kwargs.items():
            url = f'{url}&{key}={value}'
        return requests.get(url, headers=self.headers)

    def create_delivery(self, data):
        """
        For more details on the data format, check the official documentation
        Post delivery to ChannelDock API
        :param data: delivery data
        :return: The response from the POST request.
        """

        url = Constants.DELIVERIES_URL
        data = json.dumps(data, indent=4)
        return requests.post(url, headers=self.headers, data=data)

    def update_delivery(self, data):
        """
        For more details on the data format, check the official documentation
        Update delivery to ChannelDock API
        :param data: delivery data
        :return: The response from the PUT request.
        """

        url = Constants.DELIVERIES_URL
        data = json.dumps(data, indent=4)
        return requests.put(url, headers=self.headers, data=data)

    def delete_delivery(self, data):
        """
        For more details on the data format, check the official documentation
        Delete delivery to ChannelDock API
        :param data: delivery data
        :return: The response from the DELETE request.
        """

        url = Constants.DELIVERIES_URL
        data = json.dumps(data, indent=4)
        return requests.delete(url, headers=self.headers, data=data)

    def get_suppliers(self, page=1, **kwargs):
        """
        Get suppliers from ChannelDock API
        :param page: page number - mandatory
        :param kwargs: id, company, sort_attr, sort_dir
        id: the supplier id
        company: the supplier company name
        sort_attr: the attribute to sort by
        sort_dir: the direction to sort by (ASC, DESC)
        :return: The response from the GET request.
        """

        url = f'{Constants.SUPPLIERS_URL}?page={page}'
        for key, value in kwargs.items():
            url = f'{url}&{key}={value}'
        return requests.get(url, headers=self.headers)

    def get_all_suppliers(self, **kwargs):
        """
        Get all suppliers from ChannelDock API
        :param kwargs: id, company, sort_attr, sort_dir
        id: the supplier id
        company: the supplier company name
        sort_attr: the attribute to sort by
        sort_dir: the direction to sort by (ASC, DESC)
        :return: List of all suppliers
        """
        page = 0
        suppliers = []
        while True:
            page += 1
            response = self.get_suppliers(page, **kwargs)
            if response.status_code == 200:
                response = response.json()
                if len(response['suppliers']) > 0 and response['response'] == 'success':
                    suppliers.extend(response['suppliers'])
                else:
                    break
            else:
                break
        return suppliers

    def create_update_supplier(self, data):
        """
        For more details on the data format, check the official documentation
        Post supplier to ChannelDock API
        :param data: supplier data
        :return: The response from the POST request.
        """

        url = Constants.SUPPLIERS_URL
        data = json.dumps(data, indent=4)
        return requests.post(url, headers=self.headers, data=data)

    def delete_supplier(self, data):
        """
        For more details on the data format, check the official documentation
        Delete supplier to ChannelDock API
        :param data: supplier data
        :return: The response from the DELETE request.
        """

        url = Constants.SUPPLIERS_URL
        data = json.dumps(data, indent=4)
        return requests.delete(url, headers=self.headers, data=data)

    def get_returns(self, page=1, **kwargs):
        """
        Get returns from ChannelDock API
        :param page: page number - mandatory
        :param kwargs: id, sort_attr, sort_dir, remote_order_id, remote_return_id, is_handled, order_id
        id: the return id
        sort_attr: the attribute to sort by (order_id)
        sort_dir: the direction to sort by (ASC, DESC)
        remote_order_id: the remote order id (from r.g. Amazon or bol.com)
        remote_return_id: the remote return id (from r.g. Amazon or bol.com)
        is_handled: the return is handled (1 or 0)
        order_id: the order id
        :return: The response from the GET request.
        """
        url = f'{Constants.RETURNS_URL}?page={page}'
        for key, value in kwargs.items():
            url = f'{url}&{key}={value}'
        return requests.get(url, headers=self.headers)

    def get_all_returns(self, **kwargs):
        """
        Get all returns from ChannelDock API
                :param kwargs: id, sort_attr, sort_dir, remote_order_id, remote_return_id, is_handled, order_id
        id: the return id
        sort_attr: the attribute to sort by (order_id)
        sort_dir: the direction to sort by (ASC, DESC)
        remote_order_id: the remote order id (from r.g. Amazon or bol.com)
        remote_return_id: the remote return id (from r.g. Amazon or bol.com)
        is_handled: the return is handled (1 or 0)
        order_id: the order id
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
