from selenium import webdriver
import time

number = 10
count = 1

driver_path ='/usr/bin/chromedriver'
recipient_name = 'Human'

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(driver_path, options=options)

driver.get('https://web.whatsapp.com/')

input('Press enter after you scan the qr:')
message = input("Enter the message you want to spam: ")

sb = driver.find_element_by_xpath('//span[@title = "{}"]'.format(recipient_name))

sb.click()


def sendMsg(msg):
    msg_box = driver.find_element_by_class_name('_1Plpp')
    msg_box.send_keys('message {}: TELL MEEEE!!!!!!'.format(str(count)))
    msg_box.send_keys(f'Message {count}: {msg}')
    send_btn = driver.find_element_by_class_name('_35EW6')
    send_btn.click()


while count <= number:
    try:
        sendMsg(message)
        count = count + 1
        time.sleep(1)
    except Exception as e:
        print(e)
