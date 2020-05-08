#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  6 00:06:25 2020

@author: jonathanestrella
"""

import math as mt
import pandas as pd
import matplotlib.pyplot as plt

# percentil y five_number_summary son funciones para los primeros 3 incisos 
def percentil(lista, perc):
    pm = (len(lista) - 1) * perc
    pl = mt.floor(pm)
    pu = mt.ceil(pm)
    return lista[pl] + (lista[pu] - lista[pl]) * perc


def five_number_summary(lista):
    lista.sort()
    mini = lista[0]
    maxi = lista[-1]
    
    mediana = percentil(lista, 0.5)
    fq = percentil(lista, 0.25)
    tq = percentil(lista, 0.75)
    media = sum(lista) / len(lista)
    variance = sum([(i-media)**2 for i in lista]) / (len(lista) - 1)
    s_deviation = variance**(1/2)
    
    print('Five Number Summary')
    print('Mínimo: ',mini)
    print('Máximo: ', maxi)
    print('Mediana: ', mediana)
    print('1er Quartil: ', fq)
    print('3er Quartil: ', tq)
    
    print('Media: ', media)
    print('Desviación estándar: ', s_deviation)
        
    plt.boxplot(lista)
     

def median_mean_deviation(lista):
    lista.sort()
    
    mediana = percentil(lista, 0.5)
    media = sum(lista) / len(lista)
    print('Mediana: ', mediana)
    print('Media: %.2f' % media)

    if len(lista) == 1:
        print('Solo hay un dato, y por lo tanto la división en la varianza sería sobre cero')
    else:
        variance = sum([(i-media)**2 for i in lista]) / (len(lista) - 1)
        s_deviation = variance**(1/2)
        print('Desviación estándar: %.2f' % s_deviation)


def values_histogram(dict_):
    lista = []
    for k in sorted(dict_):
        for i in range(dict_[k]):
            lista.append(k)
    return lista


def pearson_coefficient(lista1, lista2):
    xm = sum(lista1) / len(lista1)
    ym = sum(lista2) / len(lista1)
    
    numerador = sum([(lista1[i] - xm)*(lista2[i] - ym) for i in range(len(lista1))])
    
    denominador1 = sum([(lista1[i] - xm)**2 for i in range(len(lista1))])
    denominador2 = sum([(lista2[i] - ym)**2 for i in range(len(lista1))])
    
    denominador1 = denominador1**(1/2)
    denominador2 = denominador2**(1/2)
    
    r = numerador / (denominador2 * denominador1)
    print('Coeficiente de pearson: ',r)
    
          
"""
    Inciso 1) Calcule el five_number_summary, el boxplot, la media, la desviación 
              estándar para el salario anual por género
"""
def inciso_1(data):
    annual_salary = data['ConvertedComp'].tolist()
    gender = data['Gender'].tolist()
    
    h = []
    for s, g in zip(annual_salary, gender):
        if not pd.isna(s) and not pd.isna(g):
            g = g.split(';')
            if 'Man' in g:
                h.append(s)
    
    m = []
    for s, g in zip(annual_salary, gender):
        if not pd.isna(s) and not pd.isna(g):
            g = g.split(';')
            if 'Woman' in g:
                m.append(s)
    
    n_b = []
    for s, g in zip(annual_salary, gender):
        if not pd.isna(s) and not pd.isna(g):
            g = g.split(';')
            if 'Non-binary, genderqueer, or gender non-conforming' in g:
                n_b.append(s)            
    
    print('********** Hombres **********')
    five_number_summary(h)
    plt.title('BOXPLOT')
    plt.xlabel('Hombres')
    plt.ylabel('Salario anual')
    print('\n') 
    print('********** Mujeres **********')
    plt.figure()
    five_number_summary(m)
    plt.title('BOXPLOT')
    plt.xlabel('Mujeres')
    plt.ylabel('Salario anual')
    print('\n')
    print('********** No binary **********')
    plt.figure()
    five_number_summary(n_b)
    plt.title('BOXPLOT')
    plt.xlabel('No binario')
    plt.ylabel('Salario anual')
    print('\n')


"""
    Inciso 2) Calcule el five_number_summary, el boxplot, la media, la desviación 
              estándar para el salario anual por grupo étnico
