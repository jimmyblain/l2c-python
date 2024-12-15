# 11-1, 2

def get_formatted_location (city, country, population=None):
    '''Takes city name, country name, and optional population size. Returned formatted name.'''
    
    if population:
        formatted_location = f"{city.title()}, {country.title()} - population {population}"
    else:
        formatted_location = f"{city}, {country}"
        formatted_location = formatted_location.title()
    
    return formatted_location
