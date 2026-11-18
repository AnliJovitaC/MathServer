from django.shortcuts import render

def Calculate_Churn_Rate(request):
    
        initial_cust=int(request.POST.get("Initial_Customer",'0'))
        present_cust=int(request.POST.get("Present_Customer",'0'))
        churn_rate=(initial_cust/present_cust*100)if request.method=='POST' else 0
        print("Initial_Customer=",initial_cust)
        print("Present_Customer=",present_cust)
        print("Churn Rate=", churn_rate)

        return render(request, "Anliapp/cal_churn.html",{"initial_cust": initial_cust, "present_cust": present_cust, "churn_rate": churn_rate})
