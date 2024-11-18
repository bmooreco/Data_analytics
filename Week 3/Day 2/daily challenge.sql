-- -- -- -- -- CREATE TABLE FirstTab (
-- -- -- -- --      id integer, 
-- -- -- -- --      name VARCHAR(10)
-- -- -- -- -- -- )

-- -- -- -- -- INSERT INTO FirstTab VALUES
-- -- -- -- -- (5,'Pawan'),
-- -- -- -- -- (6,'Sharlee'),
-- -- -- -- -- (7,'Krish'),
-- -- -- -- -- (NULL,'Avtaar')

-- -- -- -- -- SELECT * FROM FirstTab

-- -- -- -- -- CREATE TABLE SecondTab (
-- -- -- -- --     id integer 
-- -- -- -- -- )

-- -- -- -- -- INSERT INTO SecondTab VALUES
-- -- -- -- -- (5),
-- -- -- -- -- (NULL)


-- -- -- -- -- SELECT * FROM FirstTab
-- -- -- -- --MY PREDICTION:RETURNS id 5,6,7 (ALSO 3)

-- -- -- --     SELECT COUNT(*) 
-- -- -- --     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS null )

-- -- -- -- QUESTION 2
-- -- -- I EXPECT TO SEE 2

-- --  SELECT COUNT(*) 
-- --     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )

-- --QUESTION 3
-- -- I expect to see nothing

--     SELECT COUNT(*) 
--     FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )

    SELECT COUNT(*) 
    FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )