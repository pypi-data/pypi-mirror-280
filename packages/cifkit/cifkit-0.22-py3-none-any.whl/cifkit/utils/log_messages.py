from enum import Enum


class CifLog(Enum):
    PREPROCESSING = "Preprocessing {file_path}"
    LOADING_DATA = "Parsing .cif file and generating a supercell"
    COMPUTE_CONNECTIONS = "Computing pair distances and coordination numbers"
