############################################################
# UVU Genomics teaching demo, 01.2021
############################################################

this.dir <- dirname(parent.frame(2)$ofile)
setwd(this.dir)

library(ggplot2)

############################################################

in_data = read.table("fastq-count.txt", sep="\t", header=T)
# Read the data

qual_dist = ggplot(in_data, aes(x=Phred.score, y=Number.of.bases.with.score)) +
  geom_bar(stat="identity", fill=corecol(numcol=1)) +
  scale_y_continuous(expand=c(0,0)) +
  xlab("Phred score") +
  ylab("# bases") +
  bartheme()
# Plot and style the figure

print(qual_dist)
# Render the figure