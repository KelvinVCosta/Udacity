-- Write a query that returns all the species in the zoo, and how many
-- animals of each species there are, sorted with the most populous
-- species at the top.
--
-- The result should have two columns:  species and number.
--
-- The animals table has columns (name, species, birthdate) for each animal.

select species, count(*) as num
from animals
group by species
order by num desc;
