import pytest
from fastapi import HTTPException
from app.not_used_yet.auth import extract_bearer_token

def test_missing_header_raises_401():
    with pytest.raises(HTTPException) as exc:
        extract_bearer_token("")

    assert exc.value.status_code == 401


def test_empty_bearer_rejected():
    with pytest.raises(HTTPException):
        extract_bearer_token("Bearer")


def test_valid_bearer_token_extracted():
    token = extract_bearer_token("Bearer abc.def.ghi")
    assert token == "abc.def.ghi"
