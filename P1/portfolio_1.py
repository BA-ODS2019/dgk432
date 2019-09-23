#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 23 21:10:53 2019

@author: je
"""

# Åben og læs filen ...
import pandas as pd
titanic = pd.read_csv("../data/titanic.csv")

# Hvor mange rækker?
print( 'antal rækker: ')
print(len(titanic))

print()

# Hvor mange rækker og kolonner ...
print( 'antal rækker og kolonner: ')
print(titanic.shape)

print()

#Hvor mange 'cells' i tabellen
print( 'antal celler: ')
print(titanic.size)

print()

# Kolonnernes navne / overskrifter
print( 'Navne på kolonnerne: ')
print(titanic.columns)

print()

# Kolonnernes data type - int, float, string, object...
print( 'Data typen fra kolonnerne: ')
print(titanic.dtypes)
print()

print( 'antal overlevende: ')
print(titanic['Survived'].sum()) # Total sum of the column values - overlevende
print()

print( 'gennemsnitsalder: ')
print(titanic['Age'].mean()) # Mean of the column values - alder..
print()

print( 'median - alder: ')
print(titanic['Age'].median()) # Median of the column values - medianen..
print()

# Find antal kvinder ...
females = titanic[titanic['Sex'] == 'female']
antal   = females['Survived'].count()

print("Antal kvinder: ")
print( antal )

# Find antal kvinder ...
males = titanic[titanic['Sex'] == 'male']
antal   = males['Survived'].count()

print("Antal mænd: ")
print( antal )

# Antal personer på klasse 1, 2 og 3
titanic.groupby('Pclass').count()

# pivot tabel 

print("Antal overlevende pr klasse: ---------------")

pt = titanic.pivot_table(columns = 'Pclass', values = 'Survived', aggfunc='sum')
print(pt)
pt.plot(kind='bar');

print('Antal overlevende pr køn: -----------' )

pt = titanic.pivot_table(columns = 'Sex', values = 'Survived', aggfunc='sum')
print(pt)
pt.plot(kind='bar');

print()

print( ' sortering pr efternavn: ')
print()

#titanic[titanic['Name'].str.split().str[-1]]
last_names = titanic['Name'].str.split().str[-1]
print(last_names)

#titanic['Name'].str.split().str[-1]


#slut = last_names.groupby(last_names)
#print(slut)
#titanic['Names'].value_counts()
#last_names.describe()
#last_names.columns.value_counts()


#last_names.groupby('Name').count()

