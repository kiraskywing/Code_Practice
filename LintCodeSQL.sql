-- no2035_Calculate the number of years difference between the start date and the current date of all courses in the course schedule
select `name` as 'courses_name', `created_at` as 'courses_created_at', TIMESTAMPDIFF(YEAR, `created_at`, '2021-04-01') as 'year_diff'
from courses;