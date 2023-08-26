import requests
import datetime as dt
import time
import smtplib


MY_LAT = 9.945940
MY_LNG = 123.618990
MY_EMAIL = "magselosgrabe@gmail.com"
MY_PASSWORD = "dijixizfbvdskofv"


def is_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    print(data)
    iss_lat = float(data["iss_position"]["latitude"])
    iss_lng = float(data["iss_position"]["longitude"])
    if MY_LAT == iss_lat and MY_LNG == iss_lng:
        return True
    return False


def is_nighttime():
    now = dt.datetime.now()
    hour = now.hour
    if hour >= 19 or hour <= 5:
        return True
    return False


while True:
    time.sleep(60)
    if is_overhead() and is_nighttime():
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="magselosgrabe@yahoo.com",
                                msg="Subject:\n\nThe ISS is above you, LOOK UP!")



