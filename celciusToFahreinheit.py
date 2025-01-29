def celciusToFahrenheit(celcius):
    return 9/5 * celcius + 32

celciusTemp = float(input("Enter temperature in celcius: "))
fahrenheitTemp = celciusToFahrenheit(celciusTemp)
print(f"{celciusTemp}°C is equal to {fahrenheitTemp}°F")