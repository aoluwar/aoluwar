from models.product import Product
from models.user import User
from services.recommendation_system import RecommendationSystem

def main():
    # Create products
    products = [
        Product(1, "Laptop", "Electronics"),
        Product(2, "Smartphone", "Electronics"),
        Product(3, "Headphones", "Electronics"),
        Product(4, "T-shirt", "Apparel"),
        Product(5, "Jeans", "Apparel"),
        Product(6, "Sneakers", "Footwear"),
    ]

    # Create user
    users = [
        User(1, "Alice"),
        User(2, "Bob"),
        User(3, "Charlie"),
    ]

    # Simulate user behavior
    users[0].view_product(products[0])  # Alice views Laptop
    users[0].purchase_product(products[1])  # Alice purchases Smartphone
    users[0].view_product(products[3])  # Alice views T-shirt

    users[1].view_product(products[0])  # Bob views Laptop
    users[1].purchase_product(products[2])  # Bob purchases Headphones
    users[1].view_product(products[4])  # Bob views Jeans

    users[2].purchase_product(products[1])  # Charlie purchases Smartphone
    users[2].view_product(products[5])  # Charlie views Sneakers

    # Create recommendation system
    recommendation_system = RecommendationSystem(users, products)

    # Get recommendations for a user
    user_id_to_recommend = 1
    recommendations = recommendation_system.get_recommendations(user_id_to_recommend)

    print(f"Recommendations for {users[user_id_to_recommend - 1].name}:")
    for product in recommendations:
        print(product)

if __name__ == "__main__":
    main()
