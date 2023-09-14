
# import undetected_chromedriver as uc
import time
from selenium import webdriver
import pickle
from urllib.request import urlopen
from colored import fg, bg, attr  # pip install colored
import os, shutil
from selenium.webdriver.common.keys import Keys

class ScannerWalletSelenium:
    ref = None
    driver = None
    def __init__(self, index: str, wallet):
        super().__init__()
        self.index = index
        self.wallet = wallet

        
    def login(self):
        try:
            self.driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
            time.sleep(5)
            try:
                if self.driver.find_element("id", "password"):
                    if self.wallet["password"]:
                        for password in str(self.wallet["password"]).split("|"):
                            print('dzo ', password)
                            passElm = self.driver.find_element("id", "password")
                            passElm.send_keys(Keys.CONTROL + "a")
                            passElm.send_keys(Keys.DELETE)
                            passElm.send_keys(password)
                            btnLogin = self.driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div/button")
                            btnLogin.click()
                            time.sleep(0.2)
                            try:
                                if self.driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div/button"):
                                    #login thất bại tiếp tục login
                                    continue
                            except:
                                #login Thành công
                                return True
                        try:
                            if self.driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div/button"):
                                #login thất bại tiếp tục login
                                return False
                        except:
                            #login Thành công
                            return True
                else:
                    return False
            except:
                return False
            return True
        except:
            return False
    
    def get_cookies(self):
        self.driver.get('https://www.google.com')
        time.sleep(1)
        return self.driver.get_cookies()

    def delete_files_and_subdirectories(self, directory_path):
        try:
            with os.scandir(directory_path) as entries:
                for entry in entries:
                    if entry.is_file(): 
                        os.unlink(entry.path)
                    else:
                        shutil.rmtree(entry.path)
                print("All files and subdirectories deleted successfully.")
        except OSError:
            print("Error occurred while deleting files and subdirectories.")

    def run(self):
        if not os.path.exists(rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake"):
            os.makedirs(rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake")
        self.delete_files_and_subdirectories(rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake\Profile 1\Local Extension Settings\nkbihfbeogaeaoehlefnkodbefgpgknn")
        files = os.listdir(self.wallet["path"])
        for fname in files:
            print('coppy2', self.wallet["path"])
            shutil.copy2(os.path.join(self.wallet["path"], fname), rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake\Profile 1\Local Extension Settings\nkbihfbeogaeaoehlefnkodbefgpgknn")
        time.sleep(1)
        options = webdriver.ChromeOptions()
        options.add_argument(rf"--user-data-dir=C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
        options.add_argument(rf'--profile-directory=Profile 1') #e.g. Profile 3
        options.add_argument("start-maximized")
        self.driver = webdriver.Chrome(options=options)
        self.driver.delete_all_cookies()

        checkLogin = self.login() 
        self.driver.quit()
        if checkLogin == True:
            self.ref.show.emit(self.index, self.index, f"Login cookie thành công")
            self.ref.checksuccess.emit(True, self.index, "Login thành công")

        if checkLogin == False:
            self.ref.show.emit(self.index, self.index, f"Login thất bại")
            self.ref.checksuccess.emit(False, self.index, f"Login thất bại")  
        #protected account
