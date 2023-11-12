thread_a = {}
thread_b = {}

total = 0

# So far so good
thread_a['t'] = total
thread_a['t'] = thread_a['t'] + 1
total = thread_a['t']
thread_b['t'] = total
thread_b['t'] = thread_b['t'] + 1
total = thread_b['t']

print(total)  # 2
### (column break)
# Now both threads run in parallel
thread_a['t'] = total
thread_b['t'] = total
thread_a['t'] = thread_a['t'] + 1
total = thread_a['t']
thread_b['t'] = thread_b['t'] + 1
total = thread_b['t']

print(total)

# Again, increased twice
# Expected output: 4
# Actual output: 3
