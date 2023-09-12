
# import undetected_chromedriver as uc
import time
from selenium import webdriver
import pickle
from urllib.request import urlopen
from colored import fg, bg, attr  # pip install colored

class GmailSelenium:
    ref = None
    driver = None
    def __init__(self, index: str, mail: str, password: str):
        super().__init__()
        self.index = index
        self.mail = mail
        self.password = password

        
    def login(self):
        try:
            self.driver.get('https://accounts.google.com/signin/v2/identifier?service=mail&passive=1209600&osid=1&continue=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&followup=https%3A%2F%2Fmail.google.com%2Fmail%2Fu%2F0%2F&emr=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin')
            time.sleep(0.5)
            self.driver.find_element('xpath', '//input[@type="email"]').send_keys(self.mail)
            try:
                    self.driver.find_element('xpath', '//*[@id="identifierNext"]').click()
            except:
                pass

            time.sleep(5)
            self.driver.find_element('xpath', '//input[@type="password"]').send_keys(self.password)
            try:
                    self.driver.find_element('xpath','//*[@id="passwordNext"]').click()
            except:
                pass
            time.sleep(5)
            try:
                if self.driver.find_element("id",'email') or self.driver.find_element("id", 'pass'):
                    return False
            except:
                return True
        except:
            return False

    
    def get_cookies(self):
        self.driver.get('https://www.google.com')
        time.sleep(1)
        return self.driver.get_cookies()
    
    def save_cookie(self):
        with open(f"data/{self.mail}/cookie_{self.mail}", 'wb') as filehandler:
            pickle.dump(self.driver.get_cookies(), filehandler)
            
    def init(self):
        self.ref.show.emit(self.index, 0, self.mail)
        self.ref.show.emit(self.index, 1, self.password)

    def run(self):
        options = webdriver.ChromeOptions()
        options.add_argument(r"--user-data-dir=C:\Users\quy.ngovan\AppData\Local\Google\Chrome\User Data") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
        options.add_argument(r'--profile-directory=Profile 1') #e.g. Profile 3
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=options)
        self.driver.delete_all_cookies()

        checkLogin = self.login() 
        if checkLogin == True:
            self.ref.show.emit(self.index, 2, f"Login cookie thành công")
            self.ref.checksuccess.emit(True, self.index, self.mail, self.password)
            cookie = self.get_cookies()
            print(cookie) 

        if checkLogin == False:
            self.ref.show.emit(self.index, 2, f"Login cookie thất bại")
            self.ref.checksuccess.emit(False, self.index, self.mail, self.password)  
        #protected account
        # self.driver.quit()
