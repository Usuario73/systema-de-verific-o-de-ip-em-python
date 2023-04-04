# Verificador de IP

Este é um programa simples em Python com interface gráfica construída com a biblioteca Tkinter. O programa tem como objetivo receber um endereço IP inserido pelo usuário e verificar sua classe (privado, público ou desconhecido), a máscara de sub-rede e o endereço de broadcast correspondentes.

O programa utiliza a biblioteca ipaddress para verificar se o IP inserido é válido e obter informações sobre a classe do IP, a máscara de sub-rede e o endereço de broadcast.

## Pré-requisitos

Para executar o programa, é necessário ter o Python 3 instalado na máquina, bem como a biblioteca Tkinter, que geralmente já vem incluída na instalação padrão do Python.

## Funcionamento do programa

Ao abrir a interface gráfica do programa, o usuário verá um campo de entrada para inserir um endereço IP e um botão "Verificar". Ao clicar no botão "Verificar", o programa irá realizar as seguintes verificações:

1. Verificar se o IP inserido é válido utilizando a biblioteca ipaddress.
2. Obter a classe do IP (privado, público ou desconhecido) utilizando a biblioteca ipaddress.
3. Obter a máscara de sub-rede correspondente ao IP utilizando a biblioteca ipaddress.
4. Obter o endereço de broadcast correspondente ao IP utilizando a biblioteca ipaddress.

Caso o IP inserido seja inválido, o programa exibirá uma mensagem de erro informando que o IP é inválido. Caso contrário, o programa exibirá as informações sobre a classe do IP, a máscara de sub-rede e o endereço de broadcast correspondentes ao IP inserido.

## Considerações finais

Este é um programa simples com interface gráfica construída com a biblioteca Tkinter em Python. Ele tem como objetivo mostrar como utilizar a biblioteca ipaddress para verificar informações sobre um endereço IP inserido pelo usuário. O código pode ser facilmente modificado para adicionar mais funcionalidades e melhorias na interface gráfica.
