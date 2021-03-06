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


def unfollow ():
    
    try:
        # find unfollow button
        unfollow = chrome.find_element_by_class_name ('_5f5mN ')
        unfollow.click ()
        time.sleep (2)

        # Find confirm button
        confirm = chrome.find_element_by_class_name ('aOOlW')
        confirm.click ()
        time.sleep (2)

    except selenium.common.exceptions.NoSuchElementException:
        pass

# Driver code
textfile = NULL
try:
    textfile = open ("data/unfollow.list", "r")
except:
    print ("Could not locate file: " + "data/unfollow.list")
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
        unfollow ()
        print (str (line) + ": " + name[:-1])
        line += 1
    except selenium.common.exceptions.NoSuchElementException:
        pass

chrome.close ()
