import os
from dotenv import load_dotenv

load_dotenv()


class Constants:
    """
    Official documentation: https://documenter.getpostman.com/view/16435285/2s9XxsUbPy
    """

    # API Login
    API_KEY_SELLER = os.getenv('API_KEY_SELLER')
    API_SECRET_SELLER = os.getenv('API_SECRET_SELLER')
    HEADERS = {
        'api_key': API_KEY_SELLER,
        'api_secret': API_SECRET_SELLER
    }
    url = 'https://channeldock.com/portal/api/v2/seller'
    # GET Requests
    HOME_URL = 'https://channeldock.com/portal/api/v2'
    PRODUCTS_URL = f'{url}/inventory'  # used for getting, creating and updating products
    ORDERS_URL = f'{url}/orders'  # used for getting, creating and updating orders
    SHIPMENTS_URL = f'{url}/shipment'  # used for getting and creating shipments
    CARRIERS_URL = f'{url}/carriers'
    DELIVERIES_URL = f'{url}/delivery'  # used for getting, creating, updating and deleting deliveries
    SUPPLIERS_URL = f'{url}/suppliers'  # used for getting, creating, updating and deleting suppliers
    RETURNS_URL = f'{url}/returns'  # used for getting, and handling returns

    # POST REQUESTS
    PRODUCTS_STOCK_UPDATE_URL = f'{url}/stockupdateall'
    CREATE_STOCK_LOCATION_URL = f'{url}/stocklocation'  # used for creating, updating and deleting stock locations

