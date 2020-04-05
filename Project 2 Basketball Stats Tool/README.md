# Number Guessing Game

## Summary
You will apply your knowledge of built-in Python data types and combine these types to create structures to store and organize a team of Basketball players into distributed teams. This tool will not only balance the teams by the total number of players but also let you generate some statistics for a given team.

## Project Instructions

**Create a new script**
The very first step you will want to do after opening the workspace or unzipping the `.zip` file into your project folder is to create a new and blank Python script named `app.py` or `application.py`. 

**Proper use of Dunder Main**
Make sure the script doesn't execute when imported; Anything that is calculation, callable function, or a block of logic that needs to run, ensure you put all of your logic and function calls inside of a dunder main block at the bottom of your file:
Dunder main statement looks like this:
`if __name__ == "__main__":`

> **HINT:** *Unit 1 project files/workspace had an example of this.*

> **NOTE**: This does not mean everything you write has to be contained within Dunder Main. You can still import and define functions outside of dunder main, you can still extract pieces of logic into those functions. The main calls to your program should be protected inside Dunder Main to prevent automatic execution if your script is imported. 

**Import player data**
Import from `constants.py` the players' data to be used within your program.

>**NOTE**: *Python has no concept of actual constants like other languages have. But it is a convention you may see in the real world. When you see ALL CAPS variable name you are meant to treat it as if it were a constant or value that you cannot change/alter.

**Clean the data**
Write the logic to read the exisiting player and team  data from the PLAYERS and TEAMS constants provided in `constants.py`. Build a new collection with what you have learned up to this point.

>*HINT*: Think Lists with nested Dictionaries might be one way.

>*NOTE*: *Ensure you do not directly modify the data in `PLAYERS` or `TEAMS` constants. This data you should iterate and read from to build your own collection and would be ideal to clean the data as you loop over it building your new collection.

**Balance on total players**
Balance the players across the three teams: *Panters*, *Bandits*, and *Warriors*. Make sure the teams have the same number of total players on them when your team balancing process has finished.

**Console readability matters**
When the menu or stats display to the console, it should display in a nice readable format. Use extra spaces or line breaks to break up lines if needed.

**Displaying the stats**
When displaying the selected team's stats to the screen you will want to include:
+ Team's name
+ Total players on that team
+ The player names separated by commas.

>**NOTE**: *When displaying the player names it should not just display the List representation object. It should display them as if they are on large comma separated string so the user cannot see any hints at what data type players are held inside.*


**An Example Run**
Here is an example of what the running application might look like in the console (the design of the menus and how things are displayed are totally up to you, though it should be readable and display the proper stats)
```BASKETBALL TEAM STATS TOOL

---- MENU----

 Here are your choices:
  1) Display Team Stats
  2) Quit

Enter an option > 1

1) Panthers
2) Bandits
3) Warriors

Enter an option > 1

Team: Panthers Stats
--------------------
Total players: 6

Players on Team:
  Karl Saygan, Chloe Alaska, Phillip Helm, Suzane Greenberg, Herschel Krustofski, Joe Smith

Press ENTER to continue...
```


