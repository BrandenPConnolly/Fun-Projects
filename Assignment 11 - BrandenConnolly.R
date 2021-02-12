food = scan("/Users/brandenconnolly/Documents/DS710/ds710fall2016assignment11/finefoods_OP.txt", 
              what= character(), sep = ",",skip = 1)

food.matrix = t( matrix(food, nr = 9) )

Total.Votes = as.numeric(food.matrix[,3])
Review.Length = as.numeric(food.matrix[,5])
Numberof.Marks = as.numeric(food.matrix[,6])
Helpful.Fraction = as.numeric(food.matrix[,7])

summary(food.matrix)

plot(Helpful.Fraction,main = ("Scatterplot of Helpful Fraction"))
boxplot(Helpful.Fraction,main = ("Boxplot of Helpful Fraction"))

Helpful.Reviews = ifelse(Helpful.Fraction > 0.5, TRUE, FALSE)

summary(Review.Length)
hist(Review.Length,main = ("Histogram of Review Length"))
boxplot(Review.Length,main = ("Boxplot of Review Length"))
mean(Review.Length)
median(Review.Length)

Review.Log <- log(Review.Length)
hist(Review.Log, main = ("Histogram of LOG Review Length"))
