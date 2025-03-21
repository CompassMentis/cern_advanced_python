import memory_profiler

@memory_profiler.profile
def memory_intensive_function():
    data = [i for i in range(100000)]
    return data


memory_intensive_function()
