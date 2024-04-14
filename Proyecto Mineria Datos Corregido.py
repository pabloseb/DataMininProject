# -*- coding: utf-8 -*-
"""
Universidad del Valle de Guatemala
Mineria de Datos
Proyecto No.1 
Calidad del Aire en América
"""
import pandas as pd

def csv(file):
    return pd.read_csv(file)

nuevayork = csv("newyork.csv")
ukkel = csv("ukkel.csv")
madrid = csv("madrid.csv")
lisboa = csv("lisboa.csv")
lascondes = csv("lascondes.csv")
zhuzhou = csv("zhuzhou.csv")
beijing = csv("beijing.csv")
tokyo = csv("tokyo.csv")
xingin = csv("xingin.csv")
saopaulo = csv("saopaulo.csv")
paris = csv("paris.csv")
guadalajara = csv("guadalajara.csv")
ahmedabad = csv("ahmedabad.csv")
londres = csv("london.csv")
toronto = csv("toronto.csv")
houston = csv("houston.csv")
karamay = csv("karamay.csv")

#------------------------------------------------------------------------------
#Identificacion de las ciudades
NuevaYork = ['Nueva York' for i in range(nuevayork.shape[0])]
Ukkel = ['Ukkel' for i in range(ukkel.shape[0])]
Madrid = ['Madrid' for i in range(madrid.shape[0])]
Lisboa = ['Lisboa' for i in range(lisboa.shape[0])]
LasCondes = ['Las Condes' for i in range(lascondes.shape[0])]
Zhuzhou = ['Zhuzhou' for i in range(zhuzhou.shape[0])]
Beijing = ['Beijing' for i in range(beijing.shape[0])]
Tokyo = ['Tokyo' for i in range(tokyo.shape[0])]
Xingin = ['Xingin' for i in range(xingin.shape[0])]
SaoPaulo = ['SaoPaulo' for i in range(saopaulo.shape[0])]
Paris = ['Paris' for i in range(paris.shape[0])]
Guadalajara = ['Guadalajara' for i in range(guadalajara.shape[0])]
Ahmedabad = ['Ahmedabad' for i in range(ahmedabad.shape[0])]
Londres = ['Londres' for i in range(londres.shape[0])]
Toronto = ['Toronto' for i in range(toronto.shape[0])]
Houston = ['Houston' for i in range(houston.shape[0])]
Karamay = ['Karamay' for i in range(karamay.shape[0])]

#------------------------------------------------------------------------------
#Agregar el nombre de las ciudades en cada df
nuevayork.insert(0,'Ciudad',NuevaYork)
ukkel.insert(0,'Ciudad',Ukkel)
madrid.insert(0,'Ciudad',Madrid)
lisboa.insert(0,'Ciudad',Lisboa)
lascondes.insert(0,'Ciudad',LasCondes)
zhuzhou.insert(0,'Ciudad',Zhuzhou)
beijing.insert(0,'Ciudad',Beijing)
tokyo.insert(0,'Ciudad',Tokyo)
xingin.insert(0,'Ciudad',Xingin)
saopaulo.insert(0,'Ciudad',SaoPaulo)
paris.insert(0,'Ciudad',Paris)
guadalajara.insert(0,'Ciudad',Guadalajara)
ahmedabad.insert(0,'Ciudad',Ahmedabad)
londres.insert(0,'Ciudad',Londres)
toronto.insert(0,'Ciudad',Toronto)
houston.insert(0,'Ciudad',Houston)
karamay.insert(0,'Ciudad',Karamay)
#-----------------------------------------------------------------------------
#Se arregla la columna de tiempo para solo tener el año, en lugar de año, mes y fecha

variables = [nuevayork,madrid,lisboa,lascondes,zhuzhou,beijing,tokyo,xingin,saopaulo,paris,guadalajara,ahmedabad,londres,toronto,houston,karamay]

for i in variables:
    i['date'] = pd.to_datetime(i['date'])
    i['date'] = i['date'].dt.year

#------------------------------------------------------------------------------
#Vamos a hacer que todos los dataframes tengan las mismas variables 
ciudad = []
fecha = []
pm25 = []
o3 = []
no2 = []
pm25_category = [] 

for variable in variables:
    ciudad.extend(variable['Ciudad'].tolist())
    fecha.extend(variable['date'].tolist())
    pm25.extend(variable[nuevayork.columns.tolist()[2]].tolist())
    o3.extend(variable[nuevayork.columns.tolist()[3]].tolist())
    no2.extend(variable[nuevayork.columns.tolist()[4]].tolist())

pm25 = [float(elemento.strip()) if elemento.strip() else 0 for elemento in pm25]
o3 = [float(elemento.strip()) if elemento.strip() else 0 for elemento in o3]
no2 = [float(elemento.strip()) if elemento.strip() else 0 for elemento in no2]

for i in pm25:
    if 0 <= i <= 12.0:
        pm25_category.append('Bien')
    elif 12.0 < i < 35.5:
        pm25_category.append('Moderado')
    elif 35.5 <= i < 55.4:
        pm25_category.append('Peligroso Para grupos de Riesgo')
    elif 55.5 <= i < 150.4:
        pm25_category.append('Insano')
    elif 150.5 <= i < 250.4:
        pm25_category.append('Muy Insano')
    elif i >= 250.5:
        pm25_category.append('Extremadamente peligroso')
    else:
        pm25_category.append("No hay registro")
        
data_numerica = pd.DataFrame({'PM2.5':pm25,'O3':o3,'no2':no2})
AQI = data_numerica.max(axis=1).tolist()
#-----------------------------------------------------------------------------

df = pd.DataFrame({'Ciudad':ciudad,'Fecha':fecha,'O3':o3,'no2':no2,'PM2.5':pm25,'Valor AQI': AQI,'Categoria AQI': pm25_category})
print(df)