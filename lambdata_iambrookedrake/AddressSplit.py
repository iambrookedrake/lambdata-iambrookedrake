import usaddress
# Split address into multiple columns
from pdb import set_trace as breakpoint




def address_split(address):
    return usaddress.tag(address)

if __name__ == '__main__':
    address = input("Address Column: ")
    print(usaddress.tag(address))
