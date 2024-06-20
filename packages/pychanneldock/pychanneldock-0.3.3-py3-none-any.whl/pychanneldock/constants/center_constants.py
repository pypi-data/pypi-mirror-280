import os
from dotenv import load_dotenv

load_dotenv()


class Constants:
    """
    Official documentation: https://documenter.getpostman.com/view/16435285/2s9XxsUbPy
    """

    # API Login
    API_KEY_CENTER = os.getenv('API_KEY_CENTER')
    API_SECRET_CENTER = os.getenv('API_SECRET_CENTER')
    HEADERS = {
        'api_key': API_KEY_CENTER,
        'api_secret': API_SECRET_CENTER
    }
    url = 'https://channeldock.com/portal/api/v2/center'
    # GET Requests
    HOME_URL = 'https://channeldock.com/portal/api/v2'
    PRODUCTS_URL = f'{url}/inventory'  # used for getting and creating products
    ORDERS_URL = f'{url}/orders'  # used for getting and creating orders
    SHIPMENTS_URL = f'{url}/shipment'  # used for getting, creating and updating shipments
    CARRIERS_URL = f'{url}/carriers'
    SELLERS_URL = f'{url}/sellers'
    ADMINISTRATION_URL = f'{url}/administration'
    INBOUNDS_URL = f'{url}/inbounds'  # used for getting, creating, updating and deleting inbounds
    RETURNS_URL = f'{url}/returns'  # used for getting, and handling returns

    # POST REQUESTS
    PRODUCTS_STOCK_UPDATE_URL = f'{url}/stockupdateall'

    CREATE_STOCK_LOCATION_URL = f'{url}/stocklocation'  # used for creating, updating and deleting stock locations
    STOCK_INBOUND_ITEM_URL = f'{url}/inbounds/stock'

