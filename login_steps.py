from behave import *
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys



@given('que estou na página de login')
def step_given_logged_in(context):

    context.driver = webdriver.Chrome(executable_path='/https://automationexercise.com/')
    context.driver.get("https://automationexercise.com/login")


@when('eu insiro meu nome de usuário "{usuario}" e senha "{senha}"')
def step_when_inserir_usuario_e_senha(context, usuario, senha):

    username_field = context.driver.find_element_by_css_selector('input[data-qa="login-email"][name="email"]') 
    password_field = context.driver.find_element_by_css_selector('input[data-qa="login-password"][name="password"][type="password"]')
    username_field.clear()
    password_field.clear()
    username_field.send_keys("ana01@mailinator.com")
    password_field.send_keys("Brasil@2023")


@And('eu clico no botão de login')
def step_and_clicar_botao_login(context):
   
    login_button = driver.find_element_by_css_selector('button[data-qa="login-button"].btn.btn-default')
    login_button.click()

@then('devo ser redirecionado para a página inicial')
def step_then_redirecionado_para_pagina_inicial(context):

    pagina_inicial_url = "https://automationexercise.com/" 
    url_atual = driver.current_url
    assert url_atual == pagina_inicial_url

    @And('devo ver a mensagem de boas-vindas "{mensagem}"')
    def step_and_ver_mensagem_boas_vindas(context, mensagem):

    mensagem_element = driver.find_element_by_class_name("fa-user")
    assert mensagem_element.text == mensagem


def after_all(context):
    driver.quit()


