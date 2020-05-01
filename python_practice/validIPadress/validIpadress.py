# ----------------------------
# IP address, try to expend to valid IPv6
# ----------------------------

class Solution(object):
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """

        a = IP.find(".")
        b = IP.find(":")

        def piv6_check(chunk):

            # too short or too long
            if len(chunk) == 0 or len(chunk) > 4:
                return False

            # number too large
            for ch in chunk:
                if not ch.isdigit():
                    if ch.capitalize() > 'F' or ch.capitalize() < 'A':
                        return False

            return True

        def piv4_check(chunk):

            # start with leading zero
            if len(chunk) > 1 and chunk[0] == "0":
                return False

            # empty or too long
            if len(chunk) == 0 or len(chunk) > 3:
                return False

            # number too large
            for ch in chunk:
                if not ch.isdigit():
                    return False

            if int(chunk) > 255:
                return False

            return True

        # didn't find , or :  or found both
        if (a > -1 and b > -1) or (a == -1) and (b == -1):
            return "Neither"

        if a > -1:  # ipv4

            # attempt to parse IPv6
            chunks = IP.split(".")
            if len(chunks) != 4:
                return "Neither"

            for chunk in chunks:
                if not piv4_check(chunk):
                    return "Neither"

            return "IPv4"

        if b > -1:  # IPv6
            # attempt to parse IPv6
            chunks = IP.split(":")
            if len(chunks) != 8:
                return "Neither"

            for chunk in chunks:
                if not piv6_check(chunk):
                    return "Neither"

            return "IPv6"