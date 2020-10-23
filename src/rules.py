import numpy as np


PROBS_CONTACTS_2_4 = np.array([4.0, 4.0, 6.0, 12.0, 4.0, 4.0, 9.0, 2.0, 1.0])
PROBS_CONTACTS_2_4 /= np.sum(PROBS_CONTACTS_2_4)

RULE_CONTACTS_2_4 = [
    # [1, 3] -> 4
    {
        'num_contacts': 1,
        'translations': [[1, 3], [1, -3], [-1, 3], [-1, -3]],
        'direction': 0
    },
    # [2, 2] -> 4
    {
        'num_contacts': 1,
        'translations': [[2, 2], [2, -2], [-2, 2], [-2, -2]],
        'direction': 1
    },
    # [0, 3], [1, 2] -> 6
    {
        'num_contacts': 2,
        'translations': [[0, 3], [0, -3], [1, 2], [1, -2], [-1, 2], [-1, -2]],
        'direction': 0
    },
    # [2, 1], [2, 0], [1, 2], [0, 2] -> 12
    {
        'num_contacts': 2,
        'translations': [[2, 1], [2, -1], [-2, 1], [-2, -1], [2, 0], [-2, 0], [1, 2], [1, -2], [-1, 2], [-1, -2], [0, 2], [0, -2]],
        'direction': 1
    },
    # [1, 1] -> 4
    {
        'num_contacts': 3,
        'translations': [[1, 1], [1, -1], [-1, 1], [-1, -1]],
        'direction': 0
    },
    # [0, 2], [1, 0] -> 4
    {
        'num_contacts': 4,
        'translations': [[0, 2], [0, -2], [1, 0], [-1, 0]],
        'direction': 0
    },
    # [1, 1], [1, 0], [0, 1], [0, 0] -> 9
    {
        'num_contacts': 4,
        'translations': [[1, 1], [1, -1], [-1, 1], [-1, -1], [1, 0], [-1, 0], [0, 1], [0, -1], [0, 0]],
        'direction': 1
    },
    # [0, 1] -> 2
    {
        'num_contacts': 6,
        'translations': [[0, 1], [0, -1]],
        'direction': 0
    },
    # [0, 0] -> 1
    {
        'num_contacts': 8,
        'translations': [[0, 0]],
        'direction': 0
    }
]

LIST_RULES_2_4 = []
ind = 0
for rule in RULE_CONTACTS_2_4:
    cur_direction = rule['direction']
    cur_num_contacts = rule['num_contacts']

    for translation in rule['translations']:
        cur_rule = [ind, [cur_direction, translation, cur_num_contacts]]
        LIST_RULES_2_4.append(cur_rule)

        ind += 1
