# Whiskey Shop

[View the live project here](https://whiskey-shop-320e32983cd1.herokuapp.com/ "Link to deployed site - Whiskey shop")

<hr>

## Table of contents

1. [UX](#ux)

    * [Strategy](#strategy)

        * [Project overview](#project-overview)

        * [Project goals](#project-goals)

        * [User stories](#user-stories)

    * [Scope](#scope)

        * [Consistent features implemented](#consistent-features-implemented)

        * [Features left to implement](#features-left-to-implement)

    * [Structure](#structure)

        * [Database model](#database-model)
        
        * [Applications](#applications)

    * [Skeleton](#skeleton)

        * [Wireframes](#wireframes)

    * [Surface](#surface)

        * [Color scheme](#color-scheme)

        * [Typography](#typography)

        * [Imagery](#imagery)

    * [Web marketing](#web-marketing)

        * [SEO](#seo)

        * [Social media marketing](#social-media-marketing)

        * [Email marketing](#email-marketing)

        * [Privacy policy](#privacy-policy)

* [Testing](#testing)

    * [Manual testing](#manual-testing)

    * [Bugs ans issues](#bugs-and-issues)

    * [Validator testing](#validator-testing)

* [Deployment](#deployment)

* [Credits](#credits)

    * [Technologies Used](#technologies-used)

	* [Frameworks, Libraries & Programs Used](#frameworks,-Libraries-&-Programs-Used)

	* [Content](#content)

	* [Media](#media)

* [Acknowledgments](#aknowledgements)

## UX

## 1.  Strategy

### Project overview

WhiskeyShop, built on Django's robust foundation, provides a comprehensive and user-friendly platform for whiskey enthusiasts to explore and purchase their favorite products. With its extensive catalog, secure transactions, user reviews, and powerful administration capabilities, WhiskeyShop delivers a delightful shopping experience. By leveraging Django's flexibility and scalability, the platform can easily adapt to future enhancements and meet the evolving needs of both customers and administrators in the dynamic world of whiskey retail.

### Project goals

### User Stories

[Here](https://github.com/maish79/whiskey_shop/issues) is a list of user stories displayed as a Kanban board.

## 2. Scope 

### Consistent features implemented

Most of the features have been designed to look the same, to allow users to gain familiarity with the site layout and enable them to find information quickly.

* Card design for main layout
* Home

![Whiskey Home](read_me_docs/whiskey-home.png)

* Products

![Whiskey category](read_me_docs/whiskey-category.png)

* Category

![Whiskey about](read_me_docs/whiskey-about.png)

* Location

![Whiskey location](read_me_docs/whiskey-location.png)

* FAQ

![Whiskey faq](read_me_docs/whiskey-faq.png)

* Sitemap

![Whiskey sitemap](read_me_docs/whiskey-sitemap.png)

* Whiskey add product

![Whiskey add product](read_me_docs/whiskey-add-product.png)

* Blog

![Whiskey blog](read_me_docs/whiskey-blog.png)

* Checkout

![Whiskey checkout](read_me_docs/whiskey-checkout.png)

* Signin

![Whiskey signin](read_me_docs/whiskey-signin.png)

* Signup

![Whiskey signup](read_me_docs/whiskey-signup.png)

* Success

![Whiskey success](read_me_docs/whiskey-success.png)

* Update details

![Whiskey details](read_me_docs/whiskey-update-details.png)

## 3. Structure

### Database model


In this project, seven applications have been created:

* Home

* whiskey_shop

* Bag

* Blog

* Checkout

* Contact

* Products

* Location

The custom models for PP5 are in:

* Products app

* Blog app

* Contact app
 
* Location app

## 4. Skeleton

### Wireframes

All wireframes were created used [Balsamiq](https://balsamiq.com/)

Wireframes for each device are linked here:
- [Balsamiq wireframes](assets/documents)

# Surface

## Design 
<p align="center">
<img src="read_me_docs/whiskey-coolors.png" width="50%" height="100%">
</p>

### Typography

The font selected was Dancing script because it is a flowing and handwritten style that adds a touch of elegance and playfulness to the text. It can give your design a warm and friendly feel.

### Imagery

The images selected for this project were got from [Unsplash](https://unsplash.com/)

## 6. Web marketing

The web marketing techniques implemented in this project have been inspired from the Code Institute series of videos on Introduction to Search Engine Optimization and Web Marketing, for the Full Stack Development (E-commerce applications) course.

### SEO

### Social media marketing

I Created a Facebook page for social media marketing in  ecommerce app so that i can  expand my reach, engage with my target audience, and leverage advertising opportunities to drive brand awareness and sales. [Facebook page](read_me_docs/fb-page.png) 

### Email marketing

It was implemented an email marketing feature on the footer where the user can submit his email for a newsletter.

This tool is from MailChimp, and it was personalized in order to fit the rest of the project.

![MailCchimp](read_me_docs/whiskey-mailchimp.png)

## 1. Manual testing

All the manual testing was made on the [deployed site](https://whiskey-shop-320e32983cd1.herokuapp.com/):

| Page            | Section                         | Test                                                                                                                                                                                                                                                 | Result                                                                                                                                                                                                                                                                                                                                    |
|-----------------|---------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Home            | Navigation                      | Logo link when clicked from any page needs to direct back to the home page                                                                                                                                                                           | Tested from different pages, and this works                                                                                                                                                                                                                                                                                               |
| Home            | Navigation                      | Search button shows correct results.                                                                                                                                                                                                                 | * When a search is not made but the search icon is selected, an error message appears "You didn't enter any search criteria". * Searched for flavor 'chocolate' and any product with this word in the name or in the description is showns. * Searched for any word that won't match with the project, like 'math'. Didn't show a result. |
| Home            | Navigation                      | Navigation links go to the correct pages.                                                                                                                                                                                                            | All links were tested, and they directed to the correct pages.                                                                                                                                                                                                                                                                            |
| Home            | Navigation                      | Logged in user status                                                                                                                                                                                                                                | It was used two different acccounts: One from superuser and non-superuser- The status is shown in both cases, after the user clicks on the account tab.                                                                                                                                                                                   |
| Home            | Hero container                  | Call to action button 'Shop now' leads to the 'All products' page.                                                                                                                                                                                   | It works                                                                                                                                                                                                                                                                                                                                  |
| Home            | Footer                          | Social media links need to open in a new tab.                                                                                                                                                                                                        | All links opened in a new tab, and the facebook link directs to the facebook 'Wonder Cakes' page.                                                                                                                                                                                                                                         |
| Home            | Footer                          | Mailchimp: subscribe newsletter needs to accept the user email and it requires an input.                                                                                                                                                             | If the user doesn't enter an input, a message is shown 'This field is required'. If the user enters a valid input, a message is shown 'Thank you for your subscribing!'                                                                                                                                                                   |
| About us        | Content                         | Click on the contact us here, needs to direct to the contact page.                                                                                                                                                                                   | It works                                                                                                                                                                                                                                                                                                                                  |
| About us        | Content                         | Call to action buttons 'All products' and 'blog me' need to direct to their pages.                                                                                                                                                                   | It works                                                                                                                                                                                                                                                                                                                                  |
| Contact us      | Form                            | All the inputs are required so the form is valid.                                                                                                                                                                                                    | If the user doesn't enter all the fields, it will be required and the form won't pass. If the user enters all the fields, a message is shown 'thank you for your enquiry...'                                                                                                                                                              |
| FAQ             | links                           | Click on the links for sending email or accesing to the website.                                                                                                                                                                                     | It works.                                                                                                                                                                                                                                                                                                                                 |
| FAQ             | links                           | Call to action button 'All products' leads to the 'All products' page.                                                                                                                                                                               | It works                                                                                                                                                                                                                                                                                                                                  |
| All products    | Sorting field                   | Selecting any option, needs to arrange the display of the products                                                                                                                                                                                   | It works.                                                                                                                                                                                                                                                                                                                                 |
| All products    | Back to the top link            | Clicking on the arrow icon, needs to take the user back to the top.                                                                                                                                                                                  | It works, but it will be nice that the icon only appears after the user scrolls down.                                                                                                                                                                                                                                                     |
| All products    | icon links                      | Clicking on the pencil (for editing) and on the trash can (for deleting), the admin can either edit or delete the product.                                                                                                                           | It works, by clicking on the pencil, the admin is redirected to the edit page. If the admin clicks on the trash can, it will delete the item (it sould be nicer to have more security for that action) NOTE: these links aren't shown for a non-superuser                                                                                 |
| Product_details | icon links                      | Clicking on the pencil (for editing) and on the trash can (for deleting), the admin can either edit or delete the product.                                                                                                                           | It works, by clicking on the pencil, the admin is redirected to the edit page. If the admin clicks on the trash can, it will delete the item (it sould be nicer to have more security for that action) NOTE: these links aren't shown for a non-superuser                                                                                 |
| Product_details | increment or decrement quantity | Clicking on the minus icon, decrement the quantity  of items for adding to the bag, the min value is 1. The increment icon, add items to the bag.                                                                                                    | It works                                                                                                                                                                                                                                                                                                                                  |
| Product_details | Call to action button           | Clicking on the 'Keep shopping' button, needs to direct to the 'All products' page, and by clicking on the 'Add to bag' button, adds the item to the bag, if the user doesn't change the quantity or the flavor, it will add the default input       | It works                                                                                                                                                                                                                                                                                                                                  |
| Bag             | Call to action button           | Clicking on the 'Keep shopping' button, needs to direct to the 'All products' page, and by clicking on the 'Secure checkout' button, directs the user to the checkout page.                                                                          | It works                                                                                                                                                                                                                                                                                                                                  |
| Bag             | increment or decrement quantity | Clicking on the minus icon, decrement the quantity  of items for adding to the bag, the min value is 1. The increment icon, add items to the bag.  After modifying the quantities, the user needs to click on the 'update' link, so it is effective. | It works                                                                                                                                                                                                                                                                                                                                  |
| Checkout        | Form                            | The user will have a checkout form for delivering and paying, all the required fields need to be entered in order to complete the order                                                                                                              | It works                                                                                                                                                                                                                                                                                                                                  |
| Checkout        | Call to action button           | Clicking on the 'Adjust Bag' button, needs to direct back to the 'Bag' page, and the 'Complete order' button needs to direct to the payment procedure, and if it is valid, it will direct to the 'Checkout success' page.                            | It works                                                                                                                                                                                                                                                                                                                                  |
| Profile         | Form                            | The user will have a form where he can update his personal info, and after clicking on the 'update information', a success message will be shown: 'Profile was updated successfully'                                                                 | It works                                                                                                                                                                                                                                                                                                                                  |
| Profile         | Order number links              | After the user make an order, he will have a history order where he can access to each order, the link needs to direct to the checkout success page of the product.                                                                                  | It works                                                                                                                                                                                                                                                                                                                                  |                                                                                                                              

### * Browser Testing

The website was tested using Google Chrome Developer Tools Toggle Device Toolbar to simulate viewports of different devices.

The website was tested on the following devices:
- MacBook Pro
- windows