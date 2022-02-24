from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Lead, Agent
from .forms import LeadModelForm, LeadForm

# Create your views here.

def landing_page(request):
    return render(request, "landing.html")



def lead_list(request):
    leads = Lead.objects.all()
    context = {
        "leads": leads
        }
    return render(request, "leads/lead_list.html", context)



def lead_detail(request, pk):
    lead = Lead.objects.get(id=pk)
    context = {
        "lead": lead
    }
    return render(request, "leads/lead_detail.html", context)



def lead_entry_form(request):
    '''
    This function/view will load the form and will help a new lead register.
    '''
    # When the form is submitted,
    if request.method=="POST":
        lead_form = LeadModelForm(request.POST)

        # Checking if the form is valid before entering
        # the details into database.
        if lead_form.is_valid():
            lead_form.save()
            # Redirecting the user to the list of all the leads,
            # once the details are entered for the new lead
            # so, that the new lead can see him/herself in the list.
            return redirect("/leads/all")
        
        else:
            # If the form is not valid, i.e. in the else
            # condition return the same form back to the user
            # in order to input the details in a correct manner.
            return render(request, "leads/lead_entry_form.html", {
                "form": lead_form
            })
    else:
        # If the request.method!="POST", then we need to GET the 
        # lead with the form page. Hence, rendering an empty form
        # page to the new lead.
        return render(request, "leads/lead_entry_form.html", {
            "form":LeadModelForm()
        })


# def lead_update(request, pk):
#     '''
#     This view/function is used for updating an existing Lead's info.
#     '''
#     lead = Lead.objects.get(id=pk)
#     lead_form = LeadModelForm(instance=lead)
    
#     # When the form is submitted,
#     if request.method=="POST":
#         lead_form = LeadModelForm(request.POST, instance=lead)

#         # Checking if the form is valid before entering
#         # the details into database.
#         if lead_form.is_valid():
#             lead_form.save()
#             # Redirecting the user to the list of all the leads,
#             # once the details are entered for the new lead
#             # so, that the new lead can see him/herself in the list.
#             return redirect("/leads/all")
#     context = {
#          "lead": lead,
#          "form": LeadForm()
#      }
#     return render(request, "leads/lead_update.html", context)



def lead_update(request, pk):
    '''
    This view/function is used for updating an existing Lead's info.
    '''
    lead = Lead.objects.get(id=pk)


    if request.method=="POST":
       lead_form = LeadForm(request.POST)
       if lead_form.is_valid():
           first_name = lead_form.cleaned_data['first_name']
           last_name = lead_form.cleaned_data['last_name']
           age = lead_form.cleaned_data['age']
           lead.first_name = first_name
           lead.last_name = last_name
           lead.age = age
           lead.save()
           return redirect('/leads/all')
           
    context = {
        "lead": lead,
        "form": LeadForm()
    }
    return render(request, "leads/lead_update.html", context)



def lead_delete(request, something):
    lead = get_object_or_404(Lead, id=something)
    lead.delete()
    return redirect("/leads/all")