from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
import time




def test_open_s6(browser):

    browser.get('https://future-rn-omega.tektorg.ru/#auth/login')    #открываем фомру аккредитации
    acred_new = browser.find_element(By.ID, 'ext-element-97')  #Кликаем на аккредитация на ЭТП
    acred_new.click()
    name_fzur = browser.find_element(By.CSS_SELECTOR,'[textfield-1088-inputEl]') # поиск элемента
    name_fzur.click()                                 #сравнение элемента
    name_fzur.send_keys("новый пользователь автотестер")



