def num(xxx):
    try:
        res = "".join(re.findall(r'[0-9.-]', xxx))
        return float(res)
    except Exception as error:
        return 0
