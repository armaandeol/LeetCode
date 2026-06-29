# Write your MySQL query statement below
select c.name as Customers
from Customers as c
where not Exists (
    select * 
    from Orders as o
    where o.customerId = c.id
)
