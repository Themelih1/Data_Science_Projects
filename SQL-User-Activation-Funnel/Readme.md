# SQL Project: 7-Day User Activation Funnel

## Project Overview

This SQL project is designed to analyze the speed of user activation and conversion within the critical first seven days following registration. By structuring data to measure the time taken for users to perform key actions (adding to cart and placing an order), we can assess the effectiveness of the initial user experience (UX) or onboarding flows.

The final output is a clean user backbone table augmented with binary flags (`1` or `0`) indicating activation success within the 7-day window.

### Key Metrics & Business Value

* **Activation Window (7d):** Defines the critical time period for successful onboarding.
* **`cart_activation_7d`:** Measures the percentage of users who showed intent (added a product to the cart) within the first week.
* **`order_activation_7d`:** Measures the percentage of users who successfully converted (placed an order) within the first week.

This data is vital for product teams to optimize immediate-term conversion rates and diagnose bottlenecks in the initial user journey.

### 🛠 Key SQL Techniques Used

* **CTE (Common Table Expressions):** Used to isolate and pre-process data for the user backbone, first 'add to cart' event, and first order event.
* **Date & Time Arithmetic:** Use of `INTERVAL '7 days'` to dynamically calculate the 7-day activation window for each user.
* **MIN() Aggregation:** Used to accurately identify the *first* instance of a key event (First Add to Cart, First Order Placed), ensuring the funnel logic is sound.
* **Conditional Logic (`CASE WHEN`):** Used to create the binary flags, easily consumed by analytical tools.
* **LEFT JOINs:** Ensures that the core user backbone is maintained, allowing us to track users who *never* performed the activation events.

###  SQL Query (`user_activation_funnel.sql`)

```sql
WITH user_backbone AS(SELECT 
u.id AS user_id,
u.created_timestamp,
CAST(u.created_timestamp as TIMESTAMP)
+ INTERVAL '7 days' as activation_window_7d
 FROM users.csv u
WHERE COALESCE(CAST(u.is_admin AS BOOLEAN),FALSE) = FALSE
AND u.email_address NOT LIKE '%@hypotheticalwidgetshop.com'),

first_add_to_cart AS (SELECT 
e.user_id,
MIN(e.event_time) as firs_add_to_cart_event_time
 FROM events.csv e
 WHERE e.user_id IS NOT NULL
 AND event_name = 'add_to_cart'
 GROUP BY
 e.user_id),

first_Order_placed AS (SELECT 
o.user_id,
MIN(o.created_timestamp) as firt_order_places
 FROM orders.csv o
 WHERE o.user_id IS NOT NULL
 GROUP BY
 o.user_id)

 SELECT user_backbone.*,
    first_add_to_cart.firs_add_to_cart_event_time,
    CASE WHEN first_add_to_cart.firs_add_to_cart_event_time < activation_window_7d
        THEN 1
        ELSE 0 END AS cart_activation_7d,
    first_Order_placed.firt_order_places,
    CASE WHEN first_Order_placed.firt_order_places < activation_window_7d
        THEN 1
        ELSE 0 END AS order_activation_7d
 FROM user_backbone
 LEFT JOIN first_add_to_cart
 ON first_add_to_cart.user_id = user_backbone.user_id
LEFT JOIN first_Order_placed
 ON first_Order_placed.user_id = user_backbone.user_id
