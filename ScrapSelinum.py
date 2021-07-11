from selenium import webdriver
import mysql.connector

driver = webdriver.Chrome(executable_path="C:\Users\derba\Downloads\chromedriver_win32 (1)\chromedriver.exe")
##SQL
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mohami"
)
mycursor = mydb.cursor()
sql = "INSERT INTO collegues (nom, prenom,tb ,gouv, tel) VALUES (%s, %s,%s, %s,%s)"
##END


driver.get("https://avocat.org.tn/annuaire-441")

r = 1
while r < 40:
        nom = driver.find_elements_by_xpath("//table[@id='rounded-corner']//tbody//tr["+str(r)+"]//td[1]")[0].text
        prenom = driver.find_elements_by_xpath("//table[@id='rounded-corner']//tbody//tr["+str(r)+"]//td[2]")[0].text
        tb = driver.find_elements_by_xpath("//table[@id='rounded-corner']//tbody//tr["+str(r)+"]//td[3]")[0].text
        gouv = driver.find_elements_by_xpath("//table[@id='rounded-corner']//tbody//tr["+str(r)+"]//td[4]")[0].text
        tel = driver.find_elements_by_xpath("//table[@id='rounded-corner']//tbody//tr["+str(r)+"]//td[5]")[0].text
        val = (nom, prenom, tb, gouv, tel)
        mycursor.execute(sql, val)

        mydb.commit()
        r += 2
