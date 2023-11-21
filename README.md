<b># SQLAlchemy-Challenge<br>
Module 10 Homework Challenge <br></b><br>

Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

<br>

<b>Part 1: Analyze and Explore the Climate Data</b><br>

*In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:<br><br>

1. Note that you’ll use the provided files (climate_starter.ipynb) and (hawaii.sqlite) to complete your climate analysis and data exploration. <br>
2. Use the SQLAlchemy create_engine() function to connect to your SQLite database <br>
3. Use the SQLAlchemy automap_base() function to reflect your tables into classes, and then save references to the classes named (station) and (measurement). <br>
4. Link Python to the database by creating a SQLAlchemy session. <br>
  <b> *IMPORTANT: Remember to close your session at the end of your notebook* </b><br>
5. Perform a precipitation analysis and then a station analysis by completing the steps in the following two subsections.<br>

<b>PERCIPITATION ANALYSIS</b><br>
1. Find the most recent date in the dataset. <br>
2. Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of data. <br>
    <b>*HINT: Don't pass the date as a variable to your query*</b><br>
3. Select only the "date" and "prcp" values. <br>
4. Load the query results into a Pandas DataFrame. Explicitly set the column names.<br>
5. Sort the DataFrame values by "date". <br>
6. Plot the results by using the DataFrame [plot] method, as the following image shows <br> :https://static.bc-edx.com/data/dl-1-2/m10/lms/img/precipitation.jpg <br>
7. Use Pandas to print the summary statistics for the precipitation data. <br>

<b>STATION ANALYSIS </b><br> 
1. Design a query to calculate the total number of stations in the dataset. <br>
2. Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps: <br>
    <tab> 2a. List the stations and observation counts in descending order. <br>
    <b>*HINT: You’ll need to use the [func.count] function in your query*</b><br>
    <tab> 2b. Answer the following question: which station id has the greatest number of observations? <br>
3. Design a query that calculates the lowest, highest, and average temperatures that filters on the most-active station id found in the previous query. <br>
    <tab><b>*HINT: You’ll need to use functions such as [func.min], [func.max], and [func.avg] in your query.*</b><br>
4. Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:<br>
    <tab>4a. Filter by the station that has the greatest number of observations. <br>
    <tab>4b. Query the previous 12 months of TOBS data for that station. <br>
    <tab>4c. Plot the results as a histogram with [bins=12], as the following image shows: <br> https://static.bc-edx.com/data/dl-1-2/m10/lms/img/station-histogram.jpg <br>
5. Close your session.


    
<b>Part 2: Design Your Climate App</b><br>
Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. To do so, use Flask to create your routes as follows:<br>
1. [ / ] <br>
    <tab> 1a. Start at the homepage. <br>
    <tab> 1b. List all the available routes. <br>
2. [ /api/v1.0/precipitation ] <br>
    <tab> 2a. Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary using [date] as the key and [prcp] as the value. <br>
    <tab> 2b. Return the JSON representation of your dictionary. <br>
3.  [ /api/v1.0/stations ] <br>
    <tab> 3a. Return a JSON list of stations from the dataset. <br>
4.  [ /api/v1.0/tobs ] <br>
    <tab> 4a. Query the dates and temperature observations of the most-active station for the previous year of data. <br>
    <tab> 4b. Return a JSON list of temperature observations for the previous year. <br>
5.  [ /api/v1.0/<start> ] and  [ /api/v1.0/<start>/<end> ] <br>
   <tab> 5a. Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range. <br>
   <tab> 5b. For a specified start, calculate [TMIN], [TAVG], and [TMAX] for all the dates greater than or equal to the start date. <br>
   <tab> 5c. For a specified start date and end date, calculate [TMIN], [TAVG], and [TMAX] for the dates from the start date to the end date, inclusive. <br>
   <b>*HINTS:Join the station and measurement tables for some of the queries.*</b><br>
   <b>*HINTS:Use the Flask [jsonify] function to convert your API data to a valid JSON response object.*</b><br>

<br><br><br>


<b><head>Requirements</b><br><br>
Jupyter Notebook Database Connection <b>(10 points)</b></head><br>

To receive all points, you must: <br>

*Use the SQLAlchemy [create_engine()] function to connect to your SQLite database <b>(1 point)</b> <br>

*Use the SQLAlchemy [automap_base()] function to reflect your tables into classes <b>(3 points)</b><br>

*Save references to the classes named [station] and [measurement] <b>(4 points)</b><br>

*Link Python to the database by creating a SQLAlchemy session <b>(1 point)</b><br>

