from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from datetime import datetime, timedelta
import time

# Color codes
default_ = '\033[0m'
error_ = '\033[31m'
BLUE = '\033[34m'

while True:
    name = "Kyungbae Min"
    floor = "C17"
    while True:
        reportType = int(input("<Report type>\n1. Main Hall Rounding\n2. Staying\n3. Weekend\n4. Holyday\nEnter the type number: "))
        if reportType == 1 or reportType == 2 or  reportType == 3 or reportType == 4:
            break
        else:
            print("Invalid value")
    phoneDuty = False
    incidentReport = False
    facilityIssue = "None"
    facilityIssue_sol = ""

    duty = ""
    if input("Phone duty?(y/n): ").lower() == "y":
        phoneDuty = True    
    if input("Incident report?(y/n): ").lower() == "y":
        incidentReport = True
    if input("Facility issues?(y/n): ").lower() == "y":
        facilityIssue = input("Provide any details: ")
        facilityIssue_sol = input("Your solution: ")
    commentsRHD = input("Comments to RHDs?: ")
    if commentsRHD == "":
        commentsRHD = "None"

    reportDate = datetime.today()
    DutyHour_start = "00"
    DutyHour_end = "00"
    if reportType == 1:
        reportDate = reportDate - timedelta(days=(reportDate.weekday()-1)) #Tue
        duty = "Hall rounding"
        DutyHour_start = "08"
        DutyHour_end = "00"
        week = reportDate.weekday()
    elif reportType == 2:
        reportDate = reportDate - timedelta(days=reportDate.weekday()) # Mon
        duty = "Check-in"
        DutyHour_start = "09"
        DutyHour_end = "11"
        week = reportDate.weekday()
    elif reportType == 3:
        reportDate = reportDate - timedelta(days=(reportDate.weekday()-5)) # Sat
        duty = "Staying and phone duty"
        DutyHour_start = "00"
        DutyHour_end = "00"
        week = reportDate.weekday()
    elif reportType == 4:
        week = int(input("Enter the date(1~7): "))-1
        reportDate = reportDate - timedelta(days=(reportDate.weekday()-week))
        duty = "Staying and phone duty"
        DutyHour_start = "00"
        DutyHour_end = "00"

    day = str(reportDate.day)
    mon = str(reportDate.month)
    year = str(reportDate.year)
    if len(day) == 1:
        day = "0" + day
    if len(mon) == 1:
        mon = "0" + mon
    date = year+mon+day

    weekdays = {0:"Mon", 1:"Tue", 2:"Wed", 3:"Thu", 4:"Fri", 5:"Sat", 6:"Sun"}

    print(default_ + "========== Your Responses ==========")
    print(default_ + "Name: " + name)
    print(default_ + "Floor: " + floor)
    print(default_ + "Date: " + year + "/" + mon + "/" + day + "(" + weekdays[week] + ")")
    print(default_ + "Time: " + DutyHour_start + ":00 ~ " + DutyHour_end + ":00")
    if reportType == 1:
        print(default_+"Report type: " + BLUE + "1. Main Hall Rounding")
    elif reportType == 2:
        print(default_+"Report type: " + BLUE + "2. Staying")
    elif reportType == 3:
        print(default_+"Report type: " + BLUE + "3. Weekend")
    elif reportType == 4:
        print(default_+"Report type: " + BLUE + "4. Holyday")

    def YoN(response):
        if response:
            return BLUE+"Yes"
        return error_+"No"

    print(default_+"Phone duty?: " + YoN(phoneDuty))
    print(default_+"Incident report: " + YoN(incidentReport))
    if facilityIssue == "None":
        print(default_+"Facility issues: " + error_+"None")
    else:
        print(default_+"Facility issues: " + BLUE + facilityIssue)
        print(default_+"Your solution: " + BLUE + facilityIssue_sol)
    if commentsRHD == "None":
        print(default_+"Comments to RHD: " + error_ + commentsRHD)
    else:
        print(default_+"Comments to RHD: " + BLUE + commentsRHD)

    confirmation = input(default_+"========== Continue? (y/n) ==========")
    if confirmation.lower() != 'n':
        break

print(default_+"Opening the browser...")
driver = webdriver.Chrome("./chromedriver")
driver.get("https://docs.google.com/forms/d/e/1FAIpQLSf-crrwyWM7FWqlrXcfcbYALemNYWKQW3vxEYz1i3z17ytyJg/viewform")
time.sleep(1)

# Name and floor
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(name)
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input").send_keys(floor)

# Phone duty check
if phoneDuty:
    driver.find_element_by_xpath("//*[@id='i13']/div[3]/div").click()
else:
    driver.find_element_by_xpath("//*[@id='i16']/div[3]/div").click()

# Duty type check
if reportType == 1:
    driver.find_element_by_xpath("//*[@id='i24']/div[2]").click()
elif reportType == 2:
    driver.find_element_by_xpath("//*[@id='i27']/div[2]").click()
elif reportType == 3:
    driver.find_element_by_xpath("//*[@id='i30']/div[2]").click()
elif reportType == 4:
    driver.find_element_by_xpath("//*[@id='i33']/div[2]").click()

# Date
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[5]/div/div/div[2]/div/div/div[2]/div[1]/div/div[1]/input").send_keys(date)

# Time
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input").send_keys(DutyHour_start)
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input").send_keys("00")
if DutyHour_start != "00":
    driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[4]/div[1]/div[2]").click()
    time.sleep(0.3)
    driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[6]/div/div/div[2]/div/div[4]/div[2]/div[2]").click()
    time.sleep(0.3)
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[1]/div[2]/div[1]/div/div[1]/input").send_keys(DutyHour_end)
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[3]/div/div[1]/div/div[1]/input").send_keys("00")
if DutyHour_end != "00":
    driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[4]/div[1]/div[2]").click()
    time.sleep(0.3)
    driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[7]/div/div/div[2]/div/div[4]/div[2]/div[2]").click()
    time.sleep(0.3)

# Incident report
if incidentReport:
    driver.find_element_by_xpath("//*[@id='i56']/div[3]/div").click()
else:
    driver.find_element_by_xpath("//*[@id='i59']/div[3]/div").click()

# Facility issues
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[9]/div/div/div[2]/div/div[1]/div[2]/textarea").send_keys(facilityIssue)
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[10]/div/div/div[2]/div/div[1]/div[2]/textarea").send_keys(facilityIssue_sol)

# Duty
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[11]/div/div/div[2]/div/div[1]/div[2]/textarea").send_keys(duty)

#To RHD
driver.find_element_by_xpath("//*[@id='mG61Hd']/div[2]/div/div[2]/div[12]/div/div/div[2]/div/div[1]/div[2]/textarea").send_keys(commentsRHD)