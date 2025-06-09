# (c)2025 Thomas Middleton
# 
#  command line tool

# Python Libraries
import argparse


# 3rd party Libraries


# Local Libraries
import tektds3xx


def main():
    '''
    ''' 
    argparser = argparse.ArgumentParser()
    argParser.add_argument('--list', action='store_true', help="GPIB list")
    argParser.add_argument('gpibNum', nargs='?', default=0, type=int, help="GPIB Controller Number.")
    argParser.add_argument('gpibAddr', nargs='?', default=0,type=int, help="GPIB Instrument Address.")
    args = argParser.parse_args()

    if args.list:
        print(tektds3xx.list_devices())
        return 0

    rm = tektds3xx.TekTDS3xxGPIB(args.gpibNum, args.gpibAdr)
    rm.hardcopy()
    

if __name__ == '__main__':
    sys.exit(main())
