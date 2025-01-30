from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, ObrazacZaDodavanjeZapisa
from .models import Record

def home(request):
    records = Record.objects.all()

    # Proveri da li je korisnik ulogovan
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Autentifikacija
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Uspesno ste se ulogovali!")
            return redirect('home')
        else:
            messages.success(request, "Desila se greska, molim Vas pokusajte ponovo...")
            return redirect('home')
    
    else:
        return render(request, 'home.html', {'records':records})

def logout_user(request):
    logout(request)
    messages.success(request, "Uspesno ste se izlogovali!")
    return redirect('home')

def register_user(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Autentifikacija i logovanje
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Uspesno ste se registrovali! Dobrodosli!")
            return redirect('home')
    else:
        form = SignUpForm()
        return render(request, 'register.html', {'form':form})
    
    return render(request, 'register.html', {'form':form})

def zapis_korisnika(request, pk):
    if request.user.is_authenticated:
        # Pretraga zapisa
        zapis_korisnika = Record.objects.get(id=pk)
        return render(request, 'record.html', {'zapis_korisnika':zapis_korisnika})
    else:
        messages.success(request, "Morate biti ulogovani da biste mogli videti tu stranicu...")
        return redirect('home')
    
def brisanje_zapisa(request, pk):
    if request.user.is_authenticated:
        if request.user.username == "admin":  # Provera da li je korisnik "admin"
            try:
                obrisi_zapis = Record.objects.get(id=pk)
                obrisi_zapis.delete()
                messages.success(request, "Zapis je uspesno obrisan!")
            except Record.DoesNotExist:
                messages.error(request, "Zapis nije pronađen.")
        else:
            messages.error(request, "Samo administrator moze brisati zapise...")
        
        return redirect('home')
    else:
        messages.error(request, "Morate biti ulogovani da biste mogli to da uradite...")
        return redirect('home')
    
def dodavanje_zapisa(request):
    form = ObrazacZaDodavanjeZapisa(request.POST or None)
    
    if request.user.is_authenticated:
        if request.user.username == "admin":  # Check if the logged-in user is "admin"
            if request.method == "POST":
                if form.is_valid():
                    dodavanje_zapisa = form.save()
                    messages.success(request, "Zapis je dodat!")
                    return redirect('home')
        else:
            messages.error(request, "Samo administrator može dodavati zapise...")
            return redirect('home')
    
    else:
        messages.success(request, "Morate biti ulogovani...")
        return redirect('home')

    return render(request, 'add_record.html', {'form': form})
    
def izmena_zapisa(request, pk):
    if request.user.is_authenticated:
        if request.user.username == "admin":  # Provera da li je korisnik "admin"
            try:
                trenutni_zapis = Record.objects.get(id=pk)
            except Record.DoesNotExist:
                messages.error(request, "Zapis nije pronađen.")
                return redirect('home')

            form = ObrazacZaDodavanjeZapisa(request.POST or None, instance=trenutni_zapis)
            if form.is_valid():
                form.save()
                messages.success(request, "Zapis je uspesno izmenjen!")
                return redirect('home')
            return render(request, 'update_record.html', {'form': form})
        else:
            messages.error(request, "Samo administrator moze izmeniti zapise...")
            return redirect('home')
    else:
        messages.error(request, "Morate biti ulogovani...")
        return redirect('home')