# epai-session8
EPAI course from TSAI, Assignment8

# Fake Data Profile Generator & Stock Market Simulation

This repository contains Python code that generates fake profile data using the Faker library and simulates stock market data for an imaginary exchange. The code also includes performance measurement using decorators, allowing you to assess the average execution time of various functions.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Functions](#functions)
  - [Profile Generation](#profile-generation)
  - [Stock Market Simulation](#stock-market-simulation)
- [Performance Measurement](#performance-measurement)

## Installation

To run the code, you'll need Python 3.x installed on your machine. Additionally, you need to install the `Faker` library, which is used for generating fake data.

You can install `Faker` using pip:

```bash
pip install faker
```

## Usage

This code can be used to generate fake profile data and simulate stock market data for 100 companies. It also includes decorators for measuring the execution time of the functions.

#### Example Usage
```python
from session8 import profile_maker, company_stocks

# Generate 10 fake profiles
profiles = profile_maker(10)
print(profiles)

# Simulate stock market data for 100 companies
stocks = company_stocks(100)
print(stocks.open_value)
```
# Functions

## Profile Generation

- **profile_maker(n: int) -> list:** Generates n fake profiles using Faker. Returns a list of profiles, where each profile is a named tuple.
- **profile_maker_dict(n: int) -> list:** Similar to profile_maker, but returns a list of profiles as dictionaries instead of named tuples.
- **largest_blood_type(profiles: list) -> str:** Finds and returns the most common blood type in a list of profiles.
- **largest_blood_type_dict(profiles: list) -> str:** Similar to largest_blood_type, but works with profiles as dictionaries.
- **mean_current_location(profiles: list) -> namedtuple:** Calculates the mean (average) current location (latitude and longitude) from a list of profiles.
- **mean_current_location_dict(profiles: list) -> dict:** Similar to mean_current_location, but returns the mean location as a dictionary.
- **oldest_person_age(profiles: list) -> int:** Finds and returns the age of the oldest person in the list of profiles.
- **oldest_person_age_dict(profiles: list) -> int:** Similar to oldest_person_age, but works with profiles as dictionaries.
- **average_age(profiles: list) -> float:** Calculates the average age of all profiles in the list.
- **average_age_dict(profiles: list) -> float:** Similar to average_age, but works with profiles as dictionaries.

## Stock Market Simulation

- **company_stocks(n: int = 100) -> namedtuple:** Generates a list of stock data for n companies. Each company has attributes like name, stock symbol, opening price, highest price, closing price, and a random weight. The function also calculates the overall market values at the start, highest point, and end of the day.


## Performance Measurement

The code uses a custom decorator @timed(reps) to measure the execution time of functions. The decorator runs the decorated function reps times and prints the average execution time.

#### Example Usage of the Decorator
```python
@timed(100)
def example_function():
    # Function code
    pass
```

This will measure the average execution time of example_function over 100 runs.