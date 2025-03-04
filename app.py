import os
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env file

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')

series_id_menu = {
    'Employment & Unemployment': ['National Employment, Hours, and Earnings', 
                                   'State and Area Employment, Hours, and Earnings', 
                                   'State and County Employment and Wages from Quarterly Census of Employment and Wages', 
                                   'Business Employment Dynamics', 
                                   'Local Area Unemployment Statistics', 
                                   'Job Openings and Labor Turnover Survey'],
    'Inflation & Prices': ['Average Price Data', 
                           'Consumer Price Index-All Urban Consumers (Current Series)', 
                           'Consumer Price Index-Urban Wage Earners and Clerical Workers (Current Series)', 
                           'Chained CPI-All Urban Consumers', 
                           'Producer Price Index Industry Data - Current Series', 
                           'Producer Price Index Commodity Data - Current Series'],
    'Spending & Time Use': ['American Time Use Survey', 'Consumer Expenditure Survey'],
    'Pay & Benefits': ['National Benefits (NB)', 'Compensation Index (CI)', 
                        'Compensation Measures (CM)', 'National Compensation (NW)'],
    'Work Stoppages': ['Work Stoppages Program'],
    'Productivity': ['Major Sector Productivity and Costs', 
                     'Major Sector Total Factor Productivity', 
                     'Industry Productivity'],
    'Workplace Injuries': ['Occupational injuries and illnesses: industry data (2014 forward)', 
                           'Census of Fatal Occupational Injuries (2023 forward)', 
                           'Biennial Nonfatal Case and Demographic numbers and rates: selected characteristics'],
    'Occupational Requirements': ['Occupational Requirements Survey'],
    'International': ['Import and Export Price Indexes']
}

@app.route('/')
def home():
    return render_template('index.html', series_id_menu=series_id_menu)

if __name__ == '__main__':
    app.run(debug=True)
