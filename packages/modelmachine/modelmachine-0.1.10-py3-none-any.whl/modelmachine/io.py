"""Allow to input and output program and data."""

from modelmachine.numeric import Integer


class InputOutputUnit:
    """Allow to input and output program and data."""

    def __init__(self, ram, start_address, word_size):
        """See help(type(x))."""
        self.ram = ram
        self.start_address = start_address
        self.word_size = word_size

    def put_int(self, address, value):
        """Load data from string into memory by address."""
        value = Integer(value, self.word_size, True)
        self.ram.put(address, value.get_data(), self.word_size)

    def get_int(self, address):
        """Return data by address."""
        value = Integer(
            self.ram.fetch(address, self.word_size), self.word_size, True
        )
        return value.get_value()

    def load_hex(self, start, source):
        """Load data from string into memory by start address."""
        address = start
        block, block_size = 0, 0
        for part_str in source.split():
            part_size = len(part_str) * 4
            part = int(part_str, base=16)
            block = (block << part_size) | part
            block_size += part_size
            if block_size >= self.ram.word_size:
                self.ram.put(address, block, block_size)
                address += block_size // self.ram.word_size
                block, block_size = 0, 0
        if block_size != 0:
            msg = "Cannot save string, wrong size"
            raise ValueError(msg)

    def store_hex(self, start, size):
        """Save data to string."""
        if size % self.ram.word_size != 0:
            msg = f"Cannot save {size} bits, word size is {self.ram.word_size}"
            raise KeyError(msg)
        result = []
        block_size = self.ram.word_size
        size //= block_size
        for i in range(start, start + size):
            data = self.ram.fetch(i, block_size)
            result.append(hex(data)[2:].rjust(block_size // 4, "0"))
        return " ".join(result)

    def load_source(self, source):
        """Source code loader."""
        program = ""
        for line in source:
            if line == "":
                continue
            program += " " + line
        self.load_hex(self.start_address, program)

    def load_data(self, addresses, data):
        """Data loader (decimal numbers)."""
        data = [int(value, 0) for value in data]
        for address, value in zip(addresses, data):
            self.put_int(address, value)
