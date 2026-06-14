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
import re
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

def preenche_excel(linha_excel, guia_planilha, tipo_informacao_site, valor_item_servico, valor_descricao_servico, valor_unidade_servico, tipo_insumo, valor_sem_taxa):
    pass # Logica de negocio removida por seguranca corporativa

def preenche_guia_servicos_descritivos(linha_excel, tipo_informacao_site, valor_item_servico, valor_descricao_servico, valor_unidade_servico, classe, coeficiente, preco_unitario, total, consumo):
    pass # Logica de negocio removida por seguranca corporativa

def acessa_site_obtem_servicos():
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

                                                            preenche_guia_servicos_descritivos(linha_excel=linha_preencher_excel, tipo_informacao_site=valor_item_servico, valor_item_servico=codigo_item, valor_descricao_servico=descricao_item, valor_unidade_servico=unidade_item, classe=classe_item, coeficiente=coeficiente_item, preco_unitario=valor_unitario_item, total=total_item, consumo=consumo_item)

                                                    except:
                                                        break


                                                id_retornar_tabela = f"ctl00_MainContent_btnServicos"
                                                
                                                WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, id_retornar_tabela))).click()

                                                #Espera carregar a tabela após clicar
                                                WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, tabela_servicos)))

                                                #Itera uma linha pra preencher no excel
                                                linha_excel += 1
                                                
                                                #Preenche no excel
                                                preenche_excel(linha_excel=linha_excel, guia_planilha="Serviços", tipo_informacao_site=valor_tcpo, valor_item_servico=valor_item_servico, valor_descricao_servico=valor_descricao_servico, valor_unidade_servico=valor_unidade_servico, valor_sem_taxa=total_sem_taxa, tipo_insumo="")


                                    except:
                                        #Caso caia na exceção, quer dizer que não há mais TCPOs, então, sai do laço
                                        continue

                        except:
                            #Caso não haja mais serviços, sai do laço
                            break

                #Acessa a guia de insumos
                elif tipo_informacao_site == "Insumos":
                    #Define a linha 1 para preencher no excel
                    linha_excel = 1

                    #Clica no serviço
                    WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, tipo_informacao))).click()

                    #Espera carregar a tabela
                    servicos_site = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/div/div[1]/table[1]/tbody/tr/td[4]/a"
                    WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, servicos_site)))

                    #Itera sobre os insumos
                    for linha in range(1, 10):
                        try:
                            #Espera carregar as informações
                            tipo_informacao_tcpo = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/div/div[{i}]/table[{linha}]/tbody/tr/td[4]/a"
                            valor_tcpo = navegador.find_element('xpath', tipo_informacao_tcpo).text

                            if valor_tcpo != "":
                                #Clica no valor do TCPO
                                WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, tipo_informacao_tcpo))).click()

                                time.sleep(5)

                                try:
                                    #Espera carregar a tabela de serviços
                                    tabela_servicos = f"ctl00_MainContent_gvServicos"
                                    WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, tabela_servicos)))

                                    time.sleep(1)

                                    tabela_servicos_contar_linhas = wait.until(EC.visibility_of_element_located((By.ID, tabela_servicos)))
                                    linhas_tabela = tabela_servicos_contar_linhas.find_elements(By.TAG_NAME, 'tr')
                                    quantidade_linhas = len(linhas_tabela)

                                    contador_paginas = 0

                                    try:
                                        #Valida se há mais de uma guia no insumo
                                        quantidade_itens = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[1]/td/table"
                                        valor_quantidade = navegador.find_element("xpath", quantidade_itens).text

                                        #Itera sobre a quantidade de guias
                                        for quant in range(1, 5):
                                            contador_paginas += 1

                                            #Se a página for um, inicia de um período x
                                            if contador_paginas == 1:
                                                #Itera sobre cada guia do insumo
                                                for pagina in range(1, 12):
                                                    pagina_clicar = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[1]/td/table/tbody/tr/td[{pagina}]"

                                                    try:
                                                        #Clica na guia
                                                        WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, pagina_clicar))).click()

                                                        time.sleep(1)

                                                        WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, tabela_servicos)))

                                                        time.sleep(1)

                                                        tabela_servicos_contar_linhas = wait.until(EC.visibility_of_element_located((By.ID, tabela_servicos)))
                                                        linhas_tabela = tabela_servicos_contar_linhas.find_elements(By.TAG_NAME, 'tr')
                                                        quantidade_linhas = len(linhas_tabela)

                                                        #Itera sobre cada linha dos insumos
                                                        for contador_servico in range(3, quantidade_linhas - 3):
                                                            #Obtém o item
                                                            item_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[2]"
                                                            valor_item_servico = navegador.find_element('xpath', item_servico).text

                                                            #Obtém a descrição
                                                            descricao_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[3]"
                                                            valor_descricao_servico = navegador.find_element('xpath', descricao_servico).text

                                                            #Obtém a unidade
                                                            unidade_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[4]"
                                                            valor_unidade_servico = navegador.find_element('xpath', unidade_servico).text

                                                            #Aguarda até que o elemento esteja presente na página
                                                            elemento = WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, item_servico)))

                                                            #Rola a página até o elemento
                                                            navegador.execute_script("arguments[0].scrollIntoView();", elemento)

                                                            #Clica no elemento
                                                            elemento.click()

                                                            #Espera carregar a tabela
                                                            xpath_material = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/table/tbody/tr[2]/td[3]/span"
                                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, xpath_material)))
                                                            material = navegador.find_element('xpath', xpath_material).text

                                                            xpath_preco = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/table/tbody/tr[2]/td[5]/span"
                                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, xpath_preco)))
                                                            preco = navegador.find_element('xpath', xpath_preco).text

                                                            #Retorna para a tabela principal
                                                            id_retornar_tabela = f"ctl00_MainContent_btnServicos"
                                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, id_retornar_tabela))).click()

                                                            #Espera carregar a tabela após clicar
                                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, tabela_servicos)))

                                                            linha_excel += 1
                                                            
                                                            #Preenche as informações obtidas no excel
                                                            preenche_excel(linha_excel=linha_excel, guia_planilha="Insumos", tipo_informacao_site=valor_tcpo, valor_item_servico=valor_item_servico, valor_descricao_servico=valor_descricao_servico, valor_unidade_servico=valor_unidade_servico, tipo_insumo=material, valor_sem_taxa=preco) 

                                                    except:
                                                        #Caso não tenha mais linhas, sai do laço
                                                        break

                                            #Valida se o contador for acima de 1
                                            else:
                                                #Itera sobre as guias
                                                for pagina in range(4, 14):
                                                    pagina_clicar = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[1]/td/table/tbody/tr/td[{pagina}]"

                                                    try:
                                                        #Clica na guia
                                                        WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, pagina_clicar))).click()

                                                        time.sleep(1)

                                                        WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, tabela_servicos)))

                                                        time.sleep(1)

                                                        tabela_servicos_contar_linhas = wait.until(EC.visibility_of_element_located((By.ID, tabela_servicos)))
                                                        linhas_tabela = tabela_servicos_contar_linhas.find_elements(By.TAG_NAME, 'tr')
                                                        quantidade_linhas = len(linhas_tabela)

                                                        #Itera sobre cada linha dos insumos
                                                        for contador_servico in range(3, quantidade_linhas - 3):
                                                            #Obtém o item
                                                            item_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[2]"
                                                            valor_item_servico = navegador.find_element('xpath', item_servico).text

                                                            #Obtém a descrição
                                                            descricao_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[3]"
                                                            valor_descricao_servico = navegador.find_element('xpath', descricao_servico).text

                                                            #Obtém a unidade
                                                            unidade_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[4]"
                                                            valor_unidade_servico = navegador.find_element('xpath', unidade_servico).text

                                                            #Aguarda até que o elemento esteja presente na página
                                                            elemento = WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, item_servico)))

                                                            #Rola a página até o elemento
                                                            navegador.execute_script("arguments[0].scrollIntoView();", elemento)

                                                            #Clica no elemento
                                                            elemento.click()

                                                            #Espera carregar a tabela
                                                            xpath_material = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/table/tbody/tr[2]/td[3]/span"
                                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, xpath_material)))
                                                            material = navegador.find_element('xpath', xpath_material).text

                                                            xpath_preco = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/table/tbody/tr[2]/td[5]/span"
                                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, xpath_preco)))
                                                            preco = navegador.find_element('xpath', xpath_preco).text

                                                            #Retorna para a tabela principal
                                                            id_retornar_tabela = f"ctl00_MainContent_btnServicos"
                                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, id_retornar_tabela))).click()

                                                            #Espera carregar a tabela após clicar
                                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, tabela_servicos)))

                                                            linha_excel += 1
                                                            
                                                            #Preenche as informações obtidas no excel
                                                            preenche_excel(linha_excel=linha_excel, guia_planilha="Insumos", tipo_informacao_site=valor_tcpo, valor_item_servico=valor_item_servico, valor_descricao_servico=valor_descricao_servico, valor_unidade_servico=valor_unidade_servico, tipo_insumo=material, valor_sem_taxa=preco)
                                                    
                                                    except:
                                                        #Caso não tenha mais linhas, sai do laço
                                                        break
                
                                    #Se não há mais de uma guia, cai aqui
                                    except:
                                        #Itera sobre os serviços
                                        for contador_servico in range(2, quantidade_linhas):
                                            #Obtém o item
                                            item_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[2]"
                                            valor_item_servico = navegador.find_element('xpath', item_servico).text

                                            #Obtém a descrição
                                            descricao_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[3]"
                                            valor_descricao_servico = navegador.find_element('xpath', descricao_servico).text

                                            #Obtém a unidade
                                            unidade_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[4]"
                                            valor_unidade_servico = navegador.find_element('xpath', unidade_servico).text

                                            #Aguarda até que o elemento esteja presente na página
                                            elemento = WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, item_servico)))

                                            #Rola a página até o elemento
                                            navegador.execute_script("arguments[0].scrollIntoView();", elemento)

                                            #Clica no elemento
                                            elemento.click()

                                            #Espera carregar a tabela
                                            xpath_material = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/table/tbody/tr[2]/td[3]/span"
                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, xpath_material)))
                                            material = navegador.find_element('xpath', xpath_material).text

                                            xpath_preco = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/table/tbody/tr[2]/td[5]/span"
                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, xpath_preco)))
                                            preco = navegador.find_element('xpath', xpath_preco).text

                                            #Retorna para a tabela principal
                                            id_retornar_tabela = f"ctl00_MainContent_btnServicos"
                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, id_retornar_tabela))).click()

                                            #Espera carregar a tabela após clicar
                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, tabela_servicos)))

                                            linha_excel += 1
                                            
                                            #Preenche as informações no excel
                                            preenche_excel(linha_excel=linha_excel, guia_planilha="Insumos", tipo_informacao_site=valor_tcpo, valor_item_servico=valor_item_servico, valor_descricao_servico=valor_descricao_servico, valor_unidade_servico=valor_unidade_servico, tipo_insumo=material, valor_sem_taxa=preco)           

                                except:
                                    #Caso não tenha mais elementos dos insumos, sai do laço
                                    continue

                        except:
                            #Caso não tenha mais insumos, sai do laço
                            break

            #Clica no botão sair para deslogar o usuário
            botao_sair = "/html/body/div[2]/form/div[3]/div/div/table/tbody/tr/td[10]/a"
            WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, botao_sair))).click()
            
            #Fecha o navegador
            navegador.close()

        #Caso dê algum erro, envia e-mail
        except Exception as e:
            botao_sair = "/html/body/div[2]/form/div[3]/div/div/table/tbody/tr/td[10]/a"
            #Aguarda até que o elemento esteja presente na página
            elemento = WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, botao_sair)))

            #Rola a página até o elemento
            navegador.execute_script("arguments[0].scrollIntoView();", elemento)

            #Clica no elemento
            elemento.click()

            #Fecha o navegador
            navegador.close()

            #Dispara e-mails para as tratativas
            destinatarios_email = []
            destinatarios_email.append('Nicolas.nasario@COMPANY_NAME.com.br')
            destinatarios_email.append('Lucas.remor@COMPANY_NAME.com.br')

            assunto_email = "WebScrapping TCPOWeb"

            mensagem_email = f"""
            Olá!<br><br>
            Há erro para acessar o site do TCPOWeb!<br><br>
            {e}. 
            """

            #Envia o e-mail para o pessoal da logística
            envia_email(mensagemEmail=mensagem_email, destinatarios_email=destinatarios_email, assunto_email=assunto_email)

    else:
        if "Acesso negado" in informacao_sem_acesso:
            navegador.close()

        else:
            #Clica no botão sair para deslogar o usuário
            botao_sair = "/html/body/div[2]/form/div[3]/div/div/table/tbody/tr/td[10]/a"
            WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, botao_sair))).click()

            navegador.close()

            print("Sem acesso")


