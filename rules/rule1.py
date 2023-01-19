def retalierCharacters(retailer_name):
    return len(''.join(filter(str.isalnum,retailer_name)))