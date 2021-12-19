'''
Chain of responsibility pattern is used to achieve loose coupling in software design 
where a request from the client is passed to a chain of objects to process them. 
Later, the object in the chain will decide themselves who will be processing the request 
and whether the request is required to be sent to the next object in the chain or not.

eg. In the below method we have different validators, like AlphaCharValidator, NumericValidator
Each validator is responsible for its own validation. 
If the validation get success it passes the data to the next validator.
The main point is, if we want to build new validator, we can add or remove a validator class as per our requirement.
'''

import abc
import re

class Validator(metaclass=abc.ABCMeta):
    def __init__(self, validator=None):
        self.__validator = validator

    def validate(self, data):
        if self.__validator != None:
            return self.__validator.validate(data)
        return data

class AlphaCharValidator(Validator):
    def validate(self, data):
        if not re.search('[a-zA-Z]', data):
            raise Exception('Data does not contain aplhabetical characters.')
        return super().validate(data)

class NumericValidator(Validator):
    def validate(self, data):
        if not re.search('\d', data):
            raise Exception('Data does not contain numeric characters.')
        return super().validate(data)


class SpecialCharValidator(Validator):
     def validate(self, data):
        if not re.search('[^\da-zA-Z]', data):
            raise Exception('Data does not contain special characters.')
        return super().validate(data)


class MaxLengthValidator(Validator):
    def __init__(self, max_length, validator=None):
        self.__max_length = max_length
        super().__init__(validator=validator)

    @property
    def max_length(self):
        return self.__max_length

    def validate(self, data):
        if len(data) > self.__max_length:
            raise Exception('Data exceeded the maxinum length. Must be less than {}'.format(self.__max_length))
        return super().validate(data)

class MaxLengthValidatorFactory:
    def __init__(self, max_length):
        self.__max_length = max_length

    def __call__(self, validator=None):
        return MaxLengthValidator(self.__max_length, validator=validator)


def main():
    CustomMaxLengthValidator = MaxLengthValidatorFactory(max_length=10)
    
    password_validator = CustomMaxLengthValidator(
        AlphaCharValidator(
            NumericValidator(
                SpecialCharValidator()
            )
        )
    ) # CustomMaxLengthValidator -> AlphaCharValidator -> NumericValidator -> SpecialCharValidator

    try:
        validated_data = password_validator.validate('Ajesh@123')
        print(validated_data)
    except Exception as e:
        # handling validation failed
        print('Validation failed')
        print(e)
        
        
if __name__ == '__main__':
    main()

