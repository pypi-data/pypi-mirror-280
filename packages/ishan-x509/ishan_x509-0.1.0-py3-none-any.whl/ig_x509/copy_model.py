import shutil

def copy_model(original_model_path, copied_model_path):
    try:
        shutil.copyfile(original_model_path, copied_model_path)
        print(f"Successfully copied model.bin from '{original_model_path}' to '{copied_model_path}'")
    except Exception as e:
        print(f"Error: {e}")
