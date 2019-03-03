############################################################
# For website convergence figure, 08.18
#
# Gregg Thomas
############################################################

library(ggplot2)
library(ggrepel)
this.dir <- dirname(parent.frame(2)$ofile)
setwd(this.dir)
cat("----------\n")

##########
# Formats the regression labels for ggplots geom_text()
# From: https://stackoverflow.com/questions/7549694/adding-regression-line-equation-and-r2-on-graph
lm_eqn <- function(df, y, x){
  formula = as.formula(sprintf('%s ~ %s', y, x))
  m <- lm(formula, data=df);
  # formating the values into a summary string to print out
  # ~ give some space, but equal size and comma need to be quoted
  eq <- substitute(#italic(target) == a + b %.% italic(input)*","~~
    italic(r)^2~"="~r2,#*","~~italic(p)~"="~pvalue, 
    list(target = y,
         input = x,
         a = format(as.vector(coef(m)[1]), digits = 2), 
         b = format(as.vector(coef(m)[2]), digits = 2), 
         r2 = format(summary(m)$r.squared, digits = 3),
         # getting the pvalue is painful
         pvalue = format(summary(m)$coefficients[2,'Pr(>|t|)'], digits=1)
    )
  )
  as.character(as.expression(eq));                 
}
##########

total_com = c(193262,95746,107004,127158,125852,111824,124553,141228,148834,159247,177903,176445,163967,175616,190806,56589,77901,77074,61287,75272,93205,89581,88468,73150,87006,104450,108758,94232,107588,124535,93313,106469,123234,91790,109150,121728)
com = c(12173,2237,3436,5392,5934,3523,5347,7001,3728,5772,9226,9920,5959,8863,12002,978,1776,1839,1187,1755,2151,2553,2902,1781,2478,3363,4722,2809,4006,5388,2964,4361,5925,2601,3570,5545)
total_con = c(197877,96736,108581,129249,127949,113248,126699,143837,150438,161755,181424,180262,166857,179436,194943,57544,78620,77920,61747,75962,94158,90622,89859,74004,88039,105944,109757,94937,108849,126436,96207,108206,125045,92541,110679,127130)
con = c(7558,1247,1859,3301,3837,2099,3201,4392,2124,3264,5705,6103,3069,5043,7865,23,1057,993,727,1065,1198,1512,1511,927,1445,1869,3723,2104,2745,3487,70,2624,4114,1850,2041,143)

total_con_sim = c(124600,54594,61004,74195,73695,61861,73279,81528,93432,99795,112768,112239,100580,111876,120037,29172,42386,41891,29967,41520,49883,48853,48357,36412,47987,56289,61551,49614,61174,69453,49427,60714,68999,48832,57151,68997)
con_sim = c(1316,181,299,470,486,311,515,638,355,520,909,954,604,930,1141,2,150,161,76,145,154,211,223,159,206,276,391,319,381,474,22,357,444,230,283,59)

micro_dol_con=2041
micro_dol_com = 3570
micro_dol_total=110679
micro_cow_con=4114
micro_cow_com=5925
micro_cow_total=125045

#par(mfcol=c(2,1))
#com_reg = lm(com ~ total_com)
#plot(total_com,com)
#abline(com_reg)
#legend("topleft",bty="n",legend=paste("R^2 = ", format(summary(com_reg)$adj.r.squared, digits=4)))
#points(109150,3570,col="blue",pch=16)
#abort

#png(filename="conv3.png")
par(mfcol=c(1,1),mar=c(5, 5, 2, 2) + 0.1,mgp=c(3.4,0.9,0))
com_con_reg = lm(con ~ com)

plot(com,con,xlab="Divergent substitutions",ylab="Convergent substitutions",cex.lab=2,cex=1.3,cex.axis=1.5,pch=20,bty='n')
abline(com_con_reg)

r2 = summary(com_con_reg)$adj.r.squared
leg = bquote(italic(R)^2 == .(format(r2, digits=4)))
legend("topleft",bty="n",legend=leg,cex=1.5)

points(3570,2041,col="black",pch=1,cex=2)
points(5925,4114,col="black",pch=1,cex=2)
text(3570+1750,2041-250,labels="Microbat-Dolphin")
text(5925-1000,4114+300,labels="Microbat-Cow")
#dev.off()

###########
# The same plot but in ggplot

in_data = data.frame("com"=com,"con"=con)
in_data$pair = NA
in_data = within(in_data, pair[com==3570 & con==2041] <- "Microbat-Dolphin")
in_data = within(in_data, pair[com==5925 & con==4114] <- "Microbat-Cow")

md = data.frame("pair"=c("Microbat-Dolphin"),
                      "com"=c(3570),
                      "con"=c(2041))

mc = data.frame("pair"=c("Microbat-Cow"),
                "com"=c(5925),
                "con"=c(4114))

con_p = ggplot(in_data, aes(com, con)) +
  geom_smooth(method="lm", se=F, color='black') +
  geom_point() +
  geom_text(data=data.frame(),
            aes(x=2500, y=7000, label=lm_eqn(in_data, 'com','con')),
            size=4, color='black', parse=T) +
  geom_point(data=int_data, aes(com, con), shape=1, size=5) +
  geom_text_repel(data=md, aes(label=pair), nudge_x=3000, nudge_y=-250) +
  geom_text_repel(data=mc, aes(label=pair), nudge_x=-1000, nudge_y=500) +
  xlab("Divergent sites") +
  ylab("Convergent sites") +
  theme_classic() +
  theme(axis.text=element_text(size=12), 
        axis.title=element_text(size=16), 
        axis.title.y=element_text(margin=margin(t=0,r=10,b=0,l=0),color="black"), 
        axis.title.x=element_text(margin=margin(t=10,r=0,b=0,l=0),color="black"),
        axis.line=element_line(colour='#595959',size=0.75),
        axis.ticks=element_line(colour="#595959",size = 1),
        axis.ticks.length=unit(0.2,"cm"),
        legend.title=element_text(size=14),
        legend.position="none",
        legend.text=element_text(size=12),
        plot.title=element_text(hjust=0.5, size=8, face="bold")
  )

print(con_p)

ggsave(file="conv4.png", con_p, width=4, height=4, units="in")
