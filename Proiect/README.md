# Currency Converter (B , ID : 4)
  * [Enunt](#enunt)
  * [Prezentarea solutiei](#prezentarea)
  * [Tehnologii folosite](#Tehnologii_folosite)
  

## Enunt

![image](https://user-images.githubusercontent.com/79217056/206908353-08d0ea36-cb52-473b-84fb-76b92f72f461.png)


## Prezentarea solutiei

Pentru rezolvarea problemei am ales sa impart codul in doua module:
  * [scraper.py](###scraper.py)
  * [main.py](###main.py)
  
### scraper.py

In acest modul implementez un crawl pe [BNR.ro](https://bnr.ro/Cursul-de-schimb-524.aspx) cu ajutorul unui obiect BeautifulSoup din libraria bs4. Dupa realizez o parsare pentru a lua doar datele necesare.

![image](https://user-images.githubusercontent.com/79217056/206908367-03e9c1f6-29c1-4c57-a9d1-51b198c9f362.png)
![image](https://user-images.githubusercontent.com/79217056/206908376-67e68ae3-da4e-4fde-ba3e-5adad05d688a.png)

Acest modul are o singura metoda trade_spider(), care realizeaza cele mentionate mai sus apoi returneaza un dictionar in care cheia este reprezentata de numele monedei (type(keys) = str) si valoarea este reprezentata de valoare monedei in RON (leul romanesc, type(values) = float).

![image](https://user-images.githubusercontent.com/79217056/206908746-9df3adcd-282a-4641-b077-25edc7713aae.png)

 [Codul fisierului scraper.py](https://github.com/Bordei08/3A2PP_Bordei_Mihai_Gabi/blob/main/Proiect/scraper.py)
 
 
 ### main.py
 
 In acest modul am implementat interfata grafica cu ajutorul librariei tkinter.
 ![image](https://user-images.githubusercontent.com/79217056/206909269-6f37b8dd-81da-4e99-b83b-799cb1e3679f.png)
 ![image](https://user-images.githubusercontent.com/79217056/206909442-5b1f9778-31a3-45ad-952e-c3b67b9fc840.png)
 ![image](https://user-images.githubusercontent.com/79217056/206909450-41f919e2-deab-4612-a1d1-6d2a12716aa0.png)
 
 Cursul valutar este actualizat pentru fiecare instanta noua, la fiecare apasare de buton se realizeaza un nou apel al functiei trade_spider() din modulul [scraper.py](#scraper.py).
 
 Algoritmul de conversie este unul banal, converteste moneda initiala in RON, apoi valoare noua in moneda de output.
 ![image](https://user-images.githubusercontent.com/79217056/206909798-5f93a383-65fd-49aa-b970-58ab7e5212bf.png)
 
 Aplicatia arunca si erori pentru input-uri gresite.
 
 ![image](https://user-images.githubusercontent.com/79217056/206909928-3e0f93e7-a848-4216-93d2-f34028b0ad81.png)
![image](https://user-images.githubusercontent.com/79217056/206909932-012761eb-ce6c-4f7f-8c6f-431a39f4a327.png)

[Vezi codul fisierului main.py](https://github.com/Bordei08/3A2PP_Bordei_Mihai_Gabi/blob/main/Proiect/main.py)


## Tehnologii folosite
    
   * [Python 3.0](https://www.python.org/downloads/)
   * [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/)
   * [Tkinter](https://docs.python.org/3/library/tk.html)


