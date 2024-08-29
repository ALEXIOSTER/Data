import json

with open('./project/data/processed/merged.json', 'r', encoding='utf-8') as file:
    data_file = json.load(file)

data = []

for entry in data_file:

    title = entry["title"]
    
    first_comment = entry["comments"][0]["content"]

    output_data = {
        "prompt": title,
        "completion": first_comment
    }
    data.append(output_data)


file_path = './project/data/training/sft_dataset.json'

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)
