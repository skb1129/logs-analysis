# Logs-Analysis Project

## Build

* This project is built using SQL and Python languages.
* It uses python-psycopg2 to execute SQL queries on newsdata.sql.
* Prints the query results on CLI.

## Instructions

* Install Vagrant & VirtualBox.
* Download or Clone this repository.
* Download the newsdata from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip).
* Unzip the file to the root of this repository.
* Open terminal and <code>cd</code> into root of this repository.
* Run <code>vagrant up</code> to set up the virtual machine.
* Run <code>vagrant ssh</code> to log into the virtual machine.
* Run <code>cd /vagrant</code> to move to root of repository in vagrant.
* Run <code>psql -d news -f newsdata.sql</code> to load and connect to the database.
* Create required views by running :
```
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
```
* Run <code>\q</code> to disconnect from database.
* Finally run <code>python3 logs.py</code> to see the query results.

## Dependencies

* PostgreSQL
* psycopg2
* Vagrant
* VirtualBox

Contact:<br>
Surya Kant Bansal<br>
e-mail: skbansal.cse15@chitkara.edu.in