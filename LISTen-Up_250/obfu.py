num=list()
num2=0
word=list()
word2="My naMk Rs {jamEa} and I {ikq gEttiag obfusc}rted cu{e!"
while (num2<11):
    num.append(num2)
    word.append(word2[num2+5])
    num2+=1
s="?????" #start here
y="".join(s)
s=list(s)
if len(s)>26 or "".join(s[18::2])!="flag" or s.pop()!="}" or "".join(s[0:4])!="flag" or "a".join(s[len(s)-6::2]) != "laaag" or "".join(word[i] for i in (6,3,10,1)) != "".join(s[4:8]) or "".join(s[14:18]) != "".join([chr(72),chr(ord('e')),'e','_']) or "".join(s[8:14])!="t_1s_t": #thought we'd reward you with an easy last one :p
    print "rekt"
else:
    print "FLAG IS " + y