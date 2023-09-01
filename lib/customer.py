from review import Review

class Customer:
    all_customers=[]

    def __init__(self, given_name, family_name):
        
        self.given_name=given_name
        self.family_name=family_name
        self.full_name=Customer.full_name(self)
        self.review_list=[]
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
    def all(self):
        return self.all_customers  

    @classmethod    
    def show_customer_name(cls):
        print([customer.full_name for customer in cls.all_customers])

    def restaurants(self):
        print([obj.restaurant.name for obj in self.review_list])
    
    def create_review(self,restaurant,rating):
        review = Review(self,restaurant,rating)
        self.review_list.append(review)

    def num_reviews(self):
        print(len(self.review_list))     
        return (len(self.review_list))  
    @classmethod
    def find_by_name(cls,name):
        for customer in cls.all_customers:
            if customer.full_name==name:
                print (customer.full_name)

        pass 
    @classmethod
    def find_all_by_given_name(cls, name):
        customer_list = []
        for customer in cls.all_customers:
            if customer.given_name == name:
                customer_list.append(customer.given_name)
                print(customer_list)
            else:
                return None
        return customer_list      

        pass  