#impor.search(index='test-index', filter_path=['hits.hits._*'])es.search(index='test-index', filter_path=['hits.hits._*']): pysvn
from optparse import OptionParser
import os
import sys
import time
from elasticsearch import Elasticsearch

class MiniCORE(OptionParser, object):
    def __init__(self):
        '''
        @brief: Initializes a new .
        @param: None
        @raise: None
        '''
        super(MiniCORE, self).__init__()
        self.__defineDataInput = ['gp-to-gpn','state-infant_mortility','state-telephone']
        self.execute()

    def __executeDataParse(self):
        '''
        @brief: Execute Data Parse
        @param : None
        @return: None
        @raise: None
        '''
        self.__esObj = Elasticsearch()
        #for item in self.__defineDataInput:
            
        
    def __logstashParse(self):
        '''
        @brief: Validates file-path
        @param : None
        @return: None
        @raise: None
        '''
        #os.execv("/home/ubuntu/logstash-5.6.4/bin/logstash",["-f "+ self.__defineDataInput[1] +".conf"]) 
        #os.execv("/home/ubuntu/logstash-5.6.4/bin/logstash",["-f "+ self.__defineDataInput[2] +".conf"]) 
        #os.execv("/home/ubuntu/logstash-5.6.4/bin/logstash",["-f "+ self.__defineDataInput[3] +".conf"])
        os.execl("/home/ubuntu/logstash-5.6.4/bin/logstash"," -f logstash_conf/gp-to-gpn.conf") 
        os.execl("/home/ubuntu/logstash-5.6.4/bin/logstash"," -f logstash_conf/state-infant_mortility.conf") 
        os.execl("/home/ubuntu/logstash-5.6.4/bin/logstash"," -f logstash_conf/state-telephone.conf")
        time.sleep(10) 

    def execute(self):
        '''
        @brief: Initiates node-info command
        @param: None
        @return: None
        @raise: None
        '''
        self.__logstashParse()
        self.__executeDataParse()

def main():
    try:
        miniCOREObj = MiniCORE()
    except Exception as ex:
        print ex

if __name__ == "__main__":
    main()
