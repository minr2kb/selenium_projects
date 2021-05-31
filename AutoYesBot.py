from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# Variables
meetingID = input("Enter the meeting ID: ").replace(' ', '') #4584825975
expiration = 55 # Duration of the process (min)
frequency = 4 # Detection loop's frequency (sec)
threshold = 300 # Trigger, chatbox height/frequency (px)
coolTime = 10 # Time until the next process (min)
participants_threshold = 10 # Exiting number of participants to quit
user = "Kyungbae Min"
msg = "yes"
interrupted = False

# Color codes
default_ = '\033[0m'
error_ = '\033[31m'
BLUE = '\033[34m'

#Time functions
def wait(remain):
    while remain >= 0:
            print(BLUE+"\rRemaining time %.2d:%.2d" % (remain//60, remain%60), end="")
            time.sleep(1)
            remain -= 1

def timePrint(seconds):
    return '%.2d:%.2d:%.2d' % (seconds // 3600, (seconds // 60) % 60, seconds % 60)

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
driver.get('https://stonybrook.zoom.us/wc/join/'+meetingID) 
driver.find_element_by_name('inputname').send_keys(user)
time.sleep(1)
input("Press any key to start the process")
temp_height = 0
prev_height = 0
temp_ppl = 0
max_ppl = 0
init_time = time.time()
answered_time = init_time - coolTime*60
coolTime*60
print(default_+"Process starts...")
time.sleep(1)
print(BLUE+"###### PROCESS IS RUNNING ON BROWSER ######")

# Main loop
while True:
    try:
        if max_ppl - temp_ppl > participants_threshold:
            break
        elif temp_ppl > max_ppl:
            max_ppl = temp_ppl
        try:
            driver.find_element_by_xpath('''//*[@id="chat-list-content"]''')
        except:
            driver.find_element_by_class_name("footer-button__chat-icon").click()
            print(default_ + "Trying to open the chatbox...")
            time.sleep(1)
            continue
        prev_height = temp_height
        try:
            temp_height = driver.find_element_by_class_name("ReactVirtualized__Grid__innerScrollContainer").get_property("clientHeight")
        except:
            input(error_ + "Error: No chatbox found. Please send some chat and press any key to continue")
            continue
        try:
            temp_ppl = int(driver.find_element_by_xpath('''//*[@id="wc-footer"]/div/div[2]/button[1]/div/div/span/span''').text)
        except:
            print(error_+"Error: No participants found. Please adjust the window ratio and press any key to continue")
        print(default_ + "Current chatbox height: " + str(temp_height) + "px")
        print(default_ + "Participants: " + str(temp_ppl) + "/" + str(max_ppl) +" [" +timePrint(time.time() - init_time)+ "]")
        if time.time() - answered_time > coolTime*60:
            if temp_height - prev_height >= threshold:
                print(error_ + "R U There!!!!!!!!!!!!!")
                driver.find_element_by_class_name("chat-box__chat-textarea.window-content-bottom").send_keys(msg)
                driver.find_element_by_class_name("chat-box__chat-textarea.window-content-bottom").send_keys(Keys.ENTER)
                print("Answered \""+msg+"\"")
                answered_time = time.time()
        time.sleep(frequency)
        driver.execute_script('''document.getElementById('wc-footer').className = 'footer';''')
    except KeyboardInterrupt:
        print("\n"+error_+"KeyboardInterrupt: The browser is closed due to KeyboardInterrupt")
        interrupted = True
        break
    except:
        try:
            input(error_+"Error: Something went wrong! Press any key to continue")
        except KeyboardInterrupt:
            print("\nKeyboardInterrupt: The browser is closed due to the KeyboardInterrupt")
            interrupted = True
            break

# if interrupted :
#     input(default_ + "To quit the whole process, press any key")
execTime = time.time() - init_time
driver.find_element_by_xpath('''//*[@id="wc-footer"]/div/div[3]/div/button''').click()
time.sleep(0.2)
driver.find_element_by_xpath('''//*[@id="wc-footer"]/div[2]/div[2]/div[3]/div/div/button''').click()
time.sleep(5)
print(error_+ timePrint(execTime) + " of execution, the process is terminated.")
driver.quit()
#ffmpeg -i myvid.mov MyVid.y4m