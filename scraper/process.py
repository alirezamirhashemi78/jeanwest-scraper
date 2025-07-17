from storage import save_product

def process_product(product_response, review_response):
    review = {"reviews": []}
    for review_detail in review_response.get("Results", []):
        review["reviews"].append({
            "text": review_detail.get("ReviewText"),
            "username": review_detail.get("UserNickname"),
            "userID": review_detail.get("Id"),
            "rate": review_detail.get("Rating"),
            "date": review_detail.get("SubmissionTime"),
        })

    product_response['reviews'] = review
    save_product(product_response)
