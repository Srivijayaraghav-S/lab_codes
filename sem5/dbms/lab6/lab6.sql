-- Creating the Pet table
CREATE TABLE Pet (
    Name VARCHAR(50),
    Owner VARCHAR(50),
    Species VARCHAR(50),
    Sex CHAR(1),    
    Birth_Date DATE,
    Death_Date DATE,
    Phone VARCHAR(15)
);

-- Creating the Event table
CREATE TABLE Event (
    name VARCHAR(50),
    date DATE,
    type VARCHAR(50),
    remark VARCHAR(255)
);

-- Inserting values into the Pet table
INSERT INTO Pet (Name, Owner, Species, Sex, Birth_Date, Death_Date, Phone) VALUES
('Fluffy', 'Harold Regan', 'cat', 'f', '1993-02-04', NULL, '789543210'),
('Claws', 'Gwen Cappaloo', 'cat', 'm', '1994-03-17', NULL, '875643219'),
('Buffy', 'Harold Regan', 'dog', 'f', '1989-05-13', '1990-08-27', '789543210'),
('Fang', 'Benny Robert', 'dog', 'm', '1979-08-31', NULL, '987654321'),
('Bowser', 'Diane Charles', 'dog', 'm', '1998-09-11', NULL, '985423111'),
('Chirpy', 'Gwen Cappaloo', 'bird', 'f', '1997-12-09', NULL, '875643219'),
('Whistler', 'Gwen Cappaloo', 'bird', 'm', '1996-04-29', NULL, '875643219'),
('Slim', 'Benny Robert', 'snake', 'm', '1999-03-30', NULL, '987654321'),
('Puffball', 'Hamster Daniel', 'hamster', 'f', '1995-07-29', NULL, '342567812');

-- Inserting values into the Event table
INSERT INTO Event (name, date, type, remark) VALUES
('Fluffy', '1995-05-15', 'litter', '4 kittens, 3 female, 1 male'),
('Buffy', '1993-06-23', 'litter', '5 puppies, 2 female, 3 male'),
('Buffy', '1994-06-19', 'litter', '3 puppies, 3 female'),
('Chirpy', '1999-03-21', 'vet', 'needed beak straightened'),
('Slim', '1997-08-03', 'vet', 'broken rib'),
('Bowser', '1991-10-12', 'kennel', NULL),
('Fang', '1991-10-12', 'kennel', NULL),
('Fang', '1998-08-28', 'birthday', 'Gave him a new chew toy'),
('Claws', '1998-03-17', 'birthday', 'Gave him a new flea collar'),
('Whistler', '1998-12-09', 'birthday', 'First birthday');
-- 1. Modify the structure/create new by splitting the column name to (First name and Last name) and copy the values appropriately into it.
ALTER TABLE Pet ADD COLUMN First_Name VARCHAR(50);
ALTER TABLE Pet ADD COLUMN Last_Name VARCHAR(50);

UPDATE Pet SET First_Name = SUBSTRING_INDEX(Owner, ' ', 1), Last_Name = SUBSTRING_INDEX(Owner, ' ', -1);
ALTER TABLE Pet DROP COLUMN Owner;

-- 2. List the Animals that were born during or after 1998
SELECT * FROM Pet WHERE Birth_Date >= '1998-01-01';

-- 3. List the pets that were snake or bird
SELECT * FROM Pet WHERE Species IN ('snake', 'bird');

-- 4. List each group of species based on its birthdate (oldest first)
SELECT * FROM Pet ORDER BY Species, Birth_Date ASC;

-- 5. Display the age of every species as alias
SELECT *, TIMESTAMPDIFF(YEAR, Birth_Date, CURRENT_DATE) AS Age FROM Pet;

-- 6. Determine age at death for animals that have died.
SELECT *, TIMESTAMPDIFF(YEAR, Birth_Date, Death_Date) AS Age_At_Death FROM Pet WHERE Death_Date IS NOT NULL;

-- 7. Finding animals with birthdays in the current month
SELECT * FROM Pet WHERE MONTH(Birth_Date) = MONTH(CURRENT_DATE);

-- 8. To find names containing a “f”
SELECT * FROM Pet WHERE First_Name LIKE '%f%' OR Last_Name LIKE '%f%';

-- 9. Find out how many pets each owner has:
SELECT Owner, COUNT(*) AS NumberOfPets FROM Pet GROUP BY Owner;

-- 10. Number of animals per combination of species and sex:
SELECT Species, Sex, COUNT(*) AS NumberOfAnimals FROM Pet GROUP BY Species, Sex;

-- 11. Find out the ages at which each pet had its litters
SELECT e.name, TIMESTAMPDIFF(YEAR, p.Birth_Date, e.date) AS AgeAtLitter
FROM Event e
JOIN Pet p ON e.name = p.First_Name
WHERE e.type = 'litter';

-- 12. Find breeding pairs among the pets (assuming breeding pairs are of opposite sex and same species)
SELECT a.First_Name AS Male, b.First_Name AS Female
FROM Pet a, Pet b
WHERE a.Species = b.Species AND a.Sex = 'm' AND b.Sex = 'f';

-- 13. Create a Trigger that adds “+47” to all Phone numbers in the pet table.
DELIMITER $$
CREATE TRIGGER phone_number_before_insert BEFORE INSERT ON Pet
FOR EACH ROW
BEGIN
  SET NEW.Phone = CONCAT('+47', NEW.Phone);
END;
$$
CREATE TRIGGER phone_number_before_update BEFORE UPDATE ON Pet
FOR EACH ROW
BEGIN
  SET NEW.Phone = CONCAT('+47', NEW.Phone);
END;
$$
DELIMITER ;

-- 14. Create a procedure for Pet table that will return oldest and youngest pet.
DELIMITER $$
CREATE PROCEDURE GetOldestYoungestPet()
BEGIN
  SELECT * FROM Pet ORDER BY Birth_Date ASC LIMIT 1; -- Oldest
  SELECT * FROM Pet ORDER BY Birth_Date DESC LIMIT 1; -- Youngest
END;
$$
DELIMITER ;

-- 15. Write a function that will display age for a given pet.
DELIMITER $$
CREATE FUNCTION GetAge(petFirstName VARCHAR(50), petLastName VARCHAR(50)) RETURNS INT
BEGIN
  DECLARE petAge INT;
  SELECT TIMESTAMPDIFF(YEAR, Birth_Date, CURRENT_DATE) INTO petAge FROM Pet WHERE First_Name = petFirstName AND Last_Name = petLastName;
  RETURN petAge;
END;
$$
DELIMITER ;
