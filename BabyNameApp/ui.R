library(shiny)

shinyUI(fluidPage(

    # Vertical layout: top is for selection, bottom is for plot output
    verticalLayout(
        sidebarPanel(
            radioButtons("gender", "Gender (M or F):",
                         choices = c("M", "F"), selected = "M"),
            textInput("name", "Name to Lookup:", "Jonathan")
        ),

        mainPanel(plotOutput("babyname_plot"))
    )
))
