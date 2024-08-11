users = {}

def update_user_stats(username, problem_id, is_correct):
    if username not in users:
        users[username] = {
            'total_attempts': 0,
            'correct_attempts': 0,
            'problems_attempted': {}
        }

    users[username]['total_attempts'] += 1
    if is_correct:
        users[username]['correct_attempts'] += 1

    if problem_id not in users[username]['problems_attempted']:
        users[username]['problems_attempted'][problem_id] = {
            'attempts': 0,
            'correct': 0
        }

    users[username]['problems_attempted'][problem_id]['attempts'] += 1
    if is_correct:
        users[username]['problems_attempted'][problem_id]['correct'] += 1

def get_user_stats(username):
    if username in users:
        return users[username]
    return None

def get_leaderboard():
    leaderboard = sorted(users.items(), key=lambda x: x[1]['correct_attempts'], reverse=True)
    return leaderboard


# users = {}
#
# def update_user_stats(username, problem_id, is_correct):
#     if username not in users:
#         users[username] = {
#             'total_attempts': 0,
#             'correct_attempts': 0,
#             'problems_attempted': {}
#         }
#
#     users[username]['total_attempts'] += 1
#     if is_correct:
#         users[username]['correct_attempts'] += 1
#
#     if problem_id not in users[username]['problems_attempted']:
#         users[username]['problems_attempted'][problem_id] = {
#             'attempts': 0,
#             'correct': 0
#         }
#
#     users[username]['problems_attempted'][problem_id]['attempts'] += 1
#     if is_correct:
#         users[username]['problems_attempted'][problem_id]['correct'] += 1
#
# def get_user_stats(username):
#     if username in users:
#         return users[username]
#     return None
#
# def get_leaderboard():
#     leaderboard = sorted(users.items(), key=lambda x: x[1]['correct_attempts'], reverse=True)
#     return leaderboard