"""
def inciso_2(data):
    annual_salary = data['ConvertedComp'].tolist()
    ethnicity = data['Ethnicity'].tolist()
    
    grupos = []
    # Encontrar los distintos grupos étnicos
    for g in ethnicity:
        if not pd.isna(g):
            list_g = g.split(';')
            for w in list_g:
                if w not in grupos:
                    grupos.append(w)
    
    for g_n in grupos: # Itera sobre los distintos grupos
        g_i = []
        for s, g_e in zip(annual_salary, ethnicity):
            if not pd.isna(s) and not pd.isna(g_e):
                g_e = g_e.split(';')
                if g_n in g_e:
                    g_i.append(s)
        if len(g_i) > 0:
            print('********** ' + str(g_n) + ' **********')
            five_number_summary(g_i)
            plt.title('BOXPLOT')
            plt.xlabel(str(g_n))
            plt.ylabel('Salario anual')
            plt.figure()
            print('\n')


"""
    Inciso 3) Calcule el five_number_summary, el boxplot, la media y la desviación 
              estándar para el salario anual por tipo de desarrollador.

"""
def inciso_3(data):
    annual_salary = data['ConvertedComp'].tolist()
    devtype = data['DevType'].tolist()
    
    desarrolladores = []
    # Encontrar los distintos tipos de desarrolladores
    for g in devtype:
        if not pd.isna(g):
            list_g = g.split(';')
            for w in list_g:
                if w not in desarrolladores:
                    desarrolladores.append(w)
    
    for g_n in desarrolladores: # Itera sobre los distintos desarrolladores
        g_i = []
        for s, g_e in zip(annual_salary, devtype):
            if not pd.isna(s) and not pd.isna(g_e):
                g_e = g_e.split(';')
                if g_n in g_e:
                    g_i.append(s)
        if len(g_i) > 0:
            print('********** ' + str(g_n) + ' **********')
            five_number_summary(g_i)
            plt.title('BOXPLOT')
            plt.xlabel(str(g_n))
            plt.ylabel('Salario anual')
            plt.figure()
            print('\n')


"""
    Inciso 4) Calcule la mediana, media y la desviación estándar del salario anual 
              por país.

"""
def inciso_4(data):
    annual_salary = data['ConvertedComp'].tolist()
    country = data['Country'].tolist()
    
    countries = []
    # Encontrar los distintos tipos de paises
    for g in country:
        if not pd.isna(g):
            list_g = g.split(';')
            for w in list_g:
                if w not in countries:
                    countries.append(w)

    for pais_i in countries:
        pais_valores = []
        for s, pais in zip(annual_salary, country):
            if (not pd.isna(s)) and (not pd.isna(pais)):
                pais = pais.split(';')
                if pais_i in pais:
                    pais_valores.append(s)
        # print(len(pais_valores)) # Saber cuantos valores no eran NaN
        if len(pais_valores) > 0:
            print('********** ' + str(pais_i) + ' **********')
            median_mean_deviation(pais_valores)
            print('\n')


"""
    Inciso 5) Obtenga un diagrama de barras con las frecuencias de respuestas para
              cada tipo de desarrollador.

"""        
def inciso_5(data):
    devtype = data['DevType'].tolist()
    
    d_freq = {}
    # Encontrar los distintos tipos de desarrolladores
    for g in devtype:
        if not pd.isna(g):
            list_g = g.split(';')
            for w in list_g:
                d_freq[w] = d_freq.get(w,0) + 1
    
    temp = list(d_freq.keys())
    values_x = range(len(temp))
    values_y = list(d_freq.values())
    
    plt.bar(values_x, values_y)
    plt.title('Diagrama de barras con las frecuencias de respuestas para cada tipo de desarrollador.')
    plt.ylabel('Frecuencia de respuestas de usuarios')
    plt.xticks(values_x, temp)
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right')


"""
    Inciso 6) Trace histogramas con 10 bins para los años de experiencia con la
              codificación por género.

