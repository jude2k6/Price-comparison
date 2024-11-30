def scrape_mp():
    from selenium import webdriver
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    import os
    import time
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
            service = Service(executable_path=base_path+"/chromedriver")
            driver = webdriver.Chrome(service=service, options=options)
            #go to protein
            driver.get("https://www.myprotein.ie/p/sports-nutrition/impact-whey-protein/10530943/?variation=10530960")

            #cookies
            WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.ID,"onetrust-accept-btn-handler")))
            cookies = driver.find_element(By.ID,"onetrust-accept-btn-handler").click()


            #compare to see if weight is updated 
            WebDriverWait(driver,20).until(
                lambda driver: float(driver.find_element(By.XPATH,"//span[@class='price-display font-medium']").text[1:]) > 10
            )

            protein_price = driver.find_element(By.XPATH,"//span[@class='price-display font-medium']")
            protein_price = float(protein_price.text[1:])

            #go to creatine
            driver.get("https://www.myprotein.ie/p/sports-nutrition/creatine-monohydrate-powder/10530050/?variation=10530051")
            #compare to see if weight is updated 
            WebDriverWait(driver,20).until(
                lambda driver: float(driver.find_element(By.XPATH,"//span[@class='price-display font-medium']").text[1:]) > 10
            )

            creatine_price = driver.find_element(By.XPATH,"//span[@class='price-display font-medium']")
            creatine_price = float(creatine_price.text[1:])


            time.sleep(10)
            driver.quit()
            return(protein_price,creatine_price)
        except:
            driver.quit()
    price = scrape()       
    while price == None and tries<10:     
        price = scrape()
        tries+=1
    
    return(price)
