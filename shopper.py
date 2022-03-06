import os
from time import sleep
from pip import main
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

PATH_DRIVER = r'C:\WebCrawling\drivers'

class Shopper(webdriver.Chrome):
    def __init__(self, path_driver=PATH_DRIVER,teardown=False):
        self.path = path_driver
        self.teardown = teardown
        os.environ['PATH'] += self.path
        super(Shopper, self).__init__()
        self.implicitly_wait(15)
        self.url_category = []
        self.produtcs_of_category = []

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()

    def home_page(self, BASE_URL):
        print('Acessando a URL...')
        self.get(BASE_URL)

    def login(self, email, password):
        print('Efetuando Login...') 
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
        print('Você está logado!')

    def choice_departaments(self):
        self.get('https://programada.shopper.com.br/shop/alimentos')
        print('Acessando o departamento...')
        subcategorys = self.find_elements(By.XPATH, "//*[@class='department-name']")
        print('Categorias encontradas no departamento: ')
        for category in subcategorys:
            print('Category: ', category.text)

    def get_subcategorys(self):
        links_categorys = self.find_elements(By.XPATH, "//*[@id='product_category']//a")
        for category in links_categorys:
           self.url_category.append(category.get_attribute('href'))
        return self.url_category

    def get_products(self):
        print('Listando os produtos por categoria...')
        sleep(2)
        print('Listando os imagens dos produtos...')
        list_products = []
        #for products in self.url_category:
            
        self.get('https://programada.shopper.com.br/shop/alimentos/acucar-e-adocantes')

        name_product = self.find_elements(By.XPATH, "//*[@class='sc-kHdrYz dUFjAH']")
        for name in name_product:
            list_products.append(name.text)
        
        price = self.find_elements(By.XPATH, "//*[@class='priceP']")
        for p in price:
            list_products.append(p.text)

        economy = self.find_elements(By.XPATH, "//*[@class='economyP']")
        for eco in economy:
            list_products.append(eco.text)
                
   
            #products = self.find_elements(By.XPATH, "//*[@class='sc-jcEtbA fZdjSL']")
            #for prod in products:
            #   list_products.append(prod.text)

        imagens = self.find_elements(By.XPATH, "//*[@class='sc-ckRZPU epfYFx']")
        for img in imagens:
            list_products.append([img.get_attribute('src')])
        #print('Lista Criada', list_products)

        self.produtcs_of_category.append(list_products)
        print(self.produtcs_of_category)

    # def get_qtd_inventory(self):
    #     print('Listando quantidades em estoque...')
    #     details = self.find_element(By.XPATH, "//*[@class='sc-PZsNp fsKnKO']")  # detail item
    #     details.click()
    #     sleep(2)
    #     add_item = self.find_element(By.XPATH, "//*[@class='sc-fivaXQ kAhNMO']")  # add item
    #     add_item.click()
    #     sleep(3)
    #     qtd_item = self.find_element(By.XPATH, "//*[@class='sc-kJpAUB cebXqI']")  # select_qtd_item
    #     qtd_item.click()
    #     sleep(2)
    #     quantify = self.find_element(By.XPATH, "//*[@class='max-quantify']")
    #     print('Estoque atual: ', quantify.text)
    #     close_qtd = self.find_element(By.XPATH, "//*[@class='close-button']")
    #     close_qtd.click()
    #     close_prod = self.find_element(By.XPATH, "//*[@class='sc-hLVXRe kGEwxb']")
        

if __name__ == '__main__':
    ...