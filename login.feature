# language: pt 
# encoding: utf-8

Feature: Login no Site

  Scenario: Login com sucesso
    Given que estou na página de login
    When eu insiro meu nome de usuário "ana01@mailinator.com" e senha "Brasil@2023"
    And eu clico no botão de login
    Then devo ser redirecionado para a página inicial
    And devo ver a mensagem de boas-vindas "Logged in as, Ana Maria Braga"

