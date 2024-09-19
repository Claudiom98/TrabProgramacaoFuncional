import subprocess



instalar = lambda x : subprocess.check_call(['pip','install',x]) # Funcao Lambda

    
def scrapper(func): #Funcao de Alta Ordem
    modulos = ['requests','bs4','lxml']
    for m in modulos: #List comprehension
        func(m)
    url = input('Por favor, digite a url que deseja baixar as imagens: ')
    def baixar(): #Closure
        import requests
        import bs4
        import lxml
        result = requests.get(url)
        readable = bs4.BeautifulSoup(result.text,'lxml')
        imagens = readable.select('img')
        for idx,x in enumerate(imagens): #List Comprehension
            try:
                link = requests.get(imagens[idx]['src'])#Na versao atual o caminho das sources deve ser absoluto
                img = open(str(idx)+'.png','wb')
                img.write(link.content)
            except:
                print('Erro, imgagem nao pode ser baixada')
    return baixar
    

executar = scrapper(instalar)
executar()