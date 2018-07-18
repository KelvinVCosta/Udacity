-- Goal
-- Find the one food that is eaten by only one animal.
-- Answer: mongoose
-- The animals table has columns (name, species, birthdate) for each
-- individual.
-- The diet table has columns (species, food) for each food that a
-- species eats.

--
-- Get animals that have only one
select species, count(*) as num
from animals group by species
having num = 1;


select animals.species, diet.food, count(*) as num
from animals, diet group by animals.species

-- Gets all species and their foods
select * from diet
group by food

-- returns
+----------+-----------+
|  species |      food |
+==========+===========+
| mongoose |      eggs |
| sea lion |      fish |
|  warthog |   insects |
|  warthog |      meat |
|    zebra |    plants |
|  raccoon | shellfish |
| mongoose |    snakes |
+----------+-----------+

select species, food, count(*) as num from diet
group by food

+----------+-----------+-----+
|  species |      food | num |
+==========+===========+=====+
| mongoose |      eggs |   2 |
| sea lion |      fish |   3 |
|  warthog |   insects |   6 |
|  warthog |      meat |   7 |
|    zebra |    plants |  14 |
|  raccoon | shellfish |   2 |
| mongoose |    snakes |   1 |
+----------+-----------+-----+
