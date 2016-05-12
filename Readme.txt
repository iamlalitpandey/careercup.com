This archive contains the below files -

1) CareercupScrape.py - This is the code to scrape the questions from Careercup.com website.Once you run this code dataset.txt file will be generated which contains the set of questions. Note : we have taken 50 sample questions for further tests.

2) CareercupLDA.py - This is the Latent Dirichlet allocation algorithms which will segragate the set of documents(questions) into the number of specified topics.This code will use the dataset.txt as the input file. Each documents in the dataset.txt file will be cleaned and clean_text.txt file will be generated. (Cleaning involves removing non alpha-numeric characters,digits,punctuations,extra spaces). Now the LDA algorithm will be applied to clean_text.txt file. This will generate the top_terms_per_topic.txt and topic_mixture_per_doc.txt.

3) CareercupKmeans.py - This is the code for K-means clustering algorithm (applied on every topics resulted from LDA) which will cluster the most similar questions in every topics in to specified number of k clusters.This will use clean_file.txt & topic_mixture_per_doc.txt file as input and cluster the questions into k clusters.

Test Case -I (Using Results file)
To verify the clustering results we have created the Results.txt files manually which contains the similarity ratings (1- not similar,5 - similar) for every question in dataset.txt file. Since we have 50 questions in the dataset.txt Number of comparisions will be 50x50.For each comparisions we will verify the algorithms results with the Result.txt file to analyse accuracy of the algorithm. Using this result we are visualizing the algorithms accuracy.

Test Case -II (Without Results file on small dataset)
Dataset_small.txt file is used as sample dataset to Test the Visualization code.Rename it to dataset.txt and then run LDA again to test the on the flow Visualization results.

Please make sure the chromedriver.exe is available in the project location.Please write to lalitatg@gmail.com for any errors/comments.
