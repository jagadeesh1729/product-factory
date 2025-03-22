import requests
import json
from behave import when, then

API_URL = "http://localhost:5000/products"  

@when('I send a "{method}" request to "/products"')
def step_impl(context, method):
    """Send a request to list all products"""
    response = requests.request(method, API_URL)
    context.response = response

@when('I send a "{method}" request to "/products/{product_id}"')
def step_impl(context, method, product_id):
    """Send a request to retrieve or delete a product"""
    url = f"{API_URL}/{product_id}"
    response = requests.request(method, url)
    context.response = response

@when('I send a "{method}" request to "/products/{product_id}" with the following JSON')
def step_impl(context, method, product_id):
    """Send an update request with JSON data"""
    url = f"{API_URL}/{product_id}"
    headers = {"Content-Type": "application/json"}
    data = json.loads(context.text)
    response = requests.request(method, url, json=data, headers=headers)
    context.response = response

@when('I send a "GET" request to "/products?name={product_name}"')
def step_impl(context, product_name):
    """Search for a product by name"""
    url = f"{API_URL}?name={product_name}"
    context.response = requests.get(url)

@when('I send a "GET" request to "/products?category={category}"')
def step_impl(context, category):
    """Search for products by category"""
    url = f"{API_URL}?category={category}"
    context.response = requests.get(url)

@when('I send a "GET" request to "/products?available={availability}"')
def step_impl(context, availability):
    """Search for products by availability"""
    url = f"{API_URL}?available={availability.lower()}"
    context.response = requests.get(url)

@then('the response status should be "{status_code}"')
def step_impl(context, status_code):
    """Verify response status code"""
    assert str(context.response.status_code) == status_code, \
        f"Expected {status_code}, but got {context.response.status_code}"

@then('the response should contain "{expected_text}"')
def step_impl(context, expected_text):
    """Verify response contains expected text"""
    assert expected_text in context.response.text, \
        f"Expected text '{expected_text}' not found in response"

@then('the response should not contain "{unexpected_text}"')
def step_impl(context, unexpected_text):
    """Verify response does not contain unexpected text"""
    assert unexpected_text not in context.response.text, \
        f"Unexpected text '{unexpected_text}' found in response"
