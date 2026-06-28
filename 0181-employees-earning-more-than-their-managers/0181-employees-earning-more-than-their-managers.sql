# Write your MySQL query statement below
select name as Employee
from Employee as emp
where emp.managerId is not null and(
    select salary
    from Employee e
    where e.id = emp.managerId and e.salary < emp.salary
)