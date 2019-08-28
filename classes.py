# Create a Pizza type for representing pizzas in Python. Think about some basic properties
# that would define a pizza's values; things like size, crust type, and toppings would help.
# Define those in the __init__ method so each instance can have its own specific values for
# those properties.

# Add a method for interacting with a pizza's toppings, called add_topping.
# Add a method for outputting a description of the pizza (sample output below).
# Make two different instances of a pizza. If you have properly defined the class,
# you should be able to do something like the following code with your Pizza type.
# Output should be similar to:
# "I would like a 16-inch, deep-dish pizza with Pepperoni and Olives."

class Pizza:
    '''building a pizza'''
    def __init__(self, size, style, topping):
        '''initialize size, style and toppings attribute'''
        self.size = size
        self.style = style
        self.topping = topping

    def add_toppings(self):
        '''add toppings to pizza '''
        self.size = 12
        self.style = "pan tossed"
        self.topping = "pepperoni"


    def output_pizza(self):
        '''print a description of the pizza ordered'''
        print(f"I would like a {self.size}-inch, {self.style} pizza with {self.topping}.")

one_topping = Pizza(12, "pan tossed", "pepperoni")
two_topping = Pizza(10, "thin", "banana peppers and italian sausage")
one_topping.output_pizza()
two_topping.output_pizza()