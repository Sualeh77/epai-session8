from faker import Faker
from collections import namedtuple
import datetime

def timed(reps):
	"""
	It's a decorator factory that starts with setting up number of repeatation.
	"""
	def decorator(fn):
		"""
		This decorator runs the decorated function reps times and compute the avg execution time for that function.
		"""
		from time import perf_counter
		from functools import wraps
		
		@wraps(fn)
		def inner(*args, **kwargs):
			total_elapsed = 0
			for i in range(reps):
				start = perf_counter()
				result = fn(*args, **kwargs)
				end = perf_counter()
				total_elapsed += (end - start)
			avg_elapsed = total_elapsed / reps
			print(f'Avg Run time: {avg_elapsed:.7f}s ({reps} reps)')
			return result
		return inner
	return decorator

# ToDo: Add code to handle corner cases, Write unit tests for all cases
@timed(1)
def profile_maker(n : int) -> list:
    """
        profile maker function can be used to generate n fake profiles using the Faker module.

        parameters: n (int) | Number of profiles to be generated
        return: list of profiles | Each profile is an instance of namedtuple
    """
    fake = Faker()
    Profile = namedtuple("Profile", fake.profile().keys())

    profiles = list()
    for _ in range(n):
        profiles.append(Profile(**fake.profile()))
    
    return profiles

# ToDo: Add code to handle corner cases, Write unit tests for all cases
@timed(1)
def profile_maker_dict(n : int) -> list:
    """
        profile maker function can be used to generate n fake profiles using the Faker module.

        parameters: n (int) | Number of profiles to be generated
        return: list of profiles | Each profile is an instance of dictionary
    """
    fake = Faker()

    profiles = list()
    for _ in range(n):
        profiles.append(fake.profile())
    
    return profiles

# ToDo: Add corner cases, Write test function
@timed(1000)
def largest_blood_type(profiles: list) -> str:
    """
       largest_blood_type function iterates through the profiles (list of named tuples), access the blood group of each profile
        and maintains the count of each blood group in a dictionary. Then it returns the blood group with the largest frequency.

        parameters: profiles (list) | list of named tuple, Where each named tuple represents a profile.
        return: largest blood group (str)
    """
    blood_groups = dict()

    for profile in profiles:
        bg = getattr(profile, "blood_group", "other")
        blood_groups[bg] = blood_groups.get(bg, 0) + 1

    # print(blood_groups)

    return max(blood_groups, key=blood_groups.get)

# ToDo: Add corner cases, Write test function
@timed(1000)
def largest_blood_type_dict(profiles: list) -> str:
    """
       largest_blood_type function iterates through the profiles (list of dictionaries), access the blood group of each profile
        and maintains the count of each blood group in a dictionary. Then it returns the blood group with the largest frequency.

        parameters: profiles (list) | list of dictionaries, Where each dictionary represents a profile.
        return: largest blood group (str)
    """
    blood_groups = dict()

    for profile in profiles:
        bg = profile.get("blood_group", "other")
        blood_groups[bg] = blood_groups.get(bg, 0) + 1

    # print(blood_groups)

    return max(blood_groups, key=blood_groups.get)


# ToDo: Add corner cases, write unit tests
@timed(1000)
def mean_current_location(profiles: list) -> namedtuple:
    """
        mean_current_location function iterates through the profiles (list of named tuples), It access the current location of each profile
        and computes the mean location of all profiles.

        parameters: profiles (list) | list of named tuple, Where each named tuple represents a profile.
        return: mean current location (namedtuple)
    """
    x = y = 0

    for profile in profiles:
        current_location = getattr(profile, "current_location", None)
        x += current_location[0]
        y += current_location[1]

    n = len(profiles)
    x_mean = x/n
    y_mean = y/n

    MeanLocation = namedtuple("MeanLocation", "x y")
    return MeanLocation(x=x_mean, y=y_mean)

# ToDo: Add corner cases, write unit tests
@timed(1000)
def mean_current_location_dict(profiles: list) -> namedtuple:
    """
        mean_current_location function iterates through the profiles (list of dictionaries), It access the current location of each profile
        and computes the mean location of all profiles.

        parameters: profiles (list) | list of dictionaries, Where each dictionaries represents a profile.
        return: mean current location (dictionary)
    """
    x = y = 0

    for profile in profiles:
        current_location = profile.get("current_location", None)
        x += current_location[0]
        y += current_location[1]

    n = len(profiles)
    x_mean = x/n
    y_mean = y/n

    return {"x":x_mean, "y":y_mean}


