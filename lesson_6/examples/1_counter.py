from collections import Counter
from operator import itemgetter

# ------------------------
# ---- Setup testdata ----
# ------------------------
test_set = ["red", "green", "yellow"]*40
test_set.append("green")
test_set.append("green")
test_set.append("yellow")

sorted_votes = sorted(test_set)

# ------------------------
# ---- Basic Solution ----
# ------------------------

# Version 1 - For loop

count_votes = {}
for vote in sorted_votes:
    if vote in count_votes:
        count_votes[vote] += 1
    else:
        count_votes[vote] = 1

print(count_votes)

# Version 2 - negate expression

count_votes = {}
for vote in sorted_votes:
    if not vote in count_votes:
        count_votes[vote] = 0
    count_votes[vote] += 1

print(count_votes)

# Version 3 - dict update

count_votes = {}
for vote in sorted_votes:
    count_or_default = count_votes.get(vote, 0)
    count_votes.update({vote: count_or_default + 1})

print(count_votes)

# --------------------------
# ---- Which color won? ----
# --------------------------

dict_items = count_votes.items()

# This will sort on key
print(f"Failing Manual sort: {sorted(dict_items)}")

# This will sort on value
dict_items_sorted = sorted(dict_items, key=itemgetter(1))
print(f"Manual sort: {list(reversed(dict_items_sorted))}")

# In one line using sorted options reverse=True
print(f"Manual sort: {sorted(dict_items, key=itemgetter(1), reverse=True)}")

# ---------------------------
# ------ Using Counter ------
# ---------------------------

c = Counter(sorted_votes)
print(c)

# --------------------------
# ---- Which color won? ----
# --------------------------

print(c.most_common())
