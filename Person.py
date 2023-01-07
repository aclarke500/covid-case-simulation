class Person:
    def __init__(self):
        self.sick=False
        self.days_spent_sick=0
        self.immune=False

    # when we make a person sick
    def infect(self):
        self.sick = True
        self.days_spent_sick=0
    # when a person is done being sick
    def heal(self):
        self.sick = False
        self.immune = True
        self.days_since_recovery=0

    def day(self):
        self.days_since_recovery+=1

    # def day(self, max_sickness_length):
 
    #     # self.days_spent_sick+=1

    #     if self.days_spent_sick < max_sickness_length:
    #         self.heal()

    def get_sick_days(self):
        return self.days_spent_sick
    
    






# print(p1.sick)

# p1.infect()
# print(p1.days_spent_sick, p1.sick)