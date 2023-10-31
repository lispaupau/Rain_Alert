import requests
from twilio.rest import Client

api_key = 'c76961f6ac612cc2726bd32c05f75157'
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
lat = 'enter your lat'
lon = 'enter your lon'

parameters = {
    'lat': lat,
    'lon': lon,
    'appid': api_key,
    'exclude': 'current,minutely,daily'
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()['hourly']

will_rain = False

for i in range(0, 12):
    if weather_data[i]['weather'][0]['id'] <= 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(body='It`s going to rain today. Remember to bring an umbrella.',
                                     from_='from_number',
                                     to='Your verified number')
