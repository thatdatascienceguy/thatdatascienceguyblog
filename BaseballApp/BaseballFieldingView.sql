CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `lahmansbaseballdb`.`BaseballFieldingQuery` AS
    SELECT 
        `f`.`playerID` AS `playerID`,
        `f`.`yearID` AS `year`,
        `f`.`stint` AS `stint`,
        `f`.`teamID` AS `team`,
        `f`.`lgID` AS `lg`,
        `f`.`POS` AS `POS`,
        `f`.`G` AS `G`,
        `f`.`GS` AS `GS`,
        `f`.`InnOuts` AS `InnOuts`,
        `f`.`PO` AS `PO`,
        `f`.`A` AS `A`,
        `f`.`E` AS `E`,
        `f`.`DP` AS `DP`,
        `f`.`PB` AS `PB`,
        `f`.`WP` AS `WP`,
        `f`.`SB` AS `SB`,
        `f`.`CS` AS `CS`,
        `f`.`ZR` AS `ZR`,
        `p`.`nameFirst` AS `FirstName`,
        `p`.`nameLast` AS `LastName`,
        `p`.`nameGiven` AS `BirthName`,
        `p`.`weight` AS `weight`,
        `p`.`height` AS `height`,
        `p`.`bats` AS `bats`,
        `p`.`throws` AS `throws`,
        `p`.`debut` AS `debut`
    FROM
        (`lahmansbaseballdb`.`fielding` `f`
        JOIN `lahmansbaseballdb`.`people` `p` ON ((`f`.`playerID` = `p`.`playerID`)))