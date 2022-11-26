import os
owo = ["BA", "BE", "BI", "BO", "BU", "CA", "CE", "CI", "CO", "CU", "DA", "DE", "DI", "DO", "DU", "FA", "FE", "FI", "FO", "GA", "GE", "GI", "GO", "JA", "JE", "JI", "JO", "JU", "LA", "LE", "LI", "LLA", "LLE", "LLO", "LO", "LU",
       "MA", "ME", "MI", "MO", "MU", "NA", "NE", "NI", "NO", "NU", "PA", "PE", "PI", "PO", "PU", "QUE", "QUI", "RA", "RE", "RI", "RO", "RU", "SA", "SO", "SU", "TA", "TE", "TI", "TO", "TU", "VA", "VE", "VI", "VO", "YA", "YE", "YO"]
silabas = []
for i in range(len(owo)):
    silabas.append(owo[i].lower())
da = str(silabas)
file = open('./silabas.txt', 'w')
file.write(da)
file.close
