##### lambdata-iambrookedrake

## Installations

TrainValTest requires installation of [sklearn](https://scikit-learn.org/stable/install.html)

AddressSplit requires installation of [usaddress](https://pypi.org/project/usaddress/) using the following command:
 pip install usaddress

## Usage

postISA.py requests input for 'Salary Offer' and 'Tax Rate %'. Providing these will return the Annual, Monthly and Weekly salaries, after taxes and Lambda ISA payments are taken out. 

TrainValTest.py splits one dataset into three for the purpose of training, validating, and testing on that dataset.

AddressSplit.py returns an Ordered Dictionary of address parses seperated with tags.
