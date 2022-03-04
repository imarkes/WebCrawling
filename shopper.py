import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


class Shopper(webdriver.Chrome):
    def __init__(self, path_driver=r'C:\SCRAPY\drivers\chromedriver.exe', teardown=False):
        self.path = path_driver
        self.teardown = teardown
        os.environ['PATH'] += self.path
        super(Shopper, self).__init__()
        self.implicitly_wait(15)

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def home_page(self, BASE_URL):
        self.get(BASE_URL)

    def login(self, email, password):
        entrar = self.find_element(By.XPATH, '//*[@id="benefits"]/div/div[1]/button')
        entrar.click()
        sleep(2)
        login = self.find_element(By.XPATH, "//*[@class='bt-primary bt-neg login']")
        login.click()
        sleep(2)
        email_imput = self.find_element(By.XPATH, "//*[@class='field']/input[@name='email']")
        email_imput.send_keys(email)
        senha_imput = self.find_element(By.XPATH, "//*[@class='field']/input[@name='senha']")
        senha_imput.send_keys(password)
        submit = self.find_element(By.XPATH, "//button[@type='submit']")
        submit.click()
        close_pop_up = self.find_element(By.XPATH, "//*[@class='jconfirm-buttons']/button")
        close_pop_up.click()

    def choice_departaments(self):
        self.get('https://programada.shopper.com.br/shop/alimentos')
        subcategorys = self.find_elements(By.XPATH, "//*[@class='department-name']")
        for category in subcategorys:
            print(category.text)

    def get_subcategorys(self):
        links_categorys = self.find_elements(By.XPATH, "//*[@id='product_category']//a")
        for category in links_categorys:
            url_category = category.get_attribute('href')
            return url_category

    def get_products(self):
        list_products = []
        self.get('https://programada.shopper.com.br/shop/alimentos/acucar-e-adocantes')

        products = self.find_elements(By.XPATH, "//*[@class='sc-jcEtbA fZdjSL']")
        for prod in products:
            list_products.append(prod.text.split('\n'))

        imagens = self.find_elements(By.XPATH, "//*[@class='sc-ckRZPU epfYFx']")
        for img in imagens:
            list_products.append(img.get_attribute('src'))
        print(list_products)

    def get_qtd_inventory(self):
        details = self.find_element(By.XPATH, "//*[@class='sc-PZsNp fsKnKO']")  # detail item
        details.click()
        sleep(2)
        add_item = self.find_element(By.XPATH, "//*[@class='sc-fivaXQ kAhNMO']")  # add item
        add_item.click()
        sleep(2)
        qtd_item = self.find_element(By.XPATH, "//*[@class='sc-kJpAUB cebXqI']")  # select_qtd_item
        qtd_item.click()
        sleep(2)
        quantify = self.find_element(By.XPATH, "//*[@class='max-quantify']")
        print(quantify.text)
