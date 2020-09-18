from django.shortcuts import render,redirect

# Create your views here.
def terminal_login(request):
    try:
        if request.method == 'POST':
            that_id = request.POST['that_id']
            that_pass = request.POST['that_pass']
            return redirect('core:terminal_access',that_id=that_id,that_pass=that_pass)
    except:
        if request.method == 'POST':
                that_id = request.POST['that_id']
                return redirect('core:terminal_verify',that_id=that_id)
    
    return render(request, 'core/login.html')

def terminal_verify(request, that_id):
    try:
        if request.method == 'POST':
            that_pass = request.POST['that_pass']
            return redirect('core:terminal_access', that_id=that_id, that_pass=that_pass)
    except:
        pass
    return render(request, 'core/loginV2.html', {
                    'that_id': that_id
                    })

def terminal_access(request, that_id, that_pass):
    park = '0'
    print('1')
    if (that_id == "SuperUser" and that_pass == "MechaBot"):
        park = '1'
    print("2")   
    return render(request, 'core/Success.html', {
        'that_pass': that_pass,
        'that_id': that_id,
        'park' : park
        })