*Close your session at the end of your notebook <b>(1 point)</b>

<br><br>


<head><b> Precipitation Analysis (16 points) </head></b><br>
  
To receive all points, you must: <br>
  
*Create a query that finds the most recent date in the dataset (8/23/2017) <b>(2 points) </b><br>

*Create a query that collects only the [date] and [precipitation] for the last year of data without passing the date as a variable <b>(4 points) </b><br>

*Save the query results to a Pandas DataFrame to create [date] and [precipitation] columns <b>(2 points) </b><br>

*Sort the DataFrame by [date] <b>(2 points) </b><br>

*Plot the results by using the DataFrame [plot] method with [date] as the x and [precipitation] as the y variables <b>(4 points) </b><br>

*Use Pandas to print the summary statistics for the precipitation data <b>(2 points) </b>

<br><br>

<head><b> Station Analysis (16 points) </b></head><br>
To receive all points, you must:<br>

*Design a query that correctly finds the number of stations in the dataset (9) <b>(2 points) </b><br>

*Design a query that correctly lists the stations and observation counts in descending order and finds the most active station (USC00519281) <b>(2 points)  </b><br>

*Design a query that correctly finds the min, max, and average temperatures for the most active station (USC00519281) <b> (3 points) </b><br>

*Design a query to get the previous 12 months of temperature observation (TOBS) data that filters by the station that has the greatest number of observations <b>(3 points)  </b><br>

*Save the query results to a Pandas DataFrame <b>(2 points) </b><br>

*Correctly plot a histogram with bins=12 for the last year of data using tobs as the column to count. <b>(4 points)  </b>

<br><br>


<head><b>API SQLite Connection & Landing Page (10 points)</b><head>
To receive all points, your Flask application must:<br>
  
*Correctly generate the engine to the correct sqlite file <b>(2 points)  </b><br>

*Use [automap_base()] and reflect the database schema  <b> (2 points) </b><br>

*Correctly save references to the tables in the sqlite file ([measurement] and [station]) <b>(2 points) </b><br>

*Correctly create and binds the session between the python app and database <b>(2 points) </b><br>

*Display the available routes on the landing page <b>(2 points) </b><br><br>

<head><b>API Static Routes (15 points)</b></head><br>
<b>To receive all points, your Flask application must include:<b><br>

*A <b>precipitation route</b> that:<br>
    <tab>•Returns json with the date as the key and the value as the precipitation <b>(3 points)</b><br>
    <tab>•Only returns the jsonified precipitation data for the last year in the database <b>(3 points)</b><br>

*A <b>stations route<b> that: <br>
    <tab>•Returns jsonified data of all of the stations in the database <b>(3 points)</b><br>

*A <b>tobs route</b> that: <br>
    <tab>•Returns jsonified data for the most active station (USC00519281) <b>(3 points)</b><br>
    <tab>•Only returns the jsonified data for the last year of data <b>(3 points)</b><br><br>

<head><b>API Dynamic Route (15 points)</b></head><br>
<b>To receive all points, your Flask application must include:<br></b>

*A <b>start route</b> that: <br>
    <tab>•Accepts the start date as a parameter from the URL <b>(2 points)</b><br>
    <tab>•Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset <b>(4 points)</b><br>

*A <b>start/end route</b> that:<br>
    <tab>•Accepts the start and end dates as parameters from the URL <b>(3 points)</b><br>
    <tab>•Returns the min, max, and average temperatures calculated from the given start date to the given end date <b>(6 points)</b><br><br>

<head><b>Coding Conventions and Formatting (8 points)</b></head>
<b>To receive all points, your code must:</b>
*Place imports at the top of the file, just after any module comments and docstrings, and before module globals and constants. <b>(2 points)</b><br>
*Name functions and variables with lowercase characters, with words separated by underscores. <b>(2 points)</b><br>
*Follow DRY (Don't Repeat Yourself) principles, creating maintainable and reusable code. <b>(2 points)</b><br>
*Use concise logic and creative engineering where possible. <b>(2 points)</b><br><br>

<head><b>Deployment and Submission (6 points)</head><br>
To receive all points, you must:</b> <br>
  
*Submit a link to a GitHub repository that’s cloned to your local machine and contains your files. <b>(2 points)</b> <br>
*Use the command line to add your files to the repository. <b>(2 points)</b> <br>
*Include appropriate commit messages in your files. <b>(2 points)</b> <br><br>

<head><b>Comments (4 points)</head>
To receive all points, your code must</b> <br>
  
*Be well commented with concise, relevant notes that other developers can understand. <b>(4 points)</b> <br>





