key_phrase = input()  # The key phrase each submission must compare to.
num_submissions = int(input())  # The number of submissions.

results = []

for _ in range(num_submissions):
    submission = input()  # Each submission

    total_length = len(submission)
    matching_characters = sum(1 for x, y in zip(key_phrase, submission) if x.lower() == y.lower())
    accuracy = (matching_characters / total_length) * 100

    if accuracy >= 90:
        results.append("pass")
    else:
        results.append("fail")

for result in results:
    print(result)
