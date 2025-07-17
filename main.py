from scraper.retrieve import retrieve_products_batch, retrieve_product_detail
from scraper.process import process_product
from storage import is_id_exist

def start():
    print("[*] Starting Jeanwest scraper...")
    first_batch = retrieve_products_batch(offset=0, limit=100)
    total_results = first_batch.get("TotalResults", 0)
    print(f"[*] Total products to process: {total_results}")

    for offset in range(0, total_results, 100):
        print(f"[*] Fetching products batch with offset {offset}")
        batch = retrieve_products_batch(offset=offset, limit=100)
        results = batch.get("Results", [])
        print(f"[*] Retrieved {len(results)} products in this batch")

        for product in results:
            product_id = product.get("Id")
            if not product_id:
                continue
            if not is_id_exist(product_id):
                print(f"[*] Fetching details and reviews for product ID {product_id}")
                product_resp, review_resp = retrieve_product_detail(product_id)
                process_product(product_resp, review_resp)
            else:
                print(f"[!] Skipping product ID {product_id} (already processed)")

    print("[*] Scraping completed.")

if __name__ == "__main__":
    start()
