# seedValue

A simple server application using Flask, which stores and retrieves a seed value and handle the following two HTTP REST requests:

HTTP POST: "/" with JSON body {"num": 100} where 100 can be any integer. This should update the seed value with the number.

HTTP GET: "/" -> Returns the integer seed value in string format. The response body for the above case will be: 100