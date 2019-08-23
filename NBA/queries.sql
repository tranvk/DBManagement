-- write your queries underneath each number:

-- 1. the total number of rows in the database
select from nba_stats;

-- 2. show the first 15 rows, but only display 3 columns (your choice)
SELECT player, position, points from nba_stats limit 15;


-- 3. do the same as above, but chose a column to sort on, and sort in descending order
SELECT player, position, points from nba_stats where points IS NOT NULL order by points desc limit 15;

-- 4. add a new column without a default value
ALTER TABLE nba_stats ADD COLUMN cool_points numeric;

-- 5. set the value of that new column
UPDATE nba_stats SET cool_points = 7;


-- 6. show only the unique (non duplicates) of a column of your choice
SELECT DISTINCT player FROM nba_stats;


-- 7.group rows together by a column value (your choice) and use an aggregate function to calculate something about that group
SELECT player, count(player) FROM nba_stats GROUP BY player;

-- 8. now, using the same grouping query or creating another one, find a way to filter the query results based on the values for the groups
SELECT player, age, per FROM nba_stats  WHERE age < 21 AND per > 25;

-- 9. write a comment about your query 9
--What is the average points per season for point guards (pg)?
SELECT avg(points) FROM nba_stats WHERE position = 'PG';
-- 10. write a comment about your query 10
--Which players under 25 have the most blocks?
SELECT player, max(blocks) FROM nba_stats WHERE age < 25 AND blocks IS NOT NULL GROUP BY player ORDER BY max(blocks) DESC;
-- 11. write a comment about your query 11
--Which players under 23 have the highest PER?
SELECT player, max(per) FROM nba_stats WHERE age < 23 AND per IS NOT NULL GROUP BY player ORDER BY max(per) desc;
-- 12. write a comment about your query 12
--Who were the youngest nba players?
SELECT DISTINCT player, min(age) FROM nba_stats WHERE age IS NOT NULL GROUP BY player ORDER BY min(age);
