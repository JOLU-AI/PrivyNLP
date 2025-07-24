from privynlp import PrivyNLP

if __name__ == "__main__":
    text = """
    Patient John Doe (MRN123456) visited MedHealth on 07/10/2025. Email: john.doe@example.com
    Phone: 555-123-4567, SSN: 123-45-6789, Credit card: 4111 1111 1111 1111
    Mother's maiden name: Smith, Device serial: device-XJ1234
    Passport: K1234567, URL: https://med.org/patient, IP: 192.168.1.1
    """
    extractor = PrivyNLP()
    print("Sensitive Entities:", extractor.extract(text))
    print("Redacted Text:", extractor.redact(text))