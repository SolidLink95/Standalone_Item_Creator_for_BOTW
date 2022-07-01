import oead
from oead import yaz0, Sarc, SarcWriter

from files_manage import get_endianness


class Sarc_file:
    def __init__(self, file):
        self.file = file
        if file is not None:
            self.data_sarc = self.init()
            self.data_writer = SarcWriter.from_sarc(self.data_sarc)
            set_sarc_endian(self.data_writer)

    def init(self):
        with open(self.file + '', 'rb') as f:
            data = yaz0.decompress(f.read())
        data_dec = Sarc(data)
        return data_dec

    def get_raw_data(self, file):
        data = self.data_sarc.get_file(file).data.tobytes()
        pio = oead.aamp.ParameterIO.from_binary(data)
        return pio

def update_sarc(pio, data, old_name, new_name):
    data.data_writer.files[new_name] = oead.aamp.ParameterIO.to_binary(pio)
    if old_name in data.data_writer.files and old_name != new_name:
        del data.data_writer.files[old_name]

def set_sarc_endian(sarcwriter):
    if get_endianness():
        SarcWriter.set_endianness(sarcwriter, oead.Endianness.Big)
    else:
        SarcWriter.set_endianness(sarcwriter, oead.Endianness.Little)