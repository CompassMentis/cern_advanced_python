import cProfile
import pstats


def create_list():
    numbers = []
    for i in range(0, 400000):
        numbers.append(i)


profiler = cProfile.Profile()
profiler.enable()
create_list()
profiler.disable()
stats = pstats.Stats(profiler).strip_dirs()
stats.sort_stats("ncalls")
stats.print_stats()

stats.sort_stats('cumtime')
stats.print_stats()
