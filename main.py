
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import datetime
import time
import signal



# Le code cessera de s'exécuter après 720 secondes == 10 minutes.
signal.alarm(720) 



now = datetime.datetime.now()
current_time = now.strftime("%H:%M / %A")
 # %A est d'obtenir le nom du jour !
justtime = now.strftime("%H:%M")
print (current_time)

#  Code pour autoriser l'accès au microphone, à la caméra et aux notifications
# 0 est désactivé et 1 est autorisé.
opt = Options()
opt.add_argument("--disable-infobars")
opt.add_argument("start-maximized")
opt.add_argument("--disable-extensions")
# Passez l'argument 1 pour autoriser et 2 pour bloquer
opt.add_experimental_option("prefs", { \
"profile.default_content_setting_values.media_stream_mic": 1, 
"profile.default_content_setting_values.media_stream_camera": 1,
"profile.default_content_setting_values.geolocation": 1, 
"profile.default_content_setting_values.notifications": 1 
})

# Conditions à vérifier l'heure et à ajouter si nécessaire
while justtime !=  "09:50" or justtime != "13:50" or justtime != "15:20" or  justtime != "16:50":
    time.sleep(20)
    now = datetime.datetime.now()
    current_time = now.strftime("%H:%M / %A")
    justtime = now.strftime("%H:%M")
    print(justtime)
    if justtime == "09:50" or justtime == "13:50" or justtime == "15:20" or  justtime == "16:50":
        print("Le cours va commencer dans 10 minutes.")
        break
    
# diriger vers le lien à visiter ; Le programme se connecte d'abord à Gmail pour un accès complet aux services Google.
def gmail_login():
    driver.get("https://accounts.google.com/ServiceLogin?service=mail&passive=true&rm=false&continue=https://mail.google.com/mail/&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1#identifier")
    time.sleep(4)
    driver.find_element_by_xpath("//input[@name='identifier']").send_keys("####EMAIL ADDRESS HERE####")
    time.sleep(2)
        # Bouton Suivant:
    driver.find_element_by_xpath("//*[@id='identifierNext']/div/button/div[2]").click()
    time.sleep(5)
        #Mot de passe:
    driver.find_element_by_xpath("//input[@name='password']").send_keys("#your email password herer###")
    time.sleep(2)
        #Bouton Suivant:
    driver.find_element_by_xpath("//*[@id='passwordNext']/div/button").click()
    time.sleep(5)
        # #Ouvrir la réunion:
    driver.get(sub)
    driver.refresh()
    time.sleep(5)
        # Désactiver la vidéo
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[2]/div/div").click()
    time.sleep(5)
        # désactiver le son
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[1]/div[1]/div[3]/div[1]/div/div/div").click()
    time.sleep(180)
        # Rejoindre la classe
    driver.find_element_by_xpath("//*[@id='yDmH0d']/c-wiz/div/div/div[4]/div[3]/div/div[2]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span").click()

# Conditions qui vérifient l'heure et vont au lien de classe si les cours ont lieu à ce moment-là.

# Math
if current_time == "09:50 / Monday" or current_time == "16:50 / Tuesday" or current_time == "13:50 / Thursday" or current_time == "15:20 / Friday":
    #sub est l'identifiant de classe avec le lien de rencontre. sub change avec le temps selon la classe.
    sub = "###hangouts meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver') 
    #vous devrez remplacer executable_path=r'chromeddriver' par le chemin où vous avez téléchargé le chromedriver ou n'importe quel navigateur. J'ai utilisé du chrome pour le test.
    gmail_login()
    

# Physique 
elif current_time == "13:50 / Monday" or current_time == "16:50 / Wednesday":
    sub = " ###hangouts meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

# Anglais 
elif current_time == "15:20 / Monday" or current_time == "16:50 / Thursday" :
    sub = "###hangouts meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

#Chimie
elif current_time == "16:50 / Monday" or current_time == "15:20 / Wednesday":
    sub = "###hangouts meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

#Langage C
elif current_time == "13:52 / Tuesday" or current_time == "16:50 / Friday":
    sub = "###hangouts meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

# Cloud
elif current_time == "15:20 / Tuesday" or current_time == "13:50 / Friday":
    sub = "###hangouts meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

# POO
elif current_time == "13:50 / Wednesday" or current_time == "15:20 / Thursday":
    sub = "###hangouts meet links here with time variations###"
    driver = webdriver.Chrome(chrome_options=opt, executable_path=r'chromedriver')
    gmail_login()
    

else:
    print("Pas de cours en ce moment")


    
