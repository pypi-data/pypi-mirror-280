import os
import datetime
import json
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.backends import default_backend
from cryptography import x509
from cryptography.x509.oid import NameOID

def generate_rsa_private_key(key_size=2048):
    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=key_size,
        backend=default_backend()
    )
    return private_key

def load_private_key_from_pem(file_path):
    with open(file_path, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
            backend=default_backend()
        )
    return private_key

def load_metadata(metadata_path):
    with open(metadata_path, "r") as metadata_file:
        metadata = json.load(metadata_file)
    return metadata

def generate_x509_certificate(private_key, metadata, aes_key, expire_date_str):
    expire_date = datetime.datetime.strptime(expire_date_str, "%m%d%Y")

    builder = (
        x509.CertificateBuilder()
        .subject_name(x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, "IN"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Karnataka"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, "Bengaluru"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Sarvm"),
            x509.NameAttribute(NameOID.COMMON_NAME, "sarvm.ai"),
        ]))
        .issuer_name(x509.Name([
            x509.NameAttribute(NameOID.COUNTRY_NAME, "IN"),
            x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, "Karnataka"),
            x509.NameAttribute(NameOID.LOCALITY_NAME, "Bengaluru"),
            x509.NameAttribute(NameOID.ORGANIZATION_NAME, "Sarvm"),
            x509.NameAttribute(NameOID.COMMON_NAME, "sarvm.ai"),
        ]))
        .not_valid_before(datetime.datetime.utcnow())
        .not_valid_after(expire_date)
        .serial_number(x509.random_serial_number())
        .public_key(private_key.public_key())
    )

    metadata_extension = x509.UnrecognizedExtension(
        x509.ObjectIdentifier('2.16.840.1.113730.1.1'),
        json.dumps(metadata).encode('utf-8')
    )
    builder = builder.add_extension(metadata_extension, critical=False)

    aes_key_extension = x509.UnrecognizedExtension(
        x509.ObjectIdentifier('2.16.840.1.113730.1.2'),
        aes_key
    )
    builder = builder.add_extension(aes_key_extension, critical=False)

    certificate = builder.sign(
        private_key=private_key,
        algorithm=hashes.SHA256(),
        backend=default_backend()
    )
    return certificate

def save_certificate_as_pem(certificate, cert_path):
    with open(cert_path, "wb") as cert_file:
        cert_file.write(certificate.public_bytes(encoding=serialization.Encoding.PEM))
