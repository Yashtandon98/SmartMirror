from weather import Weather, Unit

def loc_name():
    print('\n')
    name = input("Enter name of the locaton: ")
    print('\n')
    print('Please select the unit - ')
    print('1. CELSIUS')
    print('2. FAHRENHEIT')
    ch = input()
    if ch == '1' or ch == 'c' or ch == celsius:
        weather = Weather(unit = Unit.CELSIUS)
        location = weather.lookup_by_location(name)
        condition = location.condition
        print('\n')
        print('Current Weather :')
        print("         " + condition.text)
        print('\n')
        print('Forecasts :')
        forecasts = location.forecast
        for forecast in forecasts:
            print("         " + forecast.text)
            print("         " + forecast.date)
            print("         " + forecast.high)
            print("         " + forecast.low)
    elif ch == '2' or ch == 'f' or ch == fahrenheit:
        weather = Weather(unit = Unit.FAHRENHEIT)
        location = weather.lookup_by_location(name)
        condition = location.condition
        print('\n')
        print('Current Weather :')
        print("         " + condition.text)
        print('\n')
        print('Forecasts :')
        forecasts = location.forecast
        for forecast in forecasts:
            print("         " + forecast.text)
            print("         " + forecast.date)
            print("         " + forecast.high)
            print("         " + forecast.low)
def latnlong():
    print('\n')
    print('Please select the unit - ')
    print('1. CELSIUS')
    print('2. FAHRENHEIT')
    ch = input()
    if ch == '1' or ch == 'c' or ch == celsius:
        print('\n')
        lat = input('Please enter the latitude')
        long = input('Please enter the longitude')
        print('\n')
        weather = Weather(unit = Unit.CELSIUS)
        lookup = w.lookup_by_latlng(lat,long)
        condition = lookup.condition
        print('\n')
        print('Current Weather :')
        print("         " + condition.text)
        print('\n')
        print('Forecasts :')
        forecasts = location.forecast
        for forecast in forecasts:
            print("         " + forecast.text)
            print("         " + forecast.date)
            print("         " + forecast.high)
            print("         " + forecast.low)
    elif ch == '2' or ch == 'f' or ch == fahrenheit:
        print('\n')
        lat = input('Please enter the latitude')
        long = input('Please enter the longitude')
        print('\n')
        weather = Weather(unit = Unit.FAHRENHEIT)
        lookup = w.lookup_by_latlng(lat,long)
        condition = lookup.condition
        print('\n')
        print('Current Weather :')
        print("         " + condition.text)
        print('\n')
        print('Forecasts :')
        forecasts = location.forecast
        for forecast in forecasts:
            print("         " + forecast.text)
            print("         " + forecast.date)
            print("         " + forecast.high)
            print("         " + forecast.low)

print('Search by (1 or 2) :')
print('1. Location Name')
print('2. Latitide and Longitude')
print('3. Exit')
ch = int(input())
if ch == 1:
    loc_name()

elif ch == 2:
    latnlong()

elif ch == 3:
    quit()

else :
    print('INVALID CHOICE')
    print('EXITING PROGRAM.....')
    quit()
