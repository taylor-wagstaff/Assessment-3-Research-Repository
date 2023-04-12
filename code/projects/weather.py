import requests
#import and download package
#╰─$ python3 -m pip install requests

# Lesson in....
#Intermediate Python for Non-Programmers
#Classes and weather

#notes....
#Weather api, Stand for Application Programming Interface
## json is a type of formatting for text, very machine freindly 
## JsonLint 
## essentially dictionaries and lists. 



# Simple weather API and how its worked, 
# I accidently sent up my key for this to github and had to restart the 
# research repo, very annoying. 

## access api inside our class
class City:
    def __init__(self, name, lat, long, units="metric"):
        self.name = name
        self.lat = lat
        self.long = long
        self.units = units
        self.get_data()

    #best thing sbout classes, lots of different classes
    def get_data(self):
        
        try:
          response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.long}&appid={}")

        
        except:
          print("Sorry :( you got no Internet access")
        #response of json
        self.response_json = response.json()
# to access key in dictionary with ["main"] & ["temp"]
        self.temp = self.response_json["main"]["temp"]

    def temp_print(self):
       print(f"In {self.name} it is currently {self.temp}")



#creates object with parameters
my_city = City("Tokyo", 35.6762, 130.6503)
#then prints to console, because we made a method of the class. 
my_city.temp_print()


# classes make it easier to add and customise, eg add city

vacation_city = City("Portland", 45.5152, -122.6784 )
vacation_city.temp_print()

  # typical to create virtual environment, 
  # to create a virtual env
  #  python3 -m venv weather_venv
  # to activate 
  # source weather_venv/bin/activate
  # to leave
  #deactivate