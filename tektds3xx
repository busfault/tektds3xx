
import argparse
import datetime
import io
import sys

import pyvisa
from PIL import Image


class Tektds3xxGPIB(): #This doesn't work to inherit :( pyvisa.ResourceManager):
    __outFilenamePrefix = "tekTDS340"
    def __init__(self, GPIBNum, GPIBAddr):
        self.__rm = pyvisa.ResourceManager()
        self.GPIBNum = GPIBNum
        self.GPIBAddr = GPIBAddr
        self._instr = self._open()


    @property
    def GPIBNum(self):
        return self._GPIBNum

    @GPIBNum.setter
    def GPIBNum(self, value):
        #if type(value) not int or value <= 0:
        #    raise ValueError(f'GPIBNum must be integer type and >= 0')
        self._GPIBNum = value

    @property
    def GPIBAddr(self):
        return self._GPIBAddr

    @GPIBAddr.setter
    def GPIBAddr(self, value):
        #if type(value) not int or value <= 0:
        #    raise ValueError(f'GPIBAddr must be integer type and >= 0')
        self._GPIBAddr = value
    
    @property
    def hardcopyFormat(self):
        return self._query('HARDC:FORM?')

   # @hardcopyFormat.setter
   # def hardcopyFormat(self, frmt):
        

    def _open(self):
        return self.__rm.open_resource(f'GPIB{self.GPIBNum}::{self.GPIBAddr}::INSTR')

    def get_hardcopy_image(self):
        self._hardcopy_start()
        img = None
        try:
            data = self._instr.read_raw()
            img = Image.open(io.BytesIO(data)).rotate(angle=-90, expand=True)
        except pyvisa.VisaIOError as e:
            print(f'Error: {e}')
        except error as e:
            print(f'{e}')
        return img


    def _hardcopy_start(self):
        self._write('HARDC STAR')
        
    def hardcopy(self):
        hardcopyFormat = self.hardcopyFormat
        TIMESTAMP = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        hardcopyFilename = f'{self.__outFilenamePrefix}_{TIMESTAMP}.{hardcopyFormat.lower().strip()}'
        self.get_hardcopy_image().save(hardcopyFilename)



    def _write(self, cmd):
        return self._instr.write(cmd)

    def _query(self, query):
        return self._instr.query(query).strip()
        

def list_devices():
    return pyvisa.ResourceManager().list_resources()



if __name__ == '__main__':
    

    argParser = argparse.ArgumentParser()
    argParser.add_argument('--list', action='store_true', help="GPIB list")
    argParser.add_argument('gpib_num', nargs='?', default=0, type=int, help="GPIB Controller Number.")
    argParser.add_argument('gpib_addr', nargs='?', default=0,type=int, help="GPIB Instrument Address.")
    args = argParser.parse_args()

    if args.list:
        print(list_devices())
        sys.exit(0)
    rm = Tektds3xxGPIB(args.gpib_num,args.gpib_addr)
    rm.hardcopy()
    #print(rm)


    #__TIMESTAMP__ = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    #outFilenamePrefix = f'tek'
    #rm = pyvisa.ResourceManager()
    #print(rm)
    #print(rm.list_resources())
    #tdsGpib = rm.open_resource(f'GPIB4::4::INSTR')
    ##print(tdsGpib)
    ##print(tdsGpib.query('*IDN?'))
    ##Clear errors
    ##print(tdsGpib.write('*CLS'))
    ##start a hardcopy
    #hardcopyFormat = tdsGpib.query('HARDCOPY:FORMAT?')
    ##print(f'HARDCOPY:FORMAT? :{hardcopyFormat}')
    #tdsGpib.write('HARDCOPY START')
    #hardcopyFilename = f'{outFilenamePrefix}_{__TIMESTAMP__}.{hardcopyFormat.lower().strip()}'
    #print(f'Starting Hardcopy to {hardcopyFilename}')
    #try:
    #    data = tdsGpib.read_raw()
    #    with open(hardcopyFilename,'wb') as outFile:
    #        outFile.write(data)
    #    # Fix image rotation:
    #    print('File saved, rotating image')
    #    img = Image.open(hardcopyFilename)
    #    img = img.rotate(angle=-90, expand=True)
    #    img.save(hardcopyFilename)
    #except pyvisa.VisaIOError as e:
    #    print(f'Error: {e}')
    #except error as e:
    #    print(f'{e}')
    #finally:
    #    print('Complete')
