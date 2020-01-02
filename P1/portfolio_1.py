#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 21:10:53 2019

@author: je
"""

# Åben og læs filen ...
import pandas as pd
import numpy as numpy
import matplotlib.pyplot as plt
import seaborn as sns
import re as re


# min variable sættes til titanic - som jeg så læser ind som Pandas Dataframe
# jeg har valgt konsekvent at indsætte ektra "print statements(strings) til bedre overblik og forståelse
# dette print danner overskrifter, når programmet kører, så man bedre kan se, hvad der foregår..
print()
print('indlæsningen af min csv fil, mens jeg definere min variable *titanic* : ')
print('titanic = pd.read_csv( < indsæt *FILENAME.csv* her > : )')
print()
titanic = pd.read_csv("../data/titanic.csv")

# første step er at undersøge, hvilken type jeg har med at gøre

print()
print('dokumentation for, at mit datasæt rent faktisk er en Pandas DataFrame ' )
print(type(titanic))
print()


# herunder begynder jeg min analyse af datasættet, dels for at undersøge, hvilke typer data jeg har med 
# at gøre, men også for at lære data at kende, så jeg kan uddrage enkelte visualiseringer til sidst 

# kilder der er anvendt er https://www.shanelynn.ie/using-pandas-dataframe-creating-editing-viewing-data-in-python/ 
# og https://pandas.pydata.org/pandas-docs/stable/index.html

print()
print('overskrifter på kolonnerne: ' )
# navnene/værdierne på de overskrifter som findes i datasættet 
# disse værdier kan der beregnes og analyseres på senere hen
print()
print(titanic.columns.values)

print()
print('total antal rækker og kolonner i min Pandas DataFrame: ')
# Hvor mange rækker og kolonner beregnes med shape funktionen
print( 'antal rækker og kolonner: ')
print()
print(titanic.shape)
print()
print('dimensionerne i min DataFrame: ')
print(titanic.ndim)

print()
print('samlet antal rækker og total antal kolonner:  ')
# Hvor mange rækker/entries?
print()
print(len(titanic))
print('samlet antal kolonner: ')
# hvor mange kolonner?
print()
print(len(titanic.columns))

print()
print('total antal celler: ')
#Hvor mange 'cells' i tabellen
print()
print(titanic.size)


print()
# Kolonnernes data type - int, float, string, object...
print( 'Data typen fra kolonnerne (om det er integer, float eller object/string) : ')
print( 'kort overblik via funktionen print(titanic.dtypes) :')
print()
print(titanic.dtypes)
print()

# .. med nedenstående kode snip ..info får man samme overblik som alle de ovenstående koder
# inkl type af data og overblik til videre bearbejdning
print('Hvilken type data min DataFrame indeholder: ')
print( 'mere dybdegående indsigt via funktionen print(titanic.info) :')
print()
print(titanic.info())

print('Det er tydeligt, at funktionen "print(titanic.info)" giver flere informationer end "print(titanic.dtypes)" :')

print()
print('sidste for-analyse funktioner, som er værd at kigge på er .head ( som blot viser de første 5 rækker af data ), .tail (som viser de 5 sidste rækker), samt .describe (som foretager beregninger - deskriptiv statistik på samtlige passagere, fra klasse, til køn, overlevet eller ej), inden konkret analyse foretages :')
# beregninger til at undersøge data nærmere
# antal, analyse mv. 
print()
print(titanic.head()) # viser kun de 5 første hits/rækker i DataFrame
print(titanic.tail()) # viser de 5 sidste rækker i DataFrame
print(titanic.describe())


print('____ Break inden beregning ( Descriptiv statistics ) _____ ' )

print( 'antal overlevende: ')
print( ' i [ listen Survived ] uddrages samlede antal overlevende, en boolean funktion enten eller med værdien (O eller 1)'  )
print(titanic['Survived'].sum()) # Total sum of the column values - overlevende
print()

print( 'gennemsnitsalder: ')
print()
print(titanic['Age'].mean()) # Mean of the column values - alder..
print()

print( 'median - alder: ')
print()
print(titanic['Age'].median()) # Median of the column values - medianen..
print()


# Find antal kvinder ...
females = titanic[titanic['Sex'] == 'female']
print()
print('Antal kvinder: ')
print(females)


# Find antal mænd ...
males = titanic[titanic['Sex'] == 'male']
print()
print('Antal mænd: ')
print(males)


print()
print("_____________HVORDAN ER FORDELINGEN MELLEM PASSAGERKLASSE OG OVERLEVENDE?_____")
#how are the passagers devided into class and survival..
print (titanic[['Pclass', 'Survived']].groupby(['Pclass'], as_index=False).mean().sort_values(by='Survived', ascending=False))

print()
print("_____________HVORDAN ER FORDELINGEN MELLEM KØN OG OVERLEVENDE?________________")
#how are the passangers by survivial and gender..
print (titanic[['Sex', 'Survived']].groupby(['Sex'], as_index=False).mean().sort_values(by='Survived', ascending=False))


# Antal personer på klasse 1, 2 og 3
print('antal personer på henholdsvis klasse 1, 2 og 3')
print(titanic.groupby('Pclass').count())



print("Antal overlevende pr. klasse vises som Pivot tabel: ---------------")

pt1 = titanic.pivot_table(columns = 'Pclass', values = 'Survived', aggfunc='sum')
print(pt1)
pt1.plot(kind='bar')
plt.title("antal overlevende pr. klasse")
plt.savefig("SurvivorsPrClass.png")


print('Antal overlevende pr. køn vises som Pivot tabel: -----------' )

pt2 = titanic.pivot_table(columns = 'Sex', values = 'Survived', aggfunc='sum')
print(pt2)
pt2.plot(kind='bar')
plt.title("antal overlevende pr. køn")
plt.savefig("SurvivorsPrSex.png")


# ved at anvende visualisering via Seaborn biblioteket kan man tydeligt se, at der var mange flere mænd ombord end kvinder
# snuppet fra Kaggle - https://www.kaggle.com/startupsci/titanic-data-science-solutions
print('___ ved hjælp af Seaborn visualisering kan man se forskel i antal mænd og kvinder om bord Titanic - fordelt på alder' )
t = sns.FacetGrid(titanic, col='Sex')
t.map(plt.hist, 'Age', bins=20)



print()
print( 'sortering pr efternavn: ')
print( 'ved at tage sidste værdi fra kolonnen Name har jeg fået en liste over efternavne' )
print()

#titanic[titanic['Name'].str.split().str[-1]]

last_names = titanic['Name'].str.split().str[-1]
print(last_names)

# beregning på, hvor mange som har samme efternavn
# først foretages en split på den rette kolonne, dernæst beregnes denne varialbe i forhold til value_count

print('hvor mange har samme efternavn')  
print(last_names.value_counts())




print(' ____ sidste øvelse, BONUS i forhold til oplæg, er at få samlet de mange forskellige titler, som passagererne har' )

# som lidt ekstra, kan man samle titler, denne inspiration er fundet via netsøgning
# og ved brug af RegEx.. 

# En enkelt definition inkl. brug af RegEx 
# kilde: https://regex101.com/ blandt andet.. 

def get_title(name):
	title_search = re.search('([A-Za-z]+)\.', name)
	# If the title exists, extract and return it.
	if title_search:
		return title_search.group(1)
	return ""

titanic['Title'] = titanic['Name'].apply(get_title)

print(pd.crosstab(titanic['Title'], titanic['Sex']))

titanic['Title'] = titanic['Title'].replace(['Lady', 'Countess','Capt', 'Col',\
 	'Don', 'Dr', 'Major', 'Rev', 'Sir', 'Jonkheer', 'Dona'], 'Rare')

titanic['Title'] = titanic['Title'].replace('Mlle', 'Miss')   
titanic['Title'] = titanic['Title'].replace('Ms','Miss')
titanic['Title'] = titanic['Title'].replace('Mme','Mrs')

print (titanic[['Title', 'Survived']].groupby(['Title'], as_index=False).mean())





