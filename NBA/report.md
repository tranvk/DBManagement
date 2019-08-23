# Overview
Homework 4 for Database Management and Analysis, Prof. Versoza Fall 2018
Author: Kevin Tran
Description: Introductory assignment using postgresql to clean and analyze a CSV file.

# Table Design
Primary key: Due to null values, I decided not to use a primary key. I considered using the ID column as a primary key, but there were many null values. If I converted the null values to 0, then there would be a problem of repeated primary keys. Also, my data features NBA player statistics by season, meaning that there are repeated names, so player name was also ruled out for primary key.

Null: I allow null because there are blank entries in my dataset, mainly from the early stages of the NBA. I don't give them default values because if an entry is omitted, it usually means that the statistic wasn't part of the game yet.
However, if I remove null, it can affect the synchronization of the columns as a whole.
# Import
My csv has over 50 columns and headers. I want to reduce the number of csv columns represented in the SQL table to 13. Before I can import the csv to my permanent table, I will first store it as-is to a temporary table. Then, I'll insert the 13 columns into my permanent table. The helper file that generates the temporary table is create_temp.sql, which has 50+ fields to match the number of headers the csv contains.
# Database Information
List of databases
Name    |  Owner   | Encoding |   Collate   |    Ctype    |   Access privileges   
-----------+----------+----------+-------------+-------------+-----------------------
postgres  | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 |
template0 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
|          |          |             |             | postgres=CTc/postgres
template1 | postgres | UTF8     | en_US.UTF-8 | en_US.UTF-8 | =c/postgres          +
|          |          |             |             | postgres=CTc/postgres
(3 rows)


List of relations
Schema |   Name    | Type  |  Owner   
--------+-----------+-------+----------
public | nba_stats | table | postgres
public | temp      | table | postgres
(2 rows)

# Query Results

1. the total number of rows in the database
-----+---------+-----
(34962 rows)
2. show the first 15 rows, but only display 3 columns (your choice)

     player      | position | points
-----------------+----------+--------
 Curly Armstrong | G-F      |    458
 Cliff Barker    | SG       |    279
 Leo Barnhorst   | SF       |    438
 Ed Bartels      | F        |     63
 Ed Bartels      | F        |     59
 Ed Bartels      | F        |      4
 Ralph Beard     | G        |    895
 Gene Berce      | G-F      |     10
 Charlie Black   | F-C      |    661
 Charlie Black   | F-C      |    382
 Charlie Black   | F-C      |    279
 Nelson Bobb     | PG       |    242
 Jake Bornheimer | F-C      |    254
 Vince Boryla    | SF       |    612
 Don Boven       | F-G      |    656
(15 rows)

3. do the same as above, but chose a column to sort on, and sort in descending order


        player        | position | points
----------------------+----------+--------
 Wilt Chamberlain*    | C        |   4029
 Wilt Chamberlain*    | C        |   3586
 Michael Jordan*      | SG       |   3041
 Wilt Chamberlain*    | C        |   3033
 Wilt Chamberlain*    | C        |   2948
 Michael Jordan*      | SG       |   2868
 Kobe Bryant          | SG       |   2832
 Kobe Bryant          | SG       |   2832
 Bob McAdoo*          | C        |   2831
 Kareem Abdul-Jabbar* | C        |   2822
 Rick Barry*          | SF       |   2775
 Michael Jordan*      | SG       |   2753
 Tiny Archibald*      | PG       |   2719
 Elgin Baylor*        | SF       |   2719
 Wilt Chamberlain*    | C        |   2707
(15 rows)


4. add a new column without a default value

5. set the value of that new column
UPDATE 34962

6. show only the unique (non duplicates) of a column of your choice


player          
--------------------------

Bato Govedarica
Michael Adams
Reggie Smith
Michael Wilson
Ed Pinckney
Dave Greenwood
Bill Mayfield
Al Henry
Mike Silliman
Stanley Jackson
Loren Woods
...

7. group rows together by a column value (your choice) and use an aggregate function to calculate  something about that group (count of all members of the group, the average of a column of the members of the group)
 show the column that is used for grouping AND the result of the aggregate function (so, 2 columns minimum on output)


player          | count
--------------------------+-------
                |     0
Bato Govedarica          |     1
Michael Adams            |    11
Reggie Smith             |     2
Michael Wilson           |     7
Ed Pinckney              |    16
Dave Greenwood           |    14
Bill Mayfield            |     1
Al Henry                 |     2
Mike Silliman            |     1
Stanley Jackson          |     1
Loren Woods              |    12
Freddie Crawford         |     9
Carlos Delfino           |    16

8. now, using the same grouping query or creating another one, find a way to filter the query results based on the values for the groups (for example, show all genres that have more than 2 movies in it and only show the genre and the number of movies for that genre)

player     | age | per  
----------------+-----+------
LeBron James   |  20 | 25.7
Jackie Butler  |  19 | 90.3
Korleone Young |  20 | 31.3
Anthony Davis  |  20 | 26.5

9.

avg          
----------------------
493.4835589941972921

10.

player          | max
--------------------------+-----
Manute Bol               | 397
Elmore Smith             | 393
David Robinson*          | 319
Shawn Bradley            | 288
Shaquille O'Neal*        | 286
Alonzo Mourning*         | 271
Theo Ratliff             | 258
Hakeem Olajuwon*         | 254
Tree Rollins             | 254
Bob McAdoo*              | 246
Serge Ibaka              | 242
Dwight Howard            | 231
Marcus Camby             | 230
Jermaine O'Neal          | 228
Josh Smith               | 227
Benoit Benjamin          | 225
Terry Tyler              | 220
Andrei Kirilenko         | 220
Larry Nance              | 217
Duane Causwell           | 215
Rudy Gobert              | 214
Bill Walton*             | 211
Raef LaFrentz            | 206
Tim Duncan               | 206


11.
player          |  max  
--------------------------+-------
Jackie Butler            |  90.3
Gerald Green             |  76.3
Dave Scholz              |  67.6
Marcus Williams          |    53
Sim Bhullar              |  44.3
Monti Davis              |  44.2
Ian Mahinmi              |  35.3
Mouhamed Sene            |  33.2
Korleone Young           |  31.3
Anthony Davis            |  30.8
Demetrius Jackson        |  30.8
Henry Sims               |  29.2
Alphonso Ford            |  28.9
Walter Berry             |  28.9
Shaquille O'Neal*        |  28.6
Chris Paul               |  28.3
LeBron James             |  28.1
Michael Jordan*          |  27.5
Shelton Jones            |  27.3
Amar'e Stoudemire        |  26.6
Nikola Jokic             |  26.4
Mo Howard                |  26.3
Walt Bellamy*            |  26.3
Bonzi Wells              |  26.3
Kevin Durant             |  26.2
Giannis Antetokounmpo    |  26.1
Karl-Anthony Towns       |    26
Oscar Robertson*         |  25.9
Magic Johnson*           |  25.7
Bob Peterson             |  25.4

12.          

 player                   | min
--------------------------+-----
 Al Harrington            |  18
 Tracy McGrady            |  18
 Kobe Bryant              |  18
 Jermaine O'Neal          |  18
 Andris Biedrins          |  18
 Maciej Lampe             |  18
 Yaroslav Korolev         |  18
 C.J. Miles               |  18
 Darko Milicic            |  18
 Bill Willoughby          |  18
 Amir Johnson             |  18
 Bruno Sundov             |  18
 Andrew Bynum             |  18
 Shaun Livingston         |  19
