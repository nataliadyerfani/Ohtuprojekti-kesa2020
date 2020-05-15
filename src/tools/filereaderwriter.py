'''This module provides functions for handling files.'''

import os
import sys

from typing import List, Tuple
from pathlib import Path


def read_settings(file_path: str, comment_sign: str = '#', assignment_sign: str = '=') -> List[Tuple[str,str]]:
    f'''Reads one file containing the various settings to be used in this application.
    File should be of the following format:
    variable1=value
    variablen=value
    That is one variable with the specified setting per line. Empty and comment lines are ignored.
    Returns a list containing every variable and value. If the file does not exist, returns an empty list.
    '''
    settings = []

    if not check_file_exists(file_path):
        return settings

    with open(file_path, 'r') as f:
        for l in f.readlines():
            #l = l.strip()
            
            # Skip empty, faulty and commentlines
            # Valid lines contains exactly one assignment sign: =
            if not l or l.startswith(comment_sign) or l.count(assignment_sign) != 1:
                continue
            
            settings.append(tuple(map(str.strip, l.split(assignment_sign))))
    
    return settings


def check_directory_exists(path: str) -> bool:
    '''Checks if the path provided as argument exists and is a directory.'''
    return os.path.isdir(path)


def check_file_exists(path: str) -> bool:
    '''Checks if the path provided as argument exists and is a file.'''
    return os.path.isfile(path)


def create_directory(path: str) -> None:
    '''Creates a directory with all subdirectories.
    Raises exception and quits the application if directory could not be created.'''
    try:
        os.makedirs(path)
    except Exception as e:
        print(f'Error while trying to create directory \'{path}\'')
        print(e)
        print('Exiting..')
        sys.exit()

    return check_directory_exists(path)


def build_path(*args: str) -> str:
    '''Helper function that takes an arbitrary number of strings and joins them all to build a proper filepath.'''
    return Path('/'.join(args))