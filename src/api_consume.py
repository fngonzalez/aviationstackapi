import requests
import pandas as pd


def take_data_from_api (api_link, params):
    api_result = requests.get(api_link, params)

    api_response = api_result.json()


    content_for_df = []

    for flight in api_response['data']:
        row_for_flight = [(flight['flight_date']), 
        (flight['flight_status']), 
        (flight['departure']['airport']), 
        (flight['departure']['timezone']), 
        (flight['arrival']['airport']), 
        (flight['arrival']['timezone']), 
        (flight['arrival']['terminal']), 
        (flight['airline']['name']), 
        (flight['flight']['number'])]

        print(row_for_flight[3]) 
        print(row_for_flight[5])
        try:
            row_for_flight[3] = row_for_flight[3].replace('/', ' - ')
        except: pass
        try:
            row_for_flight[5] = row_for_flight[5].replace('/', ' - ')
        except: pass
        content_for_df.append(row_for_flight)





    return content_for_df

def create_df_for_flights(df_schema, df_content):
    df_flights = pd.DataFrame(columns = df_schema, data = df_content)

    return df_flights


if __name__ == "__main__":
    api_link =  'https://api.aviationstack.com/v1/flights'

    params = {
    'access_key':       '6534382cfa07b54707a8b20a4d912d60',
    'limit':            100,
    'flight_status':    'active'
    }

    content_for_df = take_data_from_api (api_link, params)

    df_columns = ['flight_date', 'flight_status','departure_airport', 'departure_timezone','arrival_airport','arrival_timezone','arrival_terminal','ariline_name','flight_number']

    df_flights = create_df_for_flights(df_columns, content_for_df)
