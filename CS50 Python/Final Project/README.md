    # Fuel Calculator for Simracing
    #### Description: A simple calculator that will allow you to calculate how many liters of fuel you need to complete your virtual race!
    Functions desriptions:
    - getSessionTime()
        Allows the user to input the race duration (hours, minutes, and seconds). Then it looks for any errors in user input. Such as TypeError or ValueError. Also of course the time
        has to be provided in valid extent. Minutes cannot go over 59, and so do seconds. If everything is fine the function converts the input time into total amount of seconds and returns it.

    - calculateRaceTime()
        Allows the user to input the anticipated lap time of the leader (minutes, seconds, and milliseconds). Like before, firstly it looks for errors. The time of course has to be in a valid
        extent. Minutes not over 59, so do seconds and millis can't go over 999. If the program catches some error user has the chance to go again! Finally, the function converts the input values into total seconds and returns the leader's lap time.

    - calculateLaps(sessionTime, raceTime)
        Calculates the total number of laps based on the session time and leader’s lap time. The race ends, when the leader crosses the line with timer at 0:00. So technically only leader's pace
        decides about the amount of laps for the race. Returns the number of laps.

    - calculateFuel(laps)
        Allows the user to input fuel consumption per lap and account for the formation lap. The fuel per lap data will be shown in the game after completing some laps. User can use that.
        Before some longer races there is also a formation lap. That is basically an extra lap before the start of the race, so we need to take that into consideration. Finally, it calculates the total amount of fuel needed for the entire race and rounds up to the nearest liter using ceil().

    -display(laps, fuel)
        Displays the final results of our program: the total number of laps and the amount of fuel required for the race.

    Tests desriptions:
        For each fuction there are some tests that will check, if our program is still working. For some of them there had to be simulated user input, because they require it to actually work.
