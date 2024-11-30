def scrape_pworks():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import os
    
    tries = 1
    def scrape():
        try:
            #sets file directory
            base_path = os.path.dirname(__file__)

            #options

            options = webdriver.ChromeOptions()
            options.add_argument('--headless')  
            options.add_argument('--disable-gpu')  # Disables GPU hardware acceleration
            options.add_argument('--no-sandbox')  # Required for some environments like Docker
            options.add_argument('--disable-dev-shm-usage')  # Avoids shared memory issues
            #initalises chrome driver
            service = Service(executable_path="/var/www/flask/Price-comparison/website/chromedriver")
            driver = webdriver.Chrome(service=service,options=options)
            #go to protein
            driver.get("https://ie.theproteinworks.com/whey-protein-80-concentrate")

            #cookies
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"onetrust-accept-btn-handler")))
            cookies = driver.find_element(By.ID,"onetrust-accept-btn-handler").click()

            #click weight 
            weight = driver.find_element(By.XPATH,"//button[text()='4kg']").click()
            

            #compare to see if weight is updated 
            WebDriverWait(driver,20).until(
                lambda driver: float(driver.find_element(By.XPATH,"//span[@class='ProductItem_price_current__y7vcV ProductItem_price_offer__c1ZxK price-offer']").text[4:9]) > 10
            )

            protein_price = driver.find_element(By.XPATH,"//span[@class='ProductItem_price_current__y7vcV ProductItem_price_offer__c1ZxK price-offer']")
            protein_price = float(protein_price.text[4:9])
            
            

             #go to creatine
            driver.get("https://ie.theproteinworks.com/creatine-monohydrate")
            weight = driver.find_element(By.XPATH,"//button[text()='1kg']").click()
            #compare to see if weight is updated 
            WebDriverWait(driver,20).until(
                lambda driver: float(driver.find_element(By.XPATH,"//span[@class='ProductItem_price_current__y7vcV ProductItem_price_offer__c1ZxK price-offer']").text[4:9]) > 10
            )

            creatine_price = float(driver.find_element(By.XPATH,"//span[@class='ProductItem_price_current__y7vcV ProductItem_price_offer__c1ZxK price-offer']").text[4:9])
            


            
            driver.quit()
            return(protein_price,creatine_price)
        except:
            driver.quit()
    price = scrape()       
    while price == None and tries<10:     
        price = scrape()
        tries+=1
    
    return(price)

