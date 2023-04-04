def convertSalary(salary, country):
    conversion_rates = {
        'Canada': 1,
        'USA': 1.18,
        'Cambodia': 4847.38,
        'United Kingdom': 0.91
    }
    converted_salary = salary / conversion_rates[country]
    return converted_salary
    
def compareSalary(salary, country):
    average_salaries = {
        'Canada': 64000,
        'USA': 56516,
        'Cambodia': 5649856,
        'United Kingdom': 35423
    }
    converted_salary = convertSalary(salary, country)
    
    if converted_salary > average_salaries[country]:
       print (f'You will be rich in {country} with a salary of {converted_salary:.2f} {country} currency.')
    else:
        print( f'You will be poor in {country} with a salary of {converted_salary:.2f} {country} currency.')
        
# Example usage
salary = int(input('Enter your salary in Euros: '))
print("Valid countries: Canada, USA, Cambodia, United Kingdom")
country = input('Enter the country you want to migrate to: ')

compareSalary(salary, country)