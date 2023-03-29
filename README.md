# Parking Lot System
A really simple use case for an automated ticketing system using Python3.


## :white_check_mark: Requirements
- [x] [Python3](https://www.python.org/downloads/)
- [x] [Git](https://github.com/git-guides/install-git)


## :pushpin: How to start
1. Clone the python code from this repository
   ```
   git clone git@github.com:fa-fajrin/DKatalis-parking-lot.git
   ```
2. Go to the `DKatalis-parking-lot` directory
   ```
   cd DKatalis-parking-lot
   ```

## :rocket: Commands
* `create [size]` - Creates parking lot of size n
* `park [car-number]` - Parks a car
* `leave [car-number] [hours]` -> Removes (unpark) a car
* `status` -> Prints status of the parking lot


## :bulb: Example
You can create your own list of commands and put it in a file. It makes you able to run the code followed by the file name
```
python3 parking-lot.py your_filename
```

For example, I've provided a list of commands in the commands.txt file. You can try it on your local machine by running:
```
python3 parking-lot.py example-1.txt
```
