# contest.py

from datetime import datetime
from problems import problems
from code_execution import execute_code

contests = []
submissions = []

def create_contest(title, description, problem_ids, start_time, end_time):
    contest_id = len(contests) + 1
    contest = {
        'id': contest_id,
        'title': title,
        'description': description,
        'problem_ids': problem_ids,
        'start_time': start_time,
        'end_time': end_time,
        'participants': []
    }
    contests.append(contest)
    return contest_id

def register_participant(contest_id, participant_name):
    contest = next((c for c in contests if c['id'] == contest_id), None)
    if contest:
        contest['participants'].append(participant_name)
        return True
    return False

def submit_code(contest_id, participant_name, problem_id, code, language):
    contest = next((c for c in contests if c['id'] == contest_id), None)
    if contest:
        submission_id = len(submissions) + 1
        submission = {
            'id': submission_id,
            'contest_id': contest_id,
            'participant_name': participant_name,
            'problem_id': problem_id,
            'code': code,
            'language': language,
            'submitted_at': datetime.now()
        }
        submissions.append(submission)
        return submission_id
    return None

def evaluate_submission(submission_id):
    submission = next((s for s in submissions if s['id'] == submission_id), None)
    if submission:
        problem = next((p for p in problems if p['id'] == submission['problem_id']), None)
        if problem:
            results = []
            for test_case, expected_output in zip(problem['test_cases'], problem['expected_outputs']):
                output = execute_code(submission['code'], submission['language'], test_case)
                is_correct = output.strip() == expected_output.strip()
                results.append({
                    "input": test_case,
                    "expected_output": expected_output,
                    "actual_output": output,
                    "is_correct": is_correct
                })
            return results
    return None
