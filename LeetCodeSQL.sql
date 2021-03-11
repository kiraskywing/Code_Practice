-- no.175. Combine Two Tables
SELECT FirstName, LastName, City, State FROM Person LEFT JOIN Address ON Person.PersonID = Address.PersonID;

-- no.176. Second Highest Salary
SELECT MAX(Salary) as SecondHighestSalary FROM Employee WHERE Salary < (SELECT MAX(Salary) FROM Employee);