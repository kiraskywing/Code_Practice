-- no1928 · Analysis of Online Class I
select `student_id`, min(`date`) as `earliest_course_date`
from `online_class_situations`
where `course_number` > 0
group by `student_id`;

-- no1932 · Students with the Most Failed Subjects I
select `student_id` from `exams`
where `is_pass` = 0
group by `student_id`
order by count(*) desc
limit 1

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

-- no1963 · Search for teachers aged 20~25 whose nationality is not Chinese or British
select * from `teachers` where `age` between 20 and 25 and `country` not in ('CN', 'UK')

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

-- no2053 · Check the name, email and course name of the teacher from China
select 
`courses`.`name` as `course_name`, 
`teachers`.`name` as `teacher_name`, 
`teachers`.`email` as `teacher_email` 
from `courses` right join `teachers` on `courses`.`teacher_id` = `teachers`.`id`
where `teachers`.`country` = 'CN'

-- no2055 · Search for all course names and their corresponding instructor names and nationalities
(select 
c.`name` as `course_name`, 
t.`name` as `teacher_name`, 
t.`country` as `teacher_country` 
from `courses` as c left join `teachers` as t on c.`teacher_id` = t.`id`)
union
(select 
c.`name` as `course_name`, 
t.`name` as `teacher_name`, 
t.`country` as `teacher_country` 
from `courses` as c right join `teachers` as t on c.`teacher_id` = t.`id`)

-- no2056 · Copy the data in the teachers table that are older than 20 to another table
insert into `teachers_bkp` (select * from `teachers` where `age` > 20)

-- no2057 · Modify course information created by instructor Eastern Heretic
update `courses` set `name` = 'PHP', `student_count` = 300
where `teacher_id` = (select `id` from `teachers` where `name` = 'Eastern Heretic')

-- no2059 · Remove faculty who have created courses before 2020
delete from `teachers` 
where `id` in (
	select `teacher_id` from `courses` 
	where year(`created_at`) < 2020
)

-- no2060 · Search for the name of the teacher for the 'Big Data' course
select `name` from `teachers` where `id` = (
	select `teacher_id` from `courses` where `name` = 'Big Data'
)

-- no2062 · Query the id and name of all courses taught by the specified teacher
select `courses`.`id` as `id`, `courses`.`name` as `course_name`, `teachers`.`name` as `teacher_name` 
from `courses` join `teachers` on `courses`.`teacher_id` = `teachers`.`id`
where `teachers`.`name` = 'Eastern Heretic'

-- no2065 · Check the course names of all courses taught by all teachers who are older than 20 years old
select `courses`.`name` from `courses` 
join `teachers` on `courses`.`teacher_id` = `teachers`.`id`
where `courses`.`teacher_id` in (
	select `id` from `teachers` where `age` > 20
)

-- no2066 · Search for course information for courses with more students than the number of students in all courses of the oldest teacher
select * from `courses` where `student_count` > (
	select max(`student_count`) from `courses` where `teacher_id` in (
		select `id` from `teachers` where `age` = (
			select max(`age`) from `teachers`
		)
	)
)

-- no2069 · Search for the course name and number of students in the course with the highest number of students per instructor
select `name`, `student_count` from `courses` where (`student_count`, `teacher_id`) in (
	select max(`student_count`), `teacher_id` from `courses` group by `teacher_id`
)

-- no2070 · Search for the name of a course created later than the creation time of any of the specified teacher's courses
select `name` from `courses` 
where `created_at` > any (
	select `created_at` from `courses`
	where `teacher_id` = (
		select `id` from `teachers`
		where `name` = 'Southern Emperor'
	)
)
and `teacher_id` != (
    select `id` from `teachers`
    where `name` = 'Southern Emperor'
)

-- no2076 · Search for teacher information based on national average age
select * from `teachers` where `country` in (
	select `country` from `teachers` group by `country`
	having avg(`age`) > (select avg(`age`) from `teachers`)
)

