# from datetime import datetime as dt
# import pytz
# print(dt.now())
# tz = pytz.timezone('Singapore') #identifier like gmt , or somthing df for each country
# print(dt.now(tz))



# from selenium import webdriver
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as ec
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# import time

# driver = webdriver.Chrome('path_to_chromedriver.exe')
# driver.get('https://web.whatsapp.com/')
# recipents_name = 'Ravi Kiran'
# msg = 'Message By Bye'
# xpath = f"//span[contains(@title,'{recipents_name}')]"
# target = WebDriverWait(driver,10).until(ec.presence_of_all_elements_located(By.XPATH,xpath))
# target.click()
# input_box = driver.find_element(By.CLASS_NAME,"_1Plpp")
# for i in range(50):
#     input_box.send_keys(msg)
#     input_box.send_keys(Keys.RETURN)
#     time.sleep(1)

# driver.quit()

import datetime
login_time = datetime.datetime.now()
print(login_time)

semester_start = datetime.dat(2025,8,5)
mid_exam = datetime.date(2025,10,12)
gap = mid_exam - semester_start
print(gap.days)
year = semester_start.year
month = semester_start.month
day = semester_start.day
formmatted_date = semester_start.strftime("%A,%d %B %Y")
print(formmatted_date)

import calendar
print(calendar.month(2025,8))
calendar.isleap(2024)
exam_day = calendar.weekday(2025,10,12)
print(calendar.day_name(exam_day))

days_in_august = calendar.monthrange(2025,8)[1]
print(days_in_august)
gap = mid_exam - semester_start
print(gap.days)
semester_start = datetime.date(2025,8,5)
semester_start.strftime('%A , %d %B %Y')
calendar.isleap(2024)
