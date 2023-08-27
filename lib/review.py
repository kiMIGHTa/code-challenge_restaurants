import customers
import restaurant
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
    
    def customer(self):
        return self.customer
    def restaurant(self):
        return self.restaurant
    pass

kim = Review(customers,restaurant, 10)