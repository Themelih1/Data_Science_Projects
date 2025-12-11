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
