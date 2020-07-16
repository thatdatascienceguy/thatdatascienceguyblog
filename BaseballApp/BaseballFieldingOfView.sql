CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `lahmansbaseballdb`.`BaseballFieldingOfQuery` AS
    SELECT 
        `f`.`playerID` AS `playerID`,
        `f`.`yearID` AS `year`,
        `f`.`stint` AS `stint`,
        `f`.`Glf` AS `Glf`,
        `f`.`Gcf` AS `Gcf`,
        `f`.`Grf` AS `Grf`,
        `p`.`nameFirst` AS `FirstName`,
        `p`.`nameLast` AS `LastName`,
        `p`.`nameGiven` AS `BirthName`,
        `p`.`weight` AS `weight`,
        `p`.`height` AS `height`,
        `p`.`bats` AS `bats`,
        `p`.`throws` AS `throws`,
        `p`.`debut` AS `debut`
    FROM
        (`lahmansbaseballdb`.`fieldingof` `f`
        JOIN `lahmansbaseballdb`.`people` `p` ON ((`f`.`playerID` = `p`.`playerID`)))