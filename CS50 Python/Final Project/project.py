#Project title: Fuel Calculator for simracing
#My name: Dawid Głód
#GitHub username: DawGlod
#Country - city: Poland - Cracow
#edX username: Dawid Głód
#Date: 05.12.2024

from math import ceil

def getSessionTime():
    while True:
        try:
            print("How long is the race?")
            hours = int(input("Hours: "))
            minutes = int(input("Minutes: "))
            seconds = int(input("Seconds: "))
            if hours >= 0 and 0 <= minutes < 60 and 0 <= seconds < 60:
                time = hours * 3600 + minutes * 60 + seconds
                return time
            else:
                raise ValueError("Invalid time values. Please enter valid hour, minute, and second values.")
        except (ValueError, TypeError) as e:
            print(f"Error: {e}. Try again!\n")

def calculateRaceTime():
    while True:
        try:
            print("What is the average lap time during the race?")
            minutes = int(input("Minutes: "))
            seconds = int(input("Seconds: "))
            milliseconds = int(input("Milliseconds: "))
            if 0 <= minutes < 60 and 0 <= seconds < 60 and 0 <= milliseconds < 999:
                raceTime = minutes * 60 + seconds + milliseconds * 0.001
                return raceTime
            else:
                raise ValueError("Invalid time values. Please enter valid minute, second, and millisecond values.")
        except (ValueError, TypeError) as e:
            print(f"Error: {e}. Try again!\n")

def calculateLaps(sessionTime, raceTime):
    laps = ceil(sessionTime / raceTime)
    return laps

def calculateFuel(laps):
    while True:
        try:
            print("What is your fuel consumption per lap?")
            fuelPerLap = float(input("Fuel per lap: "))
            if fuelPerLap <= 0:
                raise ValueError("Fuel consumption must be a positive number greater than zero.")

            print("Is there a formation lap?")
            formationLap = input("Y/N: ").lower()

            if formationLap == "y":
                return ceil(fuelPerLap * laps + fuelPerLap)
            elif formationLap == "n":
                return ceil(fuelPerLap * laps)
            else:
                raise ValueError("Invalid input. Please enter 'Y' for Yes or 'N' for No.")
        except (ValueError, TypeError) as e:
            print(f"Error: {e}. Try again!\n")

def display(laps, fuel):
    return f"\nRace will be {laps} laps. You need {fuel} liters!"

def main():
    try:
        sessionTime = getSessionTime()
        raceTime = calculateRaceTime()
        laps = calculateLaps(sessionTime, raceTime)
        fuel = calculateFuel(laps)
        print(display(laps, fuel))
    except KeyboardInterrupt:
        print("\n\nYou stopped the program!")

if __name__ == "__main__":
    main()
