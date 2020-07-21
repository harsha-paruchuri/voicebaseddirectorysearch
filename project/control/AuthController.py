from models.AuthModel import AuthModel

class AuthController:

    def login(self,username,password):

        if len(username) == 0:
            message = "Username cannot be empty"
            return message


        if len(password) == 0:
            message = "password cannot be empty"
            return message

        am = AuthModel()
        result = am.getUser(username,password)

        if result:
            message = 1
            msg = f'Hello {result[1]}'
            return message,msg

        else:
            message = 0
            msg = 'Invalid Username or Password'
            return msg

    def register(self,name,phone,email,username,password):

        if len(name) == 0:
            message = "Name cannot be empty"
            return message
        
        if '@' not in email:
            message = "Invalid email. Kindly Include '@' "
            return message
        

        am = AuthModel()
        result = am.createUser(name,phone,email,username,password)

        if result :
            message = 'You are successfully registered. You can login now'
        else:
            message = 'Some database error. Kindly retry'

        return message


