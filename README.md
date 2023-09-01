# A uthor
- Dennis Kimaita

# Restaurant Review System

This Python code implements a basic restaurant review system. It consists of three main classes: `Review`, `Restaurant`, and `Customer`.

## Review Class

The `Review` class represents individual reviews, allowing customers to rate restaurants. It provides methods to set and get ratings and associate reviews with customers and restaurants.

## Restaurant Class

The `Restaurant` class represents restaurants and their associated reviews. It includes methods to add reviews, calculate the average star rating, and list the customers who reviewed the restaurant.

## Customer Class

The `Customer` class represents customers who can create reviews for restaurants. It offers methods to update customer information, create reviews, find customers by name, and retrieve a list of restaurants the customer reviewed.

## Usage

Here's how to use the provided classes:

1. Create instances of `Customer`, `Restaurant`, and `Review`.
2. Use the `create_review` method of the `Customer` class to associate a review with a restaurant.
3. Utilize various methods to retrieve information such as average ratings and customer details.

Example usage:

```python
kim = Customer("Dennis", "Kimaita")
restaurant = Restaurant("Pizzeria")
restaurant2 = Restaurant("Taco")
review1 = Review(kim, restaurant, 10)
kim.create_review(restaurant2, 6)
kim.num_reviews()
Customer.find_all_by_given_name("Dennis")
print(restaurant.average_star_rating())