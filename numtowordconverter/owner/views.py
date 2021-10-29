from django.shortcuts import render,redirect

from owner import forms

from owner.models import owner
def Num_to_str(request):
    if request.method=="GET":
        form =forms.NumtostringForm(initial={})
        # form=BookForm()
        context={}
        context["form"]=form

        return render (request,"num_to_str_converter.html",context)
    if request.method == "POST":

        form=forms.NumtostringForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect("Numtostrconverter")
        else:

            return render(request,"num_to_str_converter.html",{"form":form})
