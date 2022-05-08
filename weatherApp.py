import tkinter as tk
import requests

scrn_h = 1200
scren_w = 950
green_c = "#689967"
gray_c = "#e8e8e6"
orange_c = "#eb7036"

#Exeption handler in case of errors
def format_response(weather):
	try:
		name = weather['name']
		desc = weather['weather'][0]['description']
		temp = weather['main']['temp']

		info_str = 'City: %s \nConditions: %s \nTemperature (°F): %s' % (name, desc, temp)
	except:
		info_str = 'No info.. try again :)'

	return info_str

#Function for getting data
def get_weather(city):
	weather_key = '6de73714caebfc516068eb3b0748c914'
	url = 'https://api.openweathermap.org/data/2.5/weather'
	params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
	response = requests.get(url, params=params)
	weather = response.json()

	label['text'] = format_response(weather)

root = tk.Tk()

canvas = tk.Canvas(root, height=scrn_h, width=scren_w, highlightthickness=0)
canvas.pack()

background_label = tk.Label(root, bg=green_c)
background_label.place(relwidth=1, relheight=1)

upFrame = tk.Frame(root, bg=gray_c, bd=5)
upFrame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(upFrame,borderwidth=0,bg=gray_c, fg=green_c, font=("Helvetica Neue Light",70))
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(upFrame,borderwidth=0,bg=gray_c, fg=orange_c, text="get", font=("Helvetica Neue Light",65), command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lowFrame = tk.Frame(root, bg=green_c, bd=10)
lowFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lowFrame, font=("Helvetica Neue Light",40), bg=gray_c, fg=green_c)
label.place(relwidth=1, relheight=1)

root.mainloop()
