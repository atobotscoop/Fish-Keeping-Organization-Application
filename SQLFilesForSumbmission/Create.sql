
--Table: Category
-- Functional Dependences: CategoryID (Type, CareLevel, TypicalTemperatureRange)
CREATE TABLE Category (
    CategoryID INTEGER PRIMARY KEY,
    Type TEXT,
    CareLevel TEXT,
    TypicalTemperatureRange TEXT
);

-- Table: Tank
-- Functional Dependencies: TankID (Size, Type, CurrentFish)
CREATE TABLE Tank (
    TankID INTEGER PRIMARY KEY,
    Size INTEGER,
    Type TEXT,
    CurrentFish TEXT
);

-- Table: Food
--Functional Dependencies: FoodID (Name, FishID (Will only be populated if a food is specific to a fish otherwise is NULL), FoodType)
CREATE TABLE Food (
    FoodID INTEGER PRIMARY KEY,
    Name TEXT,
    FishID INTEGER,
    FoodType TEXT,
    FOREIGN KEY (FishID) REFERENCES Fish(FishID)
);

-- Table:Fish
-- Functional Dependencies: FishID (Name, CategoryID,TankID, Compatibility, TemperatureRange, FoodID)
CREATE TABLE Fish (
    FishID INTEGER PRIMARY KEY,
    Name TEXT,
    CategoryID INTEGER,
    TankID INTEGER,
    Compatibility TEXT,
    TemperatureRange TEXT,
    FoodID INTEGER,
    FOREIGN KEY (CategoryID) REFERENCES Category(CategoryID),
    FOREIGN KEY (TankID) REFERENCES Tank(TankID),
    FOREIGN KEY (FoodID) REFERENCES Food(FoodID)
);


-----------------------------------------------
