def check():
    word = ['M', 'k', ' ', 'R', 's', ' ', '{', 'j', 'a', 'm', 'E']
    word2="My naMk Rs {jamEa} and I {ikq gEttiag obfusc}rted cu{e!"
    s="flag{REkt_1s_tHee_fllaagg}" # start here
    y="".join(s) # same as s
    s=list(s)
    if len(s) > 26:
        return
    print "Checkpoint 1"
    if "".join(s[18::2]) != "flag":
        return
    print "Checkpoint 2"
    if s.pop() != "}":
        return
    print "Checkpoint 3"
    if "".join(s[0:4]) != "flag":
        return
    print "Checkpoint 4"
    if "".join(s[len(s)-6::2]) != "lag":
        return
    print "Checkpoint 5"
    if [word[i] for i in (6,3,10,1)] != s[4:8]:
        print [word[i] for i in (6,3,10,1)]
        print s[4:8]
        return
    print "Checkpoint 6"
    if "".join(s[14:18]) != "Hee_":
        return
    print "Checkpoint 7"
    if "".join(s[8:14])!="t_1s_t": #thought we'd reward you with an easy last one :p
        return

    print "FLAG IS " + y

check()
