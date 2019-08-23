-- write your table creation sql here!


DROP TABLE IF EXISTS nba_stats;

CREATE TABLE nba_stats(
  id integer,
  year integer,
  player varchar(255),
  position varchar(255),
  age numeric,
  team varchar,
  games numeric,
  games_started numeric,
  efg numeric,
  per numeric,
  points numeric,
  blocks numeric,
  steals numeric,
  assists numeric
);



INSERT INTO nba_stats (year,player,position,age,team,games,games_started,efg,per,points,blocks,steals,assists)
SELECT year,player,pos,age,tm,g,gs,efg,per,pts,blk,stl,ast
FROM staging_table;
