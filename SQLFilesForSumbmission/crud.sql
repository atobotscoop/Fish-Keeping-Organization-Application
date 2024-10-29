--Get all fish fromm the cold water category
SELECT Name, TemperatureRange, Compatibility 
FROM Fish 
WHERE CategoryID = 4;

--List all fish with a temperature range between 72 and 82
SELECT Name, TemperatureRange 
FROM Fish 
WHERE TemperatureRange BETWEEN '72F' AND '82F';

-- Update the compatability of a fish
UPDATE Fish
SET Compatibility = 'Semi-Aggressive'
WHERE Name = 'Oscar';

-- Update the tank size of a specific tank
UPDATE Tank
SET Size = 75
WHERE TankID = 3;

--Delete a fish from the database (this specifically removes the convict ciclid)
DELETE FROM Fish 
WHERE FishID = 30;

--List tanks that are freshwater
SELECT TankID, Size, CurrentFish
FROM Tank
WHERE Type = 'Freshwater';

--Remove a tank if it has no fish in it
DELETE FROM Tank
WHERE CurrentFish IS NULL;

-- A slighlty more complex operation that joins several tables
-- so we can get detailed info on a fish regarding its category, tank size, and food
SELECT 
    Fish.Name AS FishName,
    Tank.Size AS TankSize,
    Category.Type AS CategoryType,
    Food.Name AS FoodName,
    Food.FoodType AS FoodType
FROM 
    Fish
JOIN 
    Tank ON Fish.TankID = Tank.TankID
JOIN 
    Category ON Fish.CategoryID = Category.CategoryID
JOIN 
    Food ON Fish.FoodID = Food.FoodID
ORDER BY 
    CategoryType, TankSize DESC;

