from pyowm.owm import OWM
owm = OWM('17e33256227cbc375e54af6a5171ff88')
mgr = owm.weather_manager()
observation = mgr.weather_at_place('Bath,GB')  # the observation object is a box containing a weather object
weather = observation.weather
mystatus = weather.status           # short version of status (eg. 'Rain')
mydetail = weather.detailed_status  # detailed version of status (eg. 'light rain')

print(weather)
print(mystatus)
print(mydetail)

