# Title     : Mark Chafin
# Objective : Testing R in Pycharm
# Created by: markchafin
# Created on: 4/18/21


knitr::opts_chunk$set(echo = TRUE)
rm(list = ls())
library(dplyr)
library(BatchGetSymbols)
library(caret)
library(ggplot2)
library(scales)
library(date)
library(DAAG)
library(mlbench)
library(tidyverse)
library(leaps)
library(glmnet)
library(GGally)
library(esquisse)



# set dates
first.date <- Sys.Date() - 120
last.date <- Sys.Date()
freq.data <- 'daily'
# set tickers
tickers <- c('doge-usd')

df <- as.data.frame(BatchGetSymbols(tickers = tickers,
                         first.date = first.date,
                         last.date = last.date,
                         freq.data = freq.data,
                         cache.folder = file.path(tempdir(),
                                                  'BGS_Cache') ), stringsAsFactors = TRUE) # cache in tempdir()

# remove variables
df <- subset(df, select = -c(df.control.src, df.control.download.status, df.control.perc.benchmark.dates, df.control.threshold.decision, df.control.total.obs, df.control.ticker))

df <- subset(df,select = -c(df.tickers.ret.adjusted.prices, df.tickers.ret.closing.prices))


# df$df.tickers.ref.date <- as.POSIXct(df$df.tickers.ref.date, format = "%Y-%m-%d")

# df$df.tickers.ref.date <- format.Date(df$df.tickers.ref.date)
df$df.tickers.ref.date <- c(1:121)



fitControl <- trainControl(method = "cv", number = 5)
set.seed(123)
scatter.smooth(x=df$df.tickers.ref.date, y=df$df.tickers.price.close, main= tickers)  # scatterplot

ggplot(df) +
  aes(
    x = df.tickers.ref.date,
    y = df.tickers.price.close,
    size = df.tickers.volume
  ) +
  geom_line(colour = "#112446") +
  theme_minimal()

# Create Training and Test data -
set.seed(123)  # setting seed to reproduce results of random sampling
trainingRowIndex <- sample(1:nrow(df), 0.8*nrow(df))  # row indices for training data
trainingData <- df[trainingRowIndex, ]  # model training data
testData  <- df[-trainingRowIndex, ]   # test data


lmMod <- lm(df.tickers.ref.date ~ df.tickers.price.close, data=trainingData)  # build the model
pricePred <- predict(lmMod, testData)  # predict distance


actuals_preds <- data.frame(cbind(actuals=testData$fd.tickers.price.close, predicteds=pricePred))  # make actuals_predicteds dataframe.

correlation_accuracy <- cor(actuals_preds)
head(actuals_preds)


CVResults <- CVlm(data = df, form.lm = df.tickers.price.close ~ df.tickers.ref.date, m = 500, dots = FALSE, seed = 123)
attr(CVResults, "ms")

