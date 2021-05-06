# pizzaorder-django-api-mongodb
# API endpoints
http://127.0.0.1:8000/api/
![image](https://user-images.githubusercontent.com/59868534/117244283-6469ae00-ae56-11eb-8fa2-09e4858df2c3.png)

API endpoint for creating pizza and listing stored pizzas
http://127.0.0.1:8000/api/pizza/
![image](https://user-images.githubusercontent.com/59868534/117244587-ef4aa880-ae56-11eb-952d-59cd96f82190.png)

API endpoint for filtering with pizza size and type
http://127.0.0.1:8000/api/pizza/?q=Medium
![image](https://user-images.githubusercontent.com/59868534/117244814-5cf6d480-ae57-11eb-83ec-c179c7423c33.png)

API endpoint for editing or deleting pizzas
http://127.0.0.1:8000/api/pizza/1/
![image](https://user-images.githubusercontent.com/59868534/117245026-ba8b2100-ae57-11eb-9d84-43daf21144d3.png)

API endpoint for adding toppings
http://127.0.0.1:8000/api/topping/
![image](https://user-images.githubusercontent.com/59868534/117245119-ed351980-ae57-11eb-8ec9-f9f20cef982d.png)

# Database

Pizzas
![image](https://user-images.githubusercontent.com/59868534/117246536-71889c00-ae5a-11eb-87c4-058889b4b4ca.png)

Toppings
![image](https://user-images.githubusercontent.com/59868534/117246627-9aa92c80-ae5a-11eb-9231-5e4464c81562.png)

# Steps to run project
-->Create a environment

-->In the PizzaOrder app navigate to settings and add your MongoDB database
![image](https://user-images.githubusercontent.com/59868534/117249713-b236e400-ae5f-11eb-83eb-1bcd26cfdc91.png)

-->Run the command "pip install -r requirements.txt", it installs all the packages used in the project
![image](https://user-images.githubusercontent.com/59868534/117248535-c4b01e00-ae5d-11eb-95cf-5823eed19425.png)

-->Run the command "python manage.py makemigrations"
![image](https://user-images.githubusercontent.com/59868534/117248716-080a8c80-ae5e-11eb-93e9-36708226a6a5.png)

-->Run the command "python manage.py migrate"
![image](https://user-images.githubusercontent.com/59868534/117248802-2f615980-ae5e-11eb-924a-3fc8c0cbd993.png)

-->Run the command "python manage.py runserver", it runs the project
![image](https://user-images.githubusercontent.com/59868534/117248938-5b7cda80-ae5e-11eb-80d3-6fb9598860c4.png)

After running the project goto "/api" path
![image](https://user-images.githubusercontent.com/59868534/117249101-a8f94780-ae5e-11eb-90e2-912daa218ac2.png)

