"""
This file contains the solution for Practice 4

J. Cihlar - January 2024
"""


def get_max(lst: list[int]) -> int:
    """
    Finds max value of a list

    Parameters:
        lst(list[int]): the list of integers to search. Assumes at least one element
    Return:
        int: the maximum value
    """
    mx: int = lst[0]
    for val in lst[1:]:
        if val > mx:
            mx = val
    return mx

def get_min(lst: list[int]) -> int:
    """
    Finds min value of a list

    Parameters:
        lst(list[int]): the list of integers to search. Assumes at least one element
    Return:
        int: the minimum value
    """
    mn: int = lst[0]
    for val in lst[1:]:
        if val < mn:
            mn = val
    return mn    

def get_avg(lst: list[int]) -> int:
    """
    Gets the average of a list of values

    Parameters:
        lst(list[int]): the list of integers to search. Assumes at least one element
    Return:
        int: the average to the nearest integer
    """
    total: int = 0
    for val in lst:
        total += val
    
    avg: int = round(total / len(lst), 0)
    return avg

def get_readings_below(lst: list[int], cutoff: int) -> int:
    """
    Gets the number of values strictly below a cutoff point.

    Parameters:
        lst(list[int]): the list of integers to search. Assumes at least one element
    Return:
        int: the number of readings below the cutoff
    """
    count: int = 0
    for val in lst:
        if val < cutoff:
            count += 1
    return count


def get_readings_above(lst: list[int], cutoff: int) -> int:
    """
    Gets the number of values strictly above a cutoff point.

    Parameters:
        lst(list[int]): the list of integers to search. Assumes at least one element
    Return:
        int: the number of readings above the cutoff
    """
    count: int = 0
    for val in lst:
        if val > cutoff:
            count += 1
    return count

def get_description(AQI: int) -> str:
    """
    Returns a description for an AQI score.
    
    Parameters:
        AQI(int): The AQI value to assign a description to
    Return:
        str: The description
    """
    if AQI < 51:
        return "Good"
    if AQI < 101:
        return "Moderate"
    if AQI < 151:
        return "Unhealthy for sensitive groups"
    if AQI < 201:
        return "Unhealthy"

    return "Hazardous"

def main() -> None:
        # get the number of readings
    num_readings: int = int(input())
        # set up an empty list
    readings: list[int] = []
        # read in the data and add to the list
    for _ in range(num_readings):
        r: int = int(input())
        readings.append(r)
    
        # these will all force separate iterations through the loop
        # it's OK for the purpose of this assignment
    maximum: int = get_max(readings)
    minimum: int = get_min(readings)
    average: int = get_avg(readings)
    readings_below: int = get_readings_below(readings, average)
    readings_above: int = get_readings_above(readings, average)
    description: str = get_description(average)

    print(f"Readings: {num_readings}")
    print(f"Min: {minimum}")
    print(f"Max: {maximum}")
    print(f"Average: {average}")
    print(f"Readings Below Average: {readings_below}")
    print(f"Readings Above Average: {readings_above}")
    print(f"Description: {description}")    
    
if __name__ == "__main__":
    main()


