# Module 5 CTA - Creating Python Programs - Joe Armani

# part 1 - Monthly rainfall totals and averages
# define functions to get the number of years and monthly rainfall
def get_num_years():
    while True:
        try:    
            num_years = int(input(f'Enter the number of years to record '))
            if num_years <= 0:
                print('Number of years must be positive. Please enter a positive number.')
                continue
            return num_years
        except ValueError:
            print('Whole numbers only. Please enter a valid number of years.')
            
def get_monthly_rainfall(month, year):
    while True:
        try:
            monthly_rainfall = float(input(f'Enter the rainfall for {month}, year {year} '))
            if monthly_rainfall < 0:
                print(f'You entered, {monthly_rainfall} inches. Rainfall cannot be negative. Please try again.')
                continue
            return monthly_rainfall
        except ValueError:
            print('Numbers only. Please enter a valid rainfall value.')

# define the months_of_year dict
months_of_year_dict = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December",
}

# store monthly rainfall in a dict (dict comprehension sets up key/value paris month: [] for each month in months_of_year)
monthly_rainfall_dict = {month: [] for month in months_of_year_dict.values()} 

# iterate from year 1 to num_years + 1
num_years = get_num_years()
for year in range(1, num_years + 1):
    for month in range(1, 13):
        # get the average rainfall for the month, then add it to monthly_rainfall_dict
        rainfall = get_monthly_rainfall(months_of_year_dict[month] , year)
        monthly_rainfall_dict[months_of_year_dict[month]].append(rainfall)
  
print(f'Calculating average rainfall for each month over {num_years} years...')
years_string = 'years' if num_years > 1 else 'year'

for month in monthly_rainfall_dict:
    monthly_rainfall_total = sum(monthly_rainfall_dict[month])
    monthly_rainfall_average = monthly_rainfall_total / num_years
    print(f'{month}, over {num_years} {years_string}: Total rainfall: {monthly_rainfall_total:.2f}\" Average monthly rainfall: {monthly_rainfall_average:.2f}\".')


# Part 2 - Bookstore book club awards program
# define functions to (1) get the number of books from user input and (2) calculate points earned
def get_num_books():
    while True:
        try:    
            num_books = int(input(f'Enter the number of books you purchased this month '))
            if num_books < 0:
                print('Number of years can\'t be negative. Please try again.')
                continue
            return num_books
        except ValueError:
            print('Whole numbers only. Please enter a valid number of books.')
        
def get_points(num_books):
    if num_books < 2:
        return 0
    elif num_books < 4:
        return 5
    elif num_books < 6:
        return 15
    elif num_books < 8:
        return 30
    else:
        return 60
    
# get the number of books purchased
num_books = get_num_books()
num_points = get_points(num_books)
books_string = 'books' if num_books != 1 else 'book'
print(f'You purchased {num_books} {books_string} and earned {num_points} points.')
