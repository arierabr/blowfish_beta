import pandas as pd
import requests
import json

def searcher(json):
    # Create a dictionary to hold query parameters:

    params_1 = {
        'fly_from': json["Origin"][1],
        'date_from': json["Departure_d"][1],
        'date_to': json["Arrivals_d"][1],
        'dtime_from': json["Departures_h"][1],
        'dtime_to': "23:00",
        'return_from': json["Origin"][1],
        'return_to': json["Arrivals_h"][1],
        'ret_atime_from': "06:00",
        'ret_atime_to': json["Arrivals_h"][1],
        'adults': json["Travelers"][1],
        'max_stopovers': json["Origin"][1],
        'one_for_city': 1,
        'ret_from_diff_city': False,
        'ret_to_diff_city': False
    }
    params_2 = {
        'fly_from': json["Origin"][2],
        'date_from': json["Departure_d"][2],
        'date_to': json["Departure_d"][2],
        'dtime_from': json["Departures_h"][2],
        'dtime_to': "23:59",
        'return_from': json["Arrivals_d"][2],
        'return_to': json["Arrivals_d"][2],
        'ret_atime_from': "00:00",
        'ret_atime_to': json["Arrivals_h"][2],
        'adults': json["Travelers"][2],
        'max_stopovers': json["Origin"][2],
        'one_for_city': 1,
        'ret_from_diff_city': False,
        'ret_to_diff_city': False
    }

    #Datos de la Query SEARCH:

    apikey = '_4bJhttcKD-fn5fGrE7XFN61WJc05rbr'
    base_url = 'https://api.tequila.kiwi.com/v2'
    endpoint_search = 'search'
    headers = {'apikey':apikey}

    # Resultados de cada Query:

    response_1 = requests.get(f'{base_url}/{endpoint_search}', params=params_1, headers=headers)
    if response_1.status_code == 200:
        data_1 = json.loads(response_1.text)

    response_2 = requests.get(f'{base_url}/{endpoint_search}', params=params_2, headers=headers)
    if response_2.status_code == 200:
        data_2 = json.loads(response_2.text)

    #Ajustamos el type de fechas para que coincida el formato:

    from datetime import datetime

     #Origin_1_from
    original_date_string = f"{json['Departure_d'][1]}T{json['Departures_h'][1]}:00.00Z"
    original_datetime = datetime.strptime(original_date_string, "%d/%m/%YT%H:%M:%S.%fZ")
    new_date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    time_from_1 = original_datetime.strftime(new_date_format)

     #Origin_1_to
    original_date_string = f"{json['Arrivals_d'][1]}T{json['Arrivals_h'][1]}:00.00Z"
    original_datetime = datetime.strptime(original_date_string, "%d/%m/%YT%H:%M:%S.%fZ")
    new_date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    time_to_1 = original_datetime.strftime(new_date_format)

     #Origin_2_from
    original_date_string = f"{json['Departure_d'][2]}T{json['Departures_h'][2]}:00.00Z"
    original_datetime = datetime.strptime(original_date_string, "%d/%m/%YT%H:%M:%S.%fZ")
    new_date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    time_from_2 = original_datetime.strftime(new_date_format)

     #Origin_2_to
    original_date_string = f"{json['Arrivals_d'][2]}T{json['Arrivals_h'][2]}:00.00Z"
    original_datetime = datetime.strptime(original_date_string, "%d/%m/%YT%H:%M:%S.%fZ")
    new_date_format = "%Y-%m-%dT%H:%M:%S.%fZ"
    time_to_2 = original_datetime.strftime(new_date_format)

    # AÑADIMOS un vuelo nulo con el mismo destino que el origen para cada respuesta.
    data_1['data'].append({"id": "null", "flyFrom": f"{json['Origin'][1]}", "flyTo": f"{json['Origin'][1]}", "cityFrom": f"{json['Origin'][1]}",
                           "cityCodeFrom": f"{json['Origin'][1]}", "cityTo": f"{json['Origin'][1]}", "cityCodeTo": f"{json['Origin'][1]}",
                           "countryFrom": {"code": "null", "name": "null"},
                           "countryTo": {"code": "null", "name": "null"}, "local_departure": time_from_1,
                           "utc_departure": time_from_1, "local_arrival": time_from_1, "utc_arrival": time_from_1,
                           "nightsInDest": 9999, "quality": 9999, "distance": 0,
                           "duration": {"departure": 0, "return": 0, "total": 0}, "price": 0, "conversion": {"EUR": 0},
                           "fare": {"adults": 0, "children": 0, "infants": 0},
                           "price_dropdown": {"base_fare": 0, "fees": 0}, "bags_price": {"1": 0, "2": 0},
                           "baglimit": {"hand_height": 999, "hand_length": 999, "hand_weight": 999, "hand_width": 999,
                                        "hold_dimensions_sum": 999, "hold_height": 999, "hold_length": 999,
                                        "hold_weight": 999, "hold_width": 999, "personal_item_height": 999,
                                        "personal_item_length": 999, "personal_item_weight": 999,
                                        "personal_item_width": 999}, "availability": {"seats": 9999},
                           "airlines": ["null"], "route": [
            {"id": "null", "combination_id": "null", "flyFrom": f"{json['Origin'][1]}", "flyTo": f"{json['Origin'][1]}",
             "cityFrom": f"{json['Origin'][1]}", "cityCodeFrom": f"{json['Origin'][1]}", "cityTo": f"{json['Origin'][1]}",
             "cityCodeTo": f"{json['Origin'][1]}", "local_departure": time_from_1, "utc_departure": time_from_1,
             "local_arrival": time_from_1, "utc_arrival": time_from_1, "airline": "N/A", "flight_no": 999,
             "operating_carrier": "null", "operating_flight_no": "999", "fare_basis": "null", "fare_category": "M",
             "fare_classes": "", "return": 0, "bags_recheck_required": False, "vi_connection": False,
             "guarantee": False, "equipment": 'null', "vehicle_type": "aircraft"},
            {"id": "null", "combination_id": "null", "flyFrom": f"{json['Origin'][1]}", "flyTo": f"{json['Origin'][1]}",
             "cityFrom": f"{json['Origin'][1]}", "cityCodeFrom": f"{json['Origin'][1]}", "cityTo": f"{json['Origin'][1]}",
             "cityCodeTo": f"{json['Origin'][1]}", "local_departure": time_to_1, "utc_departure": time_to_1,
             "local_arrival": time_to_1, "utc_arrival": time_to_1, "airline": "null", "flight_no": 999,
             "operating_carrier": "null", "operating_flight_no": "null", "fare_basis": "null", "fare_category": "null",
             "fare_classes": "", "return": 1, "bags_recheck_required": False, "vi_connection": False,
             "guarantee": False, "equipment": 'null', "vehicle_type": "null"}], "booking_token": "null",
                           "facilitated_booking_available": True, "pnr_count": 2, "has_airport_change": False,
                           "technical_stops": 0, "throw_away_ticketing": False, "hidden_city_ticketing": False,
                           "virtual_interlining": False})
    data_2['data'].append({"id": "null", "flyFrom": f"{json['Origin'][2]}", "flyTo": f"{json['Origin'][2]}", "cityFrom": f"{json['Origin'][2]}",
                           "cityCodeFrom": f"{json['Origin'][2]}", "cityTo": f"{json['Origin'][2]}", "cityCodeTo": f"{json['Origin'][2]}",
                           "countryFrom": {"code": "null", "name": "null"},
                           "countryTo": {"code": "null", "name": "null"}, "local_departure": time_from_2,
                           "utc_departure": time_from_2, "local_arrival": time_from_2, "utc_arrival": time_from_2,
                           "nightsInDest": 9999, "quality": 9999, "distance": 0,
                           "duration": {"departure": 0, "return": 0, "total": 0}, "price": 0, "conversion": {"EUR": 0},
                           "fare": {"adults": 0, "children": 0, "infants": 0},
                           "price_dropdown": {"base_fare": 0, "fees": 0}, "bags_price": {"1": 0, "2": 0},
                           "baglimit": {"hand_height": 999, "hand_length": 999, "hand_weight": 999, "hand_width": 999,
                                        "hold_dimensions_sum": 999, "hold_height": 999, "hold_length": 999,
                                        "hold_weight": 999, "hold_width": 999, "personal_item_height": 999,
                                        "personal_item_length": 999, "personal_item_weight": 999,
                                        "personal_item_width": 999}, "availability": {"seats": 9999},
                           "airlines": ["null"], "route": [
            {"id": "null", "combination_id": "null", "flyFrom": f"{json['Origin'][2]}", "flyTo": f"{json['Origin'][2]}",
             "cityFrom": f"{json['Origin'][2]}", "cityCodeFrom": f"{json['Origin'][2]}", "cityTo": f"{json['Origin'][2]}",
             "cityCodeTo": f"{json['Origin'][2]}", "local_departure": time_from_2, "utc_departure": time_from_2,
             "local_arrival": time_from_2, "utc_arrival": time_from_2, "airline": "N/A", "flight_no": 999,
             "operating_carrier": "null", "operating_flight_no": "999", "fare_basis": "null", "fare_category": "M",
             "fare_classes": "", "return": 0, "bags_recheck_required": False, "vi_connection": False,
             "guarantee": False, "equipment": 'null', "vehicle_type": "aircraft"},
            {"id": "null", "combination_id": "null", "flyFrom": f"{json['Origin'][2]}", "flyTo": f"{json['Origin'][2]}",
             "cityFrom": f"{json['Origin'][2]}", "cityCodeFrom": f"{json['Origin'][2]}", "cityTo": f"{json['Origin'][2]}",
             "cityCodeTo": f"{json['Origin'][2]}", "local_departure": time_to_2, "utc_departure": time_to_2,
             "local_arrival": time_to_2, "utc_arrival": time_to_2, "airline": "null", "flight_no": 999,
             "operating_carrier": "null", "operating_flight_no": "null", "fare_basis": "null", "fare_category": "null",
             "fare_classes": "", "return": 1, "bags_recheck_required": False, "vi_connection": False,
             "guarantee": False, "equipment": 'null', "vehicle_type": "null"}], "booking_token": "null",
                           "facilitated_booking_available": True, "pnr_count": 2, "has_airport_change": False,
                           "technical_stops": 0, "throw_away_ticketing": False, "hidden_city_ticketing": False,
                           "virtual_interlining": False})

    # Step 1: Create a list with all possible destination.

    destinos_1 = []
    destinos_2 = []


    for objeto in range(len(data_1['data'])):
        if data_1['data'][objeto]['availability']['seats'] is not None:
            if data_1['data'][objeto]['availability']['seats'] >= json["Travelers"][1]:
                if data_1['data'][objeto]['flyTo'] not in destinos_1:
                    destinos_1.append(data_1['data'][objeto]['flyTo'])

    for objeto in range(len(data_2['data'])):
        if data_2['data'][objeto]['availability']['seats'] is not None:
            if data_2['data'][objeto]['availability']['seats'] >= json["Travelers"][2]:
                if data_2['data'][objeto]['flyTo'] not in destinos_2:
                    destinos_2.append(data_2['data'][objeto]['flyTo'])
    possible = list(set(destinos_1) & set(destinos_2))

    # Step 2: Take all the flights flying to a common destination

    flights = []

    for objeto in range(len(data_1['data'])):
        if data_1['data'][objeto]['flyTo'] in possible:
            flights.append(data_1['data'][objeto])

    for objeto in range(len(data_2['data'])):
        if data_2['data'][objeto]['flyTo'] in possible:
            flights.append(data_2['data'][objeto])

    results = []
    n_max = len(flights)
    n = 0

    while n < n_max:

        # 1. Destino:
        destination = flights[n]['cityTo']

        # 2. Calculo del precio total, precio por viajero y el tiempo de vuelo medio por viajero

        total_passengers = json["Travelers"][1] + json["Travelers"][2]
        total_price = flights[n]['price'] + flights[n + 1]['price']
        price_per_person = (flights[n]['price'] + flights[n + 1]['price']) / total_passengers
        avg_flying_time = (flights[n]['duration']['total'] + flights[n + 1]['duration']['total']) / 2

        # 3. Calculo del tiempo compartido

        for e in range(len(flights[n]['route'])):
            if flights[n]['route'][e]['return'] == 1:
                time_B1 = datetime.strptime(flights[n]['route'][e]['utc_departure'], "%Y-%m-%dT%H:%M:%S.%fZ")
                time_A1 = datetime.strptime(flights[n]['utc_arrival'], "%Y-%m-%dT%H:%M:%S.%fZ")
                break

        for e in range(len(flights[n + 1]['route'])):
            if flights[n + 1]['route'][e]['return'] == 1:
                time_B2 = datetime.strptime(flights[n + 1]['route'][e]['utc_departure'], "%Y-%m-%dT%H:%M:%S.%fZ")
                time_A2 = datetime.strptime(flights[n + 1]['utc_arrival'], "%Y-%m-%dT%H:%M:%S.%fZ")
                break
        time_together = min(time_B1, time_B2) - max(time_A1, time_A2)

        # 4. Formula Pepe:

        available_time_to_1 = datetime.strptime(time_to_1, "%Y-%m-%dT%H:%M:%S.%fZ")
        available_time_from_1 = datetime.strptime(time_from_1, "%Y-%m-%dT%H:%M:%S.%fZ")

        available_time_to_2 = datetime.strptime(time_to_2, "%Y-%m-%dT%H:%M:%S.%fZ")
        available_time_from_2 = datetime.strptime(time_from_2, "%Y-%m-%dT%H:%M:%S.%fZ")
        minimum_available_time = min(available_time_to_1, available_time_to_2) - max(available_time_from_1, available_time_from_2)
        option = {'Destination': destination,
                  'Total Price': total_price,
                  'Price per person': price_per_person,
                  'time_together': time_together,
                  'avg_flying_time': avg_flying_time}

        results.append(option)
        n = n + 2
    results = sorted(results, key=lambda x: x['Total Price'], reverse=False)

    df = pd.DataFrame(results)
    return df


