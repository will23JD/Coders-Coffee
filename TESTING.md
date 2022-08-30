[Back to readme](/README.md)

***
## Table of contents
1. [User Story Testing](#user-story-testing)
2. [Manual Testing](#manual-testing)
3. [Automated Testing](#automated-testing) 
     - [Code Validation](#code-validator-testing)
4. [User Testing](#user-testing)

***

## User Story Testing

### Site User
- As a customer I can add or remove items from my basket so that I don't have items I don't want.
    - When in the bag app there is a remove button next to each item allowing the user to remove it from the bag.
- As a customer I can choose from different sizes so that I have the best size to suit my needs.
    - If a product has sizes there will be a drop down box allowing the user to select a size.
- As a customer I can filter products (eg: by rating) so that I can find the most popular products quickly.
    - When on the products page user as able to filter by a list of option such as rating.
- As a customer I can search for a product by name so that I can quickly find a product.
    - At any page on website a users can easily sreach for a product by clicking the search button.
- As a customer I can adjust the products in my bag so that I can quickly change an item if I add the quantity.
    - When in the bag app like the remove button there is a drop down allowing a user to select a new quantity and update the bag.
- As a customer I will receive a confirmation email so that I know my order has gone through.
    - When a order is place a user will revecie an email with their order information.
- As a customer I can sort by a category so that I can only see products I'm interested in.
    - In the navbar there are two main drop downs with all the catogries listed allowing a user to only look in one catagory.
- As a site user I can receive notifications so that I know what's happen after I do something(eg: add an item to the bag).
    - The website includes full CRUD functionality notifying the user of any action they take.

### Registered User
- As a customer I can leave a rating on a product so that I can help other customers with their product choices.
    - After you have purchased a product and are login you can view your order and click on add a review on any product to add a review.
- As a customer I can create an account so that my details can be saved so that I can have an easier time checking out next time.
    - When login during the checkout you can click to save your details to your account.
- As an account holder I can reset my password so that if I forget it I can get back into my account.
- As a customer I can receive a confirmation email so that I know my account registered.
    - When creating an account a confirmation email will be sent asking to verify the email.

### Site Owner
- As a site owner I can update products so that they are up to date for customers.
    - When viewing any product or product detail a superuser will have the option to edit it.
- As a site owner I can delete old product so that customers cannot buy them when they aren't available.
    - The same as with editing a product a superuser will be able to delete any product.
- As a site owner I can create blog posts so that users can keep up to date with what the business is doing.
    - When login in as a superuser there is a add blog link in the allowing them to create a new blog post.
- As a site owner I can edit blog posts so that the information can be up to date.
    - When viewing any blog or blog detail a superuser will have the option to edit it.
- As a site owner I can delete a blog post so that **only relevant post will be there **
    - When viewing any blog or blog detail a superuser will have the option to delete it.


## Manual Testing
<details>
<summary>General Testing</summary>

### Navigation
- Tested that the website Logo links back to the home page **PASS**
- Tested the all products drop down list links to the all product page with filters if selected **PASS**
- Tested the coffee drop down list links to the coffee catagories with filters if selected **PASS**
- Tested the gifts drop down list links to the gifts catagories with filters if selected **PASS**
- Tested that when the sreach button is clicked it will drop down and allow user to search the site **PASS**
- Tested that the account drop down has links to register and login in for users not logged in and links to 
profile, wishlist and logout if a user is logged in and all links work **PASS**
- Tested that the bag icon links the user to the bag page **PASS**

#### Superuser
- Tested that when the account button is clicked add product link is there and links to the add product page **PASS**
- Tested that when the account button is clicked add blog link is there and links to the add blog page **PASS**

### Footer
-Tested that socail links all work and open in a different pages **PASS**

</details>
<details>
<summary>Home</summary>

- Tested the shop now button takes the user to the all products page **PASS**
- Tested the facebook link in the about us section takes to user to the facebook page **PASS**
- Tested the blog link takes the user to the blog page **PASS**

</details>
<details>
<summary>Products</summary>

### All Products
- Tested that the link tree link back to each page **PASS**
- Tested that the filter function works and filters product base on the selection **PASS**
- Tested that when a product is clicked on it takes the user to the products detail page **PASS**

### Product Detail
- Tested that the link tree link back to each page **PASS**
- Tested that product has a quantity selector and a quantity from 1-10 can be selected **PASS**
- Tested that if a product has sizes the price is updated accordingly **PASS**
- Tested that the add to bag button works and send all the information such as sizes and quantity **PASS**
- Tested that login users can add a product to there wishlist **PASS**

#### Superuser
- Tested that each product has a edit link which takes the superuser to the edit product page **PASS**
- Tested that each product has a delete link which creates a popup asking the user to confirm they what to delete the product **PASS**
- Tested that when the popup is confirmed the product is deleted **PASS**

</details>
<details>
<summary>Bag</summary>

- Tested that the bag summery is displayed **PASS**
- Tested that the remove from bag button works **PASS**
- Tested that the update quantity selector and button works **PASS**
- Tested that when any changes are made to the bag the price total is adjusted **PASS**
- Tested that the checkout button takes the user to the checkout page **PASS**

</details>
<details>
<summary>Checkout</summary>

### Checkout page

- Tested that the bag total and summary is shown **PASS**
- Tested that all the required fields are correct to checkout **PASS**
- Tested that the checkout button takes the user to the checkout success page if the form is correct **PASS**

#### Signed in users

- Tested that if they have information saved it will pre-populate the fields **PASS**
- Tested that the save infor button will save the users information to the profile **PASS**

### Checkout Success

- Tested that the user receives an order summery **PASS**
- Tested that the user can view more information like delivery address **PASS**
- Tested that the products link takes the user back to the all products view **PASS**

</details>
<details>
<summary>Profile</summary>

### Profile

- Tested the user can see a list of their orders **PASS**
- Tested the user can see their saved information **PASS**
- Tested that when a user clicks on an order it takes them to the order history page **PASS**
- Tested that a user can update their saved information **PASS**

### Order History

- Tested that the user can see all the information on the order **PASS**
- Tested that the user can add a review and be taken to the product review page **PASS**
- Tested that the back to profile button links back to the profile **PASS**

### Wishlist

- Tested that any product added to the wishlist is shown **PASS**
- Tested that the add to bag button adds the product to the bag **PASS**
- Tested that the remove button removes the product from the wishlist **PASS** 

</details>
<summary>Blog</summary>

### All Blogs

- Tested that the link tree link back to each page **PASS**
- Tested that when a blog is clicked on it takes the user to the blogs detail page **PASS**

### Blog Detail

- Tested that the blog information is all there **PASS**
- Tested that a login user can like and unlike a post **PASS**
- Tested that a login user can create a comment on a post **PASS**
- Tested that a user can edit their own comments **PASS**
- Tested that a user can delete their own comments **PASS**

#### Superuser

- Tested that each blog has a edit link which takes the superuser to the edit blog page **PASS**
- Tested that each blog has a delete link which creates a popup asking the user to confirm they what to delete the blog **PASS**
- Tested that when the popup is confirmed the blog is deleted **PASS**

</details>

## Automated Testing

### Lighthouse

![Lighthouse results](lighthouse.png)
- Best Practices is low due the mailchimp script for the popup which I cannot change.

### Code Validator Testing
- HTML validation was done by [W3C HTML](https://validator.w3.org/).
- CSS validation was done by [W3C CSS](https://jigsaw.w3.org/css-validator/).
- python validation was done by [PEP8 online](http://pep8online.com/).
- javascript validation was done by [jshint](https://jshint.com/).
<details>
<summary>HTML validation</summary>

- Home page

![Home page validation](RM-media/homehtmlval.png)

- All Products page

![All Products page validation](RM-media/productshtmlval.png)

- Product Detail page

![Product Detail page validation](RM-media/productdetailhtmlval.png)

- Product Edit page 

![Product Edit page validation](RM-media/productedithtmlval.png)

- Product Add page

![Product Add page validation](RM-media/productaddhtmlval.png)

- Product Review page

![Product Review page validation](RM-media/productreviewhtmlval.png)

- Bag page

![Bag page validation](RM-media/baghtmlval.png)

- Checkout page

![Checkout page validation](RM-media/checkouthtmlval.png)

- Checkout Success page

![Checkout page validation](RM-media/checkoutsuccesshtmlval.png)

- Profile page

![Profile page validation](RM-media/profilehtmlval.png)

- Blog page

![Blog page validation](RM-media/bloghtmlval.png)

- Blog Detail page

![Blog Detail page validation](RM-media/blogdetailhtmlval.png)

- Blog Edit page 

![Blog Edit page validation](RM-media/blogedithtmlval.png)

- Blog Add page

![Blog Add page validation](RM-media/blogaddhtmlval.png)

</details>
<details>
<summary>CSS validation</summary>

- Base CSS

![Base CSS validation](RM-media/basecssval.png)

- Checkout CSS

![Checkout CSS validation](RM-media/checkoutcssval.png)

</details>
<details>
<summary>Python validation</summary>

- Product Model Python

![Product Model python validation](RM-media/productmodelpyval.png)

- Product View Python

![Product View python validation](RM-media/productviewpyval.png)

- Bag View Python

![Product View python validation](RM-media/bagviewspyval.png)


- Bag Context Python

![Bag Context python validation](RM-media/bagcontextpyval.png)

- Checkout Model Python

![Checkout Model python validation](RM-media/checkoutmodelpyval.png)

- Checkout View Python

![Checkout Viewpython validation](RM-media/checkoutviewpyval.png)

- Profile Model Python

![Profile Model python validation](RM-media/profilemodelpyval.png)

- Profile View Python

![Profile View python validation](RM-media/profileviewpyval.png)

- Blog Model Python

![Blog Model python validation](RM-media/blogmodelpyval.png)

- Blog Form Python

![Blog Form python validation](RM-media/blogformpyval.png)

</details>
<details>
<summary>javascript validation</summary>

- Base js 

![Base js validation](RM-media/basejsval.png)

- Profile js

![Profile js validation](RM-media/profilejsval.png)

- Finalprice js

![Finalprice js validation](RM-media/finalpricejsval.png)

- Showprice js

![Showprice js validation](RM-media/showpricejsval.png)

- Get Rating js

![Get Rating js validation](RM-media/getratingjsval.png)

- Stripe js

![Stripe js validation](RM-media/stripejsval.png)

- Checkout js

![Checkout js validation](RM-media/checkoutpricejsval.png)

- Bag js

![Bag js validation](RM-media/bagjsval.png)

- Add Blog js

![Add Blof js validation](RM-media/addblogjsval.png)

- Comment js

![Comment js validation](RM-media/commentjsval.png)

</details>

## User testing 
My Friends and family were asked to review the site and documentation to point out any bugs and/or user experience issues. Their helpful advice throughout the process led to a few small UX changes in order to create a better experience.

[Back to top ⇧](#)