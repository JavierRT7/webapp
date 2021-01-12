class Users:
    def __init__(self, first_name, surname, email, password):
        self.first_name = first_name
        self.surname = surname
        self.email = email
        self.password = password
    def check_email(email):
        correct_format = False
        for count in range(len(self.email)):
            if self.email(count) == "@"
            correct_format = True
        #Next
        return correct_format
    def check_password(password):
        lower_case = "abcdefghijklmnopqrstuvwxyz"
        upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numbers = "0123456789"
        valid_password = False
        contains_lower_case = False
        contains_upper_case = False
        contains_number = False
        if len(password) >= 6 and 12 >= len(password):
            for count in range(len(password)):
                for x in range(len(lower_case)):
                    if password(count) == lower_case(x):
                        contains_lower_case = True
                #Next
                for x in range(len(upper_case)):
                    if password(count) == upper_case(x):
                        contains_upper_case = True
                #Next
                for x in range(len(numbers)):
                    if password(count) == numbers(x):
                        contains_number = True
                #Next
            #Next
        #End If
        if contains_lower_case == True and contains_upper_case == True and contains_number == True:
            valid_password = True
        #End If
        return valid_password
    #End Function

