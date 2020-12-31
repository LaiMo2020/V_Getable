# Milestone Project 4: V-Getable

![Presentaion photo ](README-images/responsive.png)

The purpose of the project “V-getable” is to build a full-stack site based around business logic used to control a centrally-owned dataset.

The site includes an online store connecting a group of farms and gardeners selling local products, such as vegetables, fruit, eggs, milk and bread with clients interested in supporting local business. Clients can browse through products, make a selection, shop and pay their order. As a client with a profile, the page offers an option to get free delivery and discounts. Admin-options allow the shop-owner to add and edit products and keep track on the clients orders as well as interact with and inform clients on a blog.

## UX

The online-shop “V-getable” offers a great option for everyone that cares about healthy, ecological and locally produced products in his nutrition.

A variety of products, nicely presented, attracts visitors on the page to make their choice on how much and what they like and save products in their shopping basket. Sending the order and paying directly by credit card makes it easy to receive fresh products all the way to home while preventing singular car-trips to the countryside.

The shop owner profits from various and easy-to-handle options when it comes to setting up new products, prices and keep track on incoming orders and requests. The blog, included, in the page, allows the company to post news and background information about their way of farming and production of their products. This raises trust for clients interested where their food comes from and how it is produced. Clients even have the option to comment and interact thereby with the farmers.

### User stories

![User story 1](README-images/user-stories-1.png)
![User story 3](README-images/user-stories-2.png)
![User story 3](README-images/user-stories-3.png)


