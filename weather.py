import statistics

series_titles = ["Maximum temperature (Degree C)", "Minimum temperature (Degree C)", "Rainfall amount (millimetres)"]

def mean(in_series):
    pass

def variance(in_series):
    pass

def standard_deviation(in_series):
    pass

def filter_series(year_series, month_series, day_series, data_series, max_date=None, min_date=None):
    filtered = []
    for y,m, d, value in zip(year_series,
                            month_series,
                            day_series,
                            data_series):
          current = (y, m, d)
          if min_date and current < min_date:
            continue
    
          if max_date and current > max_date:
            continue
    
          filtered.append(value)
    return filtered

def interquartile_range(in_series):
    data = sorted(in_series)
    mid = len(data) // 2

    if len(data) % 2 == 0:
        lower_half = data[:mid]
        upper_half = data[mid:]
    else:
        lower_half = data[:mid]
        upper_half = data[mid + 1:]

    q1 = statistics.median(lower_half)
    q3 = statistics.median(upper_half)

    return q3 - q1

def read_csv(file,default_value=None):
    data_table = {}
    with open(file) as f:
        lines = f.readlines()
    lines = [line.strip().split(',') for line in lines]
    for i in range(len(lines[0])):
        data_table[lines[0][i]] = [default_value if (len(line[i]) == 0) else float(line[i]) for line in lines[1:]]
    return data_table

def get_user_choice(options):
    for i, option in enumerate(options):
        print(f"{i+1}. {option}")
    choice = input("Enter the number of your choice: ")
    if choice.lower() == 'exit':
        return None
    if not choice.isdigit() or int(choice) < 1 or int(choice) > len(options):
        print("Invalid choice. Please try again.")
        return get_user_choice(options)
    choice = int(choice) - 1
    return options[choice]

def menu(data_table):
    print("Select a data series:")
    choice = get_user_choice(series_titles)
    series = data_table[choice]
    print(f"Mean: {mean(data_table[choice])}")

if __name__ == "__main__":
    data = read_csv('weather.csv')
    menu(data)