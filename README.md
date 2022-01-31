## Project SMS-Data
### By Michel Atieno, created on 27th January 2022.

####  Project Link
You can view project on https://sms-data.herokuapp.com/

### Description
 As a user of the application, you are able to:
<ul>
    <li>Sign in to the application. Register an account with a phone number, username and password. Login to view the dashboard.</li>
    <li>You can view transactions of every user in the database.</li>
    <li>You can also view the API; given the routes in the description</li>
<ul>

### Behaviors

<ol>
    <li>The project has a registration page, whereby a user can create an account. After registering an account, the user can log in to the dashboard and will have access to dashboard. </li>
    <li>The User can view transactions and different categories, with information categorized on home page.</li>
    <li>Dfferent routes for API include:
        - /transactions - view all transactions
        - /transactions/<int:id> - view transaction with assigned id
        - /categories - view all categories
        - /cat/<int:id> - view category with assigned id
        - /users - view all users
        - /user/<int:id> - view user with assigned id
    </li>
    <li>With a user account, one can access different pages by clicking on links.</li>
</ol>




## Set-up and Installation
###     Prerequisites
        - Python 3.7.1
        - Ubuntu software           

## Known bugs
Working on different api routes.
Work in progress.....


## Technologies used
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
