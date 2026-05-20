


import pandas as pd 
from src.features import add_features


def test_add_features(sample_df):

    from src.clean import cleaning_data
    clean_df = cleaning_data(sample_df)
    result = add_features(clean_df)

    total_price = result['total_price'].iloc[0]
    amount_dis = result['discount_amount'].iloc[0]
    assert total_price == round((12.50*1), 2)
    assert amount_dis == round(((total_price*0) / 100), 2)
    assert result['total_amount'].iloc[0] == round((total_price - amount_dis), 2)

    import datetime

    df_test = pd.DataFrame({
        'order_time': [
            datetime.time(12, 0),  # Midi
            datetime.time(18, 59), # Limite
            datetime.time(19, 0),  # Soir
            datetime.time(22, 30)  # Soir tard
        ]
    })

    df_test['service_type'] = df_test['order_time'].apply(lambda x : 'Soir' if x.hour >= 19 else 'Dejeuner')

    assert df_test['service_type'][0] == 'Dejeuner'
    assert df_test['service_type'][1] == 'Dejeuner'
    assert df_test['service_type'][2] == 'Soir'
    assert df_test['service_type'][3] == 'Soir'