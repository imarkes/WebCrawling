import os
from re import sub
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from bs4 import BeautifulSoup


PATH_DRIVER = r'C:\WebCrawling\drivers'


class Shopper(webdriver.Chrome):
    def __init__(self, path_driver=PATH_DRIVER, teardown=False):
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
        subcategorys = self.find_elements(By.XPATH, "//*[@class='department-name']")
        print('Categorias encontradas no departamento: ')
        for category in subcategorys:
            print('Category: ', category.text)

    def set_category_products(self):
        category = self.find_element(By.XPATH, "//*[@department='alimentos']")  # Alimentos
        sleep(2)
        action = ActionChains(self)
        action.move_to_element(category).perform()
        sleep(2)
        category_set = self.find_element(By.XPATH, "//*[@department='alimentos']//a[text()='Todos']")
        sleep(2)
        category_set.click()

    def set_sub_category(self):
        subcategory = self.find_element(By.XPATH, "//*[@class='sc-epFoly gVIHAp']")
        subcategory.click()
        

    def get_products(self):
        print('-'*20)
        products = self.find_element(By.XPATH, "//*[@class='sc-fDZUdJ keuats']")
        content_html = products.get_attribute('outerHTML') 
        soup = BeautifulSoup(content_html, 'html.parser')
        list_products = soup.find('p', class_='sc-kHdrYz dUFjAH').text()
        print(list_products)
        img = soup.find('img', class_='sc-ckRZPU epfYFx').get('href')
        print(img)
        #for p in list_products:
        #    print(p.get_text())
        #print(soup.prettify())













if __name__ == '__main__':
    ...
