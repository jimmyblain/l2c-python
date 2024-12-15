# 11-1, 2
from city_functions import get_formatted_location

# Tests files and functions must start with 'test_'
def test_city_country():
    '''Testing basic City, Country format'''
    formatted_city = get_formatted_location('brooklyn', 'new york')
    # Assert what you expect the output to be in order to pass the test
    assert formatted_city == "Brooklyn, New York"

def test_city_country_population():
    '''Testing City, Country - population xxx format'''
    formatted_city = get_formatted_location('atlanta', 'georgia', 5000000)
    assert formatted_city == "Atlanta, Georgia - population 5000000"