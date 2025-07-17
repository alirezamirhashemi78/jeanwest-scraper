import requests
from config import API_PASSKEY, HEADERS, BASE_URL, DISPLAY_CODE, API_VERSION

def retrieve_product_detail(product_id):
    url_product = (
        f"{BASE_URL}/products.json?"
        f"resource=products&filter=id%3Aeq%3A{product_id}&"
        f"filter_reviews=contentlocale%3Aeq%3Aen_AU%2Cen_AU&"
        f"filter_reviewcomments=contentlocale%3Aeq%3Aen_AU%2Cen_AU&"
        f"filteredstats=Reviews&stats=Reviews&passkey={API_PASSKEY}&"
        f"apiversion={API_VERSION}&displaycode={DISPLAY_CODE}"
    )
    url_review = (
        f"{BASE_URL}/reviews.json?"
        f"resource=reviews&action=REVIEWS_N_STATS&"
        f"filter=productid%3Aeq%3A{product_id}&"
        f"filter=contentlocale%3Aeq%3Aen_AU%2Cen_AU&"
        f"filter=isratingsonly%3Aeq%3Afalse&"
        f"filter_reviews=contentlocale%3Aeq%3Aen_AU%2Cen_AU&"
        f"include=authors%2Cproducts&filteredstats=reviews&"
        f"Stats=Reviews&limit=8&offset=0&sort=submissiontime%3Adesc&"
        f"passkey={API_PASSKEY}&apiversion={API_VERSION}&displaycode={DISPLAY_CODE}"
    )

    response_product = requests.get(url_product, headers=HEADERS).json()
    response_review = requests.get(url_review, headers=HEADERS).json()

    return response_product, response_review

def retrieve_products_batch(offset=0, limit=100):
    url = (
        f"{BASE_URL}/batch.json?"
        f"passKey={API_PASSKEY}&apiversion={API_VERSION}&displaycode={DISPLAY_CODE}&"
        f"resource.q0=products&limit={limit}&offset={offset}"
    )
    response = requests.get(url, headers=HEADERS).json()
    return response.get("BatchedResults", {}).get("q0", {})
