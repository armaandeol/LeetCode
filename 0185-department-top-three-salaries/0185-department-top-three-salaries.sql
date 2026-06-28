# Write your MySQL query statement below
select D.name as Department , E.name as Employee, E.Salary as Salary
from Employee E
join Department D
on E.departmentid = D.id
where (
    select COUNT(DISTINCT emp.salary)
    from Employee as emp
    where emp.salary > E.salary and emp.departmentid = e.departmentid
)<3;