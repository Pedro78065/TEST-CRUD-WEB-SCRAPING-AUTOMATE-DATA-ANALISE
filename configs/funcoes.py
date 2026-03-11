from playwright.sync_api import sync_playwright
import mysql.connector
import pandas as pd
import plotly

def dump_csv():    
    """
acessa o site: https://mavenanalytics.io/data-playground e baixa um arquivo rar que quando extraído vira um .csv.
    """
    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        context = browser.new_context(accept_downloads=True)
        page = context.new_page()
        page.goto('https://mavenanalytics.io/data-playground')#link do site
        with page.expect_download() as p_download:
            page.locator('xpath=//*[@id="data-set-list"]/div/div/div/div/div[2]/div[6]/div/div/div[2]/div[3]/div[2]/a').click()#localização do botão
            download = p_download.value

        download.save_as('/home/pedro/VS-Project/Test_analise/base_dados' + download.suggested_filename)
        browser.close()


def ler_csv(name_to_csv):
    """
:name_to_csv:nome do csv ou da sua localização.
:separador: recebe o que divide o cada informação do csv.
    """
    separador = str(input('informe o separador do arquivo.csv(ex:se for virgula digite somente ","): '))
    df = pd.read_csv(name_to_csv, sep=separador)
    return df


df = ler_csv('Customer Loyalty History.csv')
print(df)