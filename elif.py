print("let's get started")
spy_name = raw_input("whats is your user name? : ")

if len(spy_name) > 0:
    print ' welcome ' + spy_name + 'Glad to have back with us'

    spy_saluation=raw_input("should i call u miss or mister? : ")
    spy_name = spy_saluation + " " + spy_name
    print " Alright " + spy_name + " I'd like to know littel more about u before we processed "
else:
    print "A spy must have a valid name.Try again please"
