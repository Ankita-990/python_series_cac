password = "abcdtyu123456"

pass_len = len(password)

if pass_len < 6:
    msg = "Weak password"
elif pass_len <= 10:
    msg = "Medium password. Could be more strong"
elif pass_len > 10:
    msg = "Horray! You have a strong password"

print(msg)