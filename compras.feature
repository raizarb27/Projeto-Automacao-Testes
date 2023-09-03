# language: pt 
# encoding: utf-8

Feature: Compra de Produtos no E-commerce

  Scenario: Comprar produtos no E-commerce
    Given que estou logado como cliente cadastrado
    When eu adiciono Stylish Dress ao carrinho com quantidade 3
    And eu adiciono Beautiful Peacock Blue Cotton Linen Saree ao carrinho com quantidade 2
    And eu adiciono Men Tshirt ao carrinho com quantidade 1
    Then o carrinho de compras deve conter os produtos desejados
