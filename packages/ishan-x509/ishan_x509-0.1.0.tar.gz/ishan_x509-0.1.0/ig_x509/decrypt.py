import os
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography import x509
from .certificate import load_certificate_from_pem, load_private_key_from_pem, load_aes_key_from_certificate

def decrypt_file(encrypted_file_path, certificate_path, private_key_path, output_folder):
    try:
        certificate = load_certificate_from_pem(certificate_path)
        private_key = load_private_key_from_pem(private_key_path)

        with open(encrypted_file_path, 'rb') as f:
            encrypted_aes_key = f.read(256)
            iv = f.read(16)
            encrypted_content = f.read()

        aes_key = private_key.decrypt(
            encrypted_aes_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_content = decryptor.update(encrypted_content) + decryptor.finalize()

        decrypted_file_name = os.path.basename(encrypted_file_path).replace('.sarvm', '')
        decrypted_file_path = os.path.join(output_folder, decrypted_file_name)

        os.makedirs(os.path.dirname(decrypted_file_path), exist_ok=True)
        with open(decrypted_file_path, 'wb') as f:
            f.write(decrypted_content)

        print(f"File decrypted successfully: {decrypted_file_path}")

    except Exception as e:
        print(f"Decryption failed: {e}")

def decrypt_all(input_folder, certificate_path, private_key_path, output_folder):
    os.makedirs(output_folder, exist_ok=True)
    for filename in os.listdir(input_folder):
        if filename.endswith('.sarvm'):
            encrypted_file_path = os.path.join(input_folder, filename)
            decrypt_file(encrypted_file_path, certificate_path, private_key_path, output_folder)

    print(f'Decryption of all files completed.')
