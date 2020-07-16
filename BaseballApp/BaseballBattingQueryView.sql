CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `lahmansbaseballdb`.`BaseballBattingQuery` AS
    SELECT 
        `b`.`playerID` AS `playerID`,
        `b`.`yearID` AS `year`,
        `b`.`stint` AS `stint`,
        `b`.`teamID` AS `team`,
        `b`.`lgID` AS `lg`,
        `b`.`G` AS `G`,
        `b`.`AB` AS `AB`,
        `b`.`R` AS `R`,
        `b`.`H` AS `H`,
        `b`.`2B` AS `2B`,
        `b`.`3B` AS `3B`,
        `b`.`HR` AS `HR`,
        `b`.`RBI` AS `RBI`,
        `b`.`SB` AS `SB`,
        `b`.`CS` AS `CS`,
        `b`.`BB` AS `BB`,
        `b`.`SO` AS `SO`,
        `b`.`IBB` AS `IBB`,
        `b`.`HBP` AS `HBP`,
        `b`.`SH` AS `SH`,
        `b`.`SF` AS `SF`,
        `b`.`GIDP` AS `GIDP`,
        `p`.`nameFirst` AS `FirstName`,
        `p`.`nameLast` AS `LastName`,
        `p`.`nameGiven` AS `BirthName`,
        `p`.`weight` AS `weight`,
        `p`.`height` AS `height`,
        `p`.`bats` AS `bats`,
        `p`.`throws` AS `throws`,
        `p`.`debut` AS `debut`
    FROM
        (`lahmansbaseballdb`.`batting` `b`
        JOIN `lahmansbaseballdb`.`people` `p` ON ((`b`.`playerID` = `p`.`playerID`)))