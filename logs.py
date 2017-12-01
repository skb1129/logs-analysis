"""
Q1 :-
create or replace view article_views as
select title, author, count(*) as views from
articles join log on
path = concat('/article/', slug)
group by title, author;

select * from article_views order by views desc limit 3;


Q2 :-
create view author_views as
select name, sum(views) as views
from article_views join authors
on author = id
group by name;

select * from author_views order by views desc limit 4;

Q3 :-
create view error_logs as
select date(time) as date,
round(100.0*sum(case status when '200 OK'
then 0 else 1 end)/count(status),1) as error
from log group by date;

select * from error_logs where error > 1;
"""