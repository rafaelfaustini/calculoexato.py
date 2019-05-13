from selenium import webdriver
import datetime
import pandas

def poupanca(driver,nome,valor,dataini,datafim):
    driver.get("http://calculoexato.com.br/parprima.aspx?codMenu=FinanAtualizaIndice")

    dataini
    if(datafim == ""):
        datafim = datetime.datetime.now()
    else:
        datafim = datetime.datetime.strptime(datafim, '%d/%m/%Y')

    dataini = datetime.datetime.strptime(dataini, '%d/%m/%Y')
    c = driver.find_element_by_id("txt1")
    c.clear()
    c.send_keys(valor)
    c = driver.find_element_by_id("comboDataDia2")
    c.send_keys(dataini.day)
    c = driver.find_element_by_id("comboDataMes2")
    c.send_keys(dataini.month)
    c = driver.find_element_by_id("comboDataAno2")
    c.send_keys(dataini.year)
    c = driver.find_element_by_id("comboDataDia3")
    c.send_keys(datafim.day)
    c = driver.find_element_by_id("comboDataMes3")
    c.send_keys(datafim.month)
    c = driver.find_element_by_id("comboDataAno3")
    c.send_keys(datafim.year)

    c = driver.find_element_by_id("comboIndice4")
    c.send_keys("poupanca")

    c = driver.find_element_by_id("btnContinuar")
    c.click()

    c = driver.find_element_by_css_selector("div[class='mldc']")

    f= open(nome+".txt","w+")
    f.write(c.text)

def ler_arquivo(nome):
    df = pandas.read_csv(nome, skipinitialspace=True, sep = ";")
    return df

def percorre(c):
    driver = webdriver.Chrome(r'chromedriver.exe')  
    for i in range (0, len(c["Nome"])):
        nome = str(c["Nome"][i])
        valor = str(c["Valor"][i])
        dataini = str(c["Data a partir"][i])
        datafim = str(c["Data para ser atualizado"][i])
        print(nome+valor+dataini+datafim)
        poupanca(driver,nome,valor,dataini,datafim)            
  
    driver.quit()
        
def main():
    c = ler_arquivo("clientes.csv")
    percorre(c)

    
main()      
      
