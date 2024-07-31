def Tc(tc_no):
    if len(tc_no) != 11 or not tc_no.isdigit():
        return False
    digits = [int(x) for x in tc_no]
    if digits[0] == 0:
        return False
    if sum(digits[:10]) % 10 != digits[10]:
        return False
    if (((sum(digits[0:9:2]) * 7) - sum(digits[1:8:2])) % 10) != digits[9]:
        return False
    return True
