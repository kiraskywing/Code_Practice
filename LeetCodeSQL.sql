-- no175. Combine Two Tables
SELECT FirstName, LastName, City, State FROM Person LEFT JOIN Address ON Person.PersonID = Address.PersonID;

-- no176. Second Highest Salary
SELECT MAX(Salary) as SecondHighestSalary FROM Employee WHERE Salary < (SELECT MAX(Salary) FROM Employee);

-- no181. Employees Earning More Than Their Managers
select A.Name as Employee from Employee as A inner join Employee as B on A.ManagerId = B.Id where A.Salary > B.Salary;

-- no182. Duplicate Emails
select Email from Person group by Email having count(Email) > 1;

-- no183. Customers Who Never Order
select Name as Customers from Customers Where Id not in (select CustomerId from Orders);
select A.Name as Customers from Customers A left join Orders B on A.Id = B.CustomerId Where B.CustomerId is null;

-- no196. Delete Duplicate Emails
delete A from Person A, Person B where A.Email = B.Email and A.Id > B.Id;
delete from Person where Id not in (select sub_Id from (select min(id) as sub_Id from Person group by Email) as subquery);

-- no197. Rising Temperature
select cur.id as Id from Weather cur left join Weather pre on pre.recordDate + interval 1 day = cur.recordDate where cur.Temperature > pre.Temperature;

-- no595. Big Countries
select name, population, area from World where area > 3000000 or population > 25000000;

-- no596. Classes More Than 5 Students
select class from courses group by class having count(distinct student) >= 5;

-- no620. Not Boring Movies
select * from cinema where id % 2 != 0 and description != 'boring' order by rating desc;

-- no627. Swap Salary
update Salary set sex = (case when sex = 'f' then 'm' else 'f' end);
update Salary set sex = if(sex = 'f', 'm', 'f');
