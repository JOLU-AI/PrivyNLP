from privynlp import PrivyNLP

def test_url_detection():
    extractor = PrivyNLP()
    text = "Patient portal: https://myhospital.com/records"
    results = extractor.extract(text)
    assert any(item['type'] == "URL" and "https://myhospital.com/records" in item['value'] for item in results)

def test_ip_address_detection():
    extractor = PrivyNLP()
    text = "Accessed from IP: 192.168.0.1"
    results = extractor.extract(text)
    assert any(item['type'] == "IP_ADDRESS" and "192.168.0.1" in item['value'] for item in results)

def test_device_id_detection():
    extractor = PrivyNLP()
    text = "Device serial: device-ABC1234 or serial-987654"
    results = extractor.extract(text)
    assert any(item['type'] == "DEVICE_ID" and "device-ABC1234" in item['value'] for item in results)
    assert any(item['type'] == "DEVICE_ID" and "serial-987654" in item['value'] for item in results)

def test_vehicle_id_detection():
    extractor = PrivyNLP()
    text = "Vehicle VIN: VIN:1HGCM82633A004352"
    results = extractor.extract(text)
    assert any(item['type'] == "VEHICLE_ID" and "VIN:1HGCM82633A004352" in item['value'] for item in results)

def test_biometric_terms_detection():
    extractor = PrivyNLP()
    text = "Biometric data includes fingerprintscan and retinalscan in the records."
    results = extractor.extract(text)
    assert any(item['type'] == "BIOMETRIC" and "fingerprintscan" in item['value'] for item in results)
    assert any(item['type'] == "BIOMETRIC" and "retinalscan" in item['value'] for item in results)

def test_relatives_name_detection():
    extractor = PrivyNLP()
    text = "Patient's mother's maiden name is Smith. His Father's name is John Doe."
    results = extractor.extract(text)
    assert any(item['type'] == "RELATIVE_NAME" and "mother's maiden name" in item['value'].lower() for item in results)
    assert any(item['type'] == "RELATIVE_NAME" and "Father's name" in item['value'] for item in results)

def test_dob_detection():
    extractor = PrivyNLP()
    text = "Date of birth: 12/31/1965. Another format: 1965-12-31."
    results = extractor.extract(text)
    assert any(item['type'] == "DOB" and "12/31/1965" in item['value'] for item in results)
    assert any(item['type'] == "DATE" and "1965-12-31" in item['value'] for item in results)

def test_id_detection():
    extractor = PrivyNLP()
    text = "Medical record number: MRN654321. Health insurance number: HIN987654."
    results = extractor.extract(text)
    assert any(item['type'] == "MEDICAL_RECORD" and "MRN654321" in item['value'] for item in results)
    assert any(item['type'] == "HEALTH_INSURANCE" and "HIN987654" in item['value'] for item in results)