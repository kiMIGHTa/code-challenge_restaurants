class Customer:
    def __init__(self, given_name, family_name):
        self.given_name=given_name
        self.family_name=family_name

    def given_name(self):
        return self.given_name    
     
    def update_given_name(self, new_given_name):
        self.given_name = new_given_name

    def family_name(self):
        return self.family_name 
    
    def update_family_name(self, new_family_name):
        self.family_name = new_family_name
   
    
    def full_name(self):
        return self.given_name + self.family_name
        
    pass