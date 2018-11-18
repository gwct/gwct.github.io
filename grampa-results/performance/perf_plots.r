
numproc = c(1,2,3,4,5)

yeast_cpu = c(57269.87,31339.67,21002.64,16772.11,17385.11)
wheat_cpu = c(104342.00,55032.03,36456.12,28420.54,22926.35)

ymax=max(c(wheat_cpu,yeast_cpu))
ymin=min(c(wheat_cpu,yeast_cpu))

#png("C:/Users/Gregg/Desktop/real_cpu.png", height=400, width=500)
plot(numproc,wheat_cpu,pch=16,type="b", cex=1.5, ylim=c(ymin,ymax),xlab="# of processes", ylab="Run time (sec)", cex.lab=1.5, cex.axis=1.2)
points(numproc,yeast_cpu,pch=21, type="b", cex=1.5)
legend(4,105000,c("Wheat", "Yeast"),pch=c(16,21), cex=1.5, bty="n")
#dev.off()
#stop()
##############################

wheat_ram = c(269,1150,1501,1852,2210)
yeast_ram = c(184,1034,1317,1517,1733)

ymax=max(c(wheat_ram,yeast_ram))
ymin=min(c(wheat_ram,yeast_ram))

#png("C:/Users/Gregg/Desktop/real_ram.png", height=400, width=500)
plot(numproc,wheat_ram,pch=16,type="b", cex=1.5, ylim=c(ymin,ymax),xlab="# of processes", ylab="Max memory usage (MB)", cex.lab=1.5, cex.axis=1.2)
points(numproc,yeast_ram,pch=21, type="b", cex=1.5)
legend(1,2300,c("Wheat", "Yeast"),pch=c(16,21), cex=1.5, bty="n")
#dev.off()
stop()
##############################

numproc = c(1,2,3,4)

sim_cpu_mac = c(359.65,198.8,143.91,123.41)
sim_cpu_win = c(664.48,372.81,299.17,245.62)
sim_cpu_lin = c(570.59,306.76,219.45,166.03)

ymax=max(c(sim_cpu_mac,sim_cpu_win,sim_cpu_lin))
ymin=min(c(sim_cpu_mac,sim_cpu_win,sim_cpu_lin))

#png("C:/Users/Gregg/Desktop/sim_cpu.png", height=400, width=500)
plot(numproc,sim_cpu_mac, pch=16, type="b", cex=1.5, ylim=c(ymin,ymax),xlab="# of processes", ylab="Run time (sec)", cex.lab=1.5, cex.axis=1.2)
points(numproc,sim_cpu_win,pch=21, type="b", cex=1.5)
points(numproc,sim_cpu_lin,pch=4, type="b", cex=1.5)
legend(3,690,c("Mac","Windows","Linux"),pch=c(16,21,4), cex=1.5, bty="n")
#dev.off()
stop()
##############################

sim_ram_mac = c(43,169,229,285)
sim_ram_win = c(32,103,137,168)
sim_ram_lin = c(27,96,128,159)

ymax=max(c(sim_ram_mac,sim_ram_win,sim_ram_lin))
ymin=min(c(sim_ram_mac,sim_ram_win,sim_ram_lin))

png("C:/Users/Gregg/Desktop/sim_ram.png", height=400, width=500)
plot(numproc,sim_ram_mac, pch=16, type="b", cex=1.5, ylim=c(ymin,ymax),xlab="# of processes", ylab="Max memory usage (MB)", cex.lab=1.5, cex.axis=1.2)
points(numproc,sim_ram_win,pch=21, type="b", cex=1.5)
points(numproc,sim_ram_lin,pch=4, type="b", cex=1.5)
legend(1,290,c("Mac","Windows","Linux"),pch=c(16,21,4), cex=1.5, bty="n")
dev.off()

##############################