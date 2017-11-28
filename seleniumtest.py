# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import requests
import unittest
import time
import re
import sys
from getpass import getpass
from bs4 import BeautifulSoup
import os
import threading
from selenium.webdriver.common.action_chains import ActionChains

url="http://192.168.3.106:8080/SecuDocX/"
loginfailUrl='http://192.168.3.106:8080/SecuDocX/SecuDocXLogin.jsp?LoginErrorMsg=AccountError'

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
#driver = webdriver.Firefox()
#driver = webdriver.PhantomJS(executable_path='phantomjs.exe')
actionChains = ActionChains(driver)


#passwd = getpass("input your password:")
wa_account = "wa"
wa_passwd = '123456'

ua_account = "ua"
ua_passwd = '123456'


def thread_start(times):#多執行緒 同時開很多流覽器
    def loop(i):
        test_start(account[i],passwd[i],url)
    account=['a','b','c','d','e','f','g','h','i','wa',]
    passwd=['123','123','123','123','213','123','123','123','123','123456',]
    threads = []
    for i in range(0,times):
        t = threading.Thread(target=loop,args=(i,))
        threads.append(t)

    if __name__ == '__main__':
        for i in range(0,times):
            threads[i].start()
        for i in range(0,times):
            threads[i].join()
        print('test finish')

def login(account,passwd):#登入
    driver.get(url)
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(account)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(passwd)
    driver.find_element_by_class_name("btn-info").click()
    driver.implicitly_wait(30)
    #cookie=driver.get_cookies()
    #print(cookie)
    currUrl = driver.current_url
    #print(currUrl)
    if currUrl == loginfailUrl:
        print('account: '+account+',password: '+passwd+','+'login fail')
    else:
        print(account+','+passwd+','+'login success')

def logout(account,passwd):#登出
    try:
        driver.find_element_by_css_selector("span.hidden-xs").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"登出").click()
        print('account: '+account+',password: '+passwd+','+'logout success')
    except:
        print(account+','+passwd+','+'logout fail')
def test_start(url):
        driver.implicitly_wait(30)
        login(wa_account,wa_passwd)
        #建立工作區域及新增人員
        try:
            find_alert = EC.alert_is_present()
            driver.get(url + 'uiprivate/SecuDocxSecond.jsp')
            driver.find_element_by_css_selector("button.btn.btn-block").click()
            time.sleep(1)
            driver.find_element_by_xpath("(//input[@name='project_name'])[2]").clear()
            driver.find_element_by_xpath("(//input[@name='project_name'])[2]").send_keys("12")#工作區域名稱
            driver.find_element_by_xpath("(//button[@class='btn btn-info'])[1]").click()
            driver.find_element_by_id("addManagerInput").clear()
            time.sleep(1)
            driver.find_element_by_id("addManagerInput").send_keys("ua@SecuDocX.com wa@SecuDocX.com ")#管理人員
            driver.find_element_by_xpath("(//button[@class='btn btn-info'])[1]").click()
            driver.find_element_by_id("addWorkerInput").clear()
            time.sleep(1)
            driver.find_element_by_id("addWorkerInput").send_keys("ua@SecuDocX.com wa@SecuDocX.com wcw@taiflex.com.tw ")#內部人員
            driver.find_element_by_xpath("(//button[@class='btn btn-info'])[1]").click()#建立
            time.sleep(1)
            a1 = driver.switch_to.alert
            time.sleep(1)
            print(a1.text)
            a1.accept()
            time.sleep(1)
            print(a1.text)
            a1.accept()
            time.sleep(1)
            print(a1.text)
            a1.accept()
            time.sleep(1)
            print(a1.text)
            a1.accept()
            time.sleep(1)
            print(a1.text)
            a1.accept()
            time.sleep(1)
        except:
            a1 = driver.switch_to.alert
            time.sleep(1)
            print(a1.text)
            print('effffffffff')
            a1.accept()
            time.sleep(1)

        time.sleep(1)
        logout(wa_account,wa_passwd)
        driver.implicitly_wait(30)
        login(ua_account,ua_passwd)
        driver.implicitly_wait(30)
        time.sleep(1)
        driver.find_element_by_xpath("//tr/td/div/span[text()=12]").click()
        driver.find_element_by_xpath("(//button[@type='button'])[7]").click()
        driver.find_element_by_id("base-tab-title-Members").click()
        driver.find_element_by_link_text(u"外部使用者").click()
        driver.find_element_by_xpath("(//button[@type='button'])[16]").click()
'''
        driver.find_element_by_xpath("//input[@name='']").clear()
        driver.find_element_by_xpath("//input[@name='']").send_keys("adgj5472@gmail.com")
        driver.find_element_by_id("5e88d7ab-bcc6-4b21-b8df-f84d7ee585a3").click()
        driver.find_element_by_id("688e9894-6429-494e-a890-0a8f17062f95").click()
'''
    driver.close()
    driver.quit()

test_start(url)


