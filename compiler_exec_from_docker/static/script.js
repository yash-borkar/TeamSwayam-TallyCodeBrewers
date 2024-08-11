function runCode() {
    const language = document.getElementById('language').value;
    const code = document.getElementById('code').value;
    const input = document.getElementById('input').value;
    const output = document.getElementById('output');
    const metrics = document.getElementById('metrics');

    fetch('/run', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: `language=${language}&code=${encodeURIComponent(code)}&input=${encodeURIComponent(input)}`
    })
    .then(response => response.json())
    .then(data => {
        output.textContent = data.output || data.error;
        metrics.textContent = `Execution Time: ${data.execution_time}, Memory Usage: ${data.memory_usage}`;
    })
    .catch(error => {
        output.textContent = 'Error: ' + error;
    });
}

document.addEventListener('DOMContentLoaded', (event) => {
    const problemForm = document.getElementById('problem-form');
    if (problemForm) {
        problemForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const problem = {
                title: formData.get('title'),
                description: formData.get('description'),
                constraints: formData.get('constraints'),
                testcases: JSON.parse(formData.get('testcases'))
            };
            
            fetch('/submit_problem', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(problem)
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Problem submitted successfully!');
                    problemForm.reset();
                    // Optionally refresh the problem list here
                    location.reload();
                } else {
                    alert('Failed to submit problem: ' + data.message);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('An error occurred while submitting the problem.');
            });
        });
    }


    const contestForm = document.getElementById('contest-form');
    if (contestForm) {
        contestForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const contest = {
                title: document.getElementById('contest-title').value,
                description: document.getElementById('contest-description').value,
                start: document.getElementById('contest-start').value,
                end: document.getElementById('contest-end').value
            };
            fetch('/create_contest', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(contest)
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    alert('Contest created successfully!');
                    contestForm.reset();
                }
            });
        });
    }

    const solutionForm = document.getElementById('solution-form');
    if (solutionForm) {
        solutionForm.addEventListener('submit', function(e) {
            e.preventDefault();
            const formData = new FormData(this);
            const problemId = window.location.pathname.split('/').pop();
            fetch(`/submit_solution/${problemId}`, {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                const resultsDiv = document.getElementById('results');
                resultsDiv.innerHTML = `
                    <h3>Submission Results</h3>
                    <p>All test cases passed: ${data.passed_all ? 'Yes' : 'No'}</p>
                    <ul>
                        ${data.results.map(result => `
                            <li>
                                Test Case ${result.test_case}: ${result.passed ? 'Passed' : 'Failed'}
                                <br>Input: ${result.input}
                                <br>Expected Output: ${result.expected_output}
                                <br>Actual Output: ${result.actual_output}
                                <br>Execution Time: ${result.execution_time}
                                <br>Memory Usage: ${result.memory_usage}
                            </li>
                        `).join('')}
                    </ul>
                `;
            });
        });
    }
});