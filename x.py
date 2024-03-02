from selenium import webdriver
import time

# Tarayıcıyı başlat
browser = webdriver.Safari()

# Instagram'ın ana sayfasına git
browser.get("https://www.instagram.com")

# Sayfa yüklenene kadar beklet
time.sleep(10)

# Giriş yap butonunu bul ve tıkla
# XPath güncellendi, çünkü Instagram'ın sayfa yapısı değişmiş olabilir.
giris_yap = browser.find_element_by_xpath("//a[contains(text(),'Giriş yap')]")
giris_yap.click()

# Yeni sayfa yüklenene kadar beklet
time.sleep(2)

# Kullanıcı adı ve şifre alanlarını bul
username = browser.find_element_by_name("username")
password = browser.find_element_by_name("password")

# Kullanıcı adı ve şifreyi gönder
username.send_keys("giris_adi")  # "giris_adi" yerine gerçek kullanıcı adınızı girin
password.send_keys("sifre")      # "sifre" yerine gerçek şifrenizi girin

# Giriş yap butonunu bul ve tıkla
# Bu adım eksikti, giriş yapmak için gerekli
giris_yap_butonu = browser.find_element_by_xpath("//button[contains(text(),'Giriş yap')]")
giris_yap_butonu.click()

# İşlemler tamamlandıktan sonra tarayıcıyı kapat
time.sleep(5)  # Giriş işleminin tamamlanmasını beklet
browser.close()
