import re
dictipa = open("cmudict.txt")
#frasetemp = "The official documentation is"
frasetemp= open ("romeo.txt").read()
fraseipa= dict()
frase= list ()
frase = frasetemp.lower().split()
frasefinal= list()

print "fase 1"
count = 0

for line in dictipa :

    k =  line.split("	")[0]
    if ( str (k)  in  fraseipa) :
        v.append ([ line.split("	")[1] ])
        fraseipa.update ({k:[v]})
    else :
        v = [ line.split("	")[1] ]
        fraseipa.update ({k:v})

for word in frase :
    frasefinal.append( fraseipa.get (word) )

print frasefinal
