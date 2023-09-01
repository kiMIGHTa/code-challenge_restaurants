from customer import Customer
from restaurant import Restaurant
from review  import Review


    

kim = Customer("Dennis", "Kimaita")
restaurant = Restaurant("Pizzeria")
restaurant2 = Restaurant("Taco")
review1=Review(kim,restaurant, 10)
kim.create_review(restaurant2, 6)
kim.num_reviews()
Customer.find_all_by_given_name("Dennis")

print(restaurant.average_star_rating())
