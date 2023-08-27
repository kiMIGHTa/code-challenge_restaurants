import review
import customers
class Restaurant:
    def __init__(self,name):
        self.name=name   
        self.reviews=[]

    def name(self):
        return self.name 

    def add_to_reviews(self):
        return self.reviews.append(review)        
    def reviews(self):
        return [obj.rating for obj in self.reviews]
    
    def customers(self):
        return  [obj.customer for obj in self.reviews]


