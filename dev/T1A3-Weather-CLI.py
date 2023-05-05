import requests
import os 
import json 
from datetime import datetime, timedelta, date

api_key_wapi_caleb = "3328658fef7c4737a1635629232204"

# Ui functions
# --------------------------
# This function will call the apropriate print functions to display the right info to the user
def print_ui(selected_city, current_weather_response, forecast_response, history_response, menu_option,):
    # clears the commandline to keep ui clean
    os.system('cls' if os.name == 'nt' else 'clear')
        
    print_menu(selected_city)
    if menu_option == '1':
        print_current_weather(current_weather_response)
    
    if menu_option == '2':
        print_forecast(forecast_response)
    
    if menu_option == '3':
        print_history(history_response, selected_city)
    
    if menu_option == '4':
        print_export_options(selected_city)
    print('')

def print_menu(selected_city,):
    print("================================================")
    print("---Welcome to T1A3 Weather CLI---")
    print("[s] Select City ")
    print("[1] Get current weather            for Selected City ")
    print("[2] Display current day forecast   for Selected City ")
    print("[3] **Get Weather History for last 7 days")
    print("[4] Export data options")
    print("[q] Quit Program")
    print(f"Selected City: ", {selected_city})
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
    print("---Export Sub Menu---")
    print("NOTE Currently Data is exported as .JSON")
    print("[s] Select City ")
    print("[1] Export 24 HR forecast                   .JSON")
    print("[2] Export Weather History for last 7 days  .JSON")
    print("[3] Export Current Weather                  .JSON")
    print("[0] Return to main menu")
    print("[q] Quit Program")
    print(f"Selected City: ", {selected_city})
    
# main function asks for an inital city then uses a loop to render the ui and give the user options untill they exit
# --------------------------
def main():
    # set as brisbane to expidite testing
    selected_city             = "Brisbane"
    current_weather_response  = None
    forecast_response         = None 
    menu_option               = None 
    export_option             = None
    history_response          = None

    # info = None
    print_ui(selected_city, current_weather_response, forecast_response, history_response, menu_option,)
    
    if selected_city == None:
        print("")
        print("No City selected")
        selected_city = input("Give City Name: ")
    if selected_city == "q":
         return

    while True:
        print_ui(selected_city, current_weather_response, forecast_response, history_response, menu_option,)
        menu_option= input("Enter option number here: ")
        match menu_option:
            # calls a function to alow the user to select a new city 
            case "s":
                selected_city = select_new_city()
                if selected_city == 'q':
                    return
                continue
            case '1':
                current_weather_response = get_current_weather_wapi(selected_city)
                # writing for dev testing
                write_response(current_weather_response)
                continue
            case '2':
                forecast_response = get_forecast_wapi(selected_city)
                # writing for dev testing
                write_response(forecast_response)
            case '3':
                history_response = get_history_wapi(selected_city)
                # writing for dev testing
                write_response(history_response)
                continue
            case '4':
                while export_option != '0':
                    print_ui(selected_city, current_weather_response, forecast_response, history_response, menu_option,)
                    export_option = input("Enter option number here: ")
                    match export_option:
                        case 's':
                            selected_city = select_new_city()
                        # Export forecast
                        case '1':
                            export_response(selected_city, "forecast")
                            continue
                        # Export historical data
                        case '2':
                            export_response(selected_city, "history")
                            continue
                        # Export current weather data
                        case '3':
                            export_response(selected_city, "current weather")
                            continue
                        case 'q':
                            return
                export_option = None
                menu_option   = None
                
            case "q":
                return
            # case 3:
            

    
# get functions
# ------------------------------
def get_current_weather_wapi(selected_city):
    current_weather_response = requests.get(f"http://api.weatherapi.com/v1/current.json?q={selected_city}&key={api_key_wapi_caleb}")
    return current_weather_response

def get_forecast_wapi(selected_city):
    forecast_response = requests.get(f"http://api.weatherapi.com/v1/forecast.json?q={selected_city}&key={api_key_wapi_caleb}")
    return forecast_response
# Note need to to have an input parameter currently uses chosen date as placholder 
def get_history_wapi(selected_city):
    # input("give : ?")
        
    today  = date.today()
    # dt is the past to start the histoy request 
    dt     = today - timedelta(days=7)
    # end_dt is a date in the futre ahead of dt
    end_dt = today - timedelta(days=1)
    
    forecast_response = requests.get(f"http://api.weatherapi.com/v1/history.json?q={selected_city}&key={api_key_wapi_caleb}&dt={dt}&end_dt={end_dt}")
    return forecast_response

# other functions
# -------------------------------
def check_loc_valid(selected_city):
        loc_check = requests.get(f"http://api.weatherapi.com/v1/current.json?q={selected_city}&key={api_key_wapi_caleb}")
        write_response(loc_check)
        try:
            loc_check.json()['error']
        except:
            return True

        return False

def select_new_city():
    while True:
        print('')
        new_city      = input("Give New City Name: ")
        city_is_valid = check_loc_valid(new_city)

        if new_city == "q":
            selected_city = new_city
            return selected_city
        elif city_is_valid:
            selected_city = new_city
            return selected_city
        else:
            error_text = f"City name '{new_city}' is invalid. Please try again."
            print(error_text)           

def export_response(selected_city, call_type):
    time_now = datetime.now()
    time_stamp = time_now.strftime('%Y-%m-%d %H:%M:%S')
    
    if   call_type == "forecast":
        export = get_forecast_wapi(selected_city)
    elif call_type == "history":
        export = get_history_wapi(selected_city)
    elif call_type == "current weather":
        export = get_current_weather_wapi(selected_city)
    
    export = json.dumps(export.json(), indent=5)
    
    with open(f'EXPORTS/{selected_city}_{call_type}_export_{time_stamp}.json', 'w') as file:
        file.write(export)

    
# testing fuunction for development
def write_response(response):
    response = json.dumps(response.json(), indent=5)
    file = open('EXPORTS/rqsts.json', 'a')
    file.write(response)
    file.close()

main()

print('thanks for using T1A3 Weather CLI')
print('PROGRAM EXIT')