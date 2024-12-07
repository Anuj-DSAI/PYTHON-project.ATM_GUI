class ATM:
    counter=1
    def __init__(self):
        self.pin=''
        self.balance=1000
        self.user()
        self.sno=ATM.counter
        ATM.counter=ATM.counter+1
    def user(self):
        u_input=int(input('''
                            WELCOME TO UNNIVERSAL BANK

                            LOGIN YOUR ACCOUNT PRESS 1

                            CREATE NEW ACCOUNT PRESS 2
                        '''))
        if(u_input==1):
            self.your_pin()
            self.manue()
        elif(u_input==2):
            self.user_detailse()
            self.age_limt()
            self.gander()
            self.mobile_number()
            self.check_email()
            self.aadhaar_number()
            self.get_16_digit_ATM_Number()
            self.get_4_digit_PinNo()
            self.manue()

                
        else:
            print("thanks for using ATM")

    def manue(self):
        user_input=int(input('''
                              WELCOME TO UNIVERSAL BANK
                            How would you like to proced?
                   
                            Press 1 to check balance
                            Press 2 to  deposit balance
                            Press 3 to withdral balance
                            Press 4 to change pin
                            Press 5 to Exit'''))

        if(user_input==1):
                self.check()
                self.manue()
        elif(user_input==2):
                self.deposit()
                self.manue()
        elif(user_input==3):
                self.withdral()
                self.manue()
        elif(user_input==4):
                self.change()
                self.manue()
        elif user_input in range(6, 9999999999):
          print("Invalid Number: Please Choose a Valid Number")

          self.manue()
                
        else:
                print('         Thanks for using ATM')
                self.user()

    def user_detailse(self):
        name=input("Enter your full name: ")
        address=input("Address: " )

    def age_limt(self):
      while True:
          age = int(input("Enter your age: "))  
          
          if 10 <= age <= 60:  
            return age
          else:
              print("ERROR !? :  Age must be between 10 and 60.")        
        

    def gander(self):
        valid_genders = ["Male", "Female", "Non-binary", "Other"]  
        while True:
            user_input = input("Enter your gender (Male, Female, Non-binary, Other): ")
            
            
            if user_input in valid_genders:
                return user_input
            else:
                print("Invalid gender! Please enter a valid option.")
                
    def mobile_number(self):
        while True:
            user_input = input("Enter Your 10-digit Mobile number: ")
            
            
            if user_input.isdigit() and len(user_input) == 10:
                return user_input
            else:
                print("Invalid input! Please enter exactly 10 digits.")

    def check_email(self):
        while True:
            user_input = input("Enter your email address: ")

            
            if user_input.endswith('@gmail.com'):
                print("Email verified successfully.")
                return user_input
            else:
                print("Invalid email! Please enter a valid Gmail address.")

    def aadhaar_number(self):
      while True:
        aadhaar_number = input("Enter your Aadhaar number: ")

        
        if len(aadhaar_number) == 12 and aadhaar_number.isdigit():
            print("Aadhaar number is valid.")
            return aadhaar_number
        else:
            print("Invalid Aadhaar number! It must be a 12-digit number.")


    def get_16_digit_ATM_Number(self):
        while True:
            user_input = input("Enter a 16-digit ATM number: ")
            
            
            if user_input.isdigit() and len(user_input) == 16:
                print("verification was successful!.")
                return user_input
            else:
                print("Invalid input! Please enter exactly 16 digits.")
            

            
    def get_4_digit_PinNo(self):
        while True:
            self.pin = input("Enter a 4-digit PinNo number: ")
            
            
            if self.pin.isdigit() and len(self.pin) == 4:
                print("PinNo Set Successfully.")
                print("User details saved successfully!")
                return self.pin
            else:
                print("Invalid input! Please enter exactly 4 digits.")
    
    def your_pin(self):
            self.pin=input('Enter Your ATM PinNo: ')
            print('pin set successfully')   
            

    def deposit(self):
      attempts=0  
      while attempts<5:
        temp=input('Enter your ATM PinNo: ')
        if(temp==self.pin):
            amount=int(input('Enter deposit amount: '))
            self.balance=self.balance+amount
            print('deposit successful')
            return amount
        else:
            print('incorrect pin')
            attempts += 1 
            if attempts == 5:
                print("Maximum attempts reached. Access blocked.")
                return None 
                
    def withdral(self):
      attempts=0  
      while attempts<5:  
        temp=input('Enter your ATM PinNo: ')
        if(temp==self.pin):
            amount=int(input('Enter withdral amount: '))
            if(self.balance>amount):
                self.balance=self.balance-amount
                print("Transaction successful")
                return amount
            else:
                print('you balance is low')
                print('your current balance is ',self.balance)
                print("Transaction Failed")
                
        else:
            print('incorrect pin')
            attempts += 1 
            if attempts == 5:
                print("Maximum attempts reached. Access blocked.")
                return None 
        self.user()
    
        
    def check(self):
      attempts=0  
      while attempts<5:
        temp=input('Enter your ATM PinNo: ')
        if(temp==self.pin):
            print(self.balance)
            return self.balance
        else:
          print("Incorrect pin ")
          attempts += 1 
          if attempts == 5:
                print("Maximum attempts reached. Access blocked.")
                return None
          
    def change(self):
      attempts=0  
      while attempts<5:
        temp=input('Enter you old ATM PinNo: ')
        if(temp==self.pin):
            temp1=input('Enter your new ATM PinNo: ')
            self.pin=temp1
            print('pin change successful')
            return self.pin
        else:
            print('Incorrect pin')
            attempts += 1 
            if attempts == 5:
                print("Maximum attempts reached. Access blocked.")
                return None
if __name__=='__main__':

    application=ATM()
    range(0)
