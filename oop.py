# this is class
# class Student:
# # this is class attribute used for common cases in all obkects
#     collageName = "Phoneix" 

# # they are attributes
# # this is constructr  
#     def __init__(self, name):
#         # this is obj attribute  used for each cases in objects 
#         self.name = name   
#         print('Adding new students to the database')

# # this is object
# s1 = Student('Karan')
# print(s1.name)

# s2 = Student('Arjun')
# print(s2.name)

# print(Student.collageName)



# class Student:
#      def __init__(self, name, marks):
#           self.name = name
#           self.marks = marks

#         #   method
#      def get_avg(self):
#           sum = 0
#           for val in self.marks:
#                sum += val
#           print('Hi My name is', self.name, 'and my average is', sum/3)


# s1 = Student("Madhav", [60, 68, 40]) iuigiuugiac
# s1.get_avg()


class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no

    def debit(self, amount):
        self.balance -= amount
        print('Rs.', amount, "has debited from your account")
        print('Your new balance is', self.check_balance())

    def credit(self, amount):
        self.balance += amount
        print('Rs.', amount, "has been credited to your account")
        print('Your new balance is', self.check_balance())

    def check_balance(self):
        return self.balance

acc1 = Account(1000, 878974)
print(acc1.balance)
print(acc1.account_no)
acc1.debit(100)
acc1.credit(2000)