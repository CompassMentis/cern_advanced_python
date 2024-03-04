# Introduction
Write a script which manages a pizzeria

It does the following:
- Process the orders
- Tells the cook how to prepare each pizza
- Tells the manager when to order more ingredients
- Tells the delivery driver when to deliver a pizza, and to whom

Use the following design patterns:
- Template Pattern for the cooking instructions
- Factory Pattern for instantiating all the classes. We're expecting to replace some classes with proxy classes later
- Observer Pattern to keep the manager and delivery driver informed. We'll tell the cook directly, not through an Observer Pattern

I suggest you use the following steps, but you're welcome to do this any way you want

After some set up, the main code will:
- Read the next order from orders.txt and break it up into customer name, pizza type and crust type
- Get the next order number (1, 2, 3, etc)
- Go through the steps to cook the pizza, based on the recipe, using the Template Pattern

At the start there will be enough of each ingredient for 5 pizzas
When the cook starts on the next pizza, they will decrease the level for each ingredient by 1
- Store the level in a dictionary, ingredient_name:level
- Create function/method to take an ingredient (decrease by 1), 
- and one to top up the ingredients (by a given amount) 
- Use an Observer pattern - whenever the number of ingredients is decreased, notify the subscribers
- The only subscriber is the manager. When a level reaches 2, the manager will order 4 more - this will be added immediately

Orders have a 'status' field, which can be:
- Getting ingredients
- Preparing pizza
- Pizza in oven
- Pizza ready
Use an Observer pattern on the status
- When the status changes, notify the delivery driver
- When the status becomes 'Pizza ready', the delivery driver will delivery the pizza to the customer

Show what is happening as follows:
[customer Sarah Johnson]Places an order for Margherita Pizza, Thin Crust
[cook]Gathers ingredients for Margherita Pizza, Thin Crust
[manager]Orders 4 units of Tomato sauce
[cook]Preheat your oven to 475°F (245°C).
....
[cook]Bake in the preheated oven for 10-12 minutes
[driver]Delivers order 1, Margherita Pizza, Thin Crust, to Sarah Johnson
[customer Sarah Johnson]Receives order 1, Margherita Pizza, Thin Crust
