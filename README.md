# Peach Shield: First Spring Spray Strategy

Peach leaf curl - one of the fungal diseases that can affects negatively peach trees and endanger the forthcoming harvest. Early spring spraying is the only effective way how to protect the tree. Based on an article from (https://www.pasti.cz/blog/kaderavost-broskvoni/) I decided to create a simple python script that will help me to make easier to decide when to apply first spring spray. 

According the article mentioned above the strategy is this: When the cumulative hours of temperatures above 7°C (calculated from 1 January) hits 100 in a given year, then it signals the moment for the spray treatment. 

The current solution is not probably perfect, but it works. The scripts needs to run on an hourly basis to get data from open-meteo API and count the hours.  Additionally, it would be nice to implement some notification (sms?) when the cumulative target of 100 hours is reached.  