"""
def inciso_6(data):
    language = data['LanguageWorkedWith'].tolist()
    gender = data['Gender'].tolist()
    yearscode = data['YearsCode'].tolist()
    
    languages = []
    for l in language:
        if not pd.isna(l):
            list_l = l.split(';')
            for w in list_l:
                if w not in languages:
                    languages.append(w)
    print(languages)
    
    for lang in languages:
        languages_values_m = {}
        languages_values_w = {}
        languages_values_n = {}
        for l, g, y in zip(language, gender, yearscode):
            if (not pd.isna(l)) and (not pd.isna(g)) and (not pd.isna(y)):
                list_l = l.split(';')
                list_g = g.split(';')
                
                
                if y == 'Less than 1 year':
                    y = 0
                elif y == 'More than 50 years':
                    y = 51
                else:
                    y = int(y)
                
                if (lang in list_l) and ('Man' in list_g):
                    languages_values_m[y] = languages_values_m.get(y,0) + 1
                if (lang in list_l) and ('Woman' in list_g):
                    languages_values_w[y] = languages_values_w.get(y,0) + 1
                if (lang in list_l) and ('Non-binary, genderqueer, or gender non-conforming' in list_g):
                    languages_values_n[y] = languages_values_n.get(y,0) + 1
        
        l_v_m = values_histogram(languages_values_m)
        l_v_w = values_histogram(languages_values_w)
        l_v_n = values_histogram(languages_values_n)
        
        fig, axs = plt.subplots(3, 1)
        
        axs[0].hist(l_v_m, bins = 10)
        axs[0].set_title('Hombres')
        axs[0].set(xlabel = 'Años', ylabel = 'No. de personas')
       
        axs[1].hist(l_v_w, bins = 10)
        axs[1].set_title('Mujeres')
        axs[1].set(xlabel = 'Años', ylabel = 'No. de personas')
       
        axs[2].hist(l_v_n, bins = 10)
        axs[2].set_title('No binario')
        axs[2].set(xlabel = 'Años', ylabel = 'No. de personas')
        
        fig.suptitle(str(lang), x = 1.05)
        fig.tight_layout()
        plt.figure()
    
   
"""
    Inciso 7) Trace histogramas con 10 bins para el número promedio de horas de trabajo 
              por semana, por tipo de desarrollador

"""    
def inciso_7(data):
    workweekhrs = data['WorkWeekHrs'].tolist()
    devtype = data['DevType'].tolist()
    
    desarrolladores = []
    # Encontrar los distintos tipos de desarrolladores
    for g in devtype:
        if not pd.isna(g):
            list_g = g.split(';')
            for w in list_g:
                if w not in desarrolladores:
                    desarrolladores.append(w)
    print(len(desarrolladores))
    
    for dev in desarrolladores:
        lista_hrs = []
        for h, d in zip(workweekhrs, devtype):
            if (not pd.isna(h)) and (not pd.isna(d)):
                h = float(h)
                if dev in d:
                    lista_hrs.append(h)
        
        if len(lista_hrs) > 0:
            lista_hrs.sort()
            print(len(lista_hrs))
            plt.hist(lista_hrs, bins = 10)
            plt.title(str(dev))
            plt.xlabel('Horas promedio de trabajo por semana')
            plt.ylabel('No. de personas')
            plt.figure()


"""
    Inciso 8) Trace histogramas con 10 bins para la edad por género.

"""
def inciso_8(data):
    age = data['Age'].tolist()
    gender = data['Gender'].tolist()
    
    h = []
    for a, g in zip(age, gender):
        if not pd.isna(a) and not pd.isna(g):
            g = g.split(';')
            if 'Man' in g:
                h.append(int(a))
    
    m = []
    for a, g in zip(age, gender):
        if not pd.isna(a) and not pd.isna(g):
            g = g.split(';')
            if 'Woman' in g:
                m.append(int(a))
    
    n_b = []
    for a, g in zip(age, gender):
        if not pd.isna(a) and not pd.isna(g):
            g = g.split(';')
            if 'Non-binary, genderqueer, or gender non-conforming' in g:
                n_b.append(int(a))            
    
    h.sort()
    m.sort()            
    n_b.sort()
    
    plt.hist(h, bins = 10)
    plt.title('Hombres')
    plt.xlabel('Edad')
    plt.ylabel('No. de personas')
    
    plt.figure()
    plt.hist(m, bins = 10)
    plt.title('Mujeres')
    plt.xlabel('Edad')
    plt.ylabel('No. de personas')
    
    plt.figure()
    plt.hist(n_b, bins = 10)
    plt.title('No binarios')
    plt.xlabel('Edad')
    plt.ylabel('No. de personas')


"""
    Inciso 9) Calcule la mediana, la media y la desviación estándar de la edad 
              por lenguaje de programación.

"""
def inciso_9(data):
    age = data['Age'].tolist()
    language = data['LanguageWorkedWith'].tolist()
    
    languages = []
    for l in language:
        if not pd.isna(l):
            list_l = l.split(';')
            for w in list_l:
                if w not in languages:
                    languages.append(w)
    print(len(languages))

    for lang in languages:
        lang_valores = []
        for a, l in zip(age, language):
            if (not pd.isna(a)) and (not pd.isna(l)):
                l = l.split(';')
                if lang in l:
                    lang_valores.append(int(a))
        # print(len(pais_valores)) # Saber cuantos valores no eran NaN
        if len(lang_valores) > 0:
            print('********** ' + str(lang) + ' **********')
            median_mean_deviation(lang_valores)
            print('\n')


"""
    Inciso 10) Calcule la correlación entre años de experiencia y salario anual.

