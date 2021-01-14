class Users:
    def __init__(self, first_name, surname, email, password):
        self.first_name = first_name
        self.surname = surname
        self.email = email
        self.password = password
    def check_email(self, email):
        correct_format = False
        if ("@" in email):
            correct_format = True
        return correct_format
    def check_password(self, password):
        lower_case = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        upper_case = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        valid_password = False
        contains_lower_case = False
        contains_upper_case = False
        contains_number = False
        if len(self.password) >= 6 and 12 >= len(self.password):
            for count in range(len(self.password)):
                for x in range(len(lower_case)):
                    if self.password(count) == lower_case(x):
                        contains_lower_case = True
                #Next
                for x in range(len(upper_case)):
                    if self.password(count) == upper_case(x):
                        contains_upper_case = True
                #Next
                if password(count).isdigit():
                    contains_number = True
            #Next
        #End If
        if contains_lower_case == True and contains_upper_case == True and contains_number == True:
            valid_password = True
        #End If
        return valid_password
    #End Function

