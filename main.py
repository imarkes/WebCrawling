from time import sleep
from shopper import Shopper

BASE_URL = 'https://landing.shopper.com.br/'

try:
    with Shopper() as boot:
        print('Iciniando o programa...')
        boot.home_page(BASE_URL)
        boot.login('i.markes@hotmail.com', 123456)  
        boot.choice_departaments() 
        boot.set_category_products()
        boot.set_sub_category() 
        boot.get_products()
        boot.quit()

except Exception as e:
    if 'in PATH' in str(e):
        print('Erro ao encontrar o path do sistema.')
    else:
        raise e
finally:
    print('O programa será fechado!')
