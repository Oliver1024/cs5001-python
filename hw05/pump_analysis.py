"""
https://github.ccs.neu.edu/CS-5001-SEA-Spring2021/student-KejianTong/tree/master/hw05
Name: Kejian Tong
"""

# Get input file from user
files = input("Please enter the file name: ")


def main():
    """
    Here is the main function that is used to open the file.
    When the file does not exist, it will prompt the user
    that it cannot be opened.
    """
    # Assign values to replace magic numbers
    MINS_PER_HOUR = 60
    HOURS_PER_DAY = 24
    MINS_PER_DAY = HOURS_PER_DAY * MINS_PER_HOUR  # 1440
    MINUTE_GALLON = 2
    ROUND_NUM = 3
    WATT_MINS_VALUE = 1000
    WATT_HRS_MINS = 60
    RUN_THRESHOLD = 500
    MSG = "Data covers a total of"

    # Assign values to variables
    minutes = 0
    watt_minutes = 0
    sum_total_watts = 0
    num_run = 0
    num_idle = 0
    total_min_1 = 0
    total_min_2 = -1
    bool_run_1 = False
    bool_run_2 = False
    total_galon = 5
    large_galon = 100
    previous_line = False
    count_softer = 0
    start_min = 0
    target_value = 120
    reserve_list = []

    try:
        f = open(files, 'r')
        pass
    except FileNotFoundError as e:
        print("Unable to open", files)
        return

    # Compute required results using for loop
    for line in f:
        minutes += 1
        lines = line.rstrip('\n')
        if int(lines) >= RUN_THRESHOLD:
            watt_minutes += 1
            if not previous_line:
                count_softer += 1
                start_min = minutes
                previous_line = True
            else:
                count_softer += 1
        else:
            if count_softer >= target_value:
                reserve_list.append((count_softer, start_min))
            count_softer = 0
            previous_line = False
        sum_total_watts += int(lines)
        if int(line) < RUN_THRESHOLD:
            num_idle += 1
        else:
            num_run += 1
        if num_run * MINUTE_GALLON >= total_galon and bool_run_1 is False:
            total_min_1 = num_idle + num_run
            bool_run_1 = True
        if num_run * MINUTE_GALLON >= large_galon and bool_run_2 is False:
            total_min_2 = num_idle + num_run
            bool_run_2 = True

    # Some conversion about dates, watt/minute and Kwh
    days = round(float(minutes / MINS_PER_DAY), ROUND_NUM)
    hours = minutes // MINS_PER_HOUR
    minutes_gallon = MINUTE_GALLON * watt_minutes
    num_days = minutes / MINS_PER_DAY
    day_avg_gallon = round(float(minutes_gallon / num_days), ROUND_NUM)
    kilowatt_hours = round(
        (sum_total_watts / WATT_MINS_VALUE / WATT_HRS_MINS), ROUND_NUM)

    # Print the results
    print(MSG, float(hours), "hours", end='\n')
    print("(That's", days, "days)\n")

    print("Pump was running for", watt_minutes,
          "minutes, producing", minutes_gallon, "gallons")
    print("(That's", day_avg_gallon, "gallons per day)\n")
    print("Pump required a total of",
          sum_total_watts, "watt minutes of power")
    print("That's", kilowatt_hours, "kWh\n")
    print("It took", total_min_1, "minutes of data to reach",
          total_galon, "gallons.")
    print("It took", total_min_2, "minutes of data to reach",
          large_galon, "gallons.\n")

    # Print last required results
    if len(reserve_list) > 0:
        print("Information on water softener recharges:")
        for item in reserve_list:
            print(item[0], "minute run started at", item[1])


main()
