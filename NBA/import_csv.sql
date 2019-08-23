-- write your COPY statement to import a csv here

COPY temp
  FROM '/home/kevin/Documents/NYU/Data Management/tranvk-homework04/Seasons_Stats.csv'
  csv HEADER;
