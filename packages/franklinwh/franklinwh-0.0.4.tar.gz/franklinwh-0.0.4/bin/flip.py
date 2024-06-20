"""Test script that basically turns the switch off and back on again so I can test without throwing secrets in git history"""
import logging
log = logging.getLogger(__name__)

from franklinwh import TokenFetcher, Client

class Tester(object):

    def __init__(self, client):
        self.client = client

    def turn_on(self, **kwargs):
        """Turn the switch on."""
        log.info("turn_on entry")
        res = self.client._mqtt_send(b'{"cmdType":311,"equipNo":"10050001A05F22400475","type":0,"timeStamp":1708634580,"snno":3,"len":1019,"crc":"5A9B9A49","dataArea":{"backupMaxSoc":100,"BBBackupSoc":20,"CarSwConsSupEnable":0,"CarSwConsSupEnerge":0,"CarSwConsSupStartTime":"","custom":"","genStartSoc":0,"genStat":0,"genStopSoc":0,"GridChargeEn":0,"gridVoltCheck":0,"opt":1,"order":"10050001A05F22400475","runingMode":9323,"selfMinSoc":15,"stopMode":0,"stromEn":1,"Sw1AtuoEn":0,"Sw1Freq":1,"Sw1Mode":1,"Sw1MsgType":1,"Sw1Name":"","Sw1ProLoad":0,"Sw1SocLowSet":0,"Sw1Time":["2024-02-24 02:00","2024-02-24 07:00","2000-01-01 00:00","2000-01-01 23:59"],"Sw1TimeEn":[0,0,0,0],"Sw1TimeSet":[1,0,1,0],"Sw2AtuoEn":0,"Sw2Freq":1,"Sw2Mode":1,"Sw2MsgType":1,"Sw2Name":"","Sw2ProLoad":0,"Sw2SocLowSet":0,"Sw2Time":["2024-02-24 02:00","2024-02-24 07:00","2000-01-01 00:00","2000-01-01 23:59"],"Sw2TimeEn":[0,0,0,0],"Sw2TimeSet":[1,0,1,0],"Sw3AtuoEn":0,"Sw3Freq":15,"Sw3Mode":0,"Sw3MsgType":0,"Sw3Name":"","Sw3ProLoad":0,"Sw3SocLowSet":0,"Sw3Time":["2000-01-01 00:00","2000-01-01 23:59","2000-01-01 00:00","2000-01-01 23:59"],"Sw3TimeEn":[0,0,0,0],"Sw3TimeSet":[1,0,1,0],"SwMerge":1,"touMinSoc":20}}')
        self.client._mqtt_send(b'{"cmdType":311,"equipNo":"10050001A05F22400475","type":0,"timeStamp":1708634582,"snno":4,"len":40,"crc":"CA30F49F","dataArea":{"opt":0,"order":"10050001A05F22400475"}}')
        self.client._mqtt_send(b'{"cmdType":311,"equipNo":"10050001A05F22400475","type":0,"timeStamp":1708634582,"snno":5,"len":40,"crc":"CA30F49F","dataArea":{"opt":0,"order":"10050001A05F22400475"}}')
        log.info("turn_on exit")


    def turn_off(self, **kwargs):
        """Turn the switch off."""
        log.info("turn_off entry")
        self.client._mqtt_send(b'{"cmdType":311,"equipNo":"10050001A05F22400475","type":0,"timeStamp":1708634586,"snno":6,"len":1019,"crc":"13402D8A","dataArea":{"backupMaxSoc":100,"BBBackupSoc":20,"CarSwConsSupEnable":0,"CarSwConsSupEnerge":0,"CarSwConsSupStartTime":"","custom":"","genStartSoc":0,"genStat":0,"genStopSoc":0,"GridChargeEn":0,"gridVoltCheck":0,"opt":1,"order":"10050001A05F22400475","runingMode":9323,"selfMinSoc":15,"stopMode":0,"stromEn":1,"Sw1AtuoEn":0,"Sw1Freq":1,"Sw1Mode":0,"Sw1MsgType":1,"Sw1Name":"","Sw1ProLoad":1,"Sw1SocLowSet":0,"Sw1Time":["2024-02-24 02:00","2024-02-24 07:00","2000-01-01 00:00","2000-01-01 23:59"],"Sw1TimeEn":[0,0,0,0],"Sw1TimeSet":[1,0,1,0],"Sw2AtuoEn":0,"Sw2Freq":1,"Sw2Mode":0,"Sw2MsgType":1,"Sw2Name":"","Sw2ProLoad":1,"Sw2SocLowSet":0,"Sw2Time":["2024-02-24 02:00","2024-02-24 07:00","2000-01-01 00:00","2000-01-01 23:59"],"Sw2TimeEn":[0,0,0,0],"Sw2TimeSet":[1,0,1,0],"Sw3AtuoEn":0,"Sw3Freq":15,"Sw3Mode":0,"Sw3MsgType":0,"Sw3Name":"","Sw3ProLoad":0,"Sw3SocLowSet":0,"Sw3Time":["2000-01-01 00:00","2000-01-01 23:59","2000-01-01 00:00","2000-01-01 23:59"],"Sw3TimeEn":[0,0,0,0],"Sw3TimeSet":[1,0,1,0],"SwMerge":1,"touMinSoc":20}}')
        self.client._mqtt_send(b'{"cmdType":311,"equipNo":"10050001A05F22400475","type":0,"timeStamp":1708634588,"snno":7,"len":40,"crc":"CA30F49F","dataArea":{"opt":0,"order":"10050001A05F22400475"}}')
        self.client._mqtt_send(b'{"cmdType":311,"equipNo":"10050001A05F22400475","type":0,"timeStamp":1708634588,"snno":8,"len":40,"crc":"CA30F49F","dataArea":{"opt":0,"order":"10050001A05F22400475"}}')
        log.info("turn_off exit")

    def get_status(self):
        payload = b'{"lang":"EN_US","equipNo":"10050001A05F22400475","cmdType":203,"len":25,"timeStamp":1718761302,"snno":1,"crc":"6FC3A6BF","type":0,"dataArea":{"opt":1,"refreshData":1}}'
        res = self.client._mqtt_send(payload)
        return res

if __name__ == '__main__':
    username = 'healey.rich@gmail.com'
    password = 'tugky8-xaqheR-wixzym'
    gateway = '10050001A05F22400475'

    fetcher = TokenFetcher(username, password)

    client = Client(fetcher, gateway)
    tester = Tester(client)

    print("tester")
    print(tester.get_status())
    print()
    print("mqtt")
    print(client.get_status())
