confidenceInterval <- function(x, confidenceLevel=0.95){
	N <- length(x)
	alpha <- 1-confidenceLevel
	if (N<30)
	   stat <- qt(1-alpha/2, N-1)
	else 
	   stat <- qnorm(1-alpha/2)
	interval <- stat * sd(x) / sqrt(N)
	mean_value <- mean(x)
	result <- c(mean_value-interval, mean_value+interval)
	names(result) <- c("lower", "upper")
	result
}

# function for plotting data
plotresult <- function(file, col, start = 1) {
   data <- read.csv(file)
   data <- data[start:nrow(data),]
   
   # optional for java JIT
   #data <- data[1:nrow(data),]
   plot(data[c("index", "time")], type = 'l', col="red", ylim=c(0,4e8))

   lines(data[c("index", "bub")], col="blue")

   legend('topright', legend = c('Default', 'Bubble sort'), col = c('red', 'blue'), lty = 1)
}

plot_results <- function(
    files, file_out, start = 1, 
    ylim = c(1e4, 1e9), 
    legend_pos = 'topright',
    main = "Performance Comparison") {

    cols <- list(
        list(name = "Python", col = "time", color = "red"),
        list(name = "Java", col = "time", color = "green"),
        list(name = "C", col = "time", color = "blue")
    )

    pdf(paste("plots/", file_out, ".pdf", sep=""))

    # Initialize plot
    plot(NULL, xlim = c(start, 1000), ylim = ylim, 
        xlab = "Index", ylab = "Time", main = main, log="y")
  
    # Process each file
    for (i in 1:length(files)) {
        file <- files[i]
        data <- read.csv(paste("results/", file, sep=""))
        data <- data[start:nrow(data), ]
        #print(data)

        #print(t.test(data$time))

        lines(data$index, data$time, col = cols[i][[1]]$color)
    }
  
    # Add legend
    legend_items <- sapply(cols, function(x) x$name)
    legend_colors <- sapply(cols, function(x) x$color)
    legend(legend_pos, legend = legend_items, col = legend_colors, lty = 1)
    dev.off()
}

ttest <- function(
    files, algos, start = 1
    ) {
    print("")

    # Process each file
    for (i in 1:length(files)) {
        file <- files[i]
        algo <- algos[i]
        data <- read.csv(paste("results/", file, sep=""))
        data <- data[start:nrow(data), ]
        #print(data)

        result <- t.test(data$time)

        p_value <- result$p.value
        t_statistic <- result$statistic
        confidence_interval <- result$conf.int
        degrees_freedom <- result$parameter
        estimate_means <- result$estimate
        null_value <- result$null.value
        alternative_hypothesis <- result$alternative
        method <- result$method

        print(paste("t-test for", algos[i]))
        print(paste("p-value:", p_value)) # why 0? Different answer when doing print(t.test())
        print(paste("95% confidence interval:", confidence_interval))
    }
}

files_matrix <- list("py_matrixmult.csv", "java_matrixmult.csv", "c_matrixmult.csv")
plot_results(files=files_matrix, file_out="matrix_multiplication", ylim=c(1e4, 5e9))

print("matrix mult:")
ttest(files_matrix, list("python", "java", "c"))

files_quick <- list("py_quicksort.csv", "java_quicksort.csv", "c_quicksort.csv")
plot_results(files=files_quick, file_out="quick_sort", ylim=c(1e4, 1e7))

print("quick sort:")
ttest(files_quick, list("python", "java", "c"))

files_merge <- list("py_mergesort.csv", "java_mergesort.csv", "c_mergesort.csv")
plot_results(files=files_merge, file_out="merge_sort", ylim=c(1e4, 1e8))

print("merge sort:")
ttest(files_merge, list("python", "java", "c"))

exit()