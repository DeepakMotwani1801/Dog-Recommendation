main.ipynb file contains all the code for the prohject 


The aim of the proposed model is to recommend suitable dog breed based on
used input about its height, weight, temperament etc.we have used a hybrid
model which uses collaborative filtering and content based filtering. There are mainly two functions in the program
5.1
Recommend popular dogs():-This function uses collaborative filtering to
recommend dogs on the basis of a popularity index.. In this approach, items are
recommended to users based on how popular they are among other users in the
system. The idea is that if an item is popular among many users, it is likely to be
a good recommendation for new users as well.To implement collaborative
filtering using a popularity index, we first need to calculate the popularity of
each item in the system it can be done by calculating the number of times it
occurs or on basis of star ratings but in our data a popularity index column was
already present in the dataset. One way to do this is to recommend the most popular items to all users, regardless of their individual preferences. This approach is called non- personalized collaborative filtering, as it does not take into account the
preferences of individual users but we have not followed this approach as it is
necessary to take into account the users needs so we have combined popularity
index with user-based collaborative filtering. We take different characteristics of dogs as input from the user on the basis of
three categories low,medium and high.for example a user wants low
shedding,low grooming frequency but high life expectancy and train ability the
function will provide specific results according to the input provided by the user. To make this possible we had to add new columns in our data set which
categorized the data according to the values for each column for example we had
a column named grooming frequency values and contained data ranging from 0- 1 so three new columns were created grooming frequency low,grooming
frequency medium and grooming frequency high these columns contained
boolean values so if the grooming frequency value for a dog lies between 0 and
0.4 the grooming frequency low column will have positive value whereas the
other two will have false similarly the range for high value was >=0.8 and for
medium it was between 0.4>= and =<0.8. School of Computer Engineering, KIIT, BBSR 7
DOG RECOMMENDATION SYSTEM
The Data Frame is then sorted by popularity, with the least popular dogs at the
top. The function then selects the top 10 rows of the filtered and sorted Data
Frame, or fewer if there are fewer than 10 rows.The function then prints the
recommended dogs to the console, with each dog's name and description. The
output_cols variable is used to determine which additional columns from the
Data Frame should be printed for each dog. 5.2
Recommend similar dogs():- The second function uses content based filtering
which recommends dogs on the basis of the users likes and dislikes this is taken
explicitly from the user. This function takes a breed as input, along with optional criteria such as group, low, medium, and high values, as well as columns to ignore and important
columns. It then uses these criteria to select similar dog breeds from a data set. The function first checks if the input criteria are strings, and if so, converts them
to a list. It then selects the relevant columns from the data set, excluding any
columns specified in the “ignore” list and adds a weight of 5 to columns
specified in the “important list”. If group, low, medium, or high criteria are
specified, the function selects rows that match the input criteria. Finally, it resets
the index of the selected rows. Next, the function calculates the similarity between the selected rows using a
combination of Euclidean distance and cosine similarity. It uses the "important"
list to give higher weight to certain columns when calculating the similarity. The function then selects the row corresponding to the input breed and sorts the
other rows in order of similarity to the input breed. It returns a list of the most
similar dog breeds, up to a maximum of 10, along with their descriptions and the
values of certain output columns. Finally, the function prints the selected breed and the list of similar breeds, along
with their descriptions and output column values.