"""
def inciso_10(data):
    yearscode = data['YearsCode'].tolist()
    annual_salary = data['ConvertedComp'].tolist()
    
    list1 = []
    list2 = []
    
    for y, s in zip(yearscode, annual_salary):
        if (not pd.isna(y)) and (not pd.isna(s)):
            
            if y == 'Less than 1 year':
                y = 0.5
            elif y == 'More than 50 years': 
                y = 60.0
            else:
                y = float(y)
            
            list1.append(float(y))
            list2.append(float(s))
    
    if len(list1) > 0 and len(list2) > 0:
        pearson_coefficient(list1, list2)


"""
    Inciso 11) Calcule la correlación entre la edad y el salario anual.

"""
def inciso_11(data):
    age = data['Age'].tolist()
    annual_salary = data['ConvertedComp'].tolist()
    
    list1 = []
    list2 = []
    
    for a, s in zip(age, annual_salary):
        if (not pd.isna(a)) and (not pd.isna(s)):
            list1.append(float(a))
            list2.append(float(s))
    
    if len(list1) > 0 and len(list2) > 0:
        pearson_coefficient(list1, list2)


"""
    Inciso 12) Calcule la correlación entre el nivel educativo y el salario anual. 
               En este caso, reemplazar la cadena del nivel educativo por un índice
               ordinal (por ejemplo, Primaria / primaria escuela = 1, 
               escuela secundaria = 2, y así sucesivamente).

"""
def inciso_12(data):
    edlevel = data['EdLevel'].tolist()
    annual_salary = data['ConvertedComp'].tolist()

    levels = []
    for l in edlevel:
        if not pd.isna(l):
            list_l = l.split(';')
            for w in list_l:
                if w not in levels:
                    levels.append(w)
   
    d = {'I never completed any formal education': 1, 
         'Primary/elementary school': 2, 
         'Secondary school (e.g. American high school, German Realschule or Gymnasium, etc.)': 3,
         'Some college/university study without earning a degree': 4,
         'Associate degree': 5, 
         'Bachelor’s degree (BA, BS, B.Eng., etc.)' : 6,
         'Professional degree (JD, MD, etc.)': 6, 
         'Master’s degree (MA, MS, M.Eng., MBA, etc.)': 7,
         'Other doctoral degree (Ph.D, Ed.D., etc.)': 8
         }
    # Nota: El profesor dió algunos comentarios sobre algunos grados y cómo se 
    # consideran.
    
    list1 = []
    list2 = []
    
    for el, s in zip(edlevel, annual_salary):
        if (not pd.isna(el)) and (not pd.isna(s)):
            list1.append(float(d[el]))
            list2.append(float(s))
    
    if len(list1) > 0 and len(list2) > 0:
        pearson_coefficient(list1, list2)


"""
    Inciso 13) Obtenga un diagrama de barras con las frecuencias de los diferentes
               lenguajes de programación.

"""
def inciso_13(data):
    language = data['LanguageWorkedWith'].tolist()
    
    d_freq = {}
    # Encontrar los distintos tipos de lenguajes
    for g in language:
        if not pd.isna(g):
            list_g = g.split(';')
            for w in list_g:
                d_freq[w] = d_freq.get(w,0) + 1
    
    temp = list(d_freq.keys())
    values_x = range(len(temp))
    values_y = list(d_freq.values())
    
    plt.bar(values_x, values_y)
    plt.title('Diagrama de barras con las frecuencias de los diferentes lenguajes de programación.')
    plt.ylabel('Frecuencia de respuestas de usuarios')
    plt.xticks(values_x, temp)
    plt.setp(plt.gca().get_xticklabels(), rotation=45, horizontalalignment='right', fontsize = 7.5)



"""
PRACTICA INTERMEDIA
20
"""

w_d = '/Users/jonathanestrella/Documents/MineriaDeDatos/data/'
i_f = w_d + 'survey_results_public.csv'

data = pd.read_csv(i_f)

"""
    Para revisar cada inciso solo es cambiar el número 
"""
# inciso_*(data) 
inciso_13(data)   