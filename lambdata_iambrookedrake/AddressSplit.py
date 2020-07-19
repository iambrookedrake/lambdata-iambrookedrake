import usaddress

from pdb import set_trace as breakpoint


def address_split(address):
    '''Split address into multiple columns'''
    return usaddress.tag(address)


if __name__ == '__main__':
    address = input("Address To Split: ")
    print(usaddress.tag(address))
