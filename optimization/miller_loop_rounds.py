IDLE_CUS = 2000

# ATE loop count reversed, first element removed and -1s squared
ate_rev_normalized = [1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0]

# Costs in CUs (BPF Compute Units)
adding_rounds_cus = [12673, 23173, 15199, 27102, 12907, 12661]
doubling_rounds_cus = [13078, 16767, 25817, 15379, 15070, 5567, 15070]
ell_rounds_cus = [15000, 90000, 15000, 90000, 15000, 90000]
square_in_place_cus = 90000
mul_by_char_cus = 18000

rounds_cus = list()

# Stub algorithm to sum up costs
# 0 CUs are used to skip rounds and keep the total rounds count as multiple of a certain factor
for i, complex_round in enumerate(ate_rev_normalized):
    rounds_cus.extend(doubling_rounds_cus)
    rounds_cus.extend(ell_rounds_cus)

    if i > 0:
        rounds_cus.append(square_in_place_cus)
    else:
        rounds_cus.append(0)

    if complex_round == 1:
        rounds_cus.extend(adding_rounds_cus)
        rounds_cus.extend(ell_rounds_cus)
    else:
        rounds_cus.extend([0] * len(adding_rounds_cus))
        rounds_cus.extend([0] * len(ell_rounds_cus))

rounds_main_loop = len(rounds_cus)

rounds_cus.append(mul_by_char_cus)
rounds_cus.extend(adding_rounds_cus)
rounds_cus.extend(ell_rounds_cus)
rounds_cus.append(mul_by_char_cus)
rounds_cus.extend(adding_rounds_cus)
rounds_cus.extend(ell_rounds_cus)

# Calculate the optimal distribution
from optimize_distribution import find_optimal_distribution
find_optimal_distribution(rounds_cus, IDLE_CUS)
print("Main loop rounds: ", rounds_main_loop)