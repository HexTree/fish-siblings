import random
random.seed(1)

# fixed quantities
num_fish = 5911
group_size = 6
sample_size = 168
repeats = 1000000

# dependent variables
num_groups = num_fish // group_size
num_fish = num_groups * group_size

# main loop
siblings_count = dict()
for i in range(1, group_size+1):
    siblings_count[i] = 0

for i in range(repeats):
    if i % (repeats//10) == 0:
        print("%d samples tested so far, out of %d" % (i, repeats))
    unique_fish_name = 0
    total_untaken = num_fish
    diminished = dict()
    total_diminished = 0
    sample = dict()

    for j in range(sample_size):
        r = random.randint(1, total_diminished + total_untaken)
        if r > total_diminished:
            # take an untouched fish
            total_untaken -= group_size
            diminished[unique_fish_name] = group_size-1
            total_diminished += (group_size - 1)
            sample[unique_fish_name] = 1
            unique_fish_name += 1
        else:
            # take a fish we took at least once before
            c = 0
            for fish in diminished:
                c += diminished[fish]
                if c >= r:
                    break
            # fish is the one we take
            diminished[fish] -= 1
            if diminished[fish] == 0:
                del diminished[fish]
            total_diminished -= 1
            if fish in sample:
                sample[fish] += 1
            else:
                sample[fish] = 1

    # now we have a sample of fish
    # keep running count of the numbers of singletons, pairs, triplets, etc
    for fish in sample:
        siblings_count[sample[fish]] += 1

# now we have a cumulative count of sibling pairs across all repeats
print("%d samples were attempted altogether, each of size %d" % (repeats, sample_size))
print("\nResults:\n")
for i in range(1, group_size+1):
    print("Sibling group of size: %d\t\tAverage number of occurrences: %f" % (i, siblings_count[i]/repeats))
