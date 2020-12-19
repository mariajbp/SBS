# -*- coding: utf-8 -*-
"""
Created on Thu Dec 17 16:24:47 2020

@author: Pedro
"""

import re
import pandas as pd


data = pd.read_csv("Data/data_by_genres.csv", sep = ",")

print(data['genres'].head(20))

rockN = re.findall('(?i:rock)', data['genres'].to_string())
popN = re.findall('(?i:pop)', data['genres'].to_string())
rapN = re.findall('(?i:rap)', data['genres'].to_string())
hiphopN = re.findall('(?i:hip hop)', data['genres'].to_string())
soulN = re.findall('(?i:soul)', data['genres'].to_string())
bluesN = re.findall('(?i:blues)', data['genres'].to_string())
kpopN = re.findall('(?i:k-pop)', data['genres'].to_string())
countrykN = re.findall('(?i:country)', data['genres'].to_string())
metalN = re.findall('(?i:metal)', data['genres'].to_string())
eletrN = re.findall('(?i:electr)(onic|o|ic)*', data['genres'].to_string())
danceN = re.findall('(?i:dance)', data['genres'].to_string())
latinN = re.findall('(?i:latin)', data['genres'].to_string())
indieN = re.findall('(?i:indie)', data['genres'].to_string())
classicalN = re.findall('(?i:classical)', data['genres'].to_string())
jazzN = re.findall('(?i:jazz)', data['genres'].to_string())
isntrN = re.findall('(?i:instrumental)', data['genres'].to_string())


print("-> popN ", len(rockN))
print("-> popN ", len(popN))
print("-> rapN ", len(rapN))
print("-> hiphopN ", len(hiphopN))
print("-> soulN ", len(soulN))
print("-> bluesN ", len(bluesN))
print("-> kpopN ", len(kpopN))
print("-> countrykN ", len(countrykN))
print("-> metalN ", len(metalN))
print("-> eletrN ", len(eletrN))
print("-> danceN ", len(danceN))
print("-> latinN ", len(latinN))
print("-> indieN ", len(indieN))
print("-> classicalN ", len(classicalN))
print("-> jazzN ", len(jazzN))
print("-> instrumental ", len(isntrN))


#---------------------------------------------

data = pd.read_csv("Data/Data_artists_after_join.csv", sep = ",")

print(data['genres'])

rockN = re.findall('(?i:rock)', data['genres'].to_string())
popN = re.findall('(?i:pop)', data['genres'].to_string())
rapN = re.findall('(?i:rap)', data['genres'].to_string())
hiphopN = re.findall('(?i:hip hop)', data['genres'].to_string())
soulN = re.findall('(?i:soul)', data['genres'].to_string())
bluesN = re.findall('(?i:blues)', data['genres'].to_string())
kpopN = re.findall('(?i:k-pop)', data['genres'].to_string())
countrykN = re.findall('(?i:country)', data['genres'].to_string())
metalN = re.findall('(?i:metal)', data['genres'].to_string())
eletrN = re.findall('(?i:electr)(onic|o|ic)*', data['genres'].to_string())
danceN = re.findall('(?i:dance)', data['genres'].to_string())
latinN = re.findall('(?i:latin)', data['genres'].to_string())
indieN = re.findall('(?i:indie)', data['genres'].to_string())
classicalN = re.findall('(?i:classical)', data['genres'].to_string())
jazzN = re.findall('(?i:jazz)', data['genres'].to_string())
isntrN = re.findall('(?i:instrumental)', data['genres'].to_string())
punkN = re.findall('(?i:punk)', data['genres'].to_string())


print("-> rockN ", len(rockN))
print("-> popN ", len(popN))
print("-> rapN ", len(rapN))
print("-> hiphopN ", len(hiphopN))
print("-> soulN ", len(soulN))
print("-> bluesN ", len(bluesN))
print("-> kpopN ", len(kpopN))
print("-> countrykN ", len(countrykN))
print("-> metalN ", len(metalN))
print("-> eletrN ", len(eletrN))
print("-> danceN ", len(danceN))
print("-> latinN ", len(latinN))
print("-> indieN ", len(indieN))
print("-> classicalN ", len(classicalN))
print("-> jazzN ", len(jazzN))
print("-> instrumental ", len(isntrN))
print("-> punk ", len(punkN))


