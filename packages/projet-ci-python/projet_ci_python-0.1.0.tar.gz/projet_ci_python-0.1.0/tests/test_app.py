import pytest
from app import app, add_expense, get_expenses
import os
import json

DATA_FILE = "expenses.json"

@pytest.fixture
def client():
    app.config['TESTING'] = True
    client = app.test_client()
    
    # Clear expenses before each test
    if os.path.exists(DATA_FILE):
        os.remove(DATA_FILE)
    with open(DATA_FILE, "w") as file:
        json.dump([], file)
    
    yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 302  # Redirect to login if not logged in

def test_login_route(client):
    response = client.get('/login')
    assert response.status_code == 200  # Access to login page

def test_add_expense_route(client):
    client.post('/login', data=dict(username='testuser'))
    response = client.post('/add_expense', data=dict(
        amount=100,
        category='Food',
        description='Lunch',
        date='2022-04-27'
    ), follow_redirects=True)
    assert response.status_code == 200  # Redirect to index after adding expense
    expenses = get_expenses()
    assert len(expenses) == 1  # Ensure the expense is added

def test_logout_route(client):
    client.post('/login', data=dict(username='testuser'))
    response = client.get('/logout')
    assert response.status_code == 302  # Redirect to login after logout

def test_add_expense():
    add_expense(100, 'Food', 'Lunch', '2022-04-27')
    expenses = get_expenses()
    assert len(expenses) == 1  # Verify that an expense was added

def test_get_expenses():
    expenses = get_expenses()
    assert isinstance(expenses, list)  # Verify that get_expenses returns a list

# Create custom CSS
custom_css = """
body {
    font-family: Arial, sans-serif;
    margin: 20px;
}

h1 {
    font-size: 2em;
    color: #4CAF50;
}

h2 {
    font-size: 1.5em;
    color: #333;
}

table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
}

table, th, td {
    border: 1px solid #ddd;
    padding: 8px;
}

th {
    background-color: #4CAF50;
    color: white;
}

tr:nth-child(even) {
    background-color: #f2f2f2;
}

tr:hover {
    background-color: #ddd;
}

.pass {
    color: green;
}

.fail {
    color: red;
}

.error {
    color: orange;
}

.skip {
    color: blue;
}
"""

if __name__ == "__main__":
    import pytest
    # Run pytest and generate the HTML report
    pytest.main(["--html=reports/tests/report.html"])
    
    # Embed the custom CSS into the HTML report
    report_path = "reports/tests/report.html"
    with open(report_path, "r") as file:
        report_content = file.read()

    # Inject the custom CSS
    custom_css_tag = f"<style>{custom_css}</style></head>"
    report_content = report_content.replace("</head>", custom_css_tag)

    # Save the modified report
    with open(report_path, "w") as file:
        file.write(report_content)
