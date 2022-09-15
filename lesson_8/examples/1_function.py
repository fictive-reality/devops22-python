# positional vs keywords
# https://docs.python.org/3/glossary.html#term-argument

def paint(wall='red', roof='white'):
    print(f'Wall color {wall}, roof color {roof}')


# Use defaults
paint()

# Positional argument for wall color, using default for roof
paint('blue')

# Keyword argument for roof and wall
paint(roof='yellow', wall='pink')

# For positional arguments a tuple can be used with *

colors_tuple = ('black', 'grey')
paint(*colors_tuple)

# For keyword arguments a dict can be used with **

colors_dict = {'wall': 'olive', 'roof': 'lime'}
paint(**colors_dict)
