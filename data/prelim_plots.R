setwd("~/PhD/2020-2021/Braley fellows/PHAC Wastewater project/Ottawa-COVID-Projection/Data/Observed data")
library(ggplot2)
library(tidyr)
library(gplots)
library(phenocamr)

obs.csv <- read.csv("OPH_Observed_COVID_Data.csv")
obs.df <- as.data.frame(obs.csv)

virus.csv <- read.csv("wastewater_virus.csv")
virus.df <- as.data.frame(virus.csv)
virus.df$sampleDate <- as.Date(virus.df$sampleDate) #convert to date format from string
n1.df <- virus.df%>% drop_na(covN1_nPMMoV_meanMnNr)

n1.df$index <- 1:nrow(n1.df)
n1.loess10 <- loess(covN1_nPMMoV_meanMnNr ~ index, data = n1.df, span = 0.10 )
n1.loess25 <- loess(covN1_nPMMoV_meanMnNr ~ index, data = n1.df, span = 0.25 )
n1.loess50 <- loess(covN1_nPMMoV_meanMnNr ~ index, data = n1.df, span = 0.50)
n1.predict10 <- predict(n1.loess10)
n1.predict25 <- predict(n1.loess25)
n1.predict50 <- predict(n1.loess50)


plot(n1.df$covN1_nPMMoV_meanMnNr, x=n1.df$sampleDate, type="l")
lines(n1.predict10, x=n1.df$sampleDate,col="blue")
lines(n1.predict50, x=n1.df$sampleDate,col="red")

plot(n1.df$covN1_nPMMoV_meanMnNr, x=n1.df$sampleDate, type="l")
lines(n1.predict10, x=n1.df$sampleDate,col="red")

plotLowess(covN1_nPMMoV_meanMnNr ~ sampleDate, data=n1.df)

#smoothed data in ggplot
ggplot(n1.df, aes(sampleDate, covN1_nPMMoV_meanMnNr))+
  geom_line(color='#4A6990FF', group=1, size = 2, alpha=.9)+
  theme_bw()+
  labs(x = '', subtitle = "Regional Viral Load Per Population", y = 'Population Normalized Viral Load all WWTPs')

ggplot(n1.df, aes(sampleDate, covN1_nPMMoV_meanMnNr))+
  geom_point(color='#4A6990FF')+
  geom_line(aes(y=n1.predict25), size=2, alpha=0.5, color="orange")+
  theme_bw()+
  labs(x = '', subtitle = "Regional Viral Load Per Population", y = 'Population Normalized Viral Load all WWTPs')

#determining optimum value for span
optimal_span(n1.df$covN1_nPMMoV_meanMnNr) #returns value of 0.13
n1.loess13 <- loess(covN1_nPMMoV_meanMnNr ~ index, data = n1.df, span = 0.13 )
n1.predict13 <- predict(n1.loess13)

ggplot(n1.df, aes(sampleDate, covN1_nPMMoV_meanMnNr))+
  geom_point(color='#4A6990FF')+
  geom_line(aes(y=n1.predict25), size=2, alpha=0.5, color="orange")+
  theme_bw()+
  labs(x = '', subtitle = "Regional Viral Load Per Population", y = 'Population Normalized Viral Load all WWTPs')

#adding clinical data into the dataframe
obs.df$date <- as.Date(obs.df$date)
n1.obs <- merge(n1.df, obs.df, by.x = "sampleDate", by.y = "date", all.x = TRUE)

ggplot(n1.obs, aes(x=sampleDate))+
  geom_point(aes(y=covN1_nPMMoV_meanMnNr, color="Normalized N1 copies"))+
  geom_line(aes(y=observed_new_cases/100000, color="New cases"))+
  geom_line(aes(y=n1.predict25, color="LOESS"), size=2, alpha=1)+
  scale_y_continuous(name="Normalized N1 copies", sec.axis = sec_axis(~ 100000*., name="Number of new infections"))+
    theme_bw()+
  theme(legend.title = element_blank())+
  theme(axis.title.x = element_blank())+
  theme(axis.title = element_text(size = 17, face="bold", colour = "black"))+
  theme(axis.text = element_text(size = 12, face="bold", colour = "black"))+
  theme(legend.text = element_text(size=12))

ggsave("Ottawa_N1.png",height=20,width=35)

#repeat for N2
n2.df <- virus.df%>% drop_na(covN2_nPMMoV_meanMnNr)
n2.df$index <- 1:nrow(n2.df)
optimal_span(n2.df$covN2_nPMMoV_meanMnNr) #returns value of 0.13

n2.loess13 <- loess(covN2_nPMMoV_meanMnNr ~ index, data = n2.df, span = 0.13 )
n2.predict13 <- predict(n2.loess13)

n2.obs <- merge(n2.df, obs.df, by.x = "sampleDate", by.y = "date", all.x = TRUE)

ggplot(n2.obs, aes(x=sampleDate))+
  geom_point(aes(y=covN2_nPMMoV_meanMnNr, color="Normalized N2 copies"), size=2)+
  geom_line(aes(y=observed_new_ICU_p_acute_care/10000, color="New cases"), size=1)+
  geom_line(aes(y=n2.predict13, color="LOESS"), size=2, alpha=1)+
  scale_y_continuous(name="Normalized N2 copies", sec.axis = sec_axis(~ 10000*., name="New ICU cases"))+
  theme_bw()+
  theme(legend.title = element_blank())+
  theme(axis.title = element_text(size = 17, face="bold", colour = "black"))+
  theme(axis.text = element_text(size = 12, face="bold", colour = "black"))+
  theme(legend.text = element_text(size=12))

ggsave("Ottawa_N2_latermonths.png",height=20,width=35)

