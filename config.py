# Baiskoafu loagin details
username = "sotti"
password = "1234567890,,"

def media_quality(quality='high'):

    q = ['high', 'low', 'medium']

    if quality == q[0]: return q[0]
    if quality == q[1]: return q[1]
    if quality == q[2]: return q[2]
    return q[2] # < --- default is medium

media_quality() # ['high', 'low', 'medium']
ASK_BEFORE_DOWNLOAD = False	# set 'False' for automatic download
IS_PRIMARY_DEVICE   = False	# set 'True' only if you have premium subscription
