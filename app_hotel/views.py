from django.shortcuts import render,redirect
from .models import Room,Reservation,RoomCategory,SpecialRate
from django.utils import timezone
from django.contrib.auth import logout

# Create your views here.
def home(request):
    rooms = Room.objects.all()
    categories = RoomCategory.objects.all()
    return render(request,'home.html',{'rooms':rooms,
                                       "categories":categories,
                                       "category":'',
                                       "special_rate":"",
                                         "startDate":'',
                                         "endDate":'',
                                         "adult":'',
                                         "child":''})

def get_filtered_rooms(request):
    if request.method == 'POST':
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        category = request.POST.get('category_name')
        adult = request.POST.get('adult')
        child = request.POST.get('child')

        if startDate and endDate:
            try:
                start_date = timezone.make_aware(timezone.datetime.strptime(startDate, '%Y-%m-%d'))
                end_date = timezone.make_aware(timezone.datetime.strptime(endDate, '%Y-%m-%d'))

                reserved_rooms = Reservation.objects.filter(
                    start_date__lt=end_date,
                    end_date__gt=start_date
                ).values_list('room_id', flat=True)

                categories = RoomCategory.objects.all()
                available_rooms = Room.objects.exclude(id__in=reserved_rooms)
                
                special_rate = None
                
                if category:
                    available_rooms = available_rooms.filter(category__id=category)
                    category = int(category)
                
                special_rate = SpecialRate.objects.filter(
                    start_date__lt=end_date,
                    end_date__gt=start_date).first()
                
                if special_rate:
                    print(f'=== {special_rate.id} ====')

                return render(request, 'home.html', {'rooms': available_rooms,
                                        "categories":categories,
                                        "category":category,
                                        "special_rate":special_rate,
                                            "startDate":startDate,
                                            "endDate":endDate,
                                            "adult":adult,
                                            "child":child})

            except ValueError:
                return render(request, 'home.html', {'error': 'Invalid date format. Please use YYYY-MM-DD.'})

    return render(request, 'home.html', {'rooms': None,
                                       "categories":None,
                                       "category":None,
                                       "special_rate":None,
                                         "startDate":None,
                                         "endDate":None,
                                         "adult":None,
                                         "child":None})

def book_reservation(request):
    print('out')
    if request.method == "POST" :
        print('in')
        cust_name = request.POST.get('cust_name')
        cust_mail = request.POST.get('cust_mail')
        adult = request.POST.get('adult')
        child = request.POST.get('child')
        startDate = request.POST.get('startDate')
        endDate = request.POST.get('endDate')
        payment = request.POST.get('payment')
        room_id = request.POST.get('room_id')

        room = Room.objects.get(id=room_id)

        reservation = Reservation(
            room = room,
            start_date = startDate,
            end_date = endDate,
            customer_name=cust_name,
            total_price=payment
        )

        reservation.save()

        print(f'{cust_name}\n{cust_mail}\n{adult}\n{child}\n{startDate}\n{endDate}\n{payment}\n')
    return render(request, 'home.html', {'rooms': None,
                                       "categories":None,
                                       "category":None,
                                       "special_rate":None,
                                         "startDate":None,
                                         "endDate":None,
                                         "adult":None,
                                         "child":None})


def logout_admin(request):
    logout(request)
    return redirect('home')
