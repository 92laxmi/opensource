from django.shortcuts import render

def cal(request):
    c=''
    try:
      if request.method=='POST':
        n1=eval(request.POST.get('num1'))
        n2=eval(request.POST.get('num2'))
        opr=request.POST.get('opr')
        if opr=='add':
           c=n1+n2
        elif opr=='sub':
           c=n1-n2
        elif opr=='mul':
           c=n1*n2
        elif opr=='div':
           c=n1/n2

    except:
     print(c)  
    return render(request,"index.html", {'c':c})
 

