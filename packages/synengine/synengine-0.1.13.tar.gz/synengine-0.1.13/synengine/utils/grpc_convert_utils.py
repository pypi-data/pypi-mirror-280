def parse_int_from_str(content: bytes) -> int:
    # the header of the string starts with "\x03"
    # the true string value starts from the index 1
    return content.decode().strip()[1:]
