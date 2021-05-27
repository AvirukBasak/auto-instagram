from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
import time

# Login Credentials
username = open ("credentials.txt", "r").readline ();
password = open ("credentials.txt", "r").readline ();

url = ""
def path ():
        global chrome
        # starts a new headless chrome session
        option = Options ()
        # option.add_argument ("--headless")
        option.add_argument ("window-size=1024x700")
        try:
            # Add path to chrome driver executable file if required
            chrome = webdriver.Chrome ("data/chromedriver.exe", options=option)
        except:
            print ("Could not locate Chrome Driver")
            exit ();
        print ("Chrome ready")


def url_name (url):
    chrome.get (url)
    # adjust sleep if you want
    time.sleep (3)

def login (username, your_password):
    log_but = chrome.find_element_by_class_name ("L3NKy")
    time.sleep (1)
    log_but.click ()
    time.sleep (1)
     
    # finds the username box
    usern = chrome.find_element_by_name ("username")
     
    # sends the entered username
    usern.send_keys (username)
 
    # finds the password box
    passw = chrome.find_element_by_name ("password")
 
    # sends the entered password
    passw.send_keys (your_password)
     
    # press enter after sending password
    passw.send_keys (Keys.RETURN)
    time.sleep (4)
    print ("Logged in")

def send_message(msg):
    try:
        # Find message button
        message = chrome.find_element_by_class_name ('_862NM ') 
        message.click ()
        time.sleep (2)
        chrome.find_element_by_class_name ('HoLwm ').click()
        time.sleep (1)
    
        mbox = chrome.find_element_by_tag_name ('textarea')
        mbox.send_keys (msg)
        mbox.send_keys (Keys.RETURN)
        time.sleep (1.2)
    except selenium.common.exceptions.NoSuchElementException:
        pass
        
# Driver code
textfile = NULL
try:
    textfile = open ("data/dmtext.txt", "r")
except:
    print ("Could not locate file: " + "data/dmtext.txt")
    exit ()
msg = textfile.readlines ()
textfile.close ()

# check for msg
if msg[0:5] == "false":
    print ("ERROR: please overwrite content of data/dmtext.txt with\n
            the message you wish to send.");
    exit (1);

textfile = NULL
try:
    textfile = open ("data/namelist.txt", "r")
except:
    print ("Could not locate file: " + "data/namelist.txt")
    exit ()
namelist = textfile.readlines ()
textfile.close ()
line = 1

url = 'https://instagram.com/'
path ()
time.sleep (3)
url_name (url + username)
login (username, password)
for name in namelist:
    try:
        url_name (url + name)
        send_message (msg)
        print (str (line) + ": " + name[:-1])
        line += 1
    except selenium.common.exceptions.NoSuchElementException:
        pass

chrome.close ()
