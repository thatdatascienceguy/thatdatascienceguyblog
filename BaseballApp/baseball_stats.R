# Batting Query
baseball_batting_data <- dplyr::inner_join(Lahman::People,
                                           Lahman::Batting,
                                           by=c('playerID'))

baseball_batting_data <- baseball_batting_data %>%
  select(c(year=yearID, stint, team=teamID, lg=lgID, G, AB, R, H, X2B, X3B,
           HR, RBI, SB, CS, BB, SO, IBB, HBP, SH, SF, GIDP, weight, height, bats,
           throws, firstName=nameFirst, lastName=nameLast))

# Pitching Query
baseball_pitching_data <- dplyr::inner_join(Lahman::People,
                                            Lahman::Pitching,
                                            by=c('playerID'))

baseball_pitching_data <- baseball_pitching_data %>%
  select(c(year=yearID, stint, team=teamID, lg=lgID, W, L, G, GS, CG, SHO, SV,
           IPouts, H, ER, HR, BB, SO, BAOpp, ERA, IBB, WP, HBP, BK, BFP, GF, R,
           SH, SF, GIDP, weight, height, firstName=nameFirst, lastName=nameLast))

# Fielding Query
baseball_fielding_data <- dplyr::inner_join(Lahman::People,
                                            Lahman::Fielding,
                                            by=c("playerID"))

baseball_fielding_data <- baseball_fielding_data %>%
  select(c(year=yearID, stint, team=teamID, lg=lgID, POS, G, GS, InnOuts, PO, A,
           E, DP, PB, WP, SB, CS, ZR, weight, height, firstName=nameFirst,
           lastName=nameLast))

baseball_query <- function(fName, lName, baseball_stat) {
  if (baseball_stat == "batting"){
    query <- baseball_batting_data %>%
    filter(fName == firstName & lName == lastName)
    return(query)
  }
  if (baseball_stat == "pitching"){
    query <- baseball_pitching_data %>%
      filter(fName == firstName & lName == lastName)
    return(query)
  }
  if (baseball_stat == "fielding"){
    query <- baseball_fielding_data %>%
      filter(fName == firstName & lName == lastName)
    return(query)
  }
}