import requests
import json

class TestGetProducts:
    def test_get_all_products(self, base_url):
        response = requests.get(f"{base_url}products")
        data = response.json()
        assert response.status_code==200

        # check expected keys in the product data
        expected_keys = {'id', 'title', 'price', 'description','image', 'rating'}
        for key in expected_keys:
            assert key in data[0], f"Key '{key}' not found in product"
            print(f"{key} ada dalam data produk")
            rate_keys = {'rate', 'count'}
        
        # Check keys in rating
        for rate in rate_keys:
            assert rate in data[0]['rating'], f"Key '{rate}' not found in rating"
            print(f"{rate} ada dalam data rating")

    def test_get_single_product(self,base_url):
        product_id = 1
        response = requests.get(f"{base_url}products/{product_id}")
        assert response.status_code==200
        assert response.json()['id'] == product_id
        data = response.json()
        print(json.dumps(data, indent=2))

