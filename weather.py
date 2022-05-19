import csv
from datetime import datetime
from decimal import ROUND_UP
from fileinput import filename
import statistics

DEGREE_SYBMOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):                                                                        
    """Takes a temperature and returns it in string format with the degrees
        and celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees celcius."
    """
    return f"{temp}{DEGREE_SYBMOL}"


def convert_date(iso_string):                                                                     
    """Converts and ISO formatted date into a human readable format.

    Args:
        iso_string: An ISO date string..
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    date_input = datetime.strptime(iso_string,"%Y-%m-%dT%H:%M:%S%z")
    date = date_input.strftime("%A %d %B %Y")
    return date


def convert_f_to_c(temp_in_farenheit):                                                              

    """Converts an temperature from farenheit to celcius.

    Args:
        temp_in_farenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees celcius, rounded to 1dp.
    """
    temp_c_1 = (float(temp_in_farenheit) - 32) * 5 / 9
    temp_c = round(temp_c_1, 1)
    return temp_c

print (convert_f_to_c(0))  


def calculate_mean(weather_data):                                                                   
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    return statistics.mean(map(float, weather_data))
    


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
        # main []

        # with open(csv_file) as newfile:
        #     rows = csv.reader(newfile)   
        #     next(rows,None)
        #     for row in rows:
        #         main.append(row)
                
        #         return [main]


    # main_list = []

    # with open(csv_file) as file:
    #     reader = csv.reader(file)
    #     for row in reader:
    #         main_list.append(row)
    #     main_list.pop(0)
    #     for i in main_list:
    #         for j in i:
    #             i[1] = int(i[1])
    #             i[2] = int(i[2])
    # return main_list 


    # with open(csv_file) as csv_file:
    #     reader = csv.reader(csv_file)
    #     next(reader,None)
    #     for line in reader:
    #         return[line]


    main_list = []
    with open(csv_file) as file:
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            if len(line) > 0:
                main_list.append([line[0], int(line[1]), int(line[2])])
    return main_list



def find_min(weather_data): 
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minium value and it's position in the list.
    """
    

    if weather_data == []:
        return ()
    else:
        min_val = weather_data[0]
        min_loc = 0
        index = 0
        for element in weather_data:
            if float(element) <= float(min_val):
                min_val = float(element)  
                min_loc = index
            index +=1 
        return (min_val, min_loc)
    



def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list.
    """
    if weather_data == []:
        return()
    else:
        max_value = weather_data[0]
        max_loc = 0
        index = 0
        for num in weather_data:
            if float(num) >= float(max_value):
                max_value = float(num)
                max_loc = index
            index += 1
        return(max_value, max_loc)
        



def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """

    dates = []
    min_temps = []
    max_temps = []
    number_of_days = len(weather_data)

    for item in weather_data:
        if item != []:
            dates.append(item[0])
            min_temps.append(item[1])
            max_temps.append(item[2])

    min_temperature_f, index_min = find_min(min_temps)
    max_temperature_f, index_max = find_max(max_temps)

    min_temp_c = convert_f_to_c(str(min_temperature_f))
    max_temp_c = convert_f_to_c(str(max_temperature_f))

    date_min = dates[index_min]
    date_max = dates[index_max]

    av_min_f = calculate_mean(min_temps)
    av_max_f = calculate_mean(max_temps)

    av_min_c = convert_f_to_c(av_min_f)
    av_max_c = convert_f_to_c(av_max_f)

    result = ""
    result += f"{number_of_days} Day Overview\n"
    result += f"  The lowest temperature will be {format_temperature(min_temp_c)}, and will occur on {convert_date(date_min)}.\n"
    result += f"  The highest temperature will be {format_temperature(max_temp_c)}, and will occur on {convert_date(date_max)}.\n"
    result += f"  The average low this week is {format_temperature(av_min_c)}.\n"
    result += f"  The average high this week is {format_temperature(av_max_c)}.\n"

    return result

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    result = ""
    for row in weather_data:
        if len(row) != 0:
            result += f'---- {convert_date(row[0])} ----\n'
            result += f'  Minimum Temperature: {format_temperature(convert_f_to_c(row[1]))}\n'
            result += f'  Maximum Temperature: {format_temperature(convert_f_to_c(row[2]))}\n\n'

    return result


