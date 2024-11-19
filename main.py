# Student name
# Current date
# Default Values for Parameters Practice

# 8-3 (T-Shirt)
def make_shirt(text, size):
    print(f'The Shirt will be a {size} with the text "{text}".')

make_shirt('Python? But i\'m afraid of snakes!', 'large')
make_shirt(size='medium', text='I love python')

print()
# 8-4 (Large Shirts)
def make_shirt_modified(size='large', text='I love python'):
    print(f'The Shirt will be a {size} with the text "{text}".')

make_shirt_modified(size='Medium')
make_shirt_modified()
make_shirt_modified('small', 'Python? But i\'m afraid of snakes!')

print()
# 8-5 (Cities)
def describe_city(city, country='The USA'):
    print(f'{city} is in {country}.')

describe_city('Traverce City')
describe_city('New York')
describe_city('London', 'The UK')