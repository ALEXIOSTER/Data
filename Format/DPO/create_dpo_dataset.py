import json

with open('./project/data/processed/merged.json', 'r', encoding="utf-8") as f:
    data = json.load(f)

new_data = []

for post in data:
    
    input_comment =  post["title"]

    nbr_comments = len(post["comments"])//3
    
    chosen_comments = post["comments"][:nbr_comments]

    rejected_comments = post["comments"][-nbr_comments:]

    for i in range(nbr_comments):

        new_post = {
            "input": input_comment,

            "chosen": chosen_comments[i]["content"],

            "rejected": rejected_comments[i]["content"]
        }

        new_data.append(new_post)


with open('./project/data/training/dpo_dataset.json', 'w', encoding="utf-8") as f:
    json.dump(new_data, f, indent=2, ensure_ascii=False)