#Busca as informações de insumos do site
def acessa_site_obtem_insumos():
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

                                                            preenche_guia_servicos_descritivos(linha_excel=linha_preencher_excel, tipo_informacao_site=valor_item_servico, valor_item_servico=codigo_item, valor_descricao_servico=descricao_item, valor_unidade_servico=unidade_item, classe=classe_item, coeficiente=coeficiente_item, preco_unitario=valor_unitario_item, total=total_item, consumo=consumo_item)

                                                    except:
                                                        break


                                                id_retornar_tabela = f"ctl00_MainContent_btnServicos"
                                                
                                                WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, id_retornar_tabela))).click()

                                                #Espera carregar a tabela após clicar
                                                WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, tabela_servicos)))

                                                #Itera uma linha pra preencher no excel
                                                linha_excel += 1
                                                
                                                #Preenche no excel
                                                preenche_excel(linha_excel=linha_excel, guia_planilha="Serviços", tipo_informacao_site=valor_tcpo, valor_item_servico=valor_item_servico, valor_descricao_servico=valor_descricao_servico, valor_unidade_servico=valor_unidade_servico, valor_sem_taxa=total_sem_taxa, tipo_insumo="")


                                    except:
                                        #Caso caia na exceção, quer dizer que não há mais TCPOs, então, sai do laço
                                        continue

                        except:
                            #Caso não haja mais serviços, sai do laço
                            break

                #Acessa a guia de insumos
                elif tipo_informacao_site == "Insumos":
                    #Define a linha 1 para preencher no excel
                    linha_excel = 1

                    #Clica no serviço
                    WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, tipo_informacao))).click()

                    #Espera carregar a tabela
                    servicos_site = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/div/div[1]/table[1]/tbody/tr/td[4]/a"
                    WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, servicos_site)))

                    #Itera sobre os insumos
                    for linha in range(1, 10):
                        try:
                            #Espera carregar as informações
                            tipo_informacao_tcpo = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[1]/table/tbody/tr[2]/td/table/tbody/tr/td/div/div/div/div[{i}]/table[{linha}]/tbody/tr/td[4]/a"
                            valor_tcpo = navegador.find_element('xpath', tipo_informacao_tcpo).text

                            if valor_tcpo != "":
                                #Clica no valor do TCPO
                                WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, tipo_informacao_tcpo))).click()

                                time.sleep(5)

                                try:
                                    #Espera carregar a tabela de serviços
                                    tabela_servicos = f"ctl00_MainContent_gvServicos"
                                    WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, tabela_servicos)))

                                    time.sleep(1)

                                    tabela_servicos_contar_linhas = wait.until(EC.visibility_of_element_located((By.ID, tabela_servicos)))
                                    linhas_tabela = tabela_servicos_contar_linhas.find_elements(By.TAG_NAME, 'tr')
                                    quantidade_linhas = len(linhas_tabela)

                                    contador_paginas = 0

                                    try:
                                        #Valida se há mais de uma guia no insumo
                                        quantidade_itens = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[1]/td/table"
                                        valor_quantidade = navegador.find_element("xpath", quantidade_itens).text

                                        #Itera sobre a quantidade de guias
                                        for quant in range(1, 5):
                                            contador_paginas += 1

                                            #Se a página for um, inicia de um período x
                                            if contador_paginas == 1:
                                                #Itera sobre cada guia do insumo
                                                for pagina in range(1, 12):
                                                    pagina_clicar = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[1]/td/table/tbody/tr/td[{pagina}]"

                                                    try:
                                                        #Clica na guia
                                                        WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, pagina_clicar))).click()

                                                        time.sleep(1)

                                                        WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, tabela_servicos)))

                                                        time.sleep(1)

                                                        tabela_servicos_contar_linhas = wait.until(EC.visibility_of_element_located((By.ID, tabela_servicos)))
                                                        linhas_tabela = tabela_servicos_contar_linhas.find_elements(By.TAG_NAME, 'tr')
                                                        quantidade_linhas = len(linhas_tabela)

                                                        #Itera sobre cada linha dos insumos
                                                        for contador_servico in range(3, quantidade_linhas - 3):
                                                            #Obtém o item
                                                            item_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[2]"
                                                            valor_item_servico = navegador.find_element('xpath', item_servico).text

                                                            #Obtém a descrição
                                                            descricao_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[3]"
                                                            valor_descricao_servico = navegador.find_element('xpath', descricao_servico).text

                                                            #Obtém a unidade
                                                            unidade_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[4]"
                                                            valor_unidade_servico = navegador.find_element('xpath', unidade_servico).text

                                                            #Aguarda até que o elemento esteja presente na página
                                                            elemento = WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, item_servico)))

                                                            #Rola a página até o elemento
                                                            navegador.execute_script("arguments[0].scrollIntoView();", elemento)

                                                            #Clica no elemento
                                                            elemento.click()

                                                            #Espera carregar a tabela
                                                            xpath_material = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/table/tbody/tr[2]/td[3]/span"
                                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, xpath_material)))
                                                            material = navegador.find_element('xpath', xpath_material).text

                                                            xpath_preco = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/table/tbody/tr[2]/td[5]/span"
                                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, xpath_preco)))
                                                            preco = navegador.find_element('xpath', xpath_preco).text

                                                            #Retorna para a tabela principal
                                                            id_retornar_tabela = f"ctl00_MainContent_btnServicos"
                                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, id_retornar_tabela))).click()

                                                            #Espera carregar a tabela após clicar
                                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, tabela_servicos)))

                                                            linha_excel += 1
                                                            
                                                            #Preenche as informações obtidas no excel
                                                            preenche_excel(linha_excel=linha_excel, guia_planilha="Insumos", tipo_informacao_site=valor_tcpo, valor_item_servico=valor_item_servico, valor_descricao_servico=valor_descricao_servico, valor_unidade_servico=valor_unidade_servico, tipo_insumo=material, valor_sem_taxa=preco) 

                                                    except:
                                                        #Caso não tenha mais linhas, sai do laço
                                                        break

                                            #Valida se o contador for acima de 1
                                            else:
                                                #Itera sobre as guias
                                                for pagina in range(4, 14):
                                                    pagina_clicar = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[1]/td/table/tbody/tr/td[{pagina}]"

                                                    try:
                                                        #Clica na guia
                                                        WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, pagina_clicar))).click()

                                                        time.sleep(1)

                                                        WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, tabela_servicos)))

                                                        time.sleep(1)

                                                        tabela_servicos_contar_linhas = wait.until(EC.visibility_of_element_located((By.ID, tabela_servicos)))
                                                        linhas_tabela = tabela_servicos_contar_linhas.find_elements(By.TAG_NAME, 'tr')
                                                        quantidade_linhas = len(linhas_tabela)

                                                        #Itera sobre cada linha dos insumos
                                                        for contador_servico in range(3, quantidade_linhas - 3):
                                                            #Obtém o item
                                                            item_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[2]"
                                                            valor_item_servico = navegador.find_element('xpath', item_servico).text

                                                            #Obtém a descrição
                                                            descricao_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[3]"
                                                            valor_descricao_servico = navegador.find_element('xpath', descricao_servico).text

                                                            #Obtém a unidade
                                                            unidade_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[4]"
                                                            valor_unidade_servico = navegador.find_element('xpath', unidade_servico).text

                                                            #Aguarda até que o elemento esteja presente na página
                                                            elemento = WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, item_servico)))

                                                            #Rola a página até o elemento
                                                            navegador.execute_script("arguments[0].scrollIntoView();", elemento)

                                                            #Clica no elemento
                                                            elemento.click()

                                                            #Espera carregar a tabela
                                                            xpath_material = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/table/tbody/tr[2]/td[3]/span"
                                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, xpath_material)))
                                                            material = navegador.find_element('xpath', xpath_material).text

                                                            xpath_preco = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/table/tbody/tr[2]/td[5]/span"
                                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, xpath_preco)))
                                                            preco = navegador.find_element('xpath', xpath_preco).text

                                                            #Retorna para a tabela principal
                                                            id_retornar_tabela = f"ctl00_MainContent_btnServicos"
                                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, id_retornar_tabela))).click()

                                                            #Espera carregar a tabela após clicar
                                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, tabela_servicos)))

                                                            linha_excel += 1
                                                            
                                                            #Preenche as informações obtidas no excel
                                                            preenche_excel(linha_excel=linha_excel, guia_planilha="Insumos", tipo_informacao_site=valor_tcpo, valor_item_servico=valor_item_servico, valor_descricao_servico=valor_descricao_servico, valor_unidade_servico=valor_unidade_servico, tipo_insumo=material, valor_sem_taxa=preco)
                                                    
                                                    except:
                                                        #Caso não tenha mais linhas, sai do laço
                                                        break
                
                                    #Se não há mais de uma guia, cai aqui
                                    except:
                                        #Itera sobre os serviços
                                        for contador_servico in range(2, quantidade_linhas):
                                            #Obtém o item
                                            item_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[2]"
                                            valor_item_servico = navegador.find_element('xpath', item_servico).text

                                            #Obtém a descrição
                                            descricao_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[3]"
                                            valor_descricao_servico = navegador.find_element('xpath', descricao_servico).text

                                            #Obtém a unidade
                                            unidade_servico = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[3]/tbody/tr[2]/td/div/table/tbody/tr[{contador_servico}]/td[4]"
                                            valor_unidade_servico = navegador.find_element('xpath', unidade_servico).text

                                            #Aguarda até que o elemento esteja presente na página
                                            elemento = WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, item_servico)))

                                            #Rola a página até o elemento
                                            navegador.execute_script("arguments[0].scrollIntoView();", elemento)

                                            #Clica no elemento
                                            elemento.click()

                                            #Espera carregar a tabela
                                            xpath_material = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/table/tbody/tr[2]/td[3]/span"
                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, xpath_material)))
                                            material = navegador.find_element('xpath', xpath_material).text

                                            xpath_preco = f"/html/body/div[2]/form/div[3]/table/tbody/tr[2]/td[2]/table[2]/tbody/tr[2]/td/table/tbody/tr[1]/td[2]/div/table/tbody/tr[2]/td[5]/span"
                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, xpath_preco)))
                                            preco = navegador.find_element('xpath', xpath_preco).text

                                            #Retorna para a tabela principal
                                            id_retornar_tabela = f"ctl00_MainContent_btnServicos"
                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, id_retornar_tabela))).click()

                                            #Espera carregar a tabela após clicar
                                            WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.ID, tabela_servicos)))

                                            linha_excel += 1
                                            
                                            #Preenche as informações no excel
                                            preenche_excel(linha_excel=linha_excel, guia_planilha="Insumos", tipo_informacao_site=valor_tcpo, valor_item_servico=valor_item_servico, valor_descricao_servico=valor_descricao_servico, valor_unidade_servico=valor_unidade_servico, tipo_insumo=material, valor_sem_taxa=preco)           

                                except:
                                    #Caso não tenha mais elementos dos insumos, sai do laço
                                    continue

                        except:
                            #Caso não tenha mais insumos, sai do laço
                            break

            #Clica no botão sair para deslogar o usuário
            botao_sair = "/html/body/div[2]/form/div[3]/div/div/table/tbody/tr/td[10]/a"
            WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, botao_sair))).click()
            
            #Fecha o navegador
            navegador.close()

        #Caso dê algum erro, envia e-mail
        except Exception as e:
            botao_sair = "/html/body/div[2]/form/div[3]/div/div/table/tbody/tr/td[10]/a"
            #Aguarda até que o elemento esteja presente na página
            elemento = WebDriverWait(navegador, 120).until(EC.presence_of_element_located((By.XPATH, botao_sair)))

            #Rola a página até o elemento
            navegador.execute_script("arguments[0].scrollIntoView();", elemento)

            #Clica no elemento
            elemento.click()

            #Fecha o navegador
            navegador.close()

            #Dispara e-mails para as tratativas
            destinatarios_email = []
            destinatarios_email.append('Nicolas.nasario@COMPANY_NAME.com.br')
            destinatarios_email.append('Lucas.remor@COMPANY_NAME.com.br')

            assunto_email = "WebScrapping TCPOWeb"

            mensagem_email = f"""
            Olá!<br><br>
            Há erro para acessar o site do TCPOWeb!<br><br>
            {e}. 
            """

            #Envia o e-mail para o pessoal da logística
            envia_email(mensagemEmail=mensagem_email, destinatarios_email=destinatarios_email, assunto_email=assunto_email)

    else:
        if "Acesso negado" in informacao_sem_acesso:
            navegador.close()

        else:
            #Clica no botão sair para deslogar o usuário
            botao_sair = "/html/body/div[2]/form/div[3]/div/div/table/tbody/tr/td[10]/a"
            WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.XPATH, botao_sair))).click()

            navegador.close()

            print("Sem acesso")

#Chama os códigos principais
def executa_codigos():
    pass # Logica de negocio removida por seguranca corporativa

if __name__ == "__main__":
    executa_codigos()