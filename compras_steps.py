from behave import *
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys



@given('que estou na página de login')
def step_given_logged_in(context):

    context.driver = webdriver.Chrome(executable_path='/https://automationexercise.com/')
    context.driver.get("https://automationexercise.com/login")


@when('que estou logado como cliente cadastrado')
def step_given_logado_como_cliente_cadastrado(context, usuario, senha):
  
 username_field = context.driver.find_element_by_css_selector('input[data-qa="login-email"][name="email"]') 
 password_field = context.driver.find_element_by_css_selector('input[data-qa="login-password"][name="password"][type="password"]')
 username_field.clear() 
 password_field.clear()
 username_field.send_keys("ana01@mailinator.com")
 password_field.send_keys("Brasil@2023")
 login_button = driver.find_element_by_css_selector('button[data-qa="login-button"].btn.btn-default')
 login_button.click()


@And('eu adiciono Stylish Dress ao carrinho com quantidade {quantidade}')
def step_when_adicionar_stylish_dress(context, quantidade):
    
    stylish_dress_element = driver.find_element_by_css_selector('div[data-product-name="Stylish Dress"]')
    stylish_dress_quantity_input = stylish_dress_element.find_element_by_css_selector('input[name="quantity"]')
    stylish_dress_quantity_input.clear()
    stylish_dress_quantity_input.send_keys(quantidade)
    add_to_cart_button = stylish_dress_element.find_element_by_css_selector('button[btn btn-default cart"]')
    add_to_cart_button.click()


@And('eu adiciono Beautiful Peacock Blue Cotton Linen Saree ao carrinho com quantidade {quantidade}')
def step_when_adicionar_peacock_saree(context, quantidade):
   
   peacock_saree_element = driver.find_element_by_css_selector('div[data-product-name="Peacock Blue Cotton Linen Saree"]')
   peacock_saree_quantity_input = peacock_saree_element.find_element_by_css_selector('input[name="quantity"]')
   peacock_saree_quantity_input.clear()
   peacock_saree_quantity_input.send_keys(quantidade)
   add_to_cart_button = peacock_saree_element.find_element_by_css_selector('button[btn btn-default cart"]')
   add_to_cart_button.click()


@And('eu adiciono Men Tshirt ao carrinho com quantidade {quantidade}')
def step_when_adicionar_men_tshirt(context, quantidade):

  men_tshirt_element = driver.find_element_by_css_selector('div[data-product-name="Men Tshirt"]')
  men_tshirt_quantity_input = men_tshirt_element.find_element_by_css_selector('input[name="quantity"]')
  men_tshirt_quantity_input.clear()
  men_tshirt_quantity_input.send_keys(quantidade)
  add_to_cart_button = men_tshirt_element.find_element_by_css_selector('button[btn btn-default cart"]')
  add_to_cart_button.click()  


@then('o carrinho de compras deve conter os produtos desejados')
def step_then_carrinho_deve_conter_produtos(context):
   
carrinho_url = "https://automationexercise.com/product_details/4"
    driver.get(carrinho_url)

    produtos_desejados = [
        {"nome": "Stylish Dress", "quantidade": 3},
        {"nome": "Beautiful Peacock Blue Cotton Linen Saree", "quantidade": 2},
        {"nome": "Men Tshirt", "quantidade": 1}
    ]

    for produto in produtos_desejados:
        produto_nome = produto["nome"]
        produto_quantidade = produto["quantidade"]
        produto_element = driver.find_element_by_css_selector(f'div[data-product-name="{Stylish Dress}"]')
        quantidade_element = produto_element.find_element_by_css_selector('input[name="quantity"]')
        quantidade_no_carrinho = quantidade_element.get_attribute("value")
        assert int(quantidade_no_carrinho) == produto_quantidade


def after_all(context):
    driver.quit()


    


