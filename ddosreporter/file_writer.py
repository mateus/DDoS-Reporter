# -*- coding: utf-8 -*-

from datetime import datetime


class File_writer():
    '''
    Class to write in the log file the new blocked IPs
    '''

    def logAppend(self, data):
        '''
        Writes in the log file the new blocked IPs

        Args:
            data (str) - Data to append in the log file
        '''
        today = datetime.now()

        day = today.day
        if day < 10:
            day = '0{}'.format(day)
        month = today.month
        if month < 10:
            month = '0{}'.format(month)
        year = today.year
        hour = today.hour
        if hour < 10:
            hour = '0{}'.format(hour)
        minute = today.minute
        if minute < 10:
            minute = '0{}'.format(minute)
        second = today.second
        if second < 10:
            second = '0{}'.format(second)
        with open('ddosreporter.log', 'a') as f:
            f.write('{}/{}/{} {}:{}:{} - {}'.format(
                day, month, year, hour, minute, second, data))
