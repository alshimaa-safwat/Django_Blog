from django.shortcuts import render

def get_subscribe_data(request):
	userId = request.user.id
	catNum = request.GET['catNum']
	refresh = request.GET['refresh']
	cat=[]
	sub=[]
	if refresh=='1':
		subscribes = Subscribes
		for x in subscribes.objects.filter(user_name_id=userId):
			if x.user.id==userId:
				cat.append(x.Category.id)
			else:
				pass
	else:
		subscribes, created = Subscribes.objects.get_or_create(user_id=userId, Category_id=catNum)
		if created==True:
			cat.append(subscribes.Category.id)
			try:
				user=request.user
				cato=Category.objects.get(id=catNum)
				subject = 'category subscription'
				message = 'u have subscibed in :' +cato.name+' use this url to visit this category http://127.0.0.1:8000/posts/listcat/'+str(cato.id)
				recepient = user.email
				send_mail(subject,message, 'osamaeltayar011100', [recepient], fail_silently = False)
			except Exception as e:
				print(e)
			
		else:
			subscribes.delete()
	return HttpResponse(json.dumps({'categoryNum':cat}))


def add_Comment(request,postid): #the worst function i had done shitty code i know 
	if request.method=="POST":
		post= Post.objects.get(id=postid)
		uname = request.user # we have to replace it with auth user 
		con = request.POST.get('message')
		mptrn= r"^[\S][\S ]+$"
		result = re.match(mptrn, con)
		if (result):
			words =ForrbiddenWord.objects.all()
			for word in words:
				rep=""
				size=len(word.word)
				for i in range(size):
					rep+="*"
				con = con.replace(word.word,rep)
			comm = Comments(post=post,user=uname,content=con)
			comm.save()
		
		return HttpResponseRedirect('/posts/'+postid )


def delete_comment(request,comid):
	comment = Comments.objects.get(id=comid)
	postid=comment.post_id
	if(request.user==comment.user or request.user.is_staff):
		comment.delete()
	return HttpResponseRedirect('/posts/'+str(postid))



def add_reply(request,comid):
	if request.method =="POST":
		comment = Comments.objects.get(id = comid)
		uname = request.user
		con=request.POST.get('message')
		mptrn= r"^[\S][\S ]+$"
		result = re.match(mptrn, con)
		if(result):
			words =ForrbiddenWord.objects.all()
			for word in words:
				rep=""
				size=len(word.word)
				for i in range(size):
					rep+="*"
				con = con.replace(word.word,rep)
			rep=Reply(user=uname,comment=comment,content=con)
			rep.save();
		return HttpResponseRedirect('/posts/'+str(comment.post_name_id))


def delete_reply(request,repid):
	reply =Reply.objects.get(id=repid)
	comment=Comments.objects.get(id=reply.comment_name_id)
	if(request.user==reply.user or request.user.is_staff):
		reply.delete()
	return HttpResponseRedirect('/posts/'+str(comment.post_name_id))


def add_tag(request):
	if request.method =="POST":
		con=request.POST.get('othertag')
		tagPtrn=r"^#[\S]+$"
		newTag=con.split(" ")
		flag = 1
		for ourTag in newTag :
			if(re.match(tagPtrn, ourTag)):
				allTags = Tags.objects.all()
				for eachTag in allTags:
					if(eachTag.tag_name == ourTag):
						flag = 0
					else:
						continue
				if flag == 1:
					ta = Tags(tag=ourTag)
					ta.save()
	return HttpResponseRedirect('/posts/newPost') 


def list_tags(request,tagid):
	tag=Tags.objects.get(id=tagid)
	posts=Post.objects.filter(tag=tag)
	cats = Category.objects.all()
	context={'posts':posts,'cats':cats}
	return render(request,'posts/index.html', context)
# Create your views here.
