create view article_views as
select title, count(*) as views, author
from articles join log on
path = concat('/article/', slug)
group by title, author;

create view author_views as
select name, sum(views) as views
from article_views join authors
on author = id
group by name;

create view error_logs as
select date(time) as date,
round(100.0*sum(case status when '200 OK'
then 0 else 1 end)/count(status),1) as error
from log group by date;