# ToDo: Corner cases, Unit tests
@timed(1000)
def oldest_person_age(profiles: list) -> int:
    """
       oldest_person_age function iterates through the profiles (list of named tuples), It access the birthdate of each profile
        and computes age of all profiles. Then Extracts the oldest age.

        parameters: profiles (list) | list of named tuple, Where each named tuple represents a profile.
        return: oldest (int) oldest person's age in from the profiles
    """
    oldest = 0
    for profile in profiles:
        birthdate = getattr(profile, "birthdate", None)
        today = datetime.datetime.today()
        
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1

        oldest = max(oldest, age)

    return oldest

# ToDo: Corner cases, Unit tests
@timed(1000)
def oldest_person_age_dict(profiles: list) -> int:
    """
       oldest_person_age function iterates through the profiles (list of dictionaries), It access the birthdate of each profile
        and computes age of all profiles. Then Extracts the oldest age.

        parameters: profiles (list) | list of dictionaries, Where each dictionary represents a profile.
        return: oldest (int) oldest person's age in from the profiles
    """
    oldest = 0
    for profile in profiles:
        birthdate = profile.get("birthdate", None)
        today = datetime.datetime.today()
        
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1

        oldest = max(oldest, age)

    return oldest


# ToDo: Corner cases, Unit tests
@timed(1000)
def average_age(profiles : list) -> float:
    """
        average_age function iterates through the profiles (list of named tuples), It access the birthdate of each profile
        and computes age of all profiles. Then computes the average age.

        parameters: profiles (list) | list of named tuple, Where each named tuple represents a profile.
        return: average age (float) average age of all the profiles.
    """
    age_sum = 0
    for profile in profiles:
        birthdate = getattr(profile, "birthdate", None)
        if birthdate == None:
             continue
        today = datetime.datetime.today()
        
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1

        age_sum += age

    return age_sum/len(profiles)

# ToDo: Corner cases, Unit tests
@timed(1000)
def average_age_dict(profiles : list) -> float:
    """
        average_age function iterates through the profiles (list of dictionaries), It access the birthdate of each profile
        and computes age of all profiles. Then computes the average age.

        parameters: profiles (list) | list of dictionaries, Where each dictionary represents a profile.
        return: average age (float) average age of all the profiles.
    """
    age_sum = 0
    for profile in profiles:
        birthdate = profile.get("birthdate", None)
        if birthdate == None:
             continue
        today = datetime.datetime.today()
        
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1

        age_sum += age

    return age_sum/len(profiles)

# ToDo : ...
def company_stocks(n:int = 100) -> namedtuple:
    """
    Generates a list of stock data for a given number of companies and calculates the overall market values.

    This function creates fake data for an imaginary stock exchange by generating a list of `CompanyStock`
    namedtuples, each representing a company's stock information. The data includes the company's name, 
    stock symbol, opening price, highest price, closing price, and a random weight for each company. 

    The function also calculates the stock market's overall value at the start of the day, its highest value 
    during the day, and the value at the end of the day. The market values are calculated as weighted averages 
    of the respective stock prices.

    Parameters:
    -----------
    n : int, optional
        The number of companies for which stock data is to be generated. Default is 100.

    Returns:
    --------
    namedtuple
        A namedtuple `Stocks` containing the following fields:
        - company_stocks: List of `CompanyStock` namedtuples with company stock data.
        - open_value: Weighted average market value at the start of the day.
        - high_value: Weighted average market value at the highest point of the day.
        - close_value: Weighted average market value at the end of the day.
    """
    import random
    
    fake = Faker()
    CompanyStock = namedtuple("CompanyStock", ("name", "symbol", "open", "high", "close", "weight"))

    company_stocks = list()
    for _ in range(n):
        name = fake.company()
        symbol = "".join([word[0].upper() for word in name.split()])
        open = random.uniform(100, 500)
        high = random.uniform(open, open * 1.1)
        close = random.uniform(open, high)
        weight = random.random()

        company_stocks.append(CompanyStock(name, symbol, open, high, close, weight))
    
    total_weight = sum(company.weight for company in company_stocks)
    # Taking stock value as (open + close) / 2 for simplicity.
    open_value = sum(((company.open + company.close) / 2) * company.weight for company in company_stocks) / total_weight
    # For high (high + close) / 2
    high_value = sum(((company.high + company.close) / 2) * company.weight for company in company_stocks) / total_weight
    # For high (close + close) / 2
    close_value = sum(((company.close) + company.close) / 2 * company.weight for company in company_stocks) / total_weight

    Stocks = namedtuple("Stocks", ("company_stocks", "open_value", "high_value", "close_value"))
    return Stocks(company_stocks, open_value, high_value, close_value)
    
