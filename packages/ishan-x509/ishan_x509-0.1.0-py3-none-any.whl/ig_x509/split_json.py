import os
import json
import random
import math

def split_json_file(input_file, output_dir):
    with open(input_file, 'r', encoding='utf-8') as f:
        json_str = f.read().strip()

    num_parts = random.randint(7, 20)
    print(f"Dividing into {num_parts} parts.")

    total_chars = len(json_str)
    chars_per_part = math.ceil(total_chars / num_parts)

    os.makedirs(output_dir, exist_ok=True)
    for i in range(num_parts):
        start_idx = i * chars_per_part
        end_idx = min((i + 1) * chars_per_part, total_chars)
        part_data_str = json_str[start_idx:end_idx]

        part_file = os.path.join(output_dir, f'part_{i}.json')
        with open(part_file, 'w', encoding='utf-8') as f:
            f.write(part_data_str)

    print(f'Successfully split JSON into {num_parts} parts.')
