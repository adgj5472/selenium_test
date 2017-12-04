# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException #沒有alert
import time
from getpass import getpass
import os
import threading
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
#url='http://127.0.0.1:8080/'
#url="https://drive.google.com/"
url="http://192.168.3.106:8080/SecuDocX/"
loginfailUrl='http://192.168.3.106:8080/SecuDocX/SecuDocXLogin.jsp?LoginErrorMsg=AccountError'

driver = webdriver.Chrome(executable_path=r'chromedriver.exe')
#driver = webdriver.Firefox(executable_path=r'geckodriver')
#driver = webdriver.Ie(executable_path=r'IEDriverServer.exe')
actionChains = ActionChains(driver)

#passwd = getpass("input your password:")
wa_account = "wa"
wa_passwd = '123456'

ua_account = "ua"
ua_passwd = '123456'

def login(account,passwd):
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
        #driver.find_element_by_link_text(u"登出").click()
        driver.find_element_by_link_text(u"Log out").click()
        print('account: '+account+',password: '+passwd+','+'logout success')
    except:
        print(account+','+passwd+','+'logout fail')
def error_alert():
    while(1):
        try:
            a1 = driver.switch_to.alert
            time.sleep(1)
            print(a1.text)
            a1.accept()
            print('alert')
        except UnexpectedAlertPresentException:
            print('no accept alert')
            time.sleep(1)
        except NoAlertPresentException:
            print('no alert')
            break
def error_show():
    #driver.get(driver.current_url)
    pageSource = driver.page_source  # 取得網頁原始碼
    error_index=pageSource.find('Not Supported')
    error_text=pageSource[error_index:50350]
    print(error_text)
def upload_file():
    driver.find_element_by_class_name("fa-sm").click()
    time.sleep(1)
    driver.find_element_by_id("CmdCreateFile").click()
    time.sleep(1)
    driver.find_element_by_xpath("//div/form/input[@type='file']").send_keys('E:\\f.txt')
    time.sleep(1)
def test_start(url):
        driver.implicitly_wait(30)
        login(ua_account,ua_passwd)
        #建立工作區域及新增人員
        driver.get(url + 'uiprivate/SecuDocxSecond.jsp')
        driver.find_element_by_css_selector("button.btn.btn-block").click()
        time.sleep(1)
        driver.find_element_by_xpath("(//input[@name='project_name'])[2]").clear()
        driver.find_element_by_xpath("(//input[@name='project_name'])[2]").send_keys("aa")#工作區域名稱
        driver.find_element_by_xpath("(//button[@class='btn btn-info'])[1]").click()
        driver.find_element_by_id("addManagerInput").clear()
        time.sleep(1)
        driver.find_element_by_id("addManagerInput").send_keys("ua@SecuDocX.com wa@SecuDocX.com ")#管理人員
        driver.find_element_by_xpath("(//button[@class='btn btn-info'])[1]").click()
        driver.find_element_by_id("addWorkerInput").clear()
        time.sleep(1)
        driver.find_element_by_id("addWorkerInput").send_keys("wa@SecuDocX.com")#內部人員
        driver.find_element_by_xpath("(//button[@class='btn btn-info'])[1]").click()#建立
        time.sleep(1)
        error_alert()
        
        time.sleep(1)
        logout(ua_account,ua_passwd)
        driver.implicitly_wait(30)
        login(wa_account,wa_passwd)
        driver.implicitly_wait(30)
        time.sleep(1)
        driver.find_element_by_xpath("//tr/td/div/span[text()='aa']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='DivForRightMenu']/button[@onclick='gogoDiag()']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//li/a/span[@data-i18n='word18_exUser']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='nav-pills-tab-3']/div/button[@type='button']").click()
        time.sleep(1)
        driver.find_element_by_xpath("//input[@name='']").send_keys("adgj5472@gmail.com")
        driver.find_element_by_xpath("//div[@class='modal-footer']/div/div/button[@class='btn btn-info']").click()#確定
        time.sleep(1)
        error_alert()
        driver.find_element_by_xpath("//div[@class='modal-footer']/div/div/button[@class='btn btn-default']").click()#關閉
        time.sleep(1)
        actionChains.double_click(driver.find_element_by_xpath("//tr/td/div/span[text()='aa']")).perform()
        upload_file()
        error_show()
        

        
        #driver.find_element_by_xpath("(//button[@type='button'])[16]").click()
        #driver.close()
        #driver.quit()        
'''     driver.find_element_by_xpath("//input[@name='']").clear()
        driver.find_element_by_xpath("//input[@name='']").send_keys("adgj5472@gmail.com")
        driver.find_element_by_id("5e88d7ab-bcc6-4b21-b8df-f84d7ee585a3").click()
        driver.find_element_by_id("688e9894-6429-494e-a890-0a8f17062f95").click()
'''
        
        #driver.find_element_by_id("VGFpRmxleA_E_E_L2hoaGg_E").click()
        #actionChains.double_click(driver.find_element_by_id('VGFpRmxleA_E_E_L2hoaGg_E')).perform()
        
        #driver.find_element_by_xpath("//div[@id='addButton']/a/span/i[3]").click()
        #time.sleep(1)
        #driver.find_element_by_id("CmdCreateFile").click()
        #time.sleep(1)
        #driver.find_element_by_css_selector("input[type=\"file\"]").send_keys("C:\\Users\\PPP\\Desktop\\mou.jpg")
        #time.sleep(1)
        #actionChains = ActionChains(driver)
        #actionChains.double_click(driver.find_element_by_id('VGFpRmxleA_E_E_L2hoaGg_E')).perform()
        #time.sleep(1)
        #driver.find_element_by_xpath('//button[@data-original-title="設定"]').click()
        #time.sleep(1)
        #driver.find_element_by_xpath('//button[@data-original-title="設定"]').click()
        #driver.find_element_by_link_text('外部使用者').click()

        #driver.find_element_by_class_name("fa-sm").click()
        #time.sleep(1)
        #driver.find_element_by_id("CmdCreateFile").click()
        #driver.find_element_by_xpath('//form[input/@type="file"]').send_keys('123')
        #driver.find_element_by_class_name('ui-button-text').send_keys('C:\\Users\\hello\\url.txt')
        #pageSource = driver.page_source
        #print(pageSource)
        #os.system('D:\\upfile.exe "D:\\1.html"')
    
        #select = Select(driver.find_element_by_name('companyname'))
        #select.select_by_visible_text("j")    
        #r = requests.get(url)
        #assert "Login" not in driver.page_source
        #pageSource = driver.page_source
        #print(pageSource)


#driver.find_element_by_xpath('//a[img/@src="resources/img/logout.png"]').click()
#<li class="logout"> <a href="#/logout"><img src="resources/img/logout.png"/></a></li>

def thread_start(times):
    def loop(i):
        test_start(account[i],passwd[i],url)
        #os.system('test.py '+account[i]+' '+passwd[i])
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

#thread_start(10)
#test_start(sys.argv[1],sys.argv[2],url)
start=time.time()
print('測試開始')
print(time.strftime("%Y/%m/%d")+' '+time.strftime("%H:%M:%S"))
test_start(url)
print("執行時間 %f" %(time.time()-start))