-- no2077 · Search for information on courses and instructors with the highest number of students
select 
	`courses`.`name` as `course_name`, 
	`courses`.`student_count`, 
	`teachers`.`name` as `teacher_name`
from `courses` join `teachers` on `courses`.`teacher_id` = `teachers`.`id`
where `courses`.`student_count` = (
	select max(`student_count`) from `courses`
)

-- no2078 · Find out the number of teachers of different ages
select `age`, count(`age`) as `age_count` from `teachers` group by `age` order by `age` desc

-- no2080 · Search for the name of the instructor and the total number of students in all the instructor's courses with less than 3000 students
select `t`.`name`, IFNULL(sum(`c`.`student_count`), 0) as `student_count`
from `teachers` as `t` left join `courses` as `c` on `t`.`id` = `c`.`teacher_id`
group by `t`.`name`
having `student_count` < 3000;

-- no2081 · Insert the current date into the table
insert into `records` values (curdate())

-- no2082 · Statistics on the number of courses taught by each teacher
select `teachers`.`name` as `teacher_name`, count(`courses`.`name`) as `course_count` 
from `courses` right join `teachers` on `courses`.`teacher_id` = `teachers`.`id`
group by `teachers`.`id`
order by `course_count` desc, `teacher_name`

-- no2084 · Add primary key constraints to the course table courses
alter table `courses` add primary key (`id`)

-- no2085 · Remove the primary key constraint from the course table `courses`
alter table `courses` drop primary key

-- no2086 · Search for the nationality of the teacher starting with 'U' and the total number of students between 2000 and 5000 and the total number of students of that nationality
select `t`.`country`, sum(`c`.`student_count`) as `student_count`
from `courses` as `c` join `teachers` as `t`
on `c`.`teacher_id` = `t`.`id`
group by `t`.`country`
having `student_count` between 2000 and 5000
order by `student_count` desc

-- no2091 · Adding Foreign Key Constraints to Course Tables
alter table `courses` add foreign key (`teacher_id`) references `teachers`(`id`)

-- no2616 · Insert Kansas information into the teacher table
begin;
insert into `teachers` (`name`, `age`, `country`)
value ('Kansas', 41, 'UK');
commit;

-- no2617 · View the current transaction isolation level of the database
SHOW VARIABLES like '%isolation%';

-- no2620 · View the self-incrementing locking pattern for MySQL databases
show variables like '%innodb_autoinc_lock_mode%';

-- no2544 · Insert information about Feng Qingyang
LOCK TABLES teachers READ;
unlock tables;
insert into `teachers` (`name`, `email`, `age`, `country`) 
values ('Feng Qingyang', 'feng.qingyang@163.com', 37, 'CN');

-- no2547 · Query all information in the teachers table
LOCK TABLES courses WRITE;
unlock tables;
select * from `teachers`;

-- no2564 · Create a Trigger "before_teachers_insert"
CREATE TRIGGER `before_teachers_insert`
    BEFORE INSERT ON `teachers`
    FOR EACH ROW 
SET NEW.`country` = 'CN';

-- no2548 · Update Southern Emperor's email
-- 对 courses 表上写锁，不要删除该代码 --
LOCK TABLES courses WRITE;

-- Write your SQL Query here --
-- example: SELECT * FROM XX_TABLE WHERE XXX --
unlock tables;
update `teachers` set `email` = 'southern.emperor@outlook.com' where `name` = 'Southern Emperor';

-- no2565 · Create a Trigger "before_teachers_update"
create trigger `before_teachers_update`
	before update on `teachers`
	for each row
set new.`country` = 'CN';

-- no2568 · Delete the Trigger "before_teachers_update"
drop trigger `before_teachers_update`;

-- no2569 · Normative courses table data insert
create trigger `before_courses_insert`
before insert 
on `courses` for each row
begin
	if new.`teacher_id` not in (select `id` from `teachers`) then
		set new.`teacher_id` = 0, new.`created_at` = NULL;
	end if;
end;

