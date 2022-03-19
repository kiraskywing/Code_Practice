-- no1953 · Query the name of the Chinese teacher
select `name` from `teachers` where `country` = 'CN'

-- no1957 · Inquire about courses starting before May 2020
select `name`, `created_at` from `courses` 
where `created_at` >= '2020-01-01' and `created_at` < '2020-05-01'

-- no1958 · Query the courses that meet the conditions taught by the specified teacher
select * from `courses` where `student_count` > 500 and `teacher_id` = 4

-- no1959 · Query information about Chinese and British teachers
select * from `teachers` where `country` = 'UK' or `country` = 'CN'

-- no1960 · Query course information for a specific time
select * from `courses` where `created_at` in ('2021-01-01', '2021-01-03')

-- no1962 · Query courses with teacher id other than 1 and 3
select `name` from `courses` where `teacher_id` not in (1, 3)

-- no1964 · Query for course information about the number of students within the specified range
select * from `courses` where `student_count` between 50 and 55

-- no1972 · Inquire about Chinese and Japanese teachers who have e-mail addresses
select * from `teachers` where country in ('CN', 'JP') and not (email is NULL)

-- no1974 · Query teacher information by email
select `name`, `email` from `teachers` where `email` like '%@qq.com'

-- no1977 · Sorted by age of Chinese teachers in descending order
select * from `teachers` where `country` = 'CN' order by `age` desc

-- no1980 · Search for the oldest Chinese teacher
select * from `teachers` where `country` = 'CN' order by `age` desc limit 1

-- no1981 · Check the nationality of all teachers
select distinct `country` from `teachers`

-- no1982 · Check the age of teachers and sort them in ascending order
select distinct `age` from `teachers` order by `age`

-- no1985 · Number of teachers aged 20 to 28 who are Chinese and British nationals
select count(*) as `teacher_count` from `teachers` where `country` in ('CN', 'UK') and `age` between 20 and 28

-- no1987 · Find the age of the oldest Chinese teacher
select max(`age`) as `max_age` from `teachers` where `country` = 'CN'

-- no1989 · Check the age of the youngest teacher
select min(`age`) as `min_age` from `teachers`

-- no1991 · Count the total number of students for teacher #3
select sum(`student_count`) as `select_student_sum` from `courses` where `teacher_id` = 3

-- no1995 · Check the average age of teachers over 20 years old
select round(avg(`age`)) as `avg_teacher_age` from `teachers` where `age` > 20

-- no1997 · Check the information of teachers who do not have email and are older than 20 years old
select * from `teachers` where isnull(`email`) and `age` > 20

-- no2001 · Query the course information of 'Web' or 'Big Data'
select * from `courses` where `name` = 'Web' or `name` = 'Big Data'

-- no2004 · Delete all courses until 2020
delete from `courses` where `created_at` < '2020-1-1'

-- no2007 · Check course name and class size
select `name`, `student_count` from `courses`

-- no2008 · Query the course information of two courses
select * from `courses` where `name` = 'System Design' or `name` = 'Django'

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

-- no2019 · Delete all rows in the table
delete from `courses`

-- no2020 · Update on the number of students choosing artificial intelligence
update `courses` set `student_count` = 500 where `name` = 'Artificial Intelligence'

-- no2021 · Insert teacher information into the specified column of the teachers table
insert into `teachers` (`name`, `email`, `age`, `country`) value ('XiaoFu', 'XiaoFu@lintcode.com', 20, 'CN')

-- no2028 · Postpone all course creation dates by one day
select `name`, date_add(`created_at`, interval 1 day) as `new_created` from `courses`

-- no2029 · Calculate the number of days from 03/26/2019 to the course creation time
select timestampdiff(day, '2019-03-26', `created_at`) as `date_diff` from `courses`

-- no2030 · Query the hours of all course creation times
select `name`, hour(`created_at`) as `created_hour` from `courses`

-- no2031 · Advance all course creation dates by one month
select `id`, `name`, timestampadd(month, -1, `created_at`) as `new_created` from `courses`

-- no2032 · Advance all course creation dates by one day
select `id`, `name`, date_add(`created_at`, interval -1 day) as `new_created` from `courses`

-- no2034 · Check the average age of teachers at the end of the specified mailbox
select AVG(`age`) as `average_teacher_age` from `teachers` where `email` like '%@qq.com'

-- no2035_Calculate the number of years difference between the start date and the current date of all courses in the course schedule
select `name` as 'courses_name', `created_at` as 'courses_created_at', TIMESTAMPDIFF(YEAR, `created_at`, '2021-04-01') as 'year_diff'
from courses;

-- no2036 · Calculate the number of months difference between the start date and the current date of all courses in the schedule
select timestampdiff(month, `created_at`, '2020-04-22') as `MonthDiff` from `courses`

-- no2037 · Search for course titles and course dates through August 2020
select `name`, date(`created_at`) as `created_date` from `courses` where date(`created_at`) < '2020-08-01'

-- no2040 · Search for courses with an instructor id of less than 3 and more than 800 students
select * from `courses` where not (`teacher_id` = 3 or `student_count` <= 800)

-- no2045 · Output Hello LintCode
select "Hello LintCode!"

-- no2046 · The date the course was created is displayed in 'year-month-day hour:minute:second'
select date_format(`created_at`, '%Y-%m-%d %H:%i:%s') as `DATE_FORMAT` from `courses`

-- no2051 · Search for the names of teachers from China and the names of courses they taught
select `c`.`name` as `course_name`, `t`.`name` as `teacher_name`
from `courses` as `c` right join `teachers` as `t`
on `c`.`teacher_id` = `t`.`id`
where `t`.`country` = 'CN'

-- no2062 · Query the id and name of all courses taught by the specified teacher
select `courses`.`id` as `id`, `courses`.`name` as `course_name`, `teachers`.`name` as `teacher_name` 
from `courses` join `teachers` on `courses`.`teacher_id` = `teachers`.`id`
where `teachers`.`name` = 'Eastern Heretic'

-- no2081 · Insert the current date into the table
insert into `records` values (curdate())

-- no2084 · Add primary key constraints to the course table courses
alter table `courses` add primary key (`id`)

-- no2085 · Remove the primary key constraint from the course table `courses`
alter table `courses` drop primary key

-- no2091 · Adding Foreign Key Constraints to Course Tables
alter table `courses` add foreign key (`teacher_id`) references `teachers`(`id`)