import requests
from datetime import datetime
import smtplib

MY_LATITUDE = 14.680159
MY_LONGITUDE = 121.082855
my_email = "naomiarchieves2@gmail.com"
my_pw = "eukw zudt zlly mglg"

now = datetime.now()
# print(now.hour)
# print(type(now.hour))

r = requests.get("http://api.open-notify.org/iss-now.json")
data = r.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LATITUDE,
    "lng": MY_LONGITUDE,
    "formatted": 0,
}

s = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
sun_data = s.json()
sunrise = int(sun_data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(sun_data["results"]["sunset"].split("T")[1].split(":")[0])


if abs(MY_LATITUDE-iss_latitude) <= 5 and abs(MY_LONGITUDE-iss_longitude) <=5:
    if now.hour >= sunset or now.hour < sunrise:
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(my_email, my_pw)
            connection.sendmail(from_addr=my_email, to_addrs="rbpalmiano@gmail.com", msg="Subject:Look up!\n\nISS satellite is above you. Try to look for it!")