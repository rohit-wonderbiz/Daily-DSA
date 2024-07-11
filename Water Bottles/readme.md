# Bottle Exchange Problem

This Python script calculates the total number of bottles that can be consumed given an initial number of bottles and the number of empty bottles required for an exchange. The concept is that after consuming the initial bottles, empty bottles can be exchanged for full ones, and this process continues until no more exchanges can be made.

## How It Works

1. The script prompts the user to enter the number of initial bottles and the number of empty bottles needed for an exchange.
2. It defines a function `water` to calculate the total number of bottles consumed.
3. Inside the function:
   - It initializes `result` to keep track of the total number of bottles consumed.
   - It initializes `full` with the initial number of bottles and `empty` to 0.
   - While there are full bottles:
     - It adds the number of full bottles to `result`.
     - It adds the number of full bottles to `empty`.
     - It calculates the number of new full bottles that can be obtained from the empty bottles.
     - It updates `full` with the new full bottles and adjusts `empty` accordingly.
4. The function returns the total number of bottles consumed.
5. The script prints the total number of bottles consumed.
