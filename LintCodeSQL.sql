-- no1959 · Query information about Chinese and British teachers
select * from `teachers` where `country` = 'UK' or `country` = 'CN'

-- no1981 · Check the nationality of all teachers
select distinct `country` from `teachers`

-- no2004 · Delete all courses until 2020
delete from `courses` where `created_at` < '2020-1-1'

-- no2007 · Check course name and class size
select `name`, `student_count` from `courses`

-- no2009 · Query all teachers
select * from `teachers`

-- no2011 · Search for information on courses with more than 1000 participants
select * from `courses` where `student_count` > 1000

-- no2012 · Find course information for the course named Artificial Intelligence
select * from `courses` where `name` = 'Artificial Intelligence'

-- no2013 · Check the name of the teacher
select `name` from `teachers`

-- no2017 · Inserting SQL course information into the course table
insert into `courses` value (14, 'SQL',	200,	'2021-02-25', 1)

-- no2020 · Update on the number of students choosing artificial intelligence
update `courses` set `student_count` = 500 where `name` = 'Artificial Intelligence'

-- no2021 · Insert teacher information into the specified column of the teachers table
insert into `teachers` (`name`, `email`, `age`, `country`) value ('XiaoFu', 'XiaoFu@lintcode.com', 20, 'CN')

-- no2045 · Output Hello LintCode
select "Hello LintCode!"

-- no2035_Calculate the number of years difference between the start date and the current date of all courses in the course schedule
select `name` as 'courses_name', `created_at` as 'courses_created_at', TIMESTAMPDIFF(YEAR, `created_at`, '2021-04-01') as 'year_diff'
from courses;