-- no2570 · New data processing of recruitment information statistics table
create trigger `before_insert_recording`
before insert on `recording` for each row
begin
	if new.`student_id` not in (select `id` from `students`)
		then set new.`student_id` = 0;
	end if;
	
	if new.`company_id` not in (select `id` from `companies`)
		then set new.`company_id` = 0;
	end if;
end;

-- no2572 · New data trigger message alert
create trigger `memo` 
after insert on `members` for each row
begin
	if new.`birthDate` is null then
		insert into `reminders` (`memberId`, `message`)
		values (new.`id`, concat('Hi ', new.`name`, ', please update your date of birth.'));
	end if;
end;

-- no2573 · Backup New Data Trigger
create trigger `bkp`
after insert on `teachers` for each row
begin
	insert into `teachers_bkp` (`name`, `email`, `age`, `country`)
	values (new.`name`, new.`email`, new.`age`, new.`country`);
end;

-- no2575 · Normative courses table data update
create trigger `before_courses_update`
before update on `courses` for each row
begin
	if new.`teacher_id` not in (select `id` from `teachers`) then
		set new.`teacher_id` = old.`teacher_id`;
	end if;
end;

-- no2576 · Update data processing of recruitment information statistics table
create trigger `double_check`
before update on `recording` for each row
begin
	if new.`company_id` not in (select `id` from `companies`) then
		set new.`company_id` = old.`company_id`;
	end if;

	if new.`student_id` not in (select `id` from `students`) then
		set new.`student_id` = old.`student_id`;
	end if;
end;

-- no2577 · Backup Update Data Trigger
create trigger `bkp`
after update on `teachers` for each row
begin
	insert into `teachers_bkp` (`name`, `email`, `age`, `country`)
	values (old.`name`, old.`email`, old.`age`, old.`country`);
end;

-- no2578 · Update data trigger message alert
create trigger `memo`
after update on `members` for each row
begin
	declare old_msg varchar(255);
	declare new_msg varchar(255);
	
	set old_msg = 'Update {';
	set new_msg = ' To {';

	if old.`name` != new.`name` then
		set old_msg = concat(old_msg, '[name=', old.`name`, '] ');
		set new_msg = concat(new_msg, '[name=', new.`name`, '] ');
	end if;

	if old.`email` != new.`email` then
		set old_msg = concat(old_msg, '[email=', old.`email`, '] ');
		set new_msg = concat(new_msg, '[email=', new.`email`, '] ');
	end if;

	if old.`birthDate` != new.`birthDate` then
		set old_msg = concat(old_msg, '[birthDate=', old.`birthDate`, '] ');
		set new_msg = concat(new_msg, '[birthDate=', new.`birthDate`, '] ');
	end if;

	set old_msg = concat(old_msg, '}');
	set new_msg = concat(new_msg, '}');
	
	insert into `reminders` (`memberId`, `message`)
	values (old.`id`, concat(old_msg, new_msg));
end;

-- 2587 · Associated processing when deleting teachers table information (I)
create trigger check_teacher after delete on teachers for each row
begin 
        update courses set teacher_id = 0 where teacher_id = old.id;
end

-- no2627 · Troubleshoot the current database table locks and view the table lock analysis
show status like 'table%';

-- no2633 · Troubleshoot the current database row locks and view row lock analysis
SHOW STATUS LIKE 'innodb_row_lock%';

-- no2635 · The use of optimistic locks and pessimistic locks (I)
update `teachers` set `country` = 'CN', `version` = `version` + 1
where `name` = 'Western Venom' and `version` = 5;

-- no2654 · Put a line lock on the data 'id = 3'
select * from `teachers` where `id` = 3 lock in share mode;

-- no2720 · Creating a view that ensures consistency (I)
CREATE VIEW v_teachers
AS
SELECT * FROM teachers where age < 30

-- no2806 · MySQL Stored Procedure IN Parameters I
create procedure  teacher (in countryName  varchar(25))
begin
SELECT * from teachers where country=countryName;
end;
call teacher('CN');