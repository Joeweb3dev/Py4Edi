from Segment import Segment


class Envelope(object):
    def __init__(self):
        self.header = Segment()
        self.trailer = Segment()
        self.body = []

    def format_as_edi(self, document_configuration):
        document = self.header.format_as_edi(document_configuration)
        document += self.__format_body_as_edi(document_configuration)
        document += self.trailer.format_as_edi(document_configuration)
        return document

    def __format_body_as_edi(self, document_configuration):
        document = ""
        for item in self.body:
            document += item.format_as_edi(document_configuration)
        return document

    def validate(self, report):
        self.header.validate(report)
        self.__validate_body(report)
        self.trailer.validate(report)

    def __validate_body(self, report):
        for item in self.body:
            item.validate(report)


class InterchangeEnvelope(Envelope):
    def __init__(self):
        Envelope.__init__(self)
        self.groups = self.body


class GroupEnvelope(Envelope):
    def __init__(self):
        Envelope.__init__(self)
        self.transaction_sets = self.body


class TransactionSetEnvelope(Envelope):
    def __init__(self):
        Envelope.__init__(self)
        self.transaction_body = self.body