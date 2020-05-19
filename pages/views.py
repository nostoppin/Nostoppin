from django.shortcuts import render

def home(request):
	return render(request,"home.html",{})

def about(request):
	from pages.contactme import academic_details
	from pages.contactme import hobbies

	myname = "Hello my name is Himadri Roy"
	return render(request,"about.html",{"myname":myname,"academic":academic_details(),"hobby":hobbies()})


def contact(request):
	from pages.contactme import contact

	return render(request,"contact.html",{"myemail": contact()})

def content(request):
	from pages.content import abt_contentpage_line1
	
	return render(request,"content.html",{'line1':abt_contentpage_line1()})

def lastpage(request):
	from pages.lastpage import lastpageline
	from pages.lastpage import lastpageline1

	return render(request,"lastpage.html",{'lastpageline':lastpageline(),'lastpageline1':lastpageline1()})