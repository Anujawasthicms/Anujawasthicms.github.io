from flask import Flask, request, jsonify, send_from_directory
import pandas as pd
import os
import time

app = Flask(__name__)

# Path to save the CSV file
CSV_FILE_PATH = 'user_responses.csv'


def save_to_csv(data):
    # Check if CSV file exists, create it if not
    if os.path.exists(CSV_FILE_PATH):
        df = pd.read_csv(CSV_FILE_PATH)
    else:
        # Create a new DataFrame with headers if CSV doesn't exist
        df = pd.DataFrame(columns=['User', 'Level', 'Total Score', 'Category Scores'])

    # Add new data to the DataFrame
    df = df.append(data, ignore_index=True)

    # Save the updated DataFrame back to CSV
    df.to_csv(CSV_FILE_PATH, index=False)


@app.route('/save-data', methods=['POST'])
def save_data():
    # Get the JSON data from the request
    data = request.get_json()
    user = data['user']
    level = data['level']
    total_score = data['totalScore']
    category_scores = ', '.join(map(str, data['categoryScores']))  # Join category scores into a string

    # Prepare data to be saved
    record = {
        'User': user,
        'Level': level,
        'Total Score': total_score,
        'Category Scores': category_scores
    }

    # Save data to CSV
    try:
        save_to_csv(record)
        return jsonify({'message': 'Data saved successfully!'}), 200
    except Exception as e:
        print(f'Error saving data: {e}')
        return jsonify({'message': 'Error saving data'}), 500


@app.route('/')
def serve_html():
    # Serve the HTML file to the browser
    return send_from_directory('public', 'index.html')


if __name__ == '__main__':
    app.run(debug=True, port=3000)