import os
import sys
import oom_reap_me_first as ormf


if __name__ == '__main__':
    pid = os.getpid()

    oom_score = ormf.read_oom_score(pid)
    oom_score_adj = ormf.read_oom_score(pid)
    print(f"I am {pid=} with score {oom_score=} and {oom_score_adj}")

    max_oom_score = ormf.get_current_max_oom_score()
    max_oom_score_adj = ormf.get_current_max_oom_score_adj()
    print(f"Currently {max_oom_score=} and {max_oom_score_adj=}")

    ormf.set_oom_score_adj(pid)
    oom_score = ormf.read_oom_score(pid)
    oom_score_adj = ormf.read_oom_score(pid)
    max_oom_score = ormf.get_current_max_oom_score()
    max_oom_score_adj = ormf.get_current_max_oom_score_adj()
    print()
    print(f"NOW I am {pid=} with score {oom_score=} and {oom_score_adj}")
    print(f"And {max_oom_score=} and {max_oom_score_adj=}")

    print()
    print("I will now attempt to get reaped.")
    print("THIS IS DANGEROUS!")
    print("If this package doesn't work right OTHER things may crash")
    response = input("Should I proceed [Y/n]? ").strip().lower()
    if response != 'y' and response != 'yes':
        print("Aborting!")
        sys.exit(1)

    import oom_reap_me_first.auto_enable

    print()
    print("Allocating GB slices of memory...")
    gb = 1_000_000_000
    byte_slices = []  # don't let them get GC'd
    for i in range(10_000):  # if you have 10TB, hats off to you lol
        byte_slices.append(bytearray(gb))
        print(f"\t{i:>4d} GB allocated")



