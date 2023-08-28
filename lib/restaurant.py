class Restaurant:
    def __init__(self,name):
        self.name=name   
        self.reviews=[]

    def name(self):
        return self.name 

    def add_to_reviews(self):
        return self.reviews.append(Review)        
    def reviews(self):
        return [obj.rating for obj in self.reviews]
    
    def customers(self):
        return  [obj.customer for obj in self.reviews]

eats = Restaurant("Pizzeria")
