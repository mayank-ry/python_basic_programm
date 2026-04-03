from datetime import datetime as dt
import pytz
print(dt.now())
tz = pytz.timezone('Singapore') #identifier like gmt , or somthing df for each country
print(dt.now(tz))



