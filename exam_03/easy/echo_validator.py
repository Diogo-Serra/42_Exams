# Echo Validator

def echo_validator(text: str) -> bool:
    _text = text.replace(' ', '').upper()
    _reversed = text.replace(' ', '').upper()[::-1]
    return _text == _reversed
