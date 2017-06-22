import json
import os


QUESTION_TYPES = {
    b"\x00\x01": "a"
}
ZONES = {}  # Holds hostname -> record data, cannot grow as server runs


class DNSGen(object):

    def __init__(self, data):
        self.data = data
        self.QR = "1"
        self.AA = "1"
        self.TC = "0"
        self.RD = "0"
        self.RA = "0"   # 0=No Recursion Available
        self.Z = "000"
        self.RCODE = "0000"
        self.QDCOUNT = b"\x00\01"   # Answer only 1 question for now
        self.NSCOUNT = b"\x00\x00"  # Nameserver count
        self.ARCOUNT = b"\x00\x00"  # Additional records

    def _get_transaction_id(self):
        return self.data[0:2]  # first 2 bytes have transaction ID

    def _get_opcode(self):
        byte1 = self.data[2:3]    # get 1 byte after transaction id
        opcode = ""
        for bit in range(1, 5):	    # loop bits till end of OPCODE bit
            opcode += str(ord(byte1) & (1 << bit))	   # ord converts byte to unicode int
        return opcode

    def _generate_flags(self):
        flags1 = int(self.QR + self._get_opcode() + self.AA + self.TC + self.RD, 2).to_bytes(1, byteorder="big")
        flags2 = int(self.RA + self.Z + self.RCODE, 2).to_bytes(1, byteorder="big")
        return flags1 + flags2

    def _get_question_domain_type(self, data):
        state = 0   # 1 = parsing for text labels, 0 = update length of next text to parse
        expected_length = 0
        domain_string = ""
        domain_parts = []
        x = 0   # count to see if we reach end of text to parse
        y = 0   # count number of bytes
        for byte in data:
            if state == 1:
                if byte != 0:   # domain name not ended so add chars
                    domain_string += chr(byte)
                x += 1
                if x == expected_length:    # got to end of this label
                    domain_parts.append(domain_string)
                    domain_string = ""
                    state = 0   # ensure that next loop captures the byte length of the next label
                if byte == 0:   # Check if we have reached the end of the question domain
                    domain_parts.append(domain_string)
                    break
            else:
                state = 1
                expected_length = byte
            y += 1
        question_type = data[y:y+2] # after the domain the next 2 bytes are question type
        return (domain_parts, question_type)

    @staticmethod
    def _get_zone(domain):
        global ZONES
        zone_name = ".".join(domain)
        zone = {}
        try:
            zone = ZONES[zone_name]
        except KeyError:
            pass
        return zone

    def _get_records(self, data):
        domain, question_type = self._get_question_domain_type(data)
        qt = ""
        try:
            qt = QUESTION_TYPES[question_type]
        except KeyError:
            qt = "a"
        zone = self._get_zone(domain)
        return (zone[qt], qt, domain)

    def make_header(self):
        transaction_id = self._get_transaction_id()
        flags = self._generate_flags()
        ancount = len(self._get_records(self.data[12:])).to_bytes(2, byteorder="big")
        print(transaction_id + flags + self.QDCOUNT + ancount + self.NSCOUNT + self.ARCOUNT)
        return transaction_id + flags + self.QDCOUNT + ancount + self.NSCOUNT + self.ARCOUNT


def load_zones():
    global ZONES
    json_zone = {}
    for zone_file in os.listdir("Zones"):
        with open(os.path.join("Zones", zone_file), "r") as f:
            data = json.load(f)
            zone_name = data["$origin"]
            json_zone[zone_name] = data
    return json_zone
ZONES = load_zones()
