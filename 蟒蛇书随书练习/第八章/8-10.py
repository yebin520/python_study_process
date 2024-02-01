#8-10.py
def send_messages(mess):
    while mess:
        ms_temp = mess.pop()
        print (ms_temp)
        sent_messages.append(ms_temp)

def show_messages(mss):
    for ms in mss:
        print (ms)

messages = ['Hi!','Hello','Like you','Love you']
sent_messages = []
send_messages(messages[:])
show_messages(sent_messages)
show_messages(messages)