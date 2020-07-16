CREATE 
    ALGORITHM = UNDEFINED 
    DEFINER = `root`@`localhost` 
    SQL SECURITY DEFINER
VIEW `lahmansbaseballdb`.`BaseballPitchingQuery` AS
    SELECT 
        `p`.`playerID` AS `playerID`,
        `p`.`yearID` AS `year`,
        `p`.`stint` AS `stint`,
        `p`.`teamID` AS `team`,
        `p`.`lgID` AS `lg`,
        `p`.`W` AS `W`,
        `p`.`L` AS `L`,
        `p`.`G` AS `G`,
        `p`.`GS` AS `GS`,
        `p`.`CG` AS `CG`,
        `p`.`SHO` AS `SHO`,
        `p`.`SV` AS `SV`,
        `p`.`IPouts` AS `IPouts`,
        `p`.`H` AS `H`,
        `p`.`ER` AS `ER`,
        `p`.`HR` AS `HR`,
        `p`.`BB` AS `BB`,
        `p`.`SO` AS `SO`,
        `p`.`BAOpp` AS `BAOpp`,
        `p`.`ERA` AS `ERA`,
        `p`.`IBB` AS `IBB`,
        `p`.`WP` AS `WP`,
        `p`.`HBP` AS `HBP`,
        `p`.`BK` AS `BK`,
        `p`.`BFP` AS `BFP`,
        `p`.`GF` AS `GF`,
        `p`.`R` AS `R`,
        `p`.`SH` AS `SH`,
        `p`.`SF` AS `SF`,
        `p`.`GIDP` AS `GIDP`,
        `ppl`.`nameFirst` AS `FirstName`,
        `ppl`.`nameLast` AS `LastName`,
        `ppl`.`nameGiven` AS `BirthName`,
        `ppl`.`weight` AS `weight`,
        `ppl`.`height` AS `height`,
        `ppl`.`bats` AS `bats`,
        `ppl`.`throws` AS `throws`,
        `ppl`.`debut` AS `debut`
    FROM
        (`lahmansbaseballdb`.`pitching` `p`
        JOIN `lahmansbaseballdb`.`people` `ppl` ON ((`p`.`playerID` = `ppl`.`playerID`)))