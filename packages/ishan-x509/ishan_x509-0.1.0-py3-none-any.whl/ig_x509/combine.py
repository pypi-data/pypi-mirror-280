import os
import json

def combine_json_files(file_paths, output_path):
    combined_data = {}
    for file_path in file_paths:
        with open(file_path, 'r') as f:
            file_name = os.path.basename(file_path)
            combined_data[file_name] = json.load(f)
    with open(output_path, 'w') as f:
        json.dump(combined_data, f, indent=4)
    return output_path

def combine_decrypted(input_dir, output_file):
    combined_data = []
    for filename in sorted(os.listdir(input_dir)):
        if filename.startswith('part_') and filename.endswith('.json'):
            file_path = os.path.join(input_dir, filename)

            with open(file_path, 'r', encoding='utf-8') as f:
                part_data_str = f.read().strip()
            combined_data.append(part_data_str)

    combined_json_str = ''.join(combined_data)
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(combined_json_str)
    print(f'Successfully combined into {output_file}.')
