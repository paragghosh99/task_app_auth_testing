from fastapi import HTTPException, status

def extract_bearer_token(header: str) -> str:
    if not header:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    parts = header.split()
    if len(parts) != 2 or parts[0] != "Bearer":
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

    return parts[1]
