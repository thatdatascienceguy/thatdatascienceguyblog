library(shiny)
library(babynames)
library(dplyr)
library(ggplot2)

# get data and remove 'prop' variable (large dataset save some space)
baby_names_per_year <- babynames::babynames %>% select(-c("prop"))
#options(warn = -1)
shinyServer(function(input, output){
    
    output$babyname_plot <- renderPlot({
        # query the babynames dataset based on input of name and gender
        n_births_by_year <- baby_names_per_year %>%
            filter(name == input$name & sex == input$gender)
        
        # Color selection based on gender
        if(input$gender == 'F'){
            plot_color <- "#FFC0CB" # pink
        }
        else{ # if sex = 'M'
            plot_color <- "#0000FF" # blue
        }
      
        # if number of years == 2 or 1
        if(nrow(n_births_by_year) == 2 | nrow(n_births_by_year) == 1){
            # same as n>2 but scale x axis discrete
            ggplot(data = n_births_by_year, aes(x=year, y=n)) +
                geom_bar(stat="identity", fill=plot_color) +
                ggtitle(paste("Number of Babies Born in the U.S. With the Name",
                              input$name, "from 1880 to 2018")) +
                theme_classic() +
                theme(axis.title.y = element_blank(),
                      axis.title.x = element_blank(),
                      axis.text.y = element_text(size=10),
                      axis.text.x = element_text(size=10)) +
                scale_x_discrete(limits=n_births_by_year$year)
        }
        else{
        # plot the barplot of year vs number of births 
        ggplot(data = n_births_by_year, aes(x=year, y=n)) +
            geom_bar(stat="identity", width = 0.5, fill=plot_color) +
            ggtitle(paste("Number of Babies Born in the U.S. With the Name",
                          input$name, "from 1880 to 2018")) +
            theme_classic() +
            theme(axis.title.y = element_blank(),
                  axis.title.x = element_blank(),
                  axis.text.y = element_text(size=10),
                  axis.text.x = element_text(size=10))
        }
    })
})
