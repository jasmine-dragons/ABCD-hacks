
<a href="https://abcd-xdhacks.herokuapp.com/"><img src="https://i.imgur.com/0MBSEU5.png?1" title="source: imgur.com" style="width=100px;" /></a>
Click on the image to view the website


# Breast Cancer Detector

About 1 in 8 U.S. women (about 12%) will develop invasive breast cancer over the course of her lifetime. To ensure that everyone receives their deserved treatment, early detection is vital. Using machine learning, we have developed a program that detects whether a tumor is malignant or benign (given a certain set of characteristics). Both doctors and patients can use this application to improve their chances of detecting breast cancer.

*Note: to view the dataset that we used, click [here](https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Original%29).*

*Note: We used the Materialize.css file to style our pages. To obtain the css file, click [here](https://materializecss.com/).*

## Setup
Your machine will need numpy, scikit-learn, pandas, flask, pymongo, pymongo[srv], dns, json, and bson to run this code. To get any of these libraries, you can just `pip install [insert library here]` in a terminal window. To run the code, first pull the github to your computer and then navigate to the folder where app.py is. Then open terminal and run the command `flask run`. This will direct you to a localhost website where you can interact with the product.

### Detailed Instructions:
1. Open command prompt
2. Install numpy, scikit-learn, pandas, flask, pymongo, pymongo[srv], dns, json, and bson using `pip install [insert library here]`
3. Then download the github repo to your computer
4. Locate the repo in your file explorer
   -- Open command prompt from that folder's search bar by typing cmd into it
5. Then enter `flask run` in the command prompt
6. Copy the localhost link that is outputted and paste it into a web browser (example below)
![Imgur](https://i.imgur.com/glU8gAc.png)
7. You should be able to use the application now

### To use the detection feature:
Navigate to the "Detect" tab using the navigation bar on the website. Then insert values in the range (1-10) into each of the input fields. Click submit and you should see the prediction for the data you inputted. This prediction, as well as the data you input, are saved to the MongoDB database.

### To use the lookup feature:
Navigate to the "Lookup" tab using the navigation bar on the website. A doctor who had access to the database would be able to freely put in any of his patient's IDs. For demonstation purposes, use one of the following IDs: 5f2f13e8218e81e41faf62d2, 5f2f1e3d218e81e41faf62d4, 5f2f3a64755cd3292de46ebd. Click submit and you should see that the data for the patient as well as their prediction and confidence level are visible.

## How it works
Using machine learning, we have developed a program that detects whether a tumor is malignant or benign (given their symptoms or characteristics). To train our model, we used publicly available datasets for breast cancer patients. Using the machine learning algorithm, we implemented a web application where users can input 9 specific characteristics regarding the tumor. The algorithm then returns a breast cancer prediction and confidence value given the corresponding characteristics. 

We also utilized a MongoDB database for doctors to look up and store their patients' information securely allowing them to make informed decisions about their healthcare. Because new user inputs and results are continuously added to this database, the pool of resources and references provided for both doctors and patients alike will grow as more individuals use this application.

## The Site

### Homepage:
![homepage](https://i.imgur.com/o1ytDvz.png)

### Detection:
![detect](https://i.imgur.com/cQS2ZhK.png)

### Results:
![detectresults](https://i.imgur.com/f0RaOZJ.png)

### Patient Lookup:
![lookup](https://i.imgur.com/3Uzo1eL.png)

### Lookup Results:
![lookupresults](https://i.imgur.com/TLUdUYh.png)

## Future Improvements
First, we would like to increase the size of our dataset. Bringing access to a greater number of hospitals would give us increased amounts of data will give us more accurate results and would let us be much more confident in the diagnosis. Next, we would also want to increase the number of features in the dataset, giving us more variables to look at and input into the system. This would help take into account many of the other factors involved in the chances of breast cancer in people. 

## What We Used
- Python
- Flask
- Numpy
- Pandas
- Scikit-Learn
- MongoDB / Pymongo
- HTML/CSS
- DNS

## [Youtube Video](https://www.youtube.com/watch?v=m9t6jYTXXc8)

https://www.youtube.com/watch?v=m9t6jYTXXc8



## Resources

   CSS: https://materializecss.com/

   Dataset: https://archive.ics.uci.edu/ml/datasets/Breast+Cancer+Wisconsin+%28Original%29

   Citation Request:
   
   This breast cancer databases was obtained from the University of Wisconsin
   Hospitals, Madison from Dr. William H. Wolberg.  If you publish results
   when using this database, then please include this information in your
   acknowledgements.  Also, please cite one or more of:

   1. O. L. Mangasarian and W. H. Wolberg: "Cancer diagnosis via linear 
      programming", SIAM News, Volume 23, Number 5, September 1990, pp 1 & 18.

   2. William H. Wolberg and O.L. Mangasarian: "Multisurface method of 
      pattern separation for medical diagnosis applied to breast cytology", 
      Proceedings of the National Academy of Sciences, U.S.A., Volume 87, 
      December 1990, pp 9193-9196.

   3. O. L. Mangasarian, R. Setiono, and W.H. Wolberg: "Pattern recognition 
      via linear programming: Theory and application to medical diagnosis", 
      in: "Large-scale numerical optimization", Thomas F. Coleman and Yuying
      Li, editors, SIAM Publications, Philadelphia 1990, pp 22-30.

   4. K. P. Bennett & O. L. Mangasarian: "Robust linear programming 
      discrimination of two linearly inseparable sets", Optimization Methods
      and Software 1, 1992, 23-34 (Gordon & Breach Science Publishers).

1. Title: Wisconsin Breast Cancer Database (January 8, 1991)

2. Sources:
   -- Dr. WIlliam H. Wolberg (physician)
      University of Wisconsin Hospitals
      Madison, Wisconsin
      USA
   -- Donor: Olvi Mangasarian (mangasarian@cs.wisc.edu)
      Received by David W. Aha (aha@cs.jhu.edu)
   -- Date: 15 July 1992

3. Past Usage:

   Attributes 2 through 10 have been used to represent instances.
   Each instance has one of 2 possible classes: benign or malignant.

   1. Wolberg,~W.~H., \& Mangasarian,~O.~L. (1990). Multisurface method of 
      pattern separation for medical diagnosis applied to breast cytology. In
      {\it Proceedings of the National Academy of Sciences}, {\it 87},
      9193--9196.
      -- Size of data set: only 369 instances (at that point in time)
      -- Collected classification results: 1 trial only
      -- Two pairs of parallel hyperplanes were found to be consistent with
         50% of the data
         -- Accuracy on remaining 50% of dataset: 93.5%
      -- Three pairs of parallel hyperplanes were found to be consistent with
         67% of data
         -- Accuracy on remaining 33% of dataset: 95.9%

   2. Zhang,~J. (1992). Selecting typical instances in instance-based
      learning.  In {\it Proceedings of the Ninth International Machine
      Learning Conference} (pp. 470--479).  Aberdeen, Scotland: Morgan
      Kaufmann.
      -- Size of data set: only 369 instances (at that point in time)
      -- Applied 4 instance-based learning algorithms 
      -- Collected classification results averaged over 10 trials
      -- Best accuracy result: 
         -- 1-nearest neighbor: 93.7%
         -- trained on 200 instances, tested on the other 169
      -- Also of interest:
         -- Using only typical instances: 92.2% (storing only 23.1 instances)
         -- trained on 200 instances, tested on the other 169

4. Relevant Information:

   Samples arrive periodically as Dr. Wolberg reports his clinical cases.
   The database therefore reflects this chronological grouping of the data.
   This grouping information appears immediately below, having been removed
   from the data itself:

     Group 1: 367 instances (January 1989)\
     Group 2:  70 instances (October 1989)\
     Group 3:  31 instances (February 1990)\
     Group 4:  17 instances (April 1990)\
     Group 5:  48 instances (August 1990)\
     Group 6:  49 instances (Updated January 1991)\
     Group 7:  31 instances (June 1991)\
     Group 8:  86 instances (November 1991)\
     Total:   699 points (as of the donated datbase on 15 July 1992)

   Note that the results summarized above in Past Usage refer to a dataset
   of size 369, while Group 1 has only 367 instances.  This is because it
   originally contained 369 instances; 2 were removed.

5. Number of Instances: 699 (as of 15 July 1992)

6. Number of Attributes: 10 plus the class attribute

7. Attribute Information: (class attribute has been moved to last column)

     **Attributes**
   01. Sample code number            id number
   02. Clump Thickness  :            1 - 10
   03. Uniformity of Cell Size :     1 - 10
   04. Uniformity of Cell Shape :    1 - 10
   05. Marginal Adhesion :           1 - 10
   06. Single Epithelial Cell Size : 1 - 10
   07. Bare Nuclei :                 1 - 10
   08. Bland Chromatin :             1 - 10
   09. Normal Nucleoli :             1 - 10
   10. Mitoses :                     1 - 10
   11. Class :                       (2 for benign, 4 for malignant)

8. Missing attribute values: 16

   There are 16 instances in Groups 1 to 6 that contain a single missing 
   (i.e., unavailable) attribute value, now denoted by "?".  

9. Class distribution:
 
   Benign: 458 (65.5%)
   Malignant: 241 (34.5%)
   
   
   


