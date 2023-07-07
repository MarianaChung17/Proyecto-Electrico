from selenium import webdriver
from selenium.webdriver.common.by import By
from googletrans import Translator
import time

def web_parser_es():
    
    url1 ="https://www.ucrenlinea.com/categories/72/laboratorio-de-docencia-en-cirugia-y-cancer"
    browser = webdriver.Chrome()
    browser.get(url1)
    geninfo = browser.find_element(By.XPATH,"/html/body/div[2]/section[2]/div/div/div[1]/div/p/span").text
    psc = browser.find_element(By.XPATH,"/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[1]/article/div/div[2]/div/h2").text
    psc_price = browser.find_element(By.XPATH,"/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[1]/article/div/div[2]/div/span/ins/span").text
    hpv_gin = browser.find_element(By.XPATH,"/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[2]/article/div/div[2]/div/h2").text
    hpv_gin_price = browser.find_element(By.XPATH,"/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[2]/article/div/div[2]/div/span/ins/span").text
    hpv_lab = browser.find_element(By.XPATH,"/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[3]/article/div/div[2]/div/h2").text
    hpv_lab_price = browser.find_element(By.XPATH,"/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[3]/article/div/div[2]/div/span/ins/span").text
    c_sut = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[4]/article/div/div[2]/div/h2").text
    c_sut_price = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[4]/article/div/div[2]/div/span/ins/span").text
    c_laparo = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[5]/article/div/div[2]/div/h2").text
    c_laparo_price = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[5]/article/div/div[2]/div/span/ins/span").text
    tox = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[7]/article/div/div[2]/div/h2").text
    tox_price = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[7]/article/div/div[2]/div/span/ins/span").text
    pcr = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[6]/article/div/div[2]/div/h2").text
    pcr_price = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[6]/article/div/div[2]/div/span/ins/span").text
    bio = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[8]/article/div/div[2]/div/h2").text
    bio_price = browser.find_element(By.XPATH,"/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[8]/article/div/div[2]/div/span").text
    url2 = "https://www.ucrenlinea.com/products/220/prueba-secuenciacion-capilar"
    browser.get(url2)
    psc_info = browser.find_element(By.XPATH,"/html/body/div[3]/section[2]/div/div/div/div").text

    url3 ="https://www.ucrenlinea.com/products/132/prueba-hpv-oncotect-para-ginecologos"
    browser.get(url3)
    hpv_gin_info = browser.find_element(By.XPATH,"/html/body/div[3]/section[2]/div/div/div/div").text

    url4 = "https://www.ucrenlinea.com/products/131/prueba-hpv-oncotect-para-laboratorios"
    browser.get(url4)
    hpv_lab_info = browser.find_element(By.XPATH,"/html/body/div[3]/section[2]/div/div/div/div").text

    url5 = "https://www.ucrenlinea.com/products/293/curso-tecnica-de-suturas-quirurgicas"
    browser.get(url5)
    c_sut_info = browser.find_element(By.XPATH,"/html/body/div[3]/section[2]/div/div/div/div").text

    url6 = "https://www.ucrenlinea.com/products/292/curso-basico-de-laparoscopia-para-medicos-generales"
    browser.get(url6)
    c_laparo_info = browser.find_element(By.XPATH,"/html/body/div[3]/section[2]/div/div/div/div").text

    url7 = "https://www.ucrenlinea.com/products/314/toxicidad-en-fluoropirimidinas-5-fu"
    browser.get(url7)
    tox_info = browser.find_element(By.XPATH,"/html/body/div[3]/section[2]/div/div/div/div").text

    url8 = "https://www.ucrenlinea.com/products/325/pcr-real-para-deteccion-de-serotipos-de-hpv"
    browser.get(url8)
    pcr_info = browser.find_element(By.XPATH,"/html/body/div[3]/section[2]/div/div/div/div").text

    url9_en = "https://www.ucrenlinea.com/products/339/taller-de-entrenamiento-en-biopsia-al-vacio-para-deteccion-temprana-de-cancer-de-mama"
    browser.get(url9_en)
    bio_info = browser.find_element(By.XPATH,"/html/body/div[3]/section[2]/div/div/div/div").text

    browser.close()
    variables = [geninfo, psc, psc_price, psc_info, hpv_gin, hpv_gin_price, hpv_gin_info, hpv_lab,
                hpv_lab_price, hpv_lab_info, c_sut, c_sut_price, c_sut_info, c_laparo, c_laparo_price, c_laparo_info,
                tox, tox_price, tox_info, pcr, pcr_price, pcr_info, bio, bio_price, bio_info]
    


    return variables

