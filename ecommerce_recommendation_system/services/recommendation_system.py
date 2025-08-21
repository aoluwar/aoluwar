from collections import defaultdict

class RecommendationSystem:
    def __init__(self, users, products):
        self.users = users
        self.products = products
        self.user_product_matrix = self._create_user_product_matrix()

    def _create_user_product_matrix(self):
        matrix = defaultdict(lambda: defaultdict(int))
        for user in self.users:
            for product in user.viewed_products:
                matrix[user.user_id][product.product_id] += 1
            for product in user.purchased_products:
                matrix[user.user_id][product.product_id] += 2  # Purchased products have a higher weight
        return matrix

    def get_recommendations(self, user_id, num_recommendations=5):
        user_vector = self.user_product_matrix[user_id]
        recommendations = defaultdict(float)

        for other_user_id, other_user_vector in self.user_product_matrix.items():
            if user_id == other_user_id:
                continue

            similarity = self._calculate_cosine_similarity(user_vector, other_user_vector)
            if similarity > 0:
                for product_id, rating in other_user_vector.items():
                    if product_id not in user_vector:
                        recommendations[product_id] += similarity * rating

        sorted_recommendations = sorted(recommendations.items(), key=lambda item: item[1], reverse=True)
        return [self._get_product_by_id(product_id) for product_id, score in sorted_recommendations[:num_recommendations]]

    def _calculate_cosine_similarity(self, vec1, vec2):
        intersection = set(vec1.keys()) & set(vec2.keys())
        dot_product = sum(vec1[item] * vec2[item] for item in intersection)

        norm_vec1 = sum(val ** 2 for val in vec1.values()) ** 0.5
        norm_vec2 = sum(val ** 2 for val in vec2.values()) ** 0.5

        if norm_vec1 == 0 or norm_vec2 == 0:
            return 0.0

        return dot_product / (norm_vec1 * norm_vec2)

    def _get_product_by_id(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                return product
        return None
