degreeInCelsius = [12,21,15,32]
degreeInFahrenheit = [ round((9/5) * c + 32,1) for c in degreeInCelsius]

print(degreeInFahrenheit)