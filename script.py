import pandas as pd
from collections import defaultdict



judge_files = ['judge1test.csv']  # <-- update this later with the real filenames

# Mapping of nice category names to simpler keys
category_keys = {
    'Best Overall Project': 'overall',
    'Most On Theme': 'theme',
    'Most Creative': 'creative'
}

# Points per rank — kinda arbitrary but works for now
points_for_rank = {
    'Rank 1': 3,
    'Rank 2': 2,
    'Rank 3': 1,
    'Rank 4': 0  
}


category_scores = {
    'overall': defaultdict(int),
    'theme': defaultdict(int),
    'creative': defaultdict(int)
}


for csv_file in judge_files:
    try:
        data = pd.read_csv(csv_file)
    except Exception as e:
        print(f"Couldn't read file {csv_file}: {e}")
        continue  

    for _, row in data.iterrows():
        for fancy_label, key in category_keys.items():
            project_name = row.get(fancy_label)
            ranking = row.get('Your Score')  

    
            if pd.notna(project_name) and ranking in points_for_rank:
                # Add points to the running total
                category_scores[key][project_name] += points_for_rank[ranking]
            # else:
            #     print(f"Skipping invalid entry: {project_name}, {ranking}")  # Could enable this for debugging


top_projects = {}
for cat, scores_dict in category_scores.items():
    ranked_projects = sorted(scores_dict.items(), key=lambda item: item[1], reverse=True)
    top_projects[cat] = ranked_projects  # We'll grab top one or two from this later


print(f"1st Place (Best Overall): {top_projects['overall'][0][0]}")
print(f"2nd Place (Best Overall): {top_projects['overall'][1][0]}")
print(f"Most On Theme: {top_projects['theme'][0][0]}")
print(f"Most Creative: {top_projects['creative'][0][0]}")
