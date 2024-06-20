# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 15:10:57 2021
class object for connection testing with requests to speed.cloudflare.com
runs tests and stores results in dictionary
cloudflare(thedict=None,debug=False,print=True,downtests=None,uptests=None,latencyreps=20)

thedict: dictionary to store results in
    if not passed in, created here
    if passed in, used and update - allows keeping partial results from previous runs
    each result has a key and the entry is a dict with "time" and "value" items
debug: True turns on io logging for debugging
printit: if true, results are printed as well as added to the dictionary
downtests: tuple of download tests to be performed
    if None, defaultdowntests (see below) is used
    format is ((size, reps, label)......)
        size: size of block to download
        reps: number of times to repeat test
        label: text label for test - also becomes key in the dict
uptests: tuple of upload tests to be performed
    if None, defaultuptests (see below) is used
    format is ((size, reps, label)......)
        size: size of block to upload
        reps: number of times to repeat test
        label: text label for test - also becomes key in the dict
latencyreps: number of repetitions for latency test

version 1.8.0
removed dependency on ipdatabase.com
added getfulldata to get all data about test locs and isp from cloudflare
getcolo, getcolodetails, and getisp deprecated but left functional

version 1.8.1 (courtesey of Martin Brose)
removed numpy dependencies to reduce footprint in docker environments

version 1.8.2
changed cloudflare endpoint URLs to use https

