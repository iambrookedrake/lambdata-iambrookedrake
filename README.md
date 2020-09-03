##### lambdata-iambrookedrake

## Installations

TrainValTest requires installation of [sklearn](https://scikit-learn.org/stable/install.html)

AddressSplit requires installation of [usaddress](https://pypi.org/project/usaddress/) using the following command:
 pip install usaddress

## Usage

postISA.py requests input for 'Salary Offer' and 'Tax Rate %'. Providing these will return the Annual, Monthly and Weekly salaries, after taxes and Lambda ISA payments are taken out. 

#######
my_lambdata/TrainValTest.py splits one dataset into three for the purpose of training, validating, and testing on that dataset.

This function is a utility wrapper around the Scikit-Learn train_test_split that splits arrays or matrices into train, validation, and test subsets.
Args:
    X (Numpy array or DataFrame): This is a DataFrame with features.
            y (Numpy array or DataFrame): This is a Pandas Series with target.
            train_size (float or int): Proportion of the dataset to include in the train split (0 to 1).
            val_size (float or int): Proportion of the dataset to include in the validation split (0 to 1).
            test_size (float or int): Proportion of the dataset to include in the test split (0 to 1).
            random_state (int): Controls the shuffling applied to the data before applying the split for reproducibility.
            shuffle (bool): Whether or not to shuffle the data before splitting
        Returns:
            Train, test, and validation dataframes for features (X) and target (y). 
        """

#######
my_lambdata/AddressSplit.py 
#######
returns an Ordered Dictionary of address parses seperated with tags. Running code will create request for input of "Address To Split:", which will be returned as an ordered dictionary
--example: 512 Montrose Drive, Charleston, WV will return
    (OrderedDict([('AddressNumber', '512'), ('StreetName', 'Montrose'), ('StreetNamePostType', 'Drive'), ('PlaceName', 'Charleston'), ('StateName', 'WV')]), 'Street Address')'''
