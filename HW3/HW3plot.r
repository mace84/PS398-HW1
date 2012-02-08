## P398: Assignment 3
## Matthias Orlowski
## 02/08/12
## R script to plot run times generated with HW3timetest.py

library(ggplot2)
RT <- read.table("/Users/mo/Documents/Uni/Duke/ComputationSoc/PS398-HW1/HW3/runtimes.csv", header=F, as.is=T, sep=",")
names(RT) <- c("algorithm","type","length","runtime")
# correct typo in python script
RT$algorithm[RT$algorithm == "Qick Sort"] <- "Quick Sort"
RT$algorithm[RT$algorithm == "Qick Sort (RP)"] <- "Quick Sort (RP)"
# exclude screwed results due to computer usage while running the test
RT <- RT[RT$length<7680,]

# plot all four algorithms
png("/Users/mo/Documents/Uni/Duke/ComputationSoc/PS398-HW1/HW3/runtimeplot.png")
plot <- ggplot(RT,aes(x=length, y = runtime, col=as.factor(algorithm)))
plot <- plot + geom_line() + facet_grid(type ~. ) + theme_bw()
plot <- plot + scale_colour_manual(values=c(3,4,5,6),name= "Algorithm")
plot <- plot + opts(title ="Runtimes for different sorting algorithms")
plot
dev.off()

# plot all quick sort algorithms
png("/Users/mo/Documents/Uni/Duke/ComputationSoc/PS398-HW1/HW3/runtimeplotQS.png")
RTqs <- RT[RT$algorithm == "Quick Sort" | RT$algorithm == "Quick Sort (RP)",] 
plot2 <- ggplot(RTqs,aes(x=length, y = runtime, col=as.factor(algorithm)))
plot2 <- plot2 + geom_line() + facet_grid(type ~. ) + theme_bw()
plot2 <- plot2 + scale_colour_manual(values=c(5,6),name= "Algorithm")
plot2 <- plot2 + opts(title ="Runtimes for Quick Sort algorithms")
plot2
dev.off()
