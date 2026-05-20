


import pandas as pd 
from src.clean import cleaning_data




def test_cleanning_data(sample_df):
    
    result = cleaning_data(sample_df)
    expected_date = pd.to_datetime('15/03/2024', errors='coerce', dayfirst=True, format='mixed').date()
    expected_time = pd.to_datetime('19:30', errors='coerce', dayfirst=True, format='mixed').time()


    assert result['restaurant'][0] == 'Paris Central'
    assert result['customer_name'][0] == 'Alice Martin'
    assert result['menu_item'][0] == 'Pizza Margherita'
    assert result['category'][0] == 'Pizza'
    assert result['quantity'][0] == 1
    assert result['unit_price'][0] == 12.50
    assert result['discount'][0] == 0
    assert result['rating'][0] == 5
    assert result['payment_method'][0] == 'CARD'

    assert result['order_date'][0] == expected_date
    assert result['order_time'][0] == expected_time

