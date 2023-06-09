import requests
import os 
import json 
from datetime import datetime, timedelta, date

api_key_wapi_caleb = "3328658fef7c4737a1635629232204"

# Ui functions
# --------------------------
def print_ui(selected_city, current_weather_response, forecast_response, history_response, menu_option):
    """
    The function `print_ui` takes in various API responses and a menu option, and prints out the
    corresponding weather information or error message based on the selected menu option.
    
    :param selected_city: 
        The name of the city that the user has selected
    :param current_weather_response: 
        The response object containing the current weather data for aselected city
    :param forecast_response: 
        The forecast_response parameter is a response object returned by an API
        call that contains the forecast weather data for a selected city. It is used in the print_forecast
        function to display the forecasted weather information for the selected city
    :param history_response: 
        The response object containing the weather history data for a selected city
    :param menu_option: 
        A string representing the user's selected option from the main menu
    """
    # clears the commandline to keep ui clean
    os.system('cls' if os.name == 'nt' else 'clear')
        
    print_menu(selected_city)
    if menu_option == '1' and current_weather_response is not None:
        print_current_weather(current_weather_response)
    
    elif menu_option == '2' and forecast_response is not None:
        print_forecast(forecast_response)
    
    elif menu_option == '3' and history_response is not None:
        print_history(history_response, selected_city)
    
    elif menu_option == '4':
        print_export_options(selected_city)
    
# error handling for invalid inputs in the main menu 
    elif menu_option not in {'s', '1', '2', '3', '4', 'q', None}:
        print(f"menu option '{menu_option}' invalid try again")
    print('')

def print_menu(selected_city,):
    print("================================================")
    print("---Welcome to T1A3 Weather CLI---")
    print("[s] Select City ")
    print("[1] Display Current weather        for Selected City")
    print("[2] Display Current day forecast   for Selected City")
    print("[3] Display 7 day Weather History  for Selected City")
    print("[4] Export data options")
    print("[q] Quit Program")
    print(f"Selected City is: ", {selected_city})
    print("================================================")

    
def print_current_weather(current_weather_response):
    print("Current weather for:   ",current_weather_response.json()['location']['name'],)
    print('last_updated          =',current_weather_response.json()['current']['last_updated'])
    print('localtime             =',current_weather_response.json()['location']['localtime'])
    print('current condition     =',current_weather_response.json()['current']['condition']['text'])
    print('')
    print('Temps')
    print('temp c                =' , current_weather_response.json()['current']['temp_c'])
    print('feelslike c           =' , current_weather_response.json()['current']['feelslike_c'])
    print('')
    print('Precipitation')
    print('precip mm             =' , current_weather_response.json()['current']['precip_mm'])
    print('humidity              =' , current_weather_response.json()['current']['humidity'])
    print('cloud                 =' , current_weather_response.json()['current']['cloud'])
    print('pressure_mb           =' , current_weather_response.json()['current']['pressure_mb'])
    print('')
    print('Visability')
    print('vis km                =' , current_weather_response.json()['current']['vis_km'])
    print('')
    print('Wind')
    print('wind kph              =' , current_weather_response.json()['current']['wind_kph'])
    print('gust kph              =' , current_weather_response.json()['current']['gust_kph'])
    print('wind dir              =' , current_weather_response.json()['current']['wind_dir'])
    print('wind degree           =' , current_weather_response.json()['current']['wind_degree'])
    print("-----------------------------------------------")

def print_forecast(forecast_response):
    print('Forecast for:         =' , forecast_response.json()['location']['name'])
    print('date                  =' , forecast_response.json()['forecast']['forecastday'][0]['date'])
    print('condition             =' , forecast_response.json()['forecast']['forecastday'][0]['day']['condition']['text'])
    print('maxtemp_c             =' , forecast_response.json()['forecast']['forecastday'][0]['day']['maxtemp_c'])
    print('mintemp_c             =' , forecast_response.json()['forecast']['forecastday'][0]['day']['mintemp_c'])
    print('avgtemp_c             =' , forecast_response.json()['forecast']['forecastday'][0]['day']['avgtemp_c'])
    print('chance_of_rain        =' , forecast_response.json()['forecast']['forecastday'][0]['day']['daily_chance_of_rain'])
    print('chance_of_snow        =' , forecast_response.json()['forecast']['forecastday'][0]['day']['daily_chance_of_snow'])
    print('avghumidity           =' , forecast_response.json()['forecast']['forecastday'][0]['day']['avghumidity'])
    print("-----------------------------------------------")

