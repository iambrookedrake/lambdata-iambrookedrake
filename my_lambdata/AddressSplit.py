import usaddress

from pdb import set_trace as breakpoint


def address_split(address):
    '''Split address into multiple columns
    example: 512 Montrose Drive, Charleston, WV will return
    (OrderedDict([('AddressNumber', '512'),
    ('StreetName', 'Montrose'), ('StreetNamePostType', 'Drive'),
    ('PlaceName', 'Charleston'), ('StateName', 'WV')]),
    'Street Address')'''
    return usaddress.tag(address)


if __name__ == '__main__':
    address = input("Address To Split: ")
    print(usaddress.tag(address))
