1) Inspect the DataFrames using print and head:

   visits lists all of the users who have visited the website
   cart lists all of the users who have added a t-shirt to their cart
   checkout lists all of the users who have started the checkout
   purchase lists all of the users who have purchased a t-shirt
   
2) Combine visits and cart using a left merge.

3) How long is your merged DataFrame?

4) How many of the timestamps are null for the column cart_time?
   What do these null rows mean?

5) What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?
   Note: To calculate percentages, it will be helpful to turn either the numerator or the denominator into a float, by using float(), with the number to convert passed in as input. Otherwise, Python will use integer division, which truncates decimal points.

6) Repeat the left merge for cart and checkout and count null values. What percentage of users put items in their cart, but did not proceed to checkout?

7) Merge all four steps of the funnel, in order, using a series of left merges. Save the results to the variable all_data.
   Examine the result using print and head.

8) What percentage of users proceeded to checkout, but did not purchase a t-shirt?

9) Which step of the funnel is weakest (i.e., has the highest percentage of users not completing it)?
   How might Cool T-Shirts Inc. change their website to fix this problem?
   Average Time to Purchase
   
10) Using the giant merged DataFrame all_data that you created, let’s calculate the average time from initial visit to final purchase. Add a column that is the difference between purchase_time and visit_time.

11) Examine the results by printing the new column to the screen.

12) Calculate the average time to purchase by applying the .mean() function to your new column.
