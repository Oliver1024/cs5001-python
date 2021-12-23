def main():
    # Assign values to constants 
    DAY_HIGH = max([47,47,46,49,48,48,46,47,48,47])
    DAY_LOW = min([39,40,43,41,39,38,36,37,38,38])
   
    # Compute the difference between the highest temperature and lowest temperature
    DIFF = DAY_HIGH - DAY_LOW
    
    # Assign values of temperature at noon predicted for the 10 day forecast
    NOON_TEMP = [46,45,48,46,46,44,44,44,44,45]
    TOTAL_DAYS = 10

    # Compute 10 days average temperature
    AVG_TEMP = sum(NOON_TEMP) / TOTAL_DAYS
 
    # Assign values to constants
    BASE = 32
    CONVERSION_FACTOR = 5.0/9.0
    TEMP_PRECISION = 1

    # Get the highest temperature predicted for the 10 day forecast.
    DAY_HIGH = max([47,47,46,49,48,48,46,47,48,47])

    # Converte from Fahrenheit to Celsius
    celsius_cvt = (DAY_HIGH - BASE) * CONVERSION_FACTOR

    # Print the results.
    print("The temperature difference is:", DIFF, "Fahrenheit")
    print("The average temperature at noon is:", AVG_TEMP, "Fahrenheit")
    print("Converted from Fahrenheit to Celsius is:", round(celsius_cvt, TEMP_PRECISION), "degrees Celsius")


main()