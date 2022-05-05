# How crew credits reflects technological changes in film industry: through the Star Wars saga

I have always been facinated by films end credits scenes, especially after Marvel Studio started putting extra credit scenes at the very end and force you to sit through all the credits. I like to see what departments were being involved, people's name, and what they do. Sometimes I think back to the old times, when movie credits were at the beginning of the movie and it takes like a minute, and now it takes at least 5 to go through all of them.

It is innovation and technology that creates more and more positions, and legislations and union laws that allow us to see more people's names listed as part of the crew. This project aims to discuss how the appearance of new crew credits reflects technological changes during the moviemaking process by looking at the full credits of the 9 Star Wars movies since 1977. Even though this is an ambitious project, I hope that this will be the start of the bigger thing I imagine it to be someday, a step at a time.

There are four code documents invovled in this project. This includes craping data from IMDB, cleaning data, and compare all the credits to get the differences. A big part of the data cleaning was done through OpenRefine after transforming the JSON file to CSV. 

## Instructions

all_episode.py is for scraping data using Beautiful Soup. All IMDB full credit URL contians a unqiue code for each movie, and all the code for this project were provided in the Python file. When dumping the data out to a JSON file in the end, change the file name to match each movie.

convert.py is for converting the JSON file to CSV. Make sure the input file name is being changed. 

The converted version of the file is very messay, and I used OpenRefine to clean and organized the file. The code for the operations was copied and provided. 

The pull_out and drop files are for the special edition credits for the first 3 movies in order to get the original crew credits when it was first created. Any Note column strings that contians the year 1997 or 2004 were saved to new files and dropped from the original file.

Intructions for difference.py were provided in the code. Make sure to compare the movies in the right sequence.
