import session8 as s8
import datetime
import time
from io import StringIO 
import sys
from decimal import Decimal
from collections import namedtuple

class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self
    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio    # free up some memory
        sys.stdout = self._stdout

def test_timed_function():
	@s8.timed(10)
	def func(*args):
		time.sleep(0.2)
		pass

	with Capturing() as output:
		func()

	assert any(["Avg" or "Average" in o for o in output])
	assert any(["10" in o for o in output])
      
def test_profile_maker():
    # Redecorating with reps = 1
    test_profile_maker = s8.timed(1)(s8.profile_maker)
    
    profiles = test_profile_maker(10)
    
    assert len(profiles) == 10
    assert isinstance(profiles[0], tuple)

def test_profile_maker_dict():
    # Redecorating with reps = 1
    test_profile_maker_dict = s8.timed(1)(s8.profile_maker_dict)
    
    profiles = test_profile_maker_dict(10)
    
    assert len(profiles) == 10
    assert isinstance(profiles[0], dict)


profiles_dict = [{'job': 'Brewing technologist',
  'company': 'Brown-Stephenson',
  'ssn': '528-15-7664',
  'residence': '391 Keller Pass Apt. 761\nJoshuafort, PA 84799',
  'current_location': (Decimal('54.9056535'), Decimal('-137.990074')),
  'blood_group': 'B+',
  'website': ['http://calhoun.org/',
   'http://hudson-fisher.net/',
   'http://kim.com/',
   'https://www.simon.org/'],
  'username': 'anthony00',
  'name': 'Joseph Bennett',
  'sex': 'M',
  'address': '81391 Herman Shoals Suite 207\nNew Coreyhaven, NV 20172',
  'mail': 'benjamin76@yahoo.com',
  'birthdate': datetime.date(1942, 1, 16)},
 {'job': 'Technical sales engineer',
  'company': 'Howell-Cantrell',
  'ssn': '467-58-3561',
  'residence': 'PSC 8512, Box 6394\nAPO AE 06648',
  'current_location': (Decimal('83.5594775'), Decimal('-27.814060')),
  'blood_group': 'B+',
  'website': ['https://www.drake.com/'],
  'username': 'wilsoncathy',
  'name': 'William Jensen',
  'sex': 'M',
  'address': '17989 Linda Wall Suite 645\nCruzburgh, NJ 44765',
  'mail': 'ericclark@yahoo.com',
  'birthdate': datetime.date(2022, 2, 14)},
 {'job': 'Automotive engineer',
  'company': 'Bates LLC',
  'ssn': '270-57-4485',
  'residence': '9048 Gabrielle Points\nJamesfort, VT 39813',
  'current_location': (Decimal('-76.1333805'), Decimal('-80.790995')),
  'blood_group': 'O+',
  'website': ['https://www.powell-henson.com/'],
  'username': 'lisaholloway',
  'name': 'Laura Lopez',
  'sex': 'F',
  'address': '14906 Keith Course\nGibbsburgh, MO 84256',
  'mail': 'ambermarks@gmail.com',
  'birthdate': datetime.date(1908, 11, 10)}]

Profile = namedtuple("Profile", profiles_dict[0].keys())
profiles_namedtuple = [Profile(**profile) for profile in profiles_dict]


def test_largest_blood_type():
      # Redecorating with reps = 1
    test_largest_blood_type = s8.timed(1)(s8.largest_blood_type)
    result = test_largest_blood_type(profiles_namedtuple)

    assert result == "B+"

def test_largest_blood_type_dict():
    # Redecorating with reps = 1
    test_largest_blood_type_dict = s8.timed(1)(s8.largest_blood_type_dict)
    result = test_largest_blood_type_dict(profiles_dict)

    assert result == "B+"

def test_mean_current_location():
    # Redecorating with reps = 1
    test_mean_current_location = s8.timed(1)(s8.mean_current_location)
    result = test_mean_current_location(profiles_namedtuple)

    x = y = 0

    for profile in profiles_namedtuple:
        current_location = getattr(profile, "current_location", None)
        x += current_location[0]
        y += current_location[1]

    n = len(profiles_namedtuple)
    x_mean = x/n
    y_mean = y/n

    MeanLocation = namedtuple("MeanLocation", "x y")

    assert result == MeanLocation(x=x_mean, y=y_mean)

