import csv
import json
from flask import Flask, request, jsonify

app = Flask(__name__)

# Function to filter CSV and convert to JSON
def filter_csv(file_path, filters):
    filtered_data = []
    
    # Read the CSV file and apply the filters
    with open(file_path, mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            # Apply filters from the request
            match = True
            for key, value in filters.items():
                if key in row and row[key] != value:
                    match = False
                    break
            
            # If the row matches all filters, add to the filtered data
            if match:
                filtered_data.append(row)
    
    return filtered_data

# API endpoint to filter CSV
@app.route('/filter_csv', methods=['POST'])
def filter_csv_endpoint():
    file = request.files.get('file')
    if not file:
        return jsonify({'error': 'No file provided'}), 400
    
    filters = request.json.get('filters', {})
    
    # Save the file temporarily to apply the filtering
    file_path = 'temp.csv'
    file.save(file_path)
    
    # Filter the CSV and return as JSON
    filtered_data = filter_csv(file_path, filters)
    
    return jsonify(filtered_data)

if __name__ == '__main__':
    app.run(debug=True)
