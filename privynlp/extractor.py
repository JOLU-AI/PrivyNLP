import spacy
import re

class PrivyNLP:
    """
    PrivyNLP: Detect and redact sensitive data (PII/PHI/payment) in text, LLM-agnostic.
    Now covers a wider range of PII/PHI per best practices and regulatory lists.
    """

    def __init__(self, model_name="en_core_web_sm"):
        self.nlp = spacy.load(model_name)
        # Common regex patterns for PII/PHI
        self.patterns = {
            "EMAIL": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"),
            "PHONE": re.compile(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"),
            "FAX": re.compile(r"\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b"),
            "SSN": re.compile(r"\b\d{3}-\d{2}-\d{4}\b"),
            "CREDIT_CARD": re.compile(r"\b(?:\d[ -]*?){13,16}\b"),
            "MEDICAL_RECORD": re.compile(r"\bMRN\d{6,}\b", re.IGNORECASE),
            "HEALTH_INSURANCE": re.compile(r"\b[Hh][Ii][Nn]\d{6,}\b"),
            "ACCOUNT_NUMBER": re.compile(r"\b(?:ACCT|Account)\s*[:#]?\s*\d{4,}\b", re.IGNORECASE),
            "DRIVER_LICENSE": re.compile(r"\b([A-Z0-9]{1,2}-)?\d{7,9}\b"),
            "PASSPORT": re.compile(r"\b[A-PR-WYa-pr-wy][1-9]\d\s?\d{4}[1-9]\b"),
            "URL": re.compile(r"\bhttps?://[^\s/$.?#].[^\s]*\b"),
            "IP_ADDRESS": re.compile(r"\b((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)\b"),
            "BIOMETRIC": re.compile(r"\b(finger|retina|voice)(print|scan|id)\b", re.IGNORECASE),
            "CERTIFICATE_LICENSE": re.compile(r"\b(?:cert|license)[-:\s]?\w+\b", re.IGNORECASE),
            "VEHICLE_ID": re.compile(r"\bVIN[:\s]?[A-HJ-NPR-Z0-9]{11,17}\b", re.IGNORECASE),
            "DEVICE_ID": re.compile(r"\b(serial|device)[-:\s]?\w+\b", re.IGNORECASE),
            "BANK_ACCOUNT": re.compile(r"\b(?:bank|acct|account)[-:\s]?\d{6,}\b", re.IGNORECASE),
            "RELATIVE_NAME": re.compile(r"\b(mother|father|sister|brother|spouse|child|son|daughter|relative)[’'s]*\s+[A-Z][a-z]+\b", re.IGNORECASE),
            "DOB": re.compile(r"\b\d{2}/\d{2}/\d{4}\b"),  # MM/DD/YYYY
            "DATE": re.compile(r"\b\d{4}-\d{2}-\d{2}\b"),  # YYYY-MM-DD
        }
        # spaCy NER labels for entity detection
        self.ner_labels = [
            "PERSON", "GPE", "LOC", "ORG", "DATE", "FAC"
        ]

    def extract(self, text):
        """
        Extracts sensitive entities (PII/PHI).
        Returns: List[dict] [{'type':..., 'value':...}]
        """
        sensitive = []

        # spaCy NER
        doc = self.nlp(text)
        for ent in doc.ents:
            if ent.label_ in self.ner_labels:
                sensitive.append({"type": ent.label_, "value": ent.text})

        # Regex-based detection
        for label, pattern in self.patterns.items():
            for match in pattern.findall(text):
                sensitive.append({"type": label, "value": match})

        return sensitive

    def redact(self, text, mask="*"):
        """
        Redacts sensitive data in text by replacing with a mask.
        Returns: Redacted text.
        """
        entities = self.extract(text)
        for ent in entities:
            text = text.replace(ent["value"], mask * len(ent["value"]))
        return text