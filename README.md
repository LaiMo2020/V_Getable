# V-Getable

The purpose of the project “V-getable” is to build a full-stack site based around business logic used to control a centrally-owned dataset.

The site includes an online store connecting a group of farms and gardeners selling local products, such as vegetables, fruit, eggs, milk and bread with clients interested in supporting local business. Clients can browse through products, make a selection, shop and pay their order. As a client with a profile, the page offers an option to get free delivery and discounts. Admin-options allow the shop-owner to add and edit products and keep track on the clients orders as well as interact with and inform clients on a blog.

## UX

The online-shop “V-getable” offers a great option for everyone that cares about healthy, ecological and locally produced products in his nutrition.

A variety of products, nicely presented, attracts visitors on the page to make their choice on how much and what they like and save products in their shopping basket. Sending the order and paying directly bye credit card makes it easy to receive fresh products all the way to home while preventing singular car-trips to the countryside.

The shop owner profits from various and easy-to-handle options when it comes to setting up new products, prices and keep track on incoming orders and requests. The blog, included, in the page, allows the company to post news and background information about their way of farming and production of their products. This raises trust for clients interested where their food comes from and how it is produced. Clients even have the option to comment and interact thereby with the farmers.

### User stories




### Wireframe 
For the creation of my wireframes I used the Balsamiqu program (see “technologies used"). Throughout the development of the webpage the wireframes were very helpful for me to reach the final design.

I have created mobile, desktop and tablet wireframes.

1- Desktop Wireframes
2- Mobile Wireframes
3- Tablet Wireframes



## Sections and features 

### Home-page
   - Navbar <br>
   The navbar appears in all sections and helps the user to navigate through them with links to the "Home-page" (represented bye the logo) "Products", "Blog" and "Profile"
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
Overview of all products in the shop, represented bye pictures, name, price and unit. Bye klicking on a product the user reaches "Product information"

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
The payment is secured bye "stripe.com".

### Blog<br>
Shows history of all posts, though only the four latest per page (pagenation).
- Post <br>
A user can read posts, added bye the admin. Klicking "read more" the user reaches the full text of a specific post and the option to comment.

- Comments <br>
The total number of comments on a post is counted and visible for the user.
Users can interactively leave comments through a form and read previous comments. Comments need to be approved bye the admin before getting visible to public. 


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
