from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Lead, Agent
from .forms import LeadForm

# Create your views here.

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
        lead_form = LeadForm(request.POST)

        agent = Agent.objects.first()
        # Checking if the form is valid before entering
        # the details into database.
        if lead_form.is_valid():
            lead = Lead.objects.create(
                first_name=request.POST['first_name'], 
                last_name=request.POST['last_name'],
                age=request.POST['age'],
                agent=agent
            )
            # Redirecting the user to the list of all the leads,
            # once the details are entered for the new lead
            # so, that the new lead can see him/herself in the list.
            return HttpResponseRedirect("/leads/all")
        
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
            "form":LeadForm()
        })

