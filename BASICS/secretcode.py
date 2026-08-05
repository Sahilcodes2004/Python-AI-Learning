import random
import string
st=input("Enter the message")
print("What you want:\n 1.CODING \n 2.DECODING ")
coding=input("1 for coding and 0 for decoding").strip()
coding=True if (coding=="1") else False
print(coding)

words=st.split(" ")

if(coding):
  nwords=[]
  for word in words:
    if(len(word)>=3):
      t1="".join(random.choices(string.ascii_lowercase,k=3))
      t2="".join(random.choices(string.ascii_lowercase,k=3))
      stnew=t1+word[1:]+word[0]+t2
      nwords.append(stnew)
    else:
      nwords.append(word[::-1])
  print(" ".join(nwords))
else:
  nwords=[]
  for word in words:
    if(len(word)>=3):
      trimmed=word[3:-3]
      if(len(trimmed)>0):
       stnew=trimmed[-1]+trimmed[:-1]
      else:
        trimmed=stnew
      nwords.append(stnew)
    else:
      stnew=word[::-1]
      nwords.append(stnew)
  print(" ".join(nwords))
  
         

    