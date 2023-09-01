
class Restaurant:
    def __init__(self,name):
        self.name=name   
        self.reviews = []  # List to store reviews for this restaurant

    # methods for name, add_to_reviews, reviews, customers
    def name(self):
        return self.name 

    def add_to_reviews(self,review):
        return self.reviews.append(review)        
    def reviews(self):
        print( [obj.rating for obj in self.reviews])
    
    def customers(self):
        return  [obj.customer for obj in self.reviews]
    def average_star_rating(self):
        if self.reviews !=0:
            total=0
            for obj in self.reviews:
                total+=obj.rating
                return total/len(self.reviews)
            

        pass