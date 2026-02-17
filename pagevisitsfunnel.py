import pandas as pd
import numpy as np

visits = pd.read_csv('content/visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('content/cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('content/checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('content/purchase.csv',
                       parse_dates=[1])



#Q1) Inspect the DataFrames using print and head:
#
#visits lists all of the users who have visited the website
#cart lists all of the users who have added a t-shirt to their cart
#checkout lists all of the users who have started the checkout
#purchase lists all of the users who have purchased a t-shirt
#

print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())


#Q2) Combine visits and cart using a left merge.

visits_cart = pd.merge(visits, cart, how="left")
print(visits_cart.head(10))

#Q3) How long is your merged DataFrame?

print(len(visits_cart))
#Ans) 2000

#Q4) How many of the timestamps are null for the column cart_time?
#What do these null rows mean?
no_cart_time = visits_cart[visits_cart.cart_time.isnull()]
print(len(no_cart_time))

#Ans) 1652. this means there is no corresponding cart_time for the user_id in the visits dataframe.


#Q5) What percent of users who visited Cool T-Shirts Inc. ended up not placing a t-shirt in their cart?
print(np.round(((float(len(no_cart_time)) / float(len(visits_cart))) * 100),2))

#Ans) 82.6%


#Q6) Repeat the left merge for cart and checkout and count null values. What percentage of users put items in their cart, but did not proceed to checkout?

visits_checkout = pd.merge(visits, checkout, how="left")
print(visits_checkout.head(10))

no_checkout_time = visits_checkout[visits_checkout.checkout_time.isnull()]
print(no_checkout_time)
print(len(no_checkout_time))
print(np.round(((float(len(no_checkout_time)) / float(len(visits_checkout))) * 100),2))

#Ans) 88.7%

#Q7) Merge all four steps of the funnel, in order, using a series of left merges. Save the results to the variable all_data.
# Examine the result using print and head.

all_data = pd.merge(visits, cart, how="left").merge(checkout, how="left").merge(purchase, how="left")
print(all_data)

#Q8 What percentage of users proceeded to checkout, but did not purchase a t-shirt?
checkout_no_purchase = all_data[(all_data.checkout_time.isnull() == False) & (all_data.purchase_time.isnull() == True)]
print(checkout_no_purchase)
print(len(checkout_no_purchase))

#Ans) 82

#Q9) Which step of the funnel is weakest (i.e., has the highest percentage of users not completing it)?

all_data_nulls = all_data.isna()
num_missing = all_data_nulls.sum()
no_of_entries = len(all_data)

funnel = pd.DataFrame({
    "step": all_data.columns,
    "num_missing": num_missing.values,
    "percent_not_completed": (num_missing.values / no_of_entries * 100).round(2)
})

funnel["drop_off_from_prev"] = funnel["percent_not_completed"].diff().fillna(funnel["percent_not_completed"].iloc[0])

print(funnel)

#Ans) 78.37% of people never get to the cart


#Q10) Using the giant merged DataFrame all_data that you created, let’s calculate the average time from initial visit to final purchase. Add a column that is the difference between purchase_time and visit_time.

all_data["purchase_time_diff"] = all_data["purchase_time"] - all_data["visit_time"]
print(all_data)


#Q11) Examine the results by printing the new column to the screen.

print(all_data["purchase_time_diff"])


#Q12) Calculate the average time to purchase by applying the .mean() function to your new column.

print(all_data["purchase_time_diff"].mean())

#Ans) 43:12.38. average time to purchase is 43 minutes and 12 seconds