# REST-API-Limitless-assignment
## Manual for building and running project.

* 'cd' to the directory where requirements.txt is located.
* You can activate your virtualenv (not obligatory).
* Run: `pip install -r requirements.txt` in your shell (in this way You will install all needed packages).
* If You are in place where project is located run: `python manage.py makemigartions` and next `python manage.py migrate`
* If You are in place where project is located run: `python manage.py runserver`
* In case of testing I preffer using Postman. https://www.postman.com/
* You must create a new Request and choose HTTP request method and type reuest Url (Url addres you can check in command prompt after running server, on my computer it is: http://127.0.0.1:8000/
* HTTP request method and Url you must change according to which functionality you want to test:

	* Adding item to collection:
		* Method: POST
		* Url: http://127.0.0.1:8000/
		* In Headers you must specify: Key: Content-Type, Value: application/json
		* In Body you specify your element's name e.g.: `{"name":"horse"}` 
		* Click Send to add your element to data base	
	* Update item to collection:
		* Method: PUT or PATCH
		* Url: You specify element's id e.g. http://127.0.0.1:8000/1/
		* In Headers you must specify: Key: Content-Type, Value: application/json
		* In Body you specify your element's name e.g.: `{"name":"horse2"}` 
		* Click Send to add your element to data base	
	* List collection:
		* Method: GET
		* Url: http://127.0.0.1:8000/
		* Click Send to see whole collection
	* Show specified element:
		* Method: GET
		* Url: You specify element's id e.g. http://127.0.0.1:8000/1/
		* Click Send to see specified element	
	* Delete specified element:
		* Method: DELETE
		* Url: You specify element's id e.g. http://127.0.0.1:8000/1/
		* Click Send to delete specified element
	* Count whole collection:
		* Method: GET
		* Url: You specify element's id e.g. http://127.0.0.1:8000/count/
		* Click Send to count elements in collection
	* Count elements in collection with specified name:
		* Method: GET
		* Url: You specify element's name e.g. http://127.0.0.1:8000/count/?name=dog (in this example we are looking for elements with name: dog)
		* Click Send to count elements in collection	
	* Getting all unique words from collection:
		* Method: GET
		* Url: http://127.0.0.1:8000/unique/
		* Click Send list all unique elements	
