-- -- -- select * from customer
-- -- select first_name, last_name as full_name from customer 

-- -- -- select create_date from 

-- -- SELECT * FROM customer
-- -- ORDER BY first_name DESC

-- -- SELECT film_id, title, description, release_year, rental_rate 
-- -- FROM film
-- -- ORDER BY rental_rate ASC

-- SELECT address, phone 
-- FROM address
-- WHERE district = 'Texas'

-- SELECT * FROM film
-- WHERE film_id IN (15, 150)

-- SELECT film_id, title, description, length, rental_rate
-- FROM film
-- WHERE title = 'boondock saints'
-- does not exist

-- SELECT film_id, title, description, length, rental_rate 
-- FROM film
-- WHERE title LIKE 'bo%'
-- no luck

-- SELECT film_id, title, description, rental_rate 
-- FROM film
-- ORDER BY rental_rate ASC LIMIT 10

-- select film_id, title, description, rental_rate
-- from film
-- ORDER BY rental_rate ASC LIMIT 10 OFFSET 10 

-- SELECT customer.first_name, customer.last_name, payment.amount
-- FROM customer
-- FULL OUTER JOIN payment
-- ON customer.customer_id = payment.customer_id