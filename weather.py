#importing the tkinter gui library for graphics
#importing requests for requesting the api data 

import tkinter as tk
import requests
import time


#this functions helps to get the current weather info
 
def getWeather(app):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=a5564ba0a6829a511fbcfdae034df721"
    
    #gets the json data by requesting the api from the open weather app
    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main'] 
    temp = int(json_data['main']['temp'] - 273.15) #in main under temp 
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']
 
    info = condition + "\n" + str(temp) + "°C" 
    data = "\n"+ "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C" +"\n" + "Pressure: " + str(pressure) + "\n" +"Humidity: " + str(humidity) + "\n" +"Wind Speed: " + str(wind)
    label1.config(text =info)
    label2.config(text =data)


app = tk.Tk()
app.geometry("800x800")
app.title("Weather App by Kaustubh Pathak")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(app, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(app, font=t)
label1.pack()
label2 = tk.Label(app, font=t)
label2.pack()

app.mainloop()
