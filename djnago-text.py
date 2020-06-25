'''
Explain the architecture of Django?
==================================

	Django is based on MVC architecture. It contains the following layers:

	Models: It describes the database schema and data structure.

	Views: The view layer is a user interface. It controls what a user sees, the view retrieves data from appropriate models and execute any calculation made to the data and pass it to the template.

	Templates: It determines how the user sees it. It describes how the data received from the views should be changed or formatted for display on the page.

	Controller: Controller is the heart of the system. It handles requests and responses, setting up database connections and loading add-ons. It specifies the Django framework and URL parsing.
----------------------------------------------------------------------------------------------------

What are the inheritance styles in Django?
==========================================
	There are three possible inheritance styles in Django:

	1. Abstract base classes: This style is used when you only want parent?s class to hold information that you don’t want to type out for each child model.

	2. Multi-table Inheritance: This style is used if you are sub-classing an existing model and need each model to have its own database table.

	3. Proxy models: This style is used, if you only want to modify the Python level behavior of the model, without changing the model’s fields.
----------------------------------------------------------------------------------------------------
What is the usage of middlewares in Django?
===========================================
	Middlewares are used  go to modify the request i.e. HttpRequest object which is sent to the view, to modify the HttpResponse object returned from the view and to perform an operation before the view executes.

What is the use of session framework in Django?
==============================================
	In Django session is a mechanism to store information on the server side during the interaction with the web application. Session stores in the database and also allows file-based and cache based sessions,  by default,


	The session framework facilitates you to store and retrieve arbitrary data on a per-site visitor basis. It stores data on the server side and abstracts the receiving and sending of cookies. Session can be implemented through a piece of middleware.
----------------------------------------------------------------------------------------------------
Explain the role of Cookie in Django?
=====================================
	Cookie is nothing but a small piece of information which is stored in the client browser. Cookies are used to store user’s data in a file permanently (or for the specified time). There is an  expiry date and time for each cookie and removes automatically when gets expire. There are built-in methods to set and fetch cookie provided by Django.

	set_cookie() method is used to set a cookie and get() method is used to get the cookie.
---------------------------------------------------------------------------------------------------

Explain Django’s Request/Response Cycle?
========================================
	In the Request/Response Cycle, first, a request is received by the Django server. Then, the server looks for a matching URL in the urlpatterns defined for the project. If no matching URL is found, then a response with 404 status code is returned. If a URL matches, then the corresponding code in the view file associated with the URL is executed to build and send a response.
---------------------------------------------------------------------------------------------------
What is a model in Django?
==========================
	A model is a Python class in Django that is derived from the django.db.models.Model class. A model is used in Django to represent a table in a database. It is used to interact with and get results from the database tables of our application.
---------------------------------------------------------------------------------------------------
What are migrations in Django?
==============================
	A migration in Django is a Python file that contains changes we make to our models so that they can be converted into a database schema in our DBMS. So, instead of manually making changes to our database schema by writing queries in our DBMS shell, we can just make changes to our models. Then, we can use Django to generate migrations from those model changes and run those migrations to make changes to our database schema.
---------------------------------------------------------------------------------------------------
What are views in Django?
========================
	A view in Django is a class and/or a function that receives a request and returns a response. A view is usually associated with urlpatterns, and the logic encapsulated in a view is run when a request to the URL associated with it is run. A view, among other things, gets data from the database using models, passes that data to the templates, and sends back the rendered template to the user as an HttpResponse.
---------------------------------------------------------------------------------------------------
Why is Django called a loosely coupled framework?
================================================
	Django is called a loosely coupled framework because of its MVT architecture, which is a variant of the MVC architecture. It helps in separating the server code from the client-related code. Django’s models and views take care of the code that needs to be run on the server like getting records from database, etc., and the templates are mostly HTML and CSS that just need data from models passed in by the views to render them. Since these components are independent of each other, Django is called a loosely coupled framework.
----------------------------------------------------------------------------------------------------
What are the signals in Django?
===============================
	Signals in Django are pieces of code which contain information about what is happening. A dispatcher is used to sending the signals and listen for those signals

	Two important parameters in signals are:
		Receiver: It specifies the callback function which connected to the signal.
		Sender: It specifies a particular sender from where a signal is received.
---------------------------------------------------------------------------------------------------
Explain Mixins in Django ?
==========================
A mixin is a special kind of multiple inheritance. There are two main situations where mixins are used: to provide a lot of optional features for a class and to use one particular feature in a lot of different classes
---------------------------------------------------------------------------------------------------
What is Rest API ?
==================
A REST API is an application program interface that uses HTTP requests to GET, PUT, POST and DELETE data.
----------------------------------------------------------------------------------------------------
What is ORM ? Advantages of ORM ?
=================================
	ORM (Object-relational mapping) is a programming technique for converting data between incompatible type systems using object-oriented programming languages.
		Advantages include:
			Concurrency support
			Cache management
'''