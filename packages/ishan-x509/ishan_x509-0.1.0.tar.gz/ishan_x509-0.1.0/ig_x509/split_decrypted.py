import os
import json

def split_decrypted_json(combined_json_path, output_dir):
    with open(combined_json_path, 'r') as f:
        combined_data = json.load(f)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for key, value in combined_data.items():
        component_path = os.path.join(output_dir, f'{key}')
        with open(component_path, 'w') as f:
            json.dump(value, f, indent=4)

    return output_dir
