import googlemaps

api_key = "AIzaSyDeyQLXT5Fo6WYVvzQ9XSIbaXURTmbydV8"
gmaps=  googlemaps.Client(api_key)
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))

print(reverse_geocode_result)
