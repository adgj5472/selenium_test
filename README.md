# 需安裝的module   
pip install selenium

# Selenium IDE   
只支援 FrieFox 46版本以下  
[FrieFox 46 下載點](https://drive.google.com/file/d/1tA9KgcimG6Jd7IdM8jCuYDFp9jrkLhP0/view?usp=sharing)    

安裝完firefox 後下載FireFox Selenium IDE插件  
[FireFox Selenium IDE 載點](https://addons.mozilla.org/zh-TW/firefox/addon/selenium-ide/)  

安裝完插件可以在右上角找到他

![](https://imgur.com/PXGcmtJ.jpg)

用法: 按下錄制後開始動作

![](https://imgur.com/Xqc0FQ5.jpg)

可以看見你所操作的步驟

![](https://imgur.com/V1zPHxc.jpg)

匯出的方法:

![](https://imgur.com/WrRNPAG.jpg)


![](https://imgur.com/6xz9vvU.jpg)

# Browser Driver
使用Python執行時所需要的Driver  
[chromedriver.exe 下載點](https://drive.google.com/open?id=1ijKanCXUebmcSVCD-4vxeh5eFFHyrAKR)  
[phantomjs.exe下載點](https://drive.google.com/open?id=1g3JiwNayPonKRGV4vs_aFGKq3zaFOJ2H)  

# 參考資料   
* [自動化測試程式如何驗證網頁畫面?](https://www.qa-knowhow.com/?p=2431)      
* [在Selenium 輸入Enter/Return KEY](https://ask.helplib.com/selenium/post_357327)    
* [網站自動化測試程式的網頁元件定位 Xpath語法與範例](https://www.qa-knowhow.com/?p=2164)       
* [selenium滑鼠鍵盤操作](http://m.jb51.net/article/92682.htm)      

# 例外處理    
from selenium.common.exceptions import 
* NoAlertPresentException : 沒有Alert彈出視窗    
* UnexpectedAlertPresentException : 有Alert彈出視窗但是沒有按確定    
* NoSuchElementException : 在HTML中沒有找到元素(目前常遇到在程式執行動作太快，JS還沒產生HTML就執行，所以需要sleep(1)等待一下)    
* 待補充...

Python Version : 3