def test_mean_current_location_dict():
    # Redecorating with reps = 1
    test_mean_current_location_dict = s8.timed(1)(s8.mean_current_location_dict)
    result = test_mean_current_location_dict(profiles_dict)

    x = y = 0

    for profile in profiles_dict:
        current_location = profile.get("current_location", None)
        x += current_location[0]
        y += current_location[1]

    n = len(profiles_dict)
    x_mean = x/n
    y_mean = y/n

    assert result == {"x":x_mean, "y":y_mean}

def test_oldest_person_age():
    # Redecorating with reps = 1
    test_oldest_person_age = s8.timed(1)(s8.oldest_person_age)
    result = test_oldest_person_age(profiles_namedtuple)

    oldest = 0
    for profile in profiles_namedtuple:
        birthdate = getattr(profile, "birthdate", None)
        today = datetime.datetime.today()
        
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1

        oldest = max(oldest, age)  
    assert result == oldest

def test_oldest_person_age_dict():
    # Redecorating with reps = 1
    test_oldest_person_age_dict = s8.timed(1)(s8.oldest_person_age_dict)
    result = test_oldest_person_age_dict(profiles_dict)

    oldest = 0
    for profile in profiles_dict:
        birthdate = profile.get("birthdate", None)
        today = datetime.datetime.today()
        
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1

        oldest = max(oldest, age)  
    assert result == oldest

def test_average_age():
    # Redecorating with reps = 1
    test_average_age = s8.timed(1)(s8.average_age)
    result = test_average_age(profiles_namedtuple) 

    age_sum = 0
    for profile in profiles_namedtuple:
        birthdate = getattr(profile, "birthdate", None)
        if birthdate == None:
             continue
        today = datetime.datetime.today()
        
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1

        age_sum += age

    assert result == age_sum/len(profiles_namedtuple)

def test_average_age_dict():
    # Redecorating with reps = 1
    test_average_age_dict = s8.timed(1)(s8.average_age_dict)
    result = test_average_age_dict(profiles_dict) 

    age_sum = 0
    for profile in profiles_dict:
        birthdate = profile.get("birthdate", None)
        if birthdate == None:
             continue
        today = datetime.datetime.today()
        
        age = today.year - birthdate.year
        if (today.month, today.day) < (birthdate.month, birthdate.day):
            age -= 1

        age_sum += age

    assert result == age_sum/len(profiles_dict)


# Tests for testing company_stocks function:

companies_stock_values = s8.company_stocks(n=100)

def test_number_of_companies():
    assert len(companies_stock_values.company_stocks) == 100, "The number of companies should be 100."

def test_namedtuple_structure():
    for company in companies_stock_values.company_stocks:
        assert hasattr(company, 'name')
        assert hasattr(company, 'symbol')
        assert hasattr(company, 'open')
        assert hasattr(company, 'high')
        assert hasattr(company, 'close')
        assert hasattr(company, 'weight')

def test_open_less_than_high():
    for company in companies_stock_values.company_stocks:
        assert company.open <= company.high, f"Open price should be <= high price for {company.name}."

def test_close_between_open_and_high():
    for company in companies_stock_values.company_stocks:
        assert company.open <= company.close <= company.high, f"Close price should be between open and high for {company.name}."

def test_open_less_than_high():
    for company in companies_stock_values.company_stocks:
        assert company.open <= company.high, f"Open price should be <= high price for {company.name}."

def test_sum_of_weights_positive():
    total_weight = sum(company.weight for company in companies_stock_values.company_stocks)
    assert total_weight > 0, "Sum of weights should be positive."

def test_high_value_reasonable():
    assert (companies_stock_values.high_value > 0 or companies_stock_values.high_value != None), "High value should be a reasonable number."

def test_end_value_reasonable():
    assert (companies_stock_values.close_value > 0 or companies_stock_values.close_value != None), "Close value should be a reasonable number."

def test_high_value_greater_than_open_and_close():
    assert companies_stock_values.high_value >= companies_stock_values.open_value, "High value should be greater than or equal to open value."
    assert companies_stock_values.high_value >= companies_stock_values.close_value, "High value should be greater than or equal to close value."

def test_values_calculated_with_weights():
    unweighted_start_value = sum((company.open + company.close) / 2 for company in companies_stock_values.company_stocks) / len(companies_stock_values.company_stocks)
    assert companies_stock_values.open_value != unweighted_start_value, "Start value should be calculated using weights, not unweighted average."
