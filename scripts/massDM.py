def send_message(msg):
   
    # Find message button
    message = chrome.find_element_by_class_name('_862NM ') 
    message.click()
    time.sleep(2)
    chrome.find_element_by_class_name('HoLwm ').click()
    time.sleep(1)
    for x in range(10):
        mbox = chrome.find_element_by_tag_name('textarea')
        mbox.send_keys(msg)
        mbox.send_keys(Keys.RETURN)
        time.sleep(1.2)
        
# Driver code
textfile = NULL
try:
    textfile = open ("data/dmtext", "r")
except:
    print ("Could not locate file: " + "data/dmtext")
    exit ()
msg = textfile.readlines ()
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
