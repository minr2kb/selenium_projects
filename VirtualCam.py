from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Variables
AMS311 = "https://stonybrook.zoom.us/wc/join/95252181784?pwd=Zk9jMnpYTGhmK0lta0hvcVNiWDAvdz09"
AMS315 = "https://stonybrook.zoom.us/wc/join/96408767857?pwd=TDlGRmdDOHdrQWRHNW9YVC9USC9Vdz09" #688911
AMS475 = "https://stonybrook.zoom.us/wc/join/91866361315?pwd=MitGcTVqL1p6Zjd3clVpN1FsV2MyZz09"
CSE216 = "https://stonybrook.zoom.us/wc/join/5078058515"
CSE220 = "https://stonybrook.zoom.us/j/95261972344?pwd=eDdJcldoamxmd0pLSUFLZk1tZFpXdz09" #651498
course = input("<Courses>\n1. AMS311\n2. AMS315\n3. AMS475\n4. CSE216\n5. CSE220\nEnter the number: ")
if course == "1":
    meetingURL = AMS311
    print("pw: AMS311")
elif course == "2":
    meetingURL = AMS315
    print("pw: 688911")
elif course == "3":
    meetingURL = AMS475
elif course == "4":
    meetingURL = CSE216
elif course == "5":
    meetingURL = CSE220
    print("pw: 651498")
else:
    meetingURL = input("Enter the meeting URL: ").replace('/j/', '/wc/join/')

user = "kymmin"
pw = "I'm a bass-player"
participants_threshold = 10 # Exiting number of participants to quit

# Color codes
default_ = '\033[0m'
error_ = '\033[31m'
BLUE = '\033[34m'

# Chrome options
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
opt.add_argument("use-fake-device-for-media-stream")
opt.add_argument("use-fake-ui-for-media-stream")
opt.add_argument('--use-file-for-fake-video-capture=./MyVid.y4m')

# Pass the argument 1 to allow and 2 to block
opt.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1, 
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.geolocation": 1, 
    "profile.default_content_setting_values.notifications": 2 
  })

driver = webdriver.Chrome(chrome_options=opt, executable_path="./chromedriver")
print(default_+"Opening the browser...")
driver.get(meetingURL) 
# print(default_+"Please verify yourself on the browser")
# driver.find_element_by_xpath("//*[@id='username']").send_keys(user)
# driver.find_element_by_xpath("//*[@id='password']").send_keys(pw)
# driver.find_element_by_xpath("//*[@id='main-form-inputs']/div[5]/button").click()
input("Press any key to start the process")
time.sleep(1)
temp_ppl = 0
max_ppl = 0
initT = time.time()
interrupted = False

def timePrint(seconds):
    return '%.2d:%.2d:%.2d' % (seconds // 3600, (seconds // 60) % 60, seconds % 60)

while True:
    try:  
        if max_ppl - temp_ppl > participants_threshold:
            break
        elif temp_ppl > max_ppl:
            max_ppl = temp_ppl
        try:
            temp_ppl = int(driver.find_element_by_xpath('''//*[@id="wc-footer"]/div/div[2]/button[1]/div/div/span/span''').text)
            #(document.evaluate('//*[@id="wc-footer"]/div/div[2]/button[1]/div/div/span/span', document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue).innerText;
        except:
            print(error_+"Error: No participants found. Please adjust the window ratio and press any key to continue")
        print(BLUE + "Participants: " + str(temp_ppl) + "/" + str(max_ppl) +" [" +timePrint(time.time() - initT)+ "]")
        time.sleep(3)
        driver.execute_script('''document.getElementById('wc-footer').className = 'footer';''')
    except:
        try: 
            input(error_+"Error occurred")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt: The browser is closed due to the KeyboardInterrupt")
            interrupted = True
            break
if interrupted : 
    input("Press any key to terminate")
print(error_+"\nClass is finished. The process is terminated.")
driver.find_element_by_xpath('''//*[@id="wc-footer"]/div/div[3]/div/button''').click()
time.sleep(0.2)
driver.find_element_by_xpath('''//*[@id="wc-footer"]/div[2]/div[2]/div[3]/div/div/button''').click()
time.sleep(5)
driver.quit()