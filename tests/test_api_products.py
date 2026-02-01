import requests
import json

class TestGetProducts:
    # test get all products
    def test_get_all_products(self, base_url):
        response = requests.get(f"{base_url}products")
        data = response.json()
        # cek status code 200
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
        
        print(json.dumps(data, indent=2))

    # test get single product
    def test_get_single_product(self,base_url):
        product_id = 20
        response = requests.get(f"{base_url}products/{product_id}")
        assert response.status_code==200
        data = response.json()
        assert data['id'] == product_id
        print(json.dumps(data, indent=2))

class TestAddProduct:
    # test add new product
    def test_add_new_product(self, base_url):
        new_product = {
            "id":21,
            "title":"Slim Fit Sempak1",
            "price":19000,
            "description":"Slim fit sempak adem",
            "image":"https://test.com"
        }

        response = requests.post(f"{base_url}products", json=new_product)
        assert response.status_code==201
        print(json.dumps(response.json(), indent=2))
    
    # test add product with missing fields
    def test_add_product_missing_fields(self, base_url):
        incomplete_product = {
            "title":"Baju renang wanita",
            "price":18200
        }

        data = requests.post(f"{base_url}products", json=incomplete_product)
        assert data.status_code == 400, f"Expected status code 400, but got {data.status_code}"
        print(json.dumps(data.json(), indent=2))
