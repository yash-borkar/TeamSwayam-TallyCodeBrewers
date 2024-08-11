from flask import Flask, render_template, request, jsonify
import docker
import os
import uuid
import json
import time

app = Flask(__name__)
client = docker.from_env()

# Load problems from a JSON file
def load_problems():
    if os.path.exists('problems/problems.json'):
        with open('problems/problems.json', 'r') as f:
            return json.load(f)
    return []

# Save problems to a JSON file
def save_problems(problems):
    with open('problems/problems.json', 'w') as f:
        json.dump(problems, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/playground')
def playground():
    return render_template('playground.html')

@app.route('/battleground')
def battleground():
    return render_template('battleground.html')

@app.route('/run', methods=['POST'])
def run_code():
    language = request.form['language']
    code = request.form['code']
    input_data = request.form.get('input', '')

    filename = f"{uuid.uuid4()}.{language}"
    filepath = f"/app/code/{filename}"

    with open(filepath, 'w') as f:
        f.write(code)

    start_time = time.time()

    if language == 'cpp':
        container = client.containers.get('online-ide-cpp-1')
        cmd = ["/bin/sh", "-c", f"g++ /code/{filename} -o /code/prog && /code/prog"]
    elif language == 'java':
        container = client.containers.get('online-ide-java-1')
        class_name = "Main"
        cmd = ["/bin/sh", "-c", f"javac /code/{filename} && java -cp /code {class_name}"]
    elif language == 'c':
        container = client.containers.get('online-ide-c-1')
        cmd = ["/bin/sh", "-c", f"gcc /code/{filename} -o /code/prog && /code/prog"]
    elif language == 'py':
        container = client.containers.get('online-ide-python-1')
        cmd = ["/bin/sh", "-c", f"python3 /code/{filename}"]
    else:
        return jsonify({'output': 'Unsupported language'})

    exit_code, output = container.exec_run(cmd, demux=True)

    end_time = time.time()
    execution_time = end_time - start_time

    # Get memory usage (simplified version)
    stats = container.stats(stream=False)
    memory_usage = stats['memory_stats']['usage'] / (1024 * 1024)  # Convert to MB

    os.remove(filepath)

    return jsonify({
        'output': output[0].decode() if output[0] else '',
        'error': output[1].decode() if output[1] else '',
        'execution_time': f"{execution_time:.2f} seconds",
        'memory_usage': f"{memory_usage:.2f} MB"
    })

@app.route('/submit_problem', methods=['POST'])
def submit_problem():
    try:
        problem = request.json
        problems = load_problems()
        problems.append(problem)
        save_problems(problems)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400

@app.route('/create_contest', methods=['POST'])
def create_contest():
    contest = request.json
    # In a real application, you'd save this to a database
    # For now, we'll just return success
    return jsonify({'success': True})

@app.route('/arena')
def arena():
    problems = load_problems()
    return render_template('arena.html', problems=problems)

@app.route('/problem/<int:problem_id>')
def problem_detail(problem_id):
    problems = load_problems()
    if 0 <= problem_id < len(problems):
        return render_template('problem_detail.html', problem=problems[problem_id], problem_id=problem_id)
    return "Problem not found", 404

@app.route('/submit_solution/<int:problem_id>', methods=['POST'])
def submit_solution(problem_id):
    problems = load_problems()
    if problem_id >= len(problems):
        return jsonify({'success': False, 'message': 'Problem not found'})

    problem = problems[problem_id]
    language = request.form['language']
    code = request.form['code']

    # Run the code against test cases
    all_passed = True
    results = []
    for i, test_case in enumerate(problem['testcases']):
        result = run_code(language, code, test_case['input'])
        expected_output = test_case['output'].strip()
        actual_output = result['output'].strip()
        passed = expected_output == actual_output
        all_passed = all_passed and passed
        results.append({
            'test_case': i + 1,
            'passed': passed,
            'input': test_case['input'],
            'expected_output': expected_output,
            'actual_output': actual_output,
            'execution_time': result['execution_time'],
            'memory_usage': result['memory_usage']
        })

    # Save submission
    submissions = load_submissions()
    submission = {
        'problem_id': problem_id,
        'language': language,
        'code': code,
        'timestamp': time.time(),
        'passed_all': all_passed,
        'results': results
    }
    submissions.append(submission)
    save_submissions(submissions)

    return jsonify({
        'success': True,
        'passed_all': all_passed,
        'results': results
    })

@app.route('/submissions/<int:problem_id>')
def problem_submissions(problem_id):
    submissions = load_submissions()
    problem_submissions = [s for s in submissions if s['problem_id'] == problem_id]
    return render_template('submissions.html', submissions=problem_submissions, problem_id=problem_id)

def run_code(language, code, input_data):
    filename = f"{uuid.uuid4()}.{language}"
    filepath = f"/app/code/{filename}"

    with open(filepath, 'w') as f:
        f.write(code)

    start_time = time.time()

    if language == 'cpp':
        container = client.containers.get('online-ide-cpp-1')
        cmd = ["/bin/sh", "-c", f"g++ /code/{filename} -o /code/prog && /code/prog"]
    elif language == 'java':
        container = client.containers.get('online-ide-java-1')
        class_name = "Main"
        cmd = ["/bin/sh", "-c", f"javac /code/{filename} && java -cp /code {class_name}"]
    elif language == 'c':
        container = client.containers.get('online-ide-c-1')
        cmd = ["/bin/sh", "-c", f"gcc /code/{filename} -o /code/prog && /code/prog"]
    elif language == 'py':
        container = client.containers.get('online-ide-python-1')
        cmd = ["/bin/sh", "-c", f"python3 /code/{filename}"]
    else:
        return {'output': 'Unsupported language', 'error': 'Unsupported language'}

    exit_code, output = container.exec_run(cmd, demux=True)

    end_time = time.time()
    execution_time = end_time - start_time

    stats = container.stats(stream=False)
    memory_usage = stats['memory_stats']['usage'] / (1024 * 1024)  # Convert to MB

    os.remove(filepath)

    return {
        'output': output[0].decode() if output[0] else '',
        'error': output[1].decode() if output[1] else '',
        'execution_time': f"{execution_time:.2f} seconds",
        'memory_usage': f"{memory_usage:.2f} MB"
    }

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