@author: /tevslin
"""

class cloudflare:
    #tests changed 1/1/22 to mirror those done by web-based test
    uploadtests=((101000,8,'100kB'),(1001000, 6,'1MB'),(10001000, 4,'10MB'))
    downloadtests=((101000, 10,'100kB'),(1001000, 8,'1MB'),(10001000, 6,'10MB'),(25001000, 4,'25MB'))
    version="1.8.0" #7/1/23
    version="1.8.1" #8/17/23
    version="1.8.2" #6/18/24
    def __init__(self,thedict=None,debug=False,printit=True,downtests=None,uptests=None,latencyreps=20,timeout=(3.05,25)):

        import requests
        
        if debug:
            import logging
            
            # Enabling debugging at http.client level (requests->urllib3->http.client)
            # you will see the REQUEST, including HEADERS and DATA, and RESPONSE with HEADERS but without DATA.
            # the only thing missing will be the response.body which is not logged.
            try: # for Python 3
                from http.client import HTTPConnection
            except ImportError:
                from httplib import HTTPConnection
            HTTPConnection.debuglevel = 1
            
            logging.basicConfig() # you need to initialize logging, otherwise you will not see anything from requests
            logging.getLogger().setLevel(logging.DEBUG)
            requests_log = logging.getLogger("urllib3")
            requests_log.setLevel(logging.DEBUG)
            requests_log.propagate = True
            requests.get('https://httpbin.org/headers')

        self.debug=debug
        self.printit=printit
        self.latencyreps=latencyreps
        
        self.thedict={} if thedict is None else thedict
        if not downtests is None:
            self.downloadtests=downtests
        if not uptests is None:
            self.uploadtests=uptests
        self.mequests=requests.Session()
        self.timeout=timeout

    def getcolo(self):
    # retrieves cloudflare colo, user ip address 
    # deprecated but left for compatability
        colo,ip,org,region,city=self.getfulldata()
        return colo,ip
    
    def getisp(self,ip):
    # retrieves ISP
    # deprecated but left for compatability
        colo,ip,org,region,city=self.getfulldata()
        return org
    
    def getcolodetails(self,colo):
        #retrieves region and city for cf gateway
        # deprecated but left for compatability
        colo,ip,org,region,city=self.getfulldata()
        return region,city

    
    def getfulldata(self):
    # retrieves cloudflare colo, user ip address, ISP, city, and region
        r=self.mequests.get('https://speed.cloudflare.com/meta')       
        dicty=r.json()
        return dicty['colo'],dicty['clientIp'],dicty['asOrganization'],dicty['region'],dicty['city']

    def download(self,numbytes,iterations):
        #runs download tests
        import os
        from contextlib import nullcontext
        import time
        if os.name == 'nt':
            import wres
        fulltimes=() #list for all successful times
        servertimes=() #times reported by server
        requesttimes=() #rough proxy for ttfb
        if os.name == 'nt':
            cm = wres.set_resolution()
        else:
            cm = nullcontext()
        with cm:
            for i in range(iterations):
                start=time.time()
                err=False
                try: 
                    r=self.mequests.get('https://speed.cloudflare.com/__down?bytes='+str(numbytes),timeout=self.timeout)
                    end=time.time()
                except:
                    err=True
                if not err:
                    fulltimes=fulltimes+(end-start,)
                    servertimes=servertimes+(float(r.headers['Server-Timing'].split('=')[1])/1e3,)
                    requesttimes=requesttimes+(r.elapsed.seconds+r.elapsed.microseconds/1e6,)
        return (fulltimes,servertimes,requesttimes)

    def upload(self,numbytes,iterations):
        #runs upload tests
        servertimes=() #times reported by server
        thedata=bytearray(numbytes)
        for i in range(iterations):
            err=False
            try: 
                r=self.mequests.post('https://speed.cloudflare.com/__up',data=thedata,timeout=self.timeout)
            except:
                err=True
            if not err:
                servertimes=servertimes+(float(r.headers['Server-Timing'].split('=')[1])/1e3,)
        return (servertimes)

    def sprint(self,label,value):
        "time stamps entry and adds to dictionary replacing spaces with underscores in key and optionally prints"
        import time
        if self.printit:
            print(label+":",value)
        self.thedict[label.replace(' ','_')]={"time":time.time(),"value":value} #add to dictionary
        

    def calculate_percentile(self, data, percentile):
        """
        Find the percentile of a list of values.

        Input:
        data - is a list of values.
        percent - a float value from 0.0 to 1.0.

        Output: the percentile of the values
        """
        sorted_data = sorted(data)
        index = (percentile / 100) * (len(sorted_data)-1)

        if index.is_integer():
            return sorted_data[int(index)]
        else:
            lower_index = int(index)
            upper_index = lower_index + 1
            d0 = sorted_data[int(lower_index)] * (upper_index-index)
            d1 = sorted_data[int(upper_index)] * (index-lower_index)
            return d0+d1

    def runalltests(self):
        #runs full suite of tests
        import array
        import statistics
        
        self.sprint('version',self.version)
        colo,ip,isp,region,city=self.getfulldata() 
        self.sprint('your ip',ip)
        self.sprint('your ISP',isp)
        self.sprint('test location code',colo)
        self.sprint ('test location city',city)
        self.sprint ('test location region',region)        
        fulltimes,servertimes,requesttimes=self.download(1,self.latencyreps) #measure latency and jitter
        latencies= [(requesttimes[i] - servertimes[i])*1e3 for i in range(len(requesttimes))]
        jitter=statistics.median([abs(latencies[i]-latencies[i-1]) for i in range(1,len(latencies))])
        self.sprint ('latency ms',round(statistics.median(latencies),2))
        self.sprint ('Jitter ms',round(jitter,2))
        
            
        alltests=()
        
        for tests in self.downloadtests:
            fulltimes,servertimes,requesttimes=self.download(tests[0],tests[1])
            downtimes = array.array('f',[fulltimes[i] - requesttimes[i] for i in range(len(fulltimes))])
            downspeeds = [tests[0]*8 / downtimes[i] / 1e6 for i in range(len(downtimes))]
            self.sprint(tests[2]+' download Mbps',round(statistics.mean(downspeeds),2))
            for speed in downspeeds:
                alltests=alltests+(speed,)
    
        self.sprint('90th percentile download speed',round(self.calculate_percentile(alltests,90),2))
        
        alltests=()
        for tests in self.uploadtests:
            servertimes=self.upload(tests[0],tests[1])
            upspeeds = [tests[0]*8 / servertimes[i] / 1e6 for i in range(len(servertimes))]
            self.sprint(tests[2]+' upload Mbps',round(statistics.mean(upspeeds),2))
            for speed in upspeeds:
                alltests=alltests+(speed,)
        
        self.sprint('90th percentile upload speed',round(self.calculate_percentile(alltests,90),2))
        return(self.thedict)
