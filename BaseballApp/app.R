library(shiny)

if (!require(Lahman)) install.packages("Lahman")
if (!require(dplyr)) install.packages("dplyr")
if (!require(ggplot2)) install.packages("ggplot2")

source("baseball_stats.R")

# batting statistic
batdata <- c("G", "AB",	"R", "H", "X2B", "X3B", "HR", "RBI", "SB", "CS", "BB", "SO",
             "IBB", "HBP", "SH", "SF", "GIDP")

# pitching statistic
pitchdata <- c("W", "L", "G", "GS", "CG", "SHO", "SV", "IPouts", "H", "ER",
               "HR", "BB", "SO", "BAOpp", "ERA", "IBB",	"WP",	"HBP", "BK", "BFP",	
               "GF", "R", "SH",	"SF", "GIDP")

# fielding statistic
fielddata <- c("G", "GS", "InnOuts", "PO", "A", "E", "DP", "PB", "WP", "SB", 
               "CS", "ZR")

# Define UI for application that draws a histogram
ui <- fluidPage(
    # to be displayed on the left hand side
    # (introduction, radio buttons, text input, and batting data)
    sidebarPanel(
        radioButtons("position", "Position Type",
                     c("batting", "pitching", "fielding")),
        
        # first name and last name inputs as initial default
        textInput("fname", "First Name", "Derek"),
        textInput("lname", "Last Name", "Jeter"),
        
        # Create plot conditions based on position and statistic
        conditionalPanel(condition = "input.position == 'batting'",
                     selectInput("bdata", "Batting Statistic to Plot",
                                 batdata, selected = 'HR')),
    
        conditionalPanel(condition = "input.position == 'pitching'",
                     selectInput("pdata", "Batting Statistic to Plot",
                                 pitchdata, selected = 'SO')),
    
        conditionalPanel(condition = "input.position == 'fielding'",
                     selectInput("fdata", "Batting Statistic to Plot",
                                 fielddata, selected = 'InnOuts')),
    ),
    
    # main panel (gets displayed on the right hand side, the plot)
    mainPanel({
        plotOutput("plot")
    }),
    
    # data table output
    tableOutput("mlb_player_data")
)

server <- function(input, output) {
    
    baseball_stat <- reactive({
        switch(input$position,
               "batting" = input$bdata,
               "pitching" = input$pdata,
               "fielding" = input$fdata)
    })
    
    baseball_data <- reactive({
        data <- baseball_query(input$fname, input$lname, input$position)
        data
    })
    
    # output the table of the player's data based on batting, pitching or fielding
    output$mlb_player_data <- renderTable({
        baseball_data()
    })
    
    output$plot <- renderPlot({
    # plot baseball's player records based on a statistic in a histogram
    baseball_plot <- baseball_data()[, baseball_stat()]
    ggplot(data = baseball_data(),
           aes(year, as.numeric(baseball_plot))) +
        ggtitle(paste("year vs", baseball_stat())) +
        theme(plot.title = element_text(size = 30)) +
        theme(axis.title.x = element_blank()) +
        ylab(baseball_stat()) +
        theme(axis.title = element_text(size = 20)) +
        geom_bar(stat = "identity", fill = "#002D72", colour = "#D50032") +
        theme(strip.text = element_text(size = 15))
    })
}

# Run the application 
shinyApp(ui = ui, server = server)