# figured out using this loop last, its a better solution to displaying more data without haiving to write it manunaly but dont have time to redo previous print functions
def print_history(history_response, selected_city):
    history_response = history_response.json()
    print(f'Last 7 day history for {selected_city}')
    for day in history_response["forecast"]["forecastday"]:
        print("Date:", day["date"])
        print("condition             =", day["day"]["condition"]["text"])
        print("maxtemp_c             =", day["day"]["maxtemp_c"])
        print("mintemp_c             =", day["day"]["mintemp_c"])
        print("avgtemp_c             =", day["day"]["avgtemp_c"])
        print("totalprecip_mm        =", day["day"]["totalprecip_mm"])
        print("uv                    =", day["day"]["uv"])
        print("avghumidity           =", day["day"]["avghumidity"])
        print()
    
def print_export_options(selected_city):
    print("    ---Export Sub Menu---")
    print("    NOTE Currently Data is exported as .JSON")
    print("    for each export you request a new file will be created ")
    print("    in the export folder with the apropriate name and date time stamp")
    print("    [s] Select City ")
    print("    [1] Export Current Weather                  .JSON")
    print("    [2] Export 24 HR forecast                   .JSON")
    print("    [3] Export Weather History for last 7 days  .JSON")
    print("    [0] Return to main menu")
    print("    [q] Quit Program")
    print(f"Selected City: ", {selected_city})
    
# main function asks for an inital city then uses a loop to render the ui and call the options for the user untill they exit
    """
    The main function allows the user to select a city and then presents a menu of options to retrieve
    and export weather data.
    
    :return: 
        The main function does not return any value. It uses the `return` statement to exit the
        function and terminate the program when the user selects the "q" option.
    """
# --------------------------
def main():
    # set as brisbane to expidite testing
    selected_city             = None
    current_weather_response  = None
    forecast_response         = None 
    menu_option               = None 
    export_option             = None
    history_response          = None

    print_ui(selected_city, current_weather_response, forecast_response, history_response, menu_option)
    
    if selected_city == None:
        print("")
        print("No City selected")
        selected_city = select_new_city()
        if selected_city == 'q':
            return

    while True:
        print_ui(selected_city, current_weather_response, forecast_response, history_response, menu_option)
        menu_option= input("Enter option number here: ")
        match menu_option:
            # calls a function to alow the user to select a new city 
            case "s":
                print_ui(selected_city, current_weather_response, forecast_response, history_response, menu_option)
                selected_city = select_new_city()
                if selected_city == 'q':
                    return
                continue
            case '1':
                current_weather_response = get_current_weather_wapi(selected_city)
                # writing used for testing
                # write_response(current_weather_response)
                continue
            case '2':
                forecast_response = get_forecast_wapi(selected_city)
                # writing used for testing
                # write_response(forecast_response)
            case '3':
                history_response = get_history_wapi(selected_city)
                # writing used for testing
                # write_response(history_response)
                continue
            case '4':
                # this loop handles the sub menu functionality it is ordered differntly then the main loop 
                # to facilitate the printing of sucess messages for export functions
                while export_option != '0':
                    success_message = None

                    match export_option:
                        case 's':
                            print_ui(selected_city, current_weather_response, forecast_response, history_response, menu_option)
                            selected_city = select_new_city()
                            if selected_city == 'q':
                                return
                        # Export current weather data
                        case '1':
                            success_message = export_response(selected_city, "current weather")
                        # Export forecast
                        case '2':
                            success_message = export_response(selected_city, "forecast")
                        # Export historical data
                        case '3':
                            success_message = export_response(selected_city, "history")
                        case 'q':
                            return

                    print_ui(selected_city, current_weather_response, forecast_response, history_response, menu_option)

                    if success_message:
                        print(success_message)

                    if export_option not in {'s', '1', '2', '3', 'q', '0', None}:
                        print(f"export option '{export_option}' invalid try again")

                    export_option = input("Enter export option number here: ")
                # resets options to keep UI clean and avoid unintended behaviour
                export_option = None
                menu_option   = None    
            
            case "q":
                return

    
# get functions
"""
These are Python functions that use the WeatherAPI to retrieve current weather, forecast, and
historical weather data for a selected city.

:param selected_city: 
    The name of the city for which weather data is being requested
:return: 
    The `get_current_weather_wapi`, `get_forecast_wapi`, and `get_history_wapi` functions are
    returning the responses from API requests made to the WeatherAPI service for the current weather,
    forecast, and historical weather data for a selected city. If there is an error with the request,
    the functions allert the user and return `None`.
"""

# ------------------------------
def get_current_weather_wapi(selected_city):
    try:
        current_weather_response = requests.get(f"http://api.weatherapi.com/v1/current.json?q={selected_city}&key={api_key_wapi_caleb}")
        current_weather_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print()
        print(f"Error: {e}")
        print()
        input('press enter to continue: ')
        return None
    return current_weather_response

def get_forecast_wapi(selected_city):
    try:
        forecast_response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?q={selected_city}&key={api_key_wapi_caleb}")
        forecast_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print()
        print(f"Error: {e}")
        print()
        input('press enter to continue: ')
        return None
    return forecast_response

# Currently get the full 7 day history from todays date 
def get_history_wapi(selected_city):
    try:
        today  = date.today()
        dt     = today - timedelta(days=7)
        end_dt = today - timedelta(days=1)
    
        forecast_response = requests.get(f"http://api.weatherapi.com/v1/history.json?q={selected_city}&key={api_key_wapi_caleb}&dt={dt}&end_dt={end_dt}")
        forecast_response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print()
        print(f"Error: {e}")
        print()
        input('press enter to continue: ')
        return None
    return forecast_response

# other functions
"""
The function `select_new_city()` 
    prompts the user to input a new city name and checks if it is valid
    using the `check_loc_valid()` function.
:return: 
    The function `select_new_city()` returns the selected city name entered by the user or "q"
    if the user chooses to quit. The function `check_loc_valid(new_city)` returns a tuple containing a
    boolean value indicating whether the city name is valid and a string error message if the city name
    is invalid.
"""
# -------------------------------
def select_new_city():
    while True:
        print('')
        new_city = input("Give New City Name: ")
        city_is_valid, error_msg = check_loc_valid(new_city)
        
        if new_city == "q":
            selected_city = new_city
            return selected_city

        elif city_is_valid:
            selected_city = new_city
            return selected_city        
                       
import requests.exceptions

def check_loc_valid(new_city):
    try:
        if new_city == 'q':
            return True, ""
        loc_check = requests.get(f"http://api.weatherapi.com/v1/current.json?q={new_city}&key={api_key_wapi_caleb}")
        loc_check.raise_for_status()
    except requests.exceptions.RequestException as e:
        if isinstance(e, requests.exceptions.ConnectionError):
            error_msg = "Error: Unable to connect to the API. Please check your internet connection."
        else:
            error_msg = f"    Error: City name '{new_city}' is invalid."
        print()
        print(error_msg)
        print()
        input('    Press enter to try again: ')
        return False, error_msg

    if loc_check is None:
        error_msg = "Error: API is unavailable."
        print()
        print(error_msg)
        print()
        input('Press enter to continue: ')
        return False, error_msg

    return True, ""


# exports the data as a .json file
"""
This function exports weather data for a selected city and call type as a JSON file with a
timestamped filename.

:param selected_city: 
    The name of the city for which the weather data is being fetched and exported
:param call_type:
    The type of weather data to retrieve, which can be "forecast", "history", or
    "current weather"
:return: 
    a string indicating whether the export was successful or not, and the path to the exported
    file. If there was an error fetching the data, the function returns an error message.
"""
def export_response(selected_city, call_type):
    time_now = datetime.now()
    time_stamp = time_now.strftime('%Y-%m-%d %H:%M:%S')

    if call_type == "forecast":
        export = get_forecast_wapi(selected_city)
    elif call_type == "history":
        export = get_history_wapi(selected_city)
    elif call_type == "current weather":
        export = get_current_weather_wapi(selected_city)

    if export is None:
        return f"Error: Failed to fetch {call_type} data for {selected_city}."

    os.makedirs('EXPORTS', exist_ok=True)
    export_data = json.dumps(export.json(), indent=5)

    with open(f'EXPORTS/{selected_city}_{call_type}_export_{time_stamp}.json', 'w') as file:
        file.write(export_data)
    return f'Successful export: EXPORTS/{selected_city}_{call_type}_export_{time_stamp}.json'


# write_response() is a testing function i used during development to write responses to a file so i could see what the api is returning
"""    
The bellow code defines a function called `write_response` that takes in a `response` object as an
argument. The function checks if the response status code is 200 and if the response text is not
empty. If both conditions are met, the response is converted to a JSON string with indentation and
written to a file called `rqsts.json` in the `EXPORTS` directory. If the response status code is not
200 or the response text is empty, a `ValueError` is raised. If there is an error decoding the
response JSON, a `JSONDecodeError` is caught
"""
def write_response(response):
    try:
        if response.status_code == 200 and response.text:
            response = json.dumps(response.json(), indent=5)
            file = open('EXPORTS/rqsts.json', 'a')
            file.write(response)
            file.close()
        else:
            raise ValueError('Invalid or empty response')
    except (ValueError, requests.exceptions.JSONDecodeError) as e:
        print(f"Error: {e}")
        response = None

    return response

main()

print('thanks for using T1A3 Weather CLI')
print('PROGRAM EXIT')