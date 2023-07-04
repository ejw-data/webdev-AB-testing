# webdev-AB-testing  
Author:  Erin James Wills, ejw.data@gmail.com  

![AB Testing Banner](./images/AB-flask-db.png)  

<cite>Photo by <a href="https://unsplash.com/@pistos?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Jeffrey Hamilton</a> on <a href="https://unsplash.com/s/photos/identical?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText">Unsplash</a></cite>

<br>

## Overview  
<hr>  
This repo explores the basic concepts of how to obtain information for AB testing.

## Status  
This is just the starting point but the core structure of the code works as of 7/3/2023.  The Flask app currently loads and index.html page that has two buttons.  Each button is tracked through the class associated with it named `trackable`.  The database currently stores only the id of the button clicked but this can be expanded to include a data, session id, and user id.  The app already has a working feature that stores a cookie but this feature needs improved such that the database is checked for this cookie and if the id associated with the cookie can not be found then a new id is assigned.  

<br>

## Next Phase  
1.  Create cookie containing a user id
1.  Update database to collect datetime, cookie id, etc related to page interaction
1.  Create two html pages that are considered the A and B versions.  
1.  Create admin page that summarizes website interactions via a dashboard
    * Dashboard includes  
        * Table of most recent users to access page
        * Show t-test of A and B pages

<br>

## Longterm Goals
1. add authentication
1. add error handling
1. more sophisticated tracking
1. improved analysis page

<br>

## Key Performance Indicators (KPI)
1. conversion rate
1. click-through rate
1. bounce rate
1. page views
1. form submissions

<br>

## Browser Information
1.  Cookies
1.  Local Storage or Session Storage
1.  IP Address
1.  User-Agent String
1.  Referrer Header

<br>

## Creating the Database  
1.  From terminal, type: `sqlite3 <db_name>`
2.  Write SQL queries to create tables
3.  When complete type: `.exit`