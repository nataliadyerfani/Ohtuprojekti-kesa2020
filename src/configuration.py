'''Configuration module for the application. Contains variables that should be easy to change anywhere in the application.
Should be imported in the main function and let it initialize. After that can be imported anywhere to use the vars.
'''

from typing import List, Tuple
from tools import filereaderwriter as fileio

# Should only be initialized one time.
is_initialized = False

# Directories
paths = {'PATH_SETTINGS_DIR': 'config',
         'PATH_IMAGES': 'images', 
         'PATH_DATA': 'data'
}

# Filenames
fnames = {'SETTINGS_FNAME': 'settings'}

# Misc settings, default values can be assigned here.
# Also the settings read from file will be stored here.
settings = {'settings_comment_sign': '#',
            'settings_assignment_sign': '=',
            'CAMERA_ID': 0
}


# This function should probably be moved to a module containing helper functions..?
def convert_strings_to_proper_type(val: str):
    '''Helper function that takes an argument of type string and if the arguments contains a number,
    that can be converted to int or float, returns the converted number. If the arguments contains
    True or False it will return an boolean. If the argument is not of type string an empty string
    will be returned. Otherwise returns a new string object.
    '''
    if not isinstance(val, str): 
        return ''
    
    try:
        if 'true' == val.lower(): return True
        if 'false' == val.lower(): return False
        return float(val) if '.' in val else int(val)
    except ValueError:
        return str(val)


def initialize_directories() -> None:
    print('Configured directories:')
    for key, directory in paths.items():
        if not fileio.check_directory_exists(directory):
            print(f'./{directory}/ directory for {key} not found, attempting to create..')
            fileio.create_directory(directory) # If creation is unsuccessful, an exception
                                               # will be raised, and app exited.

        print(f'Using ./{directory}/ for {key}!')
        print()


def read_settings(file_path: str,
                  comment_sign: str = '#',
                  assignment_sign: str = '=') -> List[Tuple[str,str]]:
    '''Reads the file specified as the argument "file_path" and creates a List containing one
    tuple for every setting.
    File should be of the following format:
    variable1=value
    variablen=value
    That is one variable with the specified setting per line. Empty and comment lines are ignored.
    Returns a list of tuples, each one containing a variable and value pair.
    If the file is empty or could not be read returns an empty List.
    '''
    settings = []

    for l in fileio.read_file_lines(file_path):
        # Skip empty, faulty and commentlines
        # Valid lines contains exactly one assignment sign: =
        if not l or l.startswith(comment_sign) or l.count(assignment_sign) != 1:
            continue        
        settings.append(tuple(map(str.strip, l.split(assignment_sign))))
    
    return settings


def load_settings_from_file() -> None:
    '''Reads the settings, converts them into the right type and loads them'''
    settings_file = fileio.build_path(paths['PATH_SETTINGS_DIR'], fnames['SETTINGS_FNAME'])
    print(f'Using settings file \'./{settings_file}\'.')

    settings_read = read_settings(settings_file,
                                  settings['settings_comment_sign'],
                                  settings['settings_assignment_sign']
    )
    
    if len(settings_read) != 0:
        print(f'Using {len(settings_read)} setting(s) from file.')
        
        # The list contains tuples, but we still need to unpack them with map here
        for var, val in map(lambda pair: (pair[0], pair[1]), settings_read):
            settings[var] = convert_strings_to_proper_type(val)
    else:
        print('No settings loaded, using default values.')
    print()


def print_settings() -> None:
    print('Active settings')
    for k,v in settings.items():
        print(k, ':', v, '. With types', type(k), ':', type(v))
    print()


def initialize() -> None:
    '''This function should be run once, from the main-function. Creates the directories and
    loads the settings from the settings file if it exists.
    '''
    
    print('Initializing')
    initialize_directories()
    load_settings_from_file()
    print('All loaded!')


if not is_initialized:
    initialize()
    is_initialized = True
