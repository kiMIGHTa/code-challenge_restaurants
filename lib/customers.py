class Customer:
    all_customers=[]

    def __init__(self, given_name, family_name):
        self.given_name=given_name
        self.family_name=family_name
        self.full_name=Customer.full_name(self) 
        Customer.add_to_customers(self)

    def given_name(self):
        return self.given_name    
     
    def update_given_name(self, new_given_name):
        self.given_name = new_given_name

    def family_name(self):
        return self.family_name 
    
    def update_family_name(self, new_family_name):
        self.family_name = new_family_name
   
    
    def full_name(self):
        return self.given_name +" " + self.family_name

    @classmethod
    def add_to_customers(cls, customer):
        cls.all_customers.append(customer)

    @classmethod    
    def show_customer_name(cls):
        print([customer.full_name for customer in cls.all_customers])
    pass

