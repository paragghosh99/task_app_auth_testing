from app.not_used_yet.strings import normalize_email

def test_email_is_lowercased():
    assert normalize_email("TEST@EXAMPLE.COM") == "test@example.com"

def test_whitespace_trimmed():
    assert normalize_email("  test@example.com ") == "test@example.com"
