from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
import time

# Especifique o caminho para o seu GeckoDriver
caminho_geckodriver = '../geckodriver.exe'

# Especifique o caminho para o executável do Firefox
caminho_firefox = ' C:/Program Files/Mozilla Firefox/firefox.exe'

try:
    # Configura as opções do Firefox e define o caminho do binário
    options = Options()
    options.binary_location = caminho_firefox
    
    # Cria a instância do Service do GeckoDriver
    service = Service(executable_path=caminho_geckodriver)
    
    # Inicia o driver do Firefox, passando as opções
    driver = webdriver.Firefox(service=service, options=options)
    
    # Restante do seu código
    driver.get('https://bullsbet.net')
    time.sleep(5) 
    
    print("Tentando encontrar o botão...")
    try:
        botao_sim = driver.find_element(By.XPATH, "//button[contains(text(), 'sim')]")
        botao_sim.click()
        print("Botão 'sim' clicado com sucesso!")
    except Exception as e:
        print(f"Erro ao encontrar ou clicar no botão: {e}")
        
    time.sleep(3)
    
except Exception as e:
    print(f"Ocorreu um erro geral: {e}")
    
finally:
    if 'driver' in locals():
        driver.quit()
        print("Navegador fechado.")