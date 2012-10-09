VERSION = (1, 0, 0, 'BETA')


def get_version():
    '''
    Gets the actual version of DDoSReporter

    Returns the version of DDoSReporter as String (str)
    '''
    version = '%s.%s.%s %s' % (VERSION[0], VERSION[1], VERSION[2], VERSION[3])
    return version
