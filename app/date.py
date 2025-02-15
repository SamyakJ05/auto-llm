import datetime
from dateutil import parser

def count_days(input_file, output_file, target_day):
    # Initialize count of matching days
    count = 0
    
    # Read the input file containing the list of dates
    with open(input_file, 'r') as infile:
        dates = infile.readlines()

    # Loop through each line (date) in the file
    for date_str in dates:
        # Clean the date string and try to parse it into a datetime object
        date_str = date_str.strip()  # Remove any surrounding whitespaces/newlines
        try:
            # Use dateutil.parser to handle different date formats
            date_obj = parser.parse(date_str)
            
            # Check if the parsed date's day of the week matches the target day
            if date_obj.weekday() == target_day:
                count += 1
        except ValueError:
            # In case the date is invalid, print a message (optional)
            print(f"Skipping invalid date format: {date_str}")

    # Write the result to the output file
    with open(output_file, 'w') as outfile:
        outfile.write(f"Number of days matching day {target_day}: {count}\n")

# Example usage
input_file_path = "C:\\Users\\sjsam\\Downloads\\tds-p1\\data\\dates.txt"  # Path to the input file with dates
output_file_path = "C:\\Users\\sjsam\\Downloads\\tds-p1\\tds-p1\\app\\output_count.txt"  # Path to save the output count
target_day_of_week = 0  # For example, 0 for Sunday

count_days(input_file_path, output_file_path, target_day_of_week)

