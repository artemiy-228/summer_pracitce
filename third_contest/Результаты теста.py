k = int(input())  # Number of correct answers on your friend's exam
your_answers = input()  # Your answers
friend_answers = input()  # Your friend's answers

max_score = k  # Initialize the maximum score with your friend's correct answers

# Compare your answers with your friend's answers and update the maximum score
for i in range(len(your_answers)):
    if your_answers[i] == friend_answers[i] and your_answers[i] == 'F':
        max_score += 1

print(max_score)
