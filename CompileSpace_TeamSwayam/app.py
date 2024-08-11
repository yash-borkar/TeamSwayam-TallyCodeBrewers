from flask import Flask, render_template, request, redirect, url_for, jsonify, session
import subprocess
from problems import problems, add_problem
from user import users, update_user_stats, get_user_stats, get_leaderboard
from code_execution import execute_code
from c_problems import c_problems

app = Flask(__name__)
app.secret_key = 'supersecretkey'

@app.context_processor
def utility_processor():
    return dict(enumerate=enumerate)

# Home page route (Landing page)
@app.route('/')
def home():
    return render_template('home.html')

# Battleground
@app.route('/index')
def index():
    return render_template('index.html', c_problems=c_problems)

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    if username:
        session['username'] = username
        return redirect(url_for('index'))
    return redirect(url_for('index'))

@app.route('/dashboard')
def dashboard():
    if 'username' not in session:
        return redirect(url_for('index'))

    username = session['username']
    stats = get_user_stats(username)
    leaderboard = get_leaderboard()

    return render_template('dashboard.html', stats=stats, leaderboard=leaderboard)

@app.route('/problem/<int:problem_id>', methods=['GET', 'POST'])
def problem(problem_id):
    # Find the problem with the given ID
    problem = next((p for p in problems if p['id'] == problem_id), None)
    if not problem:
        return "Problem not found", 404

    result = None
    is_correct = None
    stats = None

    # Handle form submission
    if request.method == 'POST':
        code = request.form['code']
        language = request.form['language']
        input_data = request.form['input_data']

        # Execute the code and get the result
        result = execute_code(code, language, input_data)
        is_correct = check_output(problem, result)

        # Update user statistics if logged in
        if 'username' in session:
            username = session['username']
            update_user_stats(username, problem_id, is_correct)
            stats = get_user_stats(username)

    return render_template('problem.html', c_problems=problems, result=result, is_correct=is_correct, stats=stats)

@app.route('/problems')
def problem_list():
    return render_template('problem_list.html', problems=problems)

@app.route('/problem_detail/<int:problem_id>')
def problem_detail(problem_id):
    problem = next((p for p in problems if p['id'] == problem_id), None)
    if problem is None:
        return "Problem not found", 404
    return render_template('problem_detail.html', problem=problem)

@app.route('/add_problem', methods=['GET', 'POST'])
def add_problem_route():
    if request.method == 'POST':
        new_problem = {
            'title': request.form['title'],
            'description': request.form['description'],
            'test_cases': request.form['test_cases'].split('\n'),
            'expected_outputs': request.form['expected_outputs'].split('\n')
        }
        add_problem(new_problem)
        return redirect(url_for('problem_list'))
    return render_template('add_problem.html')

@app.route('/code_playground')
def code_playground():
    return render_template('code_playground.html')

@app.route('/execute_playground', methods=['POST'])
def execute_playground():
    code = request.json['code']
    language = request.json['language']
    input_data = request.json['input']

    output = execute_code(code, language, input_data)

    return jsonify({"output": output})

@app.route('/execute', methods=['POST'])
def execute():
    code = request.json['code']
    language = request.json['language']
    problem_id = request.json['problem_id']
    problem = next((p for p in problems if p['id'] == problem_id), None)
    if problem is None:
        return jsonify({"error": "Problem not found"}), 404

    results = []
    for test_case, expected_output in zip(problem['test_cases'], problem['expected_outputs']):
        output = execute_code(code, language, test_case)
        is_correct = output.strip() == expected_output.strip()
        results.append({
            "input": test_case,
            "expected_output": expected_output,
            "actual_output": output,
            "is_correct": is_correct
        })

    return jsonify(results)

def check_output(problem, result):
    expected_outputs = problem['expected_outputs']
    return result.strip() in expected_outputs

if __name__ == '__main__':
    app.run(debug=True)
