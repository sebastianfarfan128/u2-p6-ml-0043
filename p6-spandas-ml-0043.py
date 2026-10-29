import pandas as pd
import numpy as np

serie_amigos=["Pedro", "Morgan", "Farfan", "El Adrian", "Jesse", "Eliseo", "Mario"]
print(" --- Serie listado de amigos NC = 0043 ---")
amigos=pd.Series(serie_amigos)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
print(" --- Serie listado valor de billetes MX NC = 0043 ---")
amigos=pd.Series(serie_billetes)
print(amigos)

serie_billetes=[20,50,100,200,500,1000]
serie_bletras=["Veinte","Cincuenta","Cien","Docientos","Quinientos","Mil"]
print(" --- Serie listado nombre y valor de billetes MX NC = 0043 ---")
tablabilletes=pd.Series(serie_billetes, serie_bletras)
print(tablabilletes)
# Diccionario de dataframe
# Diccionario de valor monedas y nombre
print("Datos de diccionarios a DataFrame en pandas")
dic_monedas={
    "serie_billetes":[20,50,100,200,500,1000],
    "serie_bletras":["Veinte","Cincuenta","Cien","Docientos","Quinientos","Mil"]
}

tablabilletes=pd.DataFrame(dic_monedas,index=["A","B","C","D","E","F"])
print(tablabilletes)

print("Casa de cambio de Sebastian Farfan NC = 0043")