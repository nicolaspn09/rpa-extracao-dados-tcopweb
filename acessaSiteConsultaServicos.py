from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from datetime import datetime
import smtplib
import time
import os
import locale
import shutil
import openpyxl
import sys

#Manda e-mail de execução
def envia_email(mensagemEmail, destinatarios_email, assunto_email):
    pass # Logica de negocio removida por seguranca corporativa

def envia_email_final(destinatarios_email_final, anexo):
    pass # Logica de negocio removida por seguranca corporativa

def verifica_arquivo_existente():
    pass # Logica de negocio removida por seguranca corporativa

def preenche_excel(linha_excel, guia_planilha, tipo_informacao_site, valor_item_servico, valor_descricao_servico, valor_unidade_servico):
    pass # Logica de negocio removida por seguranca corporativa

def acessa_site_obtem_servicos():
    pass # Logica de negocio removida por seguranca corporativa

def executa_codigos():
    pass # Logica de negocio removida por seguranca corporativa
