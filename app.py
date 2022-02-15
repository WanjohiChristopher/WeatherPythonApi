import requests
from flask import Flask, request

app = Flask(__name__)


@app.route('/city')
def search_city():
    API_KEY = '1e5c8dadaa4cb2c4bf47e3638a57e0c9'# initialize your key here
    city = request.args.get('juja')  # city name passed as argument

    # call API and convert response into Python dictionary
    url =f' https://api.openweathermap.org/data/2.5/onecall?lat=-1.102554&lon=37.0144&exclude=minutely&appid={API_KEY}'
    response = requests.get(url).json()
       # extract data from dictionary
    # temp = response['current']['temp']

    # temp = temp - 273.15
    # temp = round(temp, 2)
    # temp = str(temp)
    # temp = temp + '°C'

    # error like unknown city name, inavalid api key
    if response.get('cod') != 200:
        message = response.get('message', '')
        return f'Error getting temperature for {city.title()}. Error message = {message}'

    # get current temperature and convert it into Celsius
    current_temperature = response.get('main', {}).get('temp')
    if current_temperature:
        current_temperature_celsius = round(current_temperature - 273.15, 2)
        return f'Current temperature of {city.title()} is {current_temperature_celsius} &#8451;'
    else:
        return f'Error getting temperature for {city.title()}'


@app.route('/')
def index():
    return '<h1>Welcome to weather app</h1>'


if __name__ == '__main__':
    app.run(debug=True)