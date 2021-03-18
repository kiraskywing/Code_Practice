-- no175. Combine Two Tables
SELECT FirstName, LastName, City, State FROM Person LEFT JOIN Address ON Person.PersonID = Address.PersonID;

-- no176. Second Highest Salary
SELECT MAX(Salary) as SecondHighestSalary FROM Employee WHERE Salary < (SELECT MAX(Salary) FROM Employee);

-- no177. Nth Highest Salary
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
DECLARE M INT;
SET M = N - 1;
  RETURN (
      select distinct Salary from Employee order by Salary desc limit M, 1
  );
END

-- no178. Rank Scores
select s1.Score, count(s2.Score) as "Rank" from Scores s1, (select distinct Score from Scores) s2
where s1.Score <= s2.Score group by s1.Id order by s1.Score desc

-- no180. Consecutive Numbers
select distinct A.num as ConsecutiveNums from Logs A, Logs B, Logs C where A.id = B.id - 1 and B.id = C.id - 1 and A.num = B.num and B.num = C.num;

-- no181. Employees Earning More Than Their Managers
select A.Name as Employee from Employee as A inner join Employee as B on A.ManagerId = B.Id where A.Salary > B.Salary;

-- no182. Duplicate Emails
select Email from Person group by Email having count(Email) > 1;

-- no183. Customers Who Never Order
select Name as Customers from Customers Where Id not in (select CustomerId from Orders);
select A.Name as Customers from Customers A left join Orders B on A.Id = B.CustomerId Where B.CustomerId is null;

-- no184. Department Highest Salary
select D.Name as Department, E.Name as Employee, T.max_S as Salary
from
    Employee as E,
    (select DepartmentId, max(Salary) as max_S from Employee group by DepartmentId) as T,
    Department as D
where 
    E.DepartmentId = T.DepartmentId and E.Salary = T.max_S and T.DepartmentId = D.Id;

-- no185. Department Top Three Salaries
select D.Name as Department, E.Name as Employee, E.Salary 
from Employee E inner join Department as D on E.DepartmentId = D.Id
where 3 > (select count(distinct Salary) from Employee E2 where E2.Salary > E.Salary and E.DepartmentId = E2.DepartmentId);

-- no196. Delete Duplicate Emails
delete A from Person A, Person B where A.Email = B.Email and A.Id > B.Id;
delete from Person where Id not in (select sub_Id from (select min(id) as sub_Id from Person group by Email) as subquery);

-- no197. Rising Temperature
select cur.id as Id from Weather cur left join Weather pre on pre.recordDate + interval 1 day = cur.recordDate where cur.Temperature > pre.Temperature;

-- no262. Trips and Users
select Request_at as Day, round(sum(if(Status != 'completed', 1, 0)) / count(*), 2) as 'Cancellation Rate'
from Trips
where (Request_at between '2013-10-01' and '2013-10-03')
    and Client_Id not in (select Users_Id from Users where Banned = 'Yes')
    and Driver_Id not in (select Users_Id from Users where Banned = 'Yes')
group by Request_at

-- no595. Big Countries
select name, population, area from World where area > 3000000 or population > 25000000;

-- no596. Classes More Than 5 Students
select class from courses group by class having count(distinct student) >= 5;

-- no620. Not Boring Movies
select * from cinema where id % 2 != 0 and description != 'boring' order by rating desc;

-- no627. Swap Salary
update Salary set sex = (case when sex = 'f' then 'm' else 'f' end);
update Salary set sex = if(sex = 'f', 'm', 'f');
