Feature: Product Management API
  As a user of the API
  I want to manage products
  So that I can add, read, update, delete, and search products

  Scenario: List all products
    When I send a "GET" request to "/products"
    Then the response status should be "200"
    And the response should contain a list of products

  Scenario: Read a single product
    Given the database is initialized with the following products
      | name   | category   | description | price  | available |
      | Laptop | Electronics | High-performance laptop | 1200.50 | true  |
    When I send a "GET" request to "/products/1"
    Then the response status should be "200"
    And the response should contain "Laptop"

  Scenario: Update a product
    Given the database is initialized with the following products
      | name   | category   | description | price  | available |
      | Laptop | Electronics | High-performance laptop | 1200.50 | true  |
    When I send a "PUT" request to "/products/1" with the following JSON
      """
      {
        "name": "Gaming Laptop",
        "category": "Electronics",
        "description": "High-end gaming laptop",
        "price": 1500.00,
        "available": true
      }
      """
    Then the response status should be "200"
    And the response should contain "Gaming Laptop"

  Scenario: Delete a product
    Given the database is initialized with the following products
      | name   | category   | description | price  | available |
      | Laptop | Electronics | High-performance laptop | 1200.50 | true  |
    When I send a "DELETE" request to "/products/1"
    Then the response status should be "204"

  Scenario: Search for a product by name
    Given the database is initialized with the following products
      | name    | category   | description | price  | available |
      | Laptop  | Electronics | High-performance laptop | 1200.50 | true  |
      | Phone   | Electronics | Smart phone | 799.99 | true  |
    When I send a "GET" request to "/products?name=Laptop"
    Then the response status should be "200"
    And the response should contain "Laptop"
    And the response should not contain "Phone"

  Scenario: Search for products by category
    Given the database is initialized with the following products
      | name    | category   | description | price  | available |
      | Laptop  | Electronics | High-performance laptop | 1200.50 | true  |
      | Phone   | Electronics | Smart phone | 799.99 | true  |
      | Chair   | Furniture | Comfortable chair | 250.00 | true  |
    When I send a "GET" request to "/products?category=Electronics"
    Then the response status should be "200"
    And the response should contain "Laptop"
    And the response should contain "Phone"
    And the response should not contain "Chair"

  Scenario: Search for products by availability
    Given the database is initialized with the following products
      | name    | category   | description | price  | available |
      | Laptop  | Electronics | High-performance laptop | 1200.50 | true  |
      | Phone   | Electronics | Smart phone | 799.99 | false |
    When I send a "GET" request to "/products?available=true"
    Then the response status should be "200"
    And the response should contain "Laptop"
    And the response should not contain "Phone"
