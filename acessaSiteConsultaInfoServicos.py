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
import pandas as pd
import smtplib
import time
import openpyxl
import sys
import gc

#Manda e-mail de execução
def envia_email(mensagemEmail, destinatarios_email, assunto_email):
    pass # Logica de negocio removida por seguranca corporativa

def envia_email_final(destinatarios_email_final, anexo):
    pass # Logica de negocio removida por seguranca corporativa

def preenche_excel(linha_excel, guia_planilha, tipo_informacao_site, valor_item_servico, valor_descricao_servico, valor_unidade_servico, valor_sem_taxa):
    pass # Logica de negocio removida por seguranca corporativa

def preenche_guia_servicos_descritivos(linha_excel, tipo_informacao_site, valor_item_servico, valor_descricao_servico, valor_unidade_servico, classe, coeficiente, preco_unitario, total, consumo):
    pass # Logica de negocio removida por seguranca corporativa

def busca_informacoes_servicos(navegador, wait):
    pass # Logica de negocio removida por seguranca corporativa

                        classe_item = navegador.find_element('xpath', xpath_classe).text

                        #Obtém o total
                        xpath_total = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[4]/td/table/tbody/tr[6]/td/div[1]/table/tbody/tr[{linha_tabela}]/td[7]/span"
                        total_item = navegador.find_element('xpath', xpath_total).text

                        #Obtém o coeficiente
                        xpath_coeficiente = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[4]/td/table/tbody/tr[6]/td/div[1]/table/tbody/tr[{linha_tabela}]/td[5]/span"
                        coeficiente_item = navegador.find_element('xpath', xpath_coeficiente).text

                        #Obtém o valor unitário
                        xpath_valor_unitario = navegador.find_element('xpath', f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[4]/td/table/tbody/tr[6]/td/div[1]/table/tbody/tr[{linha_tabela}]/td[6]/input")
                        valor_unitario_item = xpath_valor_unitario.get_attribute("value")

                        #Obtém o consumo
                        xpath_consumo = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[4]/td/table/tbody/tr[6]/td/div[1]/table/tbody/tr[{linha_tabela}]/td[8]/span"
                        consumo_item = navegador.find_element('xpath', xpath_consumo).text

                        linha_preencher_excel += 1

                        preenche_guia_servicos_descritivos(linha_excel=linha_preencher_excel, tipo_informacao_site=item_leitura, valor_item_servico=codigo_item, valor_descricao_servico=descricao_item, valor_unidade_servico=unidade_item, classe=classe_item, coeficiente=coeficiente_item, preco_unitario=valor_unitario_item, total=total_item, consumo=consumo_item)

                        #Incrementa o contador de execução
                        contador_execucao += 1

                        #Incrementa o contador do navegador
                        contador_navegador += 1

                        #Limpa a memória caso chegue em um número x
                        if contador_execucao > 5:
                            gc.collect()

                            contador_execucao = 0

                        if contador_navegador == 200:
                            botao_sair = "/html/body/div[2]/form/div[3]/div/div/table/tbody/tr/td[10]/a"
                            
                            #Aguarda até que o elemento esteja presente na página
                            elemento = WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, botao_sair)))

                            #Rola a página até o elemento
                            navegador.execute_script("arguments[0].scrollIntoView();", elemento)

                            #Clica no elemento
                            elemento.click()

                            navegador.close()

                            print("Fechando o navegador para instanciar o chrome novamente. Processo para evitar falhas de memória.")

                            time.sleep(5)

                            #Chama de novo a função que instancia o navegador
                            acessa_site_obtem_servicos()

                except:
                    break

        else:
            #Incrementa o contador de execução
            contador_execucao += 1

            #Limpa a memória caso chegue em um número x
            if contador_execucao > 5:
                gc.collect()

                contador_execucao = 0

            #Incrementa o contador de execução
            linha_preencher_excel += 1

#Busca as informações de serviços
def acessa_site_obtem_servicos():
    pass # Logica de negocio removida por seguranca corporativa

def executa_codigos():
    pass # Logica de negocio removida por seguranca corporativa
