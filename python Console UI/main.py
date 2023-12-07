import pyowm as owm

#TODO get detailed weather and forecast data
#TODO format data so it can be easily displayed
#TODO add some funzies ([something] of the day)
#TODO create a UI to display the data

owm = owm.OWM('3b360282851d2cfea5bc3c02272b83c9')
mgr = owm.weather_manager()

place = 'Amersfoort'


def get_weather(city):
    observation = mgr.weather_at_place(city)
    w = observation.weather
    return w


def main():
    weather = mgr.weather_at_place(place)
    forecast = mgr.forecast_at_place(place, '3h').forecast
    
    print(weather)
    print(forecast)


main()
