


import pandas as pd
import pytest



@pytest.fixture
def sample_df():
    data = {
        'restaurant' : ['paris_central'],
        'customer_name' : ['alice martin'],
        'order_date' : ['15/03/2024'],
        'order_time' : ['19:30'],
        'menu_item' : ['Pizza Margherita'],
        'category' : ['PIZZA'],
        'quantity' : ['1'],
        'unit_price' : ['12.50€'],
        'discount' : ['0%'],
        'payment_method' : ['CARD'],
        'rating' : ['5']
    }

    return pd.DataFrame(data)