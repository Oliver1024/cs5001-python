def main():
    age = int(input("Please enter your age: "))
    restHR = int(input("Please enter your resting heart rate: "))

    print("=======================================")

    # Compute max heart rate
    max_heart_rate = 208 - 0.7 * age
    UNIT = "bpm"
    print("Your heart rate reserve is:", round((max_heart_rate - restHR), 2), UNIT)
    print("Here is a breakdown of your training zones:")

    # The difference between the start and end values of different zones
    DIFF = 0.01 

    # Compute bpm of training zones from Zone1 to Zone5
    zone1_1 = restHR + (max_heart_rate - restHR) * 0.5
    zone1_2 = round(restHR + (max_heart_rate - restHR) * 0.6 - DIFF, 2)
    zone2_1 = round(restHR + (max_heart_rate - restHR) * 0.6, 2)
    zone2_2 = round(restHR + (max_heart_rate - restHR) * 0.7 - DIFF, 2)
    zone3_1 = round(restHR + (max_heart_rate - restHR) * 0.7, 2)
    zone3_2 = round(restHR + (max_heart_rate - restHR) * 0.8 - DIFF, 2)
    zone4_1 = round(restHR + (max_heart_rate - restHR) * 0.8, 2)
    zone4_2 = round(restHR + (max_heart_rate - restHR) * 0.93 - DIFF, 2)
    zone5_1 = round(restHR + (max_heart_rate - restHR) * 0.93, 2)
    zone5_2 = restHR + (max_heart_rate - restHR) * 1

    # Print the results
    CNT = "to"
    print("Zone 1:", zone1_1, CNT, zone1_2, UNIT)
    print("Zone 2:", zone2_1, CNT, zone2_2, UNIT)
    print("Zone 3:", zone3_1, CNT, zone3_2, UNIT)
    print("Zone 4:", zone4_1, CNT, zone4_2, UNIT)
    print("Zone 5:", zone5_1, CNT, zone5_2, UNIT)

main()