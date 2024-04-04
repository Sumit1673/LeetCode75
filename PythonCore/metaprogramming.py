"""One of the most important mantras of software development is “don’t repeat yourself.”
That is, any time you are faced with a problem of creating highly repetitive code (or
cutting or pasting source code), it often pays to look for a more elegant solution. In
Python, such problems are often solved under the category of “metaprogramming.” In
a nutshell, metaprogramming is about creating functions and classes whose main goal
is to manipulate code (e.g., modifying, generating, or wrapping existing code). The main
features for this include decorators, class decorators, and metaclasses. However, a variety
of other useful topics—including signature objects, execution of code with exec(), and
inspecting the internals of functions and classes—enter the picture. The main purpose
of this chapter is to explore various metaprogramming techniques and to give examples
of how they can be used to customize the behavior of Python to your own whims.

type is some metaclass that helps us in creating a class for us. It defines how the
structure of class should be.
Class are nothing but an object of "type".
Below code shows how we can define a class using "type".
>>> def a(self):
...     self.z=9
Test explanation-name of the class--if any class inherited---methods/variables defined
>>> Test = type('Test', (), {"a":a})
>>> type(Test)
<class 'type'>
>>> type(Test())
<class '__main__.Test'>
>>> class A:
...     pass
... 
>>> d = A()
>>> type(d)
<class '__main__.A'>
>>> type(A)
<class 'type'>


In Python, __new__ is a special method that's responsible for creating a 
new instance of a class. It's a static method that's called before the 
__init__ method when you create an object. While __init__ is responsible
for initializing the attributes of an object, __new__ is responsible for
creating the object itself.
The typical use case for defining a custom __new__ method is when you 
want to control how instances of your class are created. This might be
necessary when dealing with immutable objects, singletons, or when 
subclassing built-in types.
Here's a simple example to demonstrate the __new__ method:
class MyNewClass:
def __new__(cls, *args, **kwargs):
    instance = super().__new__(cls)
    print("Creating a new instance")
    return instance

def __init__(self):
    print("Initializing instance")

obj = MyNewClass()
In this example, when you create an instance of MyNewClass, the __new__ method 
is called first. It creates an instance using the super().__new__(cls)
call and returns the instance. Then, the __init__ method is called to 
initialize the instance.

The above example shows that __new__ method is called automatically when 
calling the class name, whereas __init__ method is called every time an
instance of the class is returned by __new__ method, passing the returned
instance to __init__ as the self parameter, therefore even if you were to
save the instance somewhere globally/statically and return it every time 
from __new__, then __init__ will be called every time you do just that.

This means that if the super is omitted for __new__ method the __init__ 
method will not be executed. Let’s see if that is the case.

"""

# creating a simple metaclass of our own
class Meta(type):
    """Meta class helps in creating a class and we can 
    change how the class should look if someone uses our Metaclass

    """
    def __new__(cls, class_name, bases,attrs):
        """_summary_

        Args:
            class_name (_type_): _description_
            bases: inherited class name
            attrs (_type_): _description_
        """
        print(attrs)
        return type(class_name, bases, attrs)
    
class Foo(metaclass=Meta):
    x= 9
    y= 0
    
    def hell0(self):
        print("hi")