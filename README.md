# [**Fuddy Duck Food Delivery System**](https://https://faddyduck-delivery.herokuapp.com/)

![Portfolio image](https://res.cloudinary.com/dqj8itdfg/image/upload/v1656884641/%E6%88%AA%E5%B1%8F2022-07-03_22.43.41_g6dkie.jpg)

## **Overview**

This website is built as my fourth portfolio for my coding course. It’s only for educational purposes not suitable to use for any commercial activities. The name of the website called Faddy Duck. It is a website for Peking(Beijing) style deli. This website is designed for an imagined small restaurant. It’s aimed to offer an opportunity to engage with their customers through the website and finally improve the possibility to influence a customer to purchase food via the website.

## **Table of Contents**

- [**Fuddy Duck Food Delivery System**](#overview)
  - [**Overview**](#overview)
  - [**Table of Contents**](#table-of-contents)
    - [**1. Draft**](#1-Draft)
    - [**2. Demand Analysis**](#2-demand-analysis)
    - [**3. Testing and Launch**](#3-testing-and-launch)
    - [**4. Deployment**](#4-deployment)
    - [**5. Support**](#5-support)
    - [**6. Reference and Research**](#6-reference-and-research)

### **1. Draft**

- Initiate Planning

![Planning](https://res.cloudinary.com/dqj8itdfg/image/upload/v1656885356/%E6%88%AA%E5%B1%8F2022-07-03_22.55.39_jxcp7t.jpg)

    - Build a simple food delivery website that allows the owner exposes their business to any potential customers.
    - Proving business information such as address, contact and opening hours.
    - Categorize menus, provide item images, display price and descriptions.
    - This website also contain essential functions such as Add to Cart, Pay online and Receive Order Confirmation via email.

- Target Audience

    - Small business.

[Back to the top](#overview)

### **2. Demand Analysis**

- Customer

  - **Login Page** 
  
  ![login page](https://res.cloudinary.com/dqj8itdfg/image/upload/v1656887220/%E6%88%AA%E5%B1%8F2022-07-03_23.26.35_rx1uiy.jpg)

    - On the header, user would go back to the home page simply by clicking the logo or the name of the business. It also allows user to view the menu, login to the site and register if they like to place an order.
    - The login page allows user login to the site, once the user login then they will be able to add products to cart and view order history.
    - The login page also contain the function of input validation, it checks if information entered by the user is valid.
    - It provides a link to registration page if a user has not been registered.
    
  - **Registration page** 
  
  ![Registration page](https://res.cloudinary.com/dqj8itdfg/image/upload/v1656889126/%E6%88%AA%E5%B1%8F2022-07-03_23.57.43_lpzbjj.jpg)

    - Registration page collects user's name, email and allow them to set up password for their personal account.
    - It provides a link to login page if a user has already registered.

  - **Sign out page** 
  
  ![Sign out page](https://res.cloudinary.com/dqj8itdfg/image/upload/v1656889457/%E6%88%AA%E5%B1%8F2022-07-04_00.04.07_miyx3i.jpg)

    - This is a confirmation page to the user confirming if they are happy to sign up. Otherwise, they can go back to the home page by clicking BACK button.

  - **Signed in page** 
  
  ![Signed in page](https://res.cloudinary.com/dqj8itdfg/image/upload/v1656890501/%E6%88%AA%E5%B1%8F2022-07-04_00.21.18_l42ai6.jpg)

    - A cart and greeting on the top right only appear when a user is successfully signed in. The user will be able to access personal profile and cart from this page.

- Business
  - **Home page** 
  
  ![home page](https://res.cloudinary.com/dqj8itdfg/image/upload/v1656890501/%E6%88%AA%E5%B1%8F2022-07-04_00.21.18_l42ai6.jpg)

    - The first section is Navbar with logo displayed, it’s simple and easy for users to navigate the site.
    - The second section would allow the business to display 3 posters and it would slide every 5 sec. On the right hand side of it would allow the business to enter any message they like to publish.
    - The third section allow the business to link to social medias such as Facebook, Twitter, Google, Instagram, Linkedin and Github.
    - The last section would be the footer of the site. It allows the business to pass important notification and display business information.


  - **Product page**
  
  ![Product page](https://res.cloudinary.com/dqj8itdfg/image/upload/v1656892276/%E6%88%AA%E5%B1%8F2022-07-04_00.51.02_ylzg0a.jpg)

    - Products are grouped in 3 categories. There are Meals, Dessert and Drinks in this case.
    - Product name and price is displayed under product images. Product description is hidden by default unless the user expend to read. All description would be expended by one click.
    - Categories can be access by clicking tabs on the top.
    - Then user is able to add to cart.

  - **Cart page**
  
  ![cart page](https://res.cloudinary.com/dqj8itdfg/image/upload/v1656980491/%E6%88%AA%E5%B1%8F2022-07-05_01.21.13_vuzqfs.jpg)

    - The cart page contain product information and linked to Paypal for online payment. The user also will provide delivery information via this page.
    - Item will be removed if quantity is zero.
    - Total item and total amount is calculated before payment.
    - The user may choose to pay by Paypal or credit card.
    - Once payment is collected, confirmation message will display.
    - Order data will be sent to the back end once the user clicked place order button.

  - **Profile page**
  
  ![profile page](https://res.cloudinary.com/dqj8itdfg/image/upload/v1656981189/%E6%88%AA%E5%B1%8F2022-07-05_01.32.57_hpnv47.jpg)

    - On the profile page, the user is able to find data of total orders, order delivered and pending orders.
    - Table below will display order data, delivery address, contact number and order status.
    - The user may login to this page by clicking their name on the top right.



- Technology Stack
  - [Font Awesome](https://fontawesome.com/)
  - [Google Fonts](https://fonts.google.com/)
  - [Heroku](https://heroku.com)
  - [Cloudinary](https://cloudinary.com/)
  - [Mdbootstrap](https://mdbootstrap.com/)

[Back to the top](#overview)

### 3. **Testing and Launch**

 - Bug1: 
 
 ![Bug 1:](https://res.cloudinary.com/dqj8itdfg/image/upload/v1656981805/%E5%9B%BE%E7%89%87_1_sgzxbk.jpg)
 
 Unable to load relevant data when given a different name in admin page, Category section. Fixed by setting context in the view.py as screenshot shown and in template/menu.html, loop as {% for meal in meals %}, data display with no issue when user set a category as meals. 
 
 - Bug2: 
 
 ![Bug 2: ](https://res.cloudinary.com/dqj8itdfg/image/upload/v1656982062/%E5%9B%BE%E7%89%87_1_hkqp7v.png)[Statement: GET /place_order/ HTTP/1.1" 405 0 ]
 
 The 405 Method Not Allowed error shouldn’t be confused with the 404 Not Found error. A 404 tells you that the requested URL couldn’t be found or that it was entered incorrectly. A 405 error message, on the other hand, confirms that the requested page does exist (and the URL was input correctly), but an unacceptable HTTP method was used to make the initial request. [Reference](https://kinsta.com/blog/405-method-not-allowed-error/). Fixed by ![debug](https://res.cloudinary.com/dqj8itdfg/image/upload/v1656982067/2_jwbgav.png)

 - Bug3: 
 
 ![Bug3:](https://res.cloudinary.com/dqj8itdfg/image/upload/v1656982457/%E5%9B%BE%E7%89%87_1_guxeu9.jpg) 
 
 [Statement: RelatedObjectDoesNotExist User has no customer.] Fixed via as per [Video](https://www.youtube.com/watch?v=Kc1Q_ayAeQk)

 - Bug 4 
 
 ![Bug 4:](https://res.cloudinary.com/dqj8itdfg/image/upload/v1656982457/%E5%9B%BE%E7%89%87_1_guxeu9.jpg) 
 
 [Statement: Errno 111 Connection refused ] fixed by added (EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend') in setting.py. [Reference](https://groups.google.com/g/django-oscar/c/kLfvDyDL47w)

 - Bug 5 
 
 ![Pending debug](https://res.cloudinary.com/dqj8itdfg/image/upload/v1656982781/%E5%9B%BE%E7%89%87_1_tnz8s5.jpg) 
 
 [Statement: __str__ returned non-string (type NoneType)] pending to fix.

 - Some other bugs: CSS file and Js seems unreliable after reverse DEBUG = False in setting.py. The website is either lost style or no responding to JS.
 
 - Payment testing was done by using Paypal sandbox.

- The project is considered as completed for phase 1. Is a simple website allowing essential business activities. 



[Back to the top](#overview)

### 4. **Deployment**

- This website is built in Github and deploy to Heroku. The steps to deploy are as follows:
  - Using the git add . command to add change in the working directory to the staging area. It tells Git what to include and updates to a particular file in the next commit.
  - Using the git commit -m "commit message", A shortcut command that immediately creates a commit with a passed commit message. [Material](https://www.atlassian.com/git/tutorials/saving-changes/git-commit)
  - Using the git push command to upload local repository content to a remote repository.
  - Once the main branch has been selected, the page provided the link to the completed website.

The live link can be found here [link](https://faddyduck-delivery.herokuapp.com/)


[Back to the top](#overview)

### 5. **Support**

- Mentor

  - [Simen Daehlin](https://www.linkedin.com/in/simendaehlin/)
  A lead Full Stack Developer & Mentor

[Back to the top](#overview)

### 6. **Reference and Research**

- Reference

  - [Welcome to django-allauth](https://django-allauth.readthedocs.io/en/latest/)
  - [Model instance reference](https://docs.djangoproject.com/zh-hans/4.0/ref/models/instances/#str)
  - [Django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/install.html)
  - [Django Forms with Django Crispy Forms](https://dontrepeatyourself.org/post/django-forms-django-crispy-forms/)
  - [BugBytes](https://www.youtube.com/channel/UCTwxaBjziKfy6y_uWu30orA)
  - [Dennis Ivy](https://www.youtube.com/c/DennisIvy)
  - [Legion Script](https://www.youtube.com/c/LegionScript)
  - [Sweetalert](https://sweetalert.js.org/guides/)

[Back to the top](#overview)