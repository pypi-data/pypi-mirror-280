from cifkit.data.mendeleev import get_mendeleev_numbers
from cifkit.utils import string_parser


def get_mendeleev_nums_from_pair_tuple(pair_tuple):
    """
    Parse Mendeleev number for each label in the tuple.
    """
    # Parse the first and second elements
    first_element = string_parser.get_atom_type_from_label(pair_tuple[0])
    second_element = string_parser.get_atom_type_from_label(pair_tuple[1])
    mendeleev_numbers = get_mendeleev_numbers()
    # Get Mendeleev number for the first element
    first_mendeleev_num = mendeleev_numbers[first_element]

    # Get Mendeleev number for the second element
    second_mendeleev_num = mendeleev_numbers[second_element]

    return first_mendeleev_num, second_mendeleev_num
