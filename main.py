from shopper import Shopper

BASE_URL = 'https://landing.shopper.com.br/'

with Shopper() as boot:
    boot.home_page(BASE_URL)
    boot.login('i.markes@hotmail.com', 123456)
    boot.choice_departaments()
    boot.get_subcategorys()
    boot.get_products()
    boot.get_qtd_inventory()
    boot.quit()