###  Wireframe 
For the creation of my wireframes I used the Balsamiqu program (see “technologies used"). Throughout the development of the webpage the wireframes were very helpful for me to reach the final design.

I have created mobile, tablet, desktop and tablet wireframes.

1- Desktop Wireframes
  - ![Homepage](README-images/wireframe/V-getable-browser.png)
  - ![Prodcuts](README-images/wireframe/Products-browser.png)
  - ![Blog](README-images/wireframe/blog-browser.png)
  - ![Checkout](README-images/wireframe/checkout-browser.png)
  - ![Comments](README-images/wireframe/comments-browser.png)
  - ![Shooping bag](README-images/wireframe/shopping-cart-browser.png)
  - ![Sign in](README-images/wireframe/signin-browser.png)
  - ![Sign up](README-images/wireframe/signup-browser.png)

2- Mobile Wireframes
  - ![Home page](README-images/wireframe/V-getable.png)
  - ![Products](README-images/wireframe/Products.png)
  - ![Blog](README-images/wireframe/blog.png)
  - ![Checkout](README-images/wireframe/checkout.png)
  - ![Comments](README-images/wireframe/comments.png)
  - ![Shopping bag](README-images/wireframe/Shoping-cart.png)
  - ![Sign in](README-images/wireframe/signin.png)
  - ![sign up](README-images/wireframe/signup.png)

3- Tablet Wireframes
  - ![Home page](README-images/wireframe/V-getable-iPad.png)
  - ![Products](README-images/wireframe/Products-Ipad.png)
  - ![Blog](README-images/wireframe/blog-pad.png)
  - ![Checkout](README-images/wireframe/checkout-ipad.png)
  - ![Comments](README-images/wireframe/comments-Ipad.png)
  - ![Shopping bag](README-images/wireframe/Shoping-cart-ipad.png)
  - ![Sign in](README-images/wireframe/signin-Ipad.png)
  - ![Sign out ](README-images/wireframe/signup-Ipad.png)



## Sections and features 

### Home-page
   - Navbar <br>
   The navbar appears in all sections and helps the user to navigate through them with links to the "Home-page" (represented by the logo) "Products", "Blog" and "Profile"
   In mobile devices and tablet the navbar transforms to a drop-down menu. The shopping bag item remains visible.
     - Search function <br>
        To find specific products in the shop
     - Shopping basket <br>
        Gives an overview of the total amount and content in the users shopping bag

   
    - Background information<br>
    A short text providing background information on the company.
        - Go to our shop<br>
        Allows the user to reach the product page
        - Go to our blog<br>
        Allows the user to reach the blog

### Products

- Product overview<br>
Overview of all products in the shop, represented by pictures, name, price and unit. By klicking on a product the user reaches "Product information"

- Product information<br>
A detailed description of the product. The user is abled to chose the quantity he/she wnats to add to the shopping bag. By klicking "add to bag" the product is added to the shopping bag. A toast appears. By klicking "keep shopping" the user can return to the product overview.

### Shopping bag

- Overview <br>
Shows information on all products in the shopping bag, subtotal, bag total and grand total. If the user reaches the required amount for free deilvery fee is automatically reduced. 
By klicking "keep shopping" the user returns to product overview. "Secure checkout" leads to "Check out".

- Check out <br>
The user is demanded to fill in a form with delivery details as well as credit card information. Pre-filled information can be used. A order summary enables the user to see the order. 
By klicking "Adjust bag" the user returns to his shopping bag. A red message with the grand total appears, reminding that the user will be charged by clicking "Complete order". After completing the order a toast appears.

- Payment <br>
The payment is secured by "stripe.com".

### Blog<br>
Shows history of all posts, though only the four latest per page (pagenation).
- Post <br>
A user can read posts, added by the admin. Klicking "read more" the user reaches the full text of a specific post and the option to comment.

- Comments <br>
The total number of comments on a post is counted and visible for the user.
Users can interactively leave comments through a form and read previous comments. Comments need to be approved by the admin before getting visible to public. 


### User profile

- Register<br>
The user is asked to fill in a form, providing E-mail, Username and password. If the user is already signed up, a linke enables him/her to reach the log in page.
Different toasts and an obligatory e-mail confirmation ensure a secure registration.

- Sign in <br>
The user can sign in with username or e-mail and password. He/She can svae the information for easy log-in. 

- Account <br>
The user can fill in his/her default delivery information and see the order history. Klicking on an order shows up detailed order information. 

### Admin profile

- Product management <br>
Enables the admin to add, edit and delete products. In the product overview the logged-in admin has an option to edit or delete existing products.

### Admin panel

- Accounts<br>
The admin can change the admin e-mail. In an overview the admin can read, and delete all registered e-mail.
- Blog <br>
The admin can read, create, edit and delete posts. When creating a post there is an option to save as a draft or publish.
Under "Comments" the admin can approve or delete selected comments.
- Checkout/Orders <br>
The admin can see an overview, edit and delete orders.
- Products <br>
The admin can add or delete categories to structure the products.
There are three categories that the admin can edit and delete.
Under "Products" the admin can see an overview, edit, create and delete products and attach photos to the product information.

### Features Left to Implement
- Possibility for users to subscribe for a weekly delivery of vegetables that get delivered to a centralized pick-up station

### Database relations

![DB relations](README-images/V-DB-Relation.png)


# Technologies Used


### 1. [HTML](https://html.com/)

For the basic structure of the project

### 2. [CSS](http://css.com/)

For the styling and design of the webpage

### 3. [JavaScript](https://www.javascript.com/) 

 Add dynamic and interactive elements to websites 

### 4.  [Bootstrap](https://getbootstrap.com/)

Quick and responsive form and method to implement.

### 5. [GitHub](https://github.com/)

Platform to publish the webpage and interact with clients and the coder community

### 6. [Gitpod](https://www.gitpod.io/)

A coding editor with an adapted and easy coding environment

### 7. [GIT](https://git-scm.com/)

For version control. This project where duplicated as gitpod was down for few days and the first project never worked after the gitpod have fixed the issues 

### 8. [Django](https://www.djangoproject.com/)

A web framework  for Python
### 9. [Font Awesome](https://fontawesome.com/6?next=%2F)

As a resource of icons to style my page
### 10. [Alluath](https://django-allauth.readthedocs.io/en/latest/installation.html)
a pckage in fjango to Secure registration 

### 11. [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools)

For live editing options while coding the page
### 12. [Balsamiq](https://balsamiq.com/)

To create wireframes
### 13. [Heroku](https://dashboard.heroku.com/apps)
Storing my app.
### 14. [Pyhton](https://www.python.org/)
Backend programmering language.
### 15. [AWS](https://aws.amazon.com/free/?all-free-tier.sort-by=item.additionalFields.SortRank&all-free-tier.sort-order=asc&awsf.Free%20Tier%20Types=*all&awsf.Free%20Tier%20Categories=categories%23compute&trk=ps_a134p000004f2onAAA&trkCampaign=acq_paid_search_brand&sc_channel=PS&sc_campaign=acquisition_EMEA&sc_publisher=Google&sc_category=Cloud%20Computing&sc_country=EMEA&sc_geo=EMEA&sc_outcome=acq&sc_detail=aws%20server&sc_content=Cloud%20Server_e&sc_matchtype=e&sc_segment=467752182153&sc_medium=ACQ-P|PS-GO|Brand|Desktop|SU|Cloud%20Computing|Solution|EMEA|EN|Text|xx|EU&s_kwcid=AL!4422!3!467752182153!e!!g!!aws%20server&ef_id=EAIaIQobChMIwqz_8Zfg7QIVAWYYCh3cBA1OEAAYASAAEgIu3fD_BwE:G:s&s_kwcid=AL!4422!3!467752182153!e!!g!!aws%20server)
To store my css files & media as images.
### 16 [Stripe](https://stripe.com/en-se?utm_campaign=paid_brand-SE_en_Search_Brand_Stripe-1436985502&utm_medium=cpc&utm_source=google&ad_content=275927467139&utm_term=stripe&utm_matchtype=e&utm_adposition=&utm_device=c&gclid=CjwKCAiA57D_BRAZEiwAZcfCxZ9ZTxZfWH88HEC3FTFdbrq5fAXY0RntFn8qP9u3jWiyBYI8aq7e0RoCsNEQAvD_BwE)
To secure online payment
### 13. [Goggle-Font](https://fonts.google.com/)
Text font 

## Testing 

### Testing and review of the webpage

1. I have tested the webpage myself in the following browsers and devices:
- Google Chrome + ggogle dev tool 
- Safari
- Iphone XR
- MacBook Air

2. I have sent the webpage to family and friends who tested the page and responsiveness on following browser and devices:
- Iphone 12
- iPad
- iPhone SE

### Validation of the code: I have used the follwoing tech to test my code:
- [W3C/HTML](https://validator.w3.org/)
to check my  HTML code.
- [W3C/CSS](https://jigsaw.w3.org/css-validator/)
to check my CSS code.
- [Jshint](https://jshint.com/)
to check my JS code.
- [PEP8](http://pep8online.com/)
to check my python code

### Autonomous Testing:

-  MostPython apps were tested autonomously

### Manual Testing:

- Navbar <br>
Test: Navigate to all pages through the navbar <BR>
Result: No error

- Homepage hero image<br>
Test: Check overlay text on readability and contrast <br>
Result: Bad readability and contras<br>
Fix: Change image and font color

- Shopping bag <br>
Test: Responsiveness on small devices<br>
Result: Not responsive <br>
Fix: Deleting the image in shopping bag, as it is unnessecary and appears again in check out 

- Footer <br>
Test: Responsiveness on all devices <br>
Result: Footer covers bottom of pages <br>
Fix: Add margin 

- Setting <br>
Test: Adding env.py <br>
Result: Deployment unseccsesfull as env is a hidden file<br>
Fix: Add if-statement "if os.path.exists('env.py'):"

- Blog <br>
Test: Opening blog page <br>
Result: Does not work <br>
Reason: Deleted require field and migrated afterwards <br>
Fix: Delete all data and remigrate again <br>

## Deployment

#### The project is stored in a Github [repository](https://v-gtable.herokuapp.com/).

#### I have made the follwoing steps to deploye my app: 

### Github/Gitpod:

1- Create a repo in GitHub using the code institute template

2- Click on the green button to open my project in gitpod

3- Install Django:  pip3 install django

4- Create the project : django-admin startproject V_getable

5- Create .gitignore file and add the files we w’ont to push

6- run the initial migrations by typing python3 manage.py migrate.

7- Create a superuser to have accuses to the app as admin by creating:

8- email&username&password

9- initial commit to github.

10- set environment variables, adding them to your Gitpod settings or to env-py and add the secret key there: 
import os
os.environ['SECRET_KEY']

11- creating the requiremtns.txt by typing :pip3 install -r requirements.txt, in the terminal. to identify the languages and packages.
I have added STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY to my gitpod setting to facilitate my checkout testing 

12- to allow hosting in both locally and heroku I have to add: ALLOWED_HOSTS = ['v-gtable.herokuapp.com', 'localhost']

python3 manage.py runserver is what we use to see our live site locally 

### Heruko:

1- creating a new app in my heroku page and called it V-Gtable.

2- to use Heroku Postgress database I have to typ the follwoing command in my gitpod terminal: 
- pip3 install dj_database_url
- pip3 install psycopg2-binary
- pip3 install gunicorn
in my seeting.py added the follwoing after importing : 
if 'DATABASE_URL' in os.environ:
    DATABASES = {
        'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
    }
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        }
    }
    I have to import dj_database_url in my setting.py 

3- freeze the requiremnt again as explained in Github deplyoment section.
so the new packages are defined. 

4- Migrate my database. always checking with the command makemigrations --dry-run to
If all is good we type python3 manage.py make migrations then python3 manage.py migrate 

5- connecting my github repo in the setting of my project in heroku

6- commit and push all:
- git add .
- git commit -m "your comment"
- git push 

see below for all config var in heroku setting:

![Config var](README-images/config-heroku.png)

### Amazon Web Services AWS
1- Creating an acount at https://aws.amazon.com/

2- Create a bucket, follow the documentation of how to set your zone, permission ... 

3- Create group and its policy 

4- create auser for this group

5- Install django-storage/boto3,  connecting my bucket to my repo by adding storage to my apps in setting.py.
adding the following to my setting.py :

    AWS_STORAGE_BUCKET_NAME = 'v-getable'
    AWS_S3_REGION_NAME = 'eu-north-1'
    AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
    AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'

6- Connecting my bucket to s3 in AWS, to store my css files and media
I had to add those settting to setting.py as well :

   STATICFILES_STORAGE = 'custom_storages.StaticStorage'
    STATICFILES_LOCATION = 'static'
    DEFAULT_FILE_STORAGE = 'custom_storages.MediaStorage'
    MEDIAFILES_LOCATION = 'media'

    # Override static and media URLs in production
    STATIC_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{STATICFILES_LOCATION}/'
    MEDIA_URL = f'https://{AWS_S3_CUSTOM_DOMAIN}/{MEDIAFILES_LOCATION}/'.


## Credits
- "Boutique Ado" project in the module
- https://djangocentral.com/building-a-blog-application-with-django/ <br>https://djangocentral.com/creating-comments-system-with-django/ <br>https://djangocentral.com/adding-pagination-with-django/<br>
to create my blog and comments models
- Bootstrap templates

### Media
The static images used across the page were obtained from https://unsplash.com/


### Acknowledgements
A very big thank you goes to my <br>
1- Code Institute Mentor Brian M. for his invaluable support and guidance throughout this project. <br>
2- Slack <br>
3- Tutor support team<br>
4- Boutique Ado lessons in the module.
### Disclaimer
The content of this website is for educational purposes only.










