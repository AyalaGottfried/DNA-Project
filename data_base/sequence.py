class Sequence:
    _next_id = 1

    def __init__(self, sequence_name, dna_sequence):
        if sequence_name == "":
            raise Exception("Exception: empty sequence name")
        self.__id = Sequence._next_id
        self.__name = sequence_name
        self.__dna_sequence = dna_sequence
        Sequence._next_id += 1

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_dna_sequence(self):
        return self.__dna_sequence

    def set_id(self, sequence_id):
        self.__id = sequence_id

    def set_name(self, sequence_name):
        if sequence_name == "":
            raise Exception("Exception: empty sequence name")
        self.__name = sequence_name

    def set_dna_sequence(self, dna_sequence):
        self.__dna_sequence = dna_sequence

    def __str__(self):
        return "[{}] {}: {}".format(self.__id, self.__name, self.__dna_sequence)

