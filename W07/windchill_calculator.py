temperature = float(input('What is the temperature? '));
temperatureType = input('Fahrenheit or Celsius (F/C)? ');
wind_speed = 5;

def wind_chill(t, v):
    return round(35.74 + 0.6215 * t - 35.75 * (v ** 0.16) + 0.4275 * t * ( v ** 0.16), 2);

def convert_celsius(temperatureCelsius):
    return temperatureCelsius * (9/5) + 32;

if temperatureType.lower() == 'c':
    temperature = convert_celsius(temperature);

while wind_speed <= 60:
    windchill = wind_chill(temperature, wind_speed);
    print(f'At temperature {temperature}F, and wind speed {wind_speed} mph, the windchill is: {windchill}F');
    wind_speed += 5;