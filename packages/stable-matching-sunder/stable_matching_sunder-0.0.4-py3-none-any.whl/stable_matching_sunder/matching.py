import csv


def stable_matching_from_csv(file_path, num_men):
    def read_preferences(file_path):
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            preferences = {row[0]: row[1:] for row in reader}
        return preferences

    def gale_shapley(men_preferences, women_preferences):
        free_men = list(men_preferences.keys())
        engaged = {}
        women_free_rank = {w: {m: rank for rank, m in enumerate(preferences)}
                           for w, preferences in women_preferences.items()}

        while free_men:
            man = free_men.pop(0)
            man_pref_list = men_preferences[man]
            for woman in man_pref_list:
                if woman not in engaged:
                    engaged[woman] = man
                    break
                else:
                    current_man = engaged[woman]
                    if women_free_rank[woman][man] < women_free_rank[woman][current_man]:
                        engaged[woman] = man
                        free_men.append(current_man)
                        break
        return engaged

    preferences = read_preferences(file_path)

    # Identify men and women by the number of men specified
    all_individuals = list(preferences.keys())
    men_preferences = {k: preferences[k] for k in all_individuals[:num_men]}
    women_preferences = {k: preferences[k] for k in all_individuals[num_men:]}

    matches = gale_shapley(men_preferences, women_preferences)

    print("Matches:")
    for woman, man in matches.items():
        print(f"{man} is matched with {woman}")

    return matches

