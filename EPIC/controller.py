

class User_detail:
    def validate(self,user_name,password):
        self.user_name = user_name
        self.password = password

        if self.user_name.strip() == "":
            return 'Enter user name'
        if self.password.strip() == "":
            return 'Enter password'
        return "ok"

db = User_detail().validate('','')
print(db)

