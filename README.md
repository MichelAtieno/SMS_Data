## Project SMS-Data
### By Michel Atieno, created on 27th January 2022.

####  Project Link
You can view project on https://sms-data.herokuapp.com/

### Description
 As a user of the application, you are able to:
<ul>
    <li>Sign in to the application. Register an account with a phone number, username and password. Login to view the dashboard.</li>
    <li>You can view transactions of every user in the database.</li>
    <li>You can view the API; given the routes in the description</li>
<ul>

### Website Routes
    - /profile/<int:id> - User profile showing transactions related to particular user
    - /cat/<int:id> - Category profile showing transactions related to particular category
    - /date/<enddate>&<firstdate>&<transactions> - Once you submit the form on home page for querying transactions for particular period of time, you will be redirected to this page that displays transactions per selected period of time.
    - /category/<startingdate>&<endingdate>&<int:id> - Once you submit the form on home page for querying categories for  a particular period of time, you will be redirected to this page that displays transactions per category per selected period of time.


### API routes
    - /transactions - view all transactions
    - /transactions/<int:id> - view transaction with assigned id
    - /categories - view all categories
    - /category/<int:id> - view category with assigned id
    - /users - view all users
    - /user/<int:id> - view user with assigned id

## Set-up and Installation
###     Prerequisites
        - Python 3.7.1
        - Ubuntu software           

###  Known bugs
Work in progress.....


### Technologies used
    - Python 3.7.12 (Flask Framework)
    - Bootstrap
    - Heroku
    - Postgresql


## Support and contact details
Contact me on michelatieno23@gmail.com for any comments, reviews or feedback.

### MIT License
Copyright (c) **Michel Atieno**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
