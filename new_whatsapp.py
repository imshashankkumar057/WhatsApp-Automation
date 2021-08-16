from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket
import csv
import getpass

message_text = 'Testing automation tool, :)'
# message you want to send

no_of_message = 1
# no. of time you want the message to be send

data_base={}
# list of phone number can be of any length

with open('target.csv', 'r') as csvfile:
    # moblie_no_list = [int(row[0])for row in csv.reader(csvfile, delimiter=';')]
    for row in (csvfile):
        x = (list(map(str, row.split(','))))
        if(x[1][0:2]=='91'):
            name=x[0]
            number=x[1]
            message=''.join(x[2:])
            data_base[number]=str(message).replace('"',"").replace("\n",'')


print(data_base)

# get mobile no from csv file

def element_presence(by, xpath, time):

    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

# def is_connected():
#
#     try:
#         # connect to the host -- tells us if the host is actually reachable
#         socket.create_connection(("www.google.com", 80))
#         return True
#     except BaseException:
#         is_connected()

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")

# Chrome shoud be closed before lauching this script

# ->format
# __user__data__PATH__="C:/Users/Vaibhaw/AppData/Local/Google/Chrome/User Data"
options.add_argument(r"C:/Users/Vaibhaw/AppData/Local/Google/Chrome/User Data".format(getpass.getuser()))
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# driver = webdriver.Chrome()
driver.get("http://web.whatsapp.com")
sleep(10)



def send_whatsapp_msg(phone_no, text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))

    try:
        driver.switch_to_alert().accept()

    except Exception as e:
        pass

    try:
        element_presence(
            By.XPATH,
            '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',
            30)
        txt_box = driver.find_element(
            By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text)
            txt_box.send_keys("\n")

    except Exception as e:
        print(e)
        print("Invailid phone no :" + str(phone_no))


def main():
      for moblie_no,message in data_base.items():
          try:
              send_whatsapp_msg(phone_no=moblie_no, text=message)
          except Exception as e:
     
              sleep(5)
              # is_connected()
    #for i in range(1000):
    #   send_whatsapp_msg(917033999418,("checking = "+str(i)))
    # send_whatsapp_msg(919729896299, "checking")

if __name__ == '__main__':
    main()


