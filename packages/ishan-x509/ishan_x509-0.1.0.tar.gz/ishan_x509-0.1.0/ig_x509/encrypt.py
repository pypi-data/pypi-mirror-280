import os
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from cryptography import x509
from .certificate import load_certificate_from_pem, load_aes_key_from_certificate

def encrypt_file(file_path, certificate_path, output_dir):
    try:
        certificate = load_certificate_from_pem(certificate_path)
        aes_key = load_aes_key_from_certificate(certificate)

        iv = os.urandom(16)

        with open(file_path, 'rb') as f:
            file_content = f.read() 

        cipher = Cipher(algorithms.AES(aes_key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        encrypted_content = encryptor.update(file_content) + encryptor.finalize()

        public_key = certificate.public_key()
        encrypted_aes_key = public_key.encrypt(
            aes_key,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        encrypted_file_path = os.path.join(output_dir, os.path.basename(file_path) + ".sarvm")

        with open(encrypted_file_path, 'wb') as f:
            f.write(encrypted_aes_key)
            f.write(iv)
            f.write(encrypted_content)

        print(f"File encrypted successfully: {encrypted_file_path}")

    except Exception as e:
        print(f"Encryption failed for {file_path}: {e}")

def encrypt_splitted_files(input_dir, output_dir, certificate_path):
    os.makedirs(output_dir, exist_ok=True)
    for filename in os.listdir(input_dir):
        if filename.startswith('part_') and filename.endswith('.json'):
            file_path = os.path.join(input_dir, filename)
            encrypt_file(file_path, certificate_path, output_dir)

    print(f'Encryption completed.')