def web_parser_en():
    
    url1_en ="https://www-ucrenlinea-com.translate.goog/categories/72/laboratorio-de-docencia-en-cirugia-y-cancer?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui"
    browser = webdriver.Chrome()
    browser.get(url1_en)
    time.sleep(2)
    geninfo_en = browser.find_element(By.XPATH,"/html/body/div[2]/section[2]/div/div/div[1]/div/p/span").text
    
    psc_en = browser.find_element(By.XPATH,"/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[1]/article/div/div[2]/div/h2").text
    
    psc_price_en = browser.find_element(By.XPATH,"/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[1]/article/div/div[2]/div/span/ins/span").text
    
    hpv_gin_en = browser.find_element(By.XPATH,"/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[2]/article/div/div[2]/div/h2").text
   
    hpv_gin_price_en = browser.find_element(By.XPATH,"/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[2]/article/div/div[2]/div/span/ins/span").text

    hpv_lab_en = browser.find_element(By.XPATH,"/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[3]/article/div/div[2]/div/h2").text

    hpv_lab_price_en = browser.find_element(By.XPATH,"/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[3]/article/div/div[2]/div/span/ins/span").text

    c_sut_en = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[4]/article/div/div[2]/div/h2").text

    c_sut_price_en = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[4]/article/div/div[2]/div/span/ins/span").text

    c_laparo_en = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[5]/article/div/div[2]/div/h2").text

    c_laparo_price_en = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[5]/article/div/div[2]/div/span/ins/span").text

    tox_en = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[7]/article/div/div[2]/div/h2").text

    tox_price_en = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[7]/article/div/div[2]/div/span").text
 
    pcr_en = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[6]/article/div/div[2]/div/h2").text

    pcr_price_en = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[6]/article/div/div[2]/div/span/ins/span").text

    bio_en = browser.find_element(By.XPATH, "/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[8]/article/div/div[2]/div/h2").text

    bio_price_en = browser.find_element(By.XPATH,"/html/body/div[2]/section[2]/div/div/div[2]/div[2]/div[8]/article/div/div[2]/div/span").text





    url2_en = "https://www-ucrenlinea-com.translate.goog/products/220/prueba-secuenciacion-capilar?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui"
    browser.get(url2_en)
    time.sleep(1)
    psc_info_en = browser.find_element(By.XPATH,"/html/body/div[3]/section[2]/div/div/div/div").text
    

    url3_en ="https://www-ucrenlinea-com.translate.goog/products/132/prueba-hpv-oncotect-para-ginecologos?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui"
    browser.get(url3_en)
    time.sleep(3)
    hpv_gin_info_en = browser.find_element(By.XPATH,"/html/body/div[3]/section[2]/div/div/div").text
    

    url4_en = "https://www-ucrenlinea-com.translate.goog/products/131/prueba-hpv-oncotect-para-laboratorios?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui"
    browser.get(url4_en)
    time.sleep(3)
    hpv_lab_info_en = browser.find_element(By.XPATH,"/html/body/div[3]/section[2]/div/div/div/div").text
    

    url5_en = "https://www-ucrenlinea-com.translate.goog/products/293/curso-tecnica-de-suturas-quirurgicas?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui"
    browser.get(url5_en)
    time.sleep(2)
    c_sut_info_en = browser.find_element(By.XPATH,"/html/body/div[3]/section[2]/div/div/div/div").text
    

    url6_en = "https://www-ucrenlinea-com.translate.goog/products/292/curso-basico-de-laparoscopia-para-medicos-generales?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui"
    browser.get(url6_en)
    time.sleep(2)
    c_laparo_info_en = browser.find_element(By.XPATH,"/html/body/div[3]/section[2]/div/div/div/div").text
    
    
    url7_en = "https://www-ucrenlinea-com.translate.goog/products/314/toxicidad-en-fluoropirimidinas-5-fu?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui"
    browser.get(url7_en)
    time.sleep(2)
    tox_info_en = browser.find_element(By.XPATH,"/html/body/div[3]/section[2]/div/div/div/div").text
    

    url8_en = "https://www-ucrenlinea-com.translate.goog/products/325/pcr-real-para-deteccion-de-serotipos-de-hpv?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui"
    browser.get(url8_en)
    time.sleep(2)
    pcr_info_en = browser.find_element(By.XPATH,"/html/body/div[3]/section[2]/div/div/div/div").text
    

    url9_en = "https://www-ucrenlinea-com.translate.goog/products/339/taller-de-entrenamiento-en-biopsia-al-vacio-para-deteccion-temprana-de-cancer-de-mama?_x_tr_sl=auto&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=nui"
    browser.get(url9_en)
    time.sleep(2)
    bio_info_en = browser.find_element(By.XPATH,"/html/body/div[3]/section[2]/div/div/div/div").text
    
    browser.close()
    variables_en = [geninfo_en, psc_en, psc_price_en, psc_info_en, hpv_gin_en, hpv_gin_price_en, hpv_gin_info_en, hpv_lab_en,
                hpv_lab_price_en, hpv_lab_info_en, c_sut_en, c_sut_price_en, c_sut_info_en, c_laparo_en, c_laparo_price_en, c_laparo_info_en,
                tox_en, tox_price_en, tox_info_en, pcr_en, pcr_price_en, pcr_info_en, bio_en, bio_price_en, bio_info_en]
    
    return variables_en
