'''Configuration module for the application. Contains variables that should be easy to change anywhere in the application.
Should be imported in the main function and let it initialize. After that can be imported anywhere to use the vars.
'''

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
    True or False it will return an boolean. Otherwise returns a new string object.
    '''
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


def load_settings_from_file() -> None:
    settings_file = fileio.build_path(paths['PATH_SETTINGS_DIR'], fnames['SETTINGS_FNAME'])
    print(f'Using settings file \'./{settings_file}\'.')

    settings_read = fileio.read_settings(settings_file, settings['settings_comment_sign'], settings['settings_assignment_sign'])
    
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