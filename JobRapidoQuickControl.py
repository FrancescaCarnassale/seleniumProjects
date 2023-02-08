from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
"""
Questi sono i dati della ricerca che verrà effettuata. Possono essere inseriti dal lavoratore o manualmente
"""
countries=['it'] #elenco dei countries da checkare
city= "Roma"#input("In che città italiana vuoi cercare il lavoro?")
#job=input("Che lavoro desideri cercare?")
fileWrongJobs = open("C:\Users\CARNASSALEF\Desktop","a")
"""
Ricerca effettiva
"""
driver = webdriver.Firefox()
for country in countries:
    driver.get("https://%s.jobrapido.com/" % country)
    driver.find_element(By.XPATH, '//button[@class="clear-button"]').click()
    driver.find_element(By.XPATH, '//input[@name="l"]').send_keys(city)
    driver.find_element(By.XPATH, '//input[@class="jr-button"]').click()
    driver.find_element(By.XPATH, '//button[@class="modal-close icon-cancel"]').click()
    jobs = driver.find_elements(By.XPATH,"//a[contains(@class, 'result-item__link')]")
    titles= driver.find_elements(By.XPATH,'//div[@class="result-item__title  result-item__title--no-date"]')
    companies= driver.find_elements(By.XPATH,'//span[@class="result-item__company-label"]')
    locations= driver.find_elements(By.XPATH,'//span[@class="result-item__location-label"]')
    driver.find_element(By.XPATH, '//button[@class="iubenda-cs-accept-btn iubenda-cs-btn-primary"]').click()
    for (job, title, company, location) in zip(jobs,titles,companies,locations):
        title=title.text.lower()
        company=company.text.lower()
        location=location.text.lower()
        WebDriverWait(driver, 20).until(EC.element_to_be_clickable(job)).click() #clicko sul job
        time.sleep(5) #attendo che la nuova pagina carichi
        #switcho scheda
        driver.switch_to.window(driver.window_handles[1])
        get_url = driver.current_url
        #lavoro sulla nuova scheda
        workPage=driver.page_source.lower()
        if( title not in workPage or company not in workPage or location not in workPage):
            #fileWrongJobs.write("Pagina corrente non corretta "+ get_url +"Titolo: %s Company: %s Location: %s" % (title, company, location))
            print("Pagina corrente non corretta "+ get_url +" Titolo: %s Company: %s Location: %s" % (title, company, location))
        driver.close()
        #ritorno indietro alla pagina precedente
        driver.switch_to.window(driver.window_handles[0])
    fileWrongJobs.close()