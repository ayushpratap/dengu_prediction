#import pysvn
from optparse import OptionParser
import os
import sys
import json

class COREACCESS(OptionParser, object):
    def __init__(self):
        '''
        @brief: Initializes a new .
        @param: None
        @raise: None
        '''
        super(COREACCESS, self).__init__()
        self.usage="usage: %prog {\
                    \n\t{-s|--state} <State> | \
                    \n\t{-d|--district} <District> | \
                    \n\t{-b|--block} <Block> | \
                    \n\t{-g|--gp} <GP>}"
        self.__cmdArgs = {}
        self.__filesInScope = []
        self.__moduleList = []
        (optionArgsMap, args) = self.__parseArguments()
        self.__cmdArgs["state"] = optionArgsMap.state
        self.__cmdArgs["district"] = optionArgsMap.district
        self.__cmdArgs["block"] = optionArgsMap.block
        self.__cmdArgs["gp"] = optionArgsMap.gp

        #Test Prints
        print "state: %s" %self.__cmdArgs["state"]
        print "district: %s" %self.__cmdArgs["district"]
        print "block: %s" %self.__cmdArgs["block"]
        print "gp: %s" %self.__cmdArgs["gp"]

    def error(self, msg=None):
        '''
        @brief: OptionParser error() method overriden 
        - Raised in case of any error while parsing or validating user input.
        - It will print Option parser usage and will exit.
        @param msg: (String) Error message to be printed on terminal.
        @return: None
        @raise: None
        '''
        print "%s" %self.usage
        if msg:
            print "***Error: %s" %msg
        else:
            print "Please enter the command again as per above command format"
        sys.exit(1)

    def __parseArguments(self):
        '''
        @brief: Add options for parsing user input.
        Validates user input after parsing.
        @param: None
        @return: None
        @raise: None
        '''
        self.add_option(
                        "-s",
                        "--state",
                        dest = "state",
                        type = "string",
                        action = "callback",
                        callback = self.__isOptionValueSet,
                        help = "state variable slected by the callee"
                        )
        self.add_option(
                        "-d",
                        "--district",
                        dest = "district",
                        type = "string",
                        action = "callback",
                        callback = self.__isOptionValueSet,
                        help = "district variable slected by the callee"
                        )
        self.add_option(
                        "-b",
                        "--block",
                        dest = "block",
                        type = "string",
                        action = "callback",
                        callback = self.__isOptionValueSet,
                        help = "block variable slected by the callee"
                        )
        self.add_option(
                        "-g",
                        "--gp",
                        dest = "gp",
                        type = "string",
                        action = "callback",
                        callback = self.__isOptionValueSet,
                        help = "gp variable slected by the callee"
                        )



        (optionArgsMap, args) = self.parse_args()
        #self.__validateUserInput(args)
        return (optionArgsMap, args)

    def __isOptionValueSet(self, option, opt, value, parser):
        '''
        @brief: Ensures that option is specified only once on command line
        @param option: (Instance) Option instance that.s calling the callback
        @param opt: (String) option string on the command-line that.s triggering the callback
        @param value: (String) argument to this option on the command-line
        @param parser: (Instance) OptionParser instance
        @return: None 
        @raise: None
        '''
        if parser.values.ensure_value(option.dest, None):
            self.error()
            #logError("Option %s is already specified" % option)
        setattr(parser.values, option.dest, value)

    def __validateUserInput(self):
        '''
        @brief: Validates user input.
        @param args: (List) list of extra arguments passed on command-line
        @return: None
        @raise: None
        '''
        self.__validateFilePath()

    def __getJSONfromElastic(self):
        '''
        @brief: Validates file-path
        @param : None
        @return: None
        @raise: None
        '''

    def getJSON(self):
        '''
        @brief: Fetches village specific JSON object 
        @param: None
        @return: None
        @raise: None
        '''
        jsonObj = self.__getJSONfromElastic()
        #Update JSON Object
        return jsonObj


def main():
    try:
        COREACCESSObj = COREACCESS()
        jsonObj = COREACCESSObj.getJSON()
        return jsonObj
    except Exception as ex:
        print ex

if __name__ == "__main__":
    main()
