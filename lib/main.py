
class Review:
    all_reviews=[]
    def __init__(self,customer,restaurant, rating):
       self.customer=customer
       self.restaurant=restaurant
       self.rating=rating
       Review.add_to_reviews(self)
    def get_rating(self):
        return self._rating  
    def set_rating(self,rating):
        if type(rating) is int:
            self._rating = rating
        else:
            print('The value must be an integer.')
    rating = property(get_rating, set_rating) 

    @classmethod
    def add_to_reviews(cls, review):
        cls.all_reviews.append(review) 

    def all(self):
        return self.all_reviews      
    
    def customer(self):
        return self.customer
    def restaurant(self):
        return self.restaurant
    pass


class Restaurant:
    def __init__(self,name):
        self.name=name   
        self.reviews=[]

    def name(self):
        return self.name 

    def add_to_reviews(self,review):
        return self.reviews.append(review)        
    def reviews(self):
        return [obj.rating for obj in self.reviews]
    
    def customers(self):
        return  [obj.customer for obj in self.reviews]




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
    def find_all_by_given_name(cls,name):
        for customer in cls.all_customers:
            customer_list=[]
            if customer.given_name==name:
                customer_list.append(customer.given_name)
                print(customer_list)
            else:
                return None
        return customer_list        

        pass  

    pass

kim = Customer("Dennis", "Kimaita")
restaurant = Restaurant("Pizzeria")
restaurant2 = Restaurant("Taco")
kim.create_review(restaurant, 10)
kim.create_review(restaurant2, 6)
kim.num_reviews()
Customer.find_all_by_given_name("Dennis")

