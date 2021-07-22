from django.http import *
from django.shortcuts import render
from .models import *
from datetime import datetime
from django.db import models
 
def index(request):
    return render(request, "index.html")
    
def rooms(request):
    if request.method == "POST":
        room = Room()
        room.price = request.POST.get("price")
        room.apart_num = request.POST.get("apart_num")
        room.free = 1
        room.save()

    rooms = Room.objects.all()
    return render(request, "rooms.html", {"rooms": rooms})

def editRoom(request, id):
    try:
        room = Room.objects.get(id=id)
 
        if request.method == "POST":
            room.price = request.POST.get("price")
            room.apart_num = request.POST.get("apart_num")
            room.save()
            return HttpResponseRedirect("/rooms")
        else:
            return render(request, "editRoom.html", {"room": room})
    except Room.DoesNotExist:
        return HttpResponseNotFound("<h2>Room not found</h2>")

def services(request):
    if request.method == "POST":
        service = Service()
        service.price = request.POST.get("price")
        service.type = request.POST.get("type")
        service.save()

    services = Service.objects.all()
    return render(request, "services.html", {"services": services})

def editService(request, id):
    try:
        service = Service.objects.get(id=id)
 
        if request.method == "POST":
            service.price = request.POST.get("price")
            service.type = request.POST.get("type")
            service.save()
            return HttpResponseRedirect("/services")
        else:
            return render(request, "editService.html", {"service": service})
    except Service.DoesNotExist:
        return HttpResponseNotFound("<h2>Service not found</h2>")
 
def clients(request):

    if request.method == "POST":
        client = Client()
        client.name = request.POST.get("name")
        client.save()
    
    clients = Client.objects.all()
    return render(request, "clients.html", {"clients": clients})

def editClient(request, id):
    try:
        client = Client.objects.get(id=id)
 
        if request.method == "POST":
            client.name = request.POST.get("name")
            client.save()
            return HttpResponseRedirect("/clients")
        else:
            return render(request, "editClient.html", {"client": client})
    except Client.DoesNotExist:
        return HttpResponseNotFound("<h2>Client not found</h2>")

def clientService(request):

    serviceList = Service.objects.values_list("type", flat=True).distinct()
    clientList = Client.objects.values_list("id","name").distinct()

    if request.method == "POST":
        clientService = ClientService()
        clientService.client = Client.objects.get(id=request.POST.get("client.id"))
        clientService.service = Service.objects.get(type=request.POST.get("service"))
        clientService.date=request.POST.get("date")
        clientService.save()

    clientsServices = ClientService.objects.all()
    return render(request, "clientService.html", {"clientsServices": clientsServices
                                        ,"serviceList": serviceList ,"clientList": clientList})

def editClientService(request, id):
    serviceList = Service.objects.values_list("type", flat=True).distinct()
    clientList = Client.objects.values_list("id","name").distinct()
    try:
        clientService = ClientService.objects.get(id=id)
        
        if request.method == "POST":
            clientService.client = Client.objects.get(id=request.POST.get("client.id"))
            clientService.service = Service.objects.get(type=request.POST.get("service"))
            clientService.date=request.POST.get("date")
            clientService.save()
            return HttpResponseRedirect("/serviceOrder")
        else:
            return render(request, "editClientService.html", {"record": clientService
                                        ,"serviceList": serviceList ,"clientList": clientList})
    except ClientService.DoesNotExist:
        return HttpResponseNotFound("<h2>Record not found</h2>")

# def clientRoom(request):
#     roomList = Room.objects.values_list("id", flat=True).distinct()
#     clientList = Client.objects.values_list("id","name").distinct()

#     if request.method == "POST":
#         clientRoom = ClientRoom()
#         clientRoom.client =  Client.objects.get(id=request.POST.get("client.id"))
#         clientRoom.room = Room.objects.get(id=request.POST.get("room"))
#         clientRoom.date_in=request.POST.get("date_in")
#         clientRoom.date_out=request.POST.get("date_out")
#         clientRoom.save()

#     clientsRooms = ClientRoom.objects.all()
#     return render(request, "clientRoom.html", {"clientsRooms": clientsRooms
#                                         ,"roomList": roomList ,"clientList": clientList})

# def editClientRoom(request, id):
#     roomList = Room.objects.values_list("id", flat=True).distinct()
#     clientList = Client.objects.values_list("id","name").distinct()
#     try:
#         clientRoom = ClientRoom.objects.get(id=id)
 
#         if request.method == "POST":
#             clientRoom.client =  Client.objects.get(id=request.POST.get("client.id"))
#             clientRoom.room = Room.objects.get(id=request.POST.get("room"))
#             clientRoom.date_in=request.POST.get("date_in")
#             clientRoom.date_out=request.POST.get("date_out")
#             clientRoom.save()
#             return HttpResponseRedirect("/roomOrder")
#         else:
#             return render(request, "editClientRoom.html", {"record": clientRoom
#                                         ,"roomList": roomList ,"clientList": clientList})
#     except ClientRoom.DoesNotExist:
#         return HttpResponseNotFound("<h2>Record not found</h2>")

def clientRoom(request):
    roomList = Room.objects.raw(
            "select room.id "
            +"from room") 
    clientList = Client.objects.values_list("id","name").distinct()
    clientsRooms = ClientRoom.objects.all()

    if request.method == "POST":
        if (request.POST.get("date_1")):

            roomList=Room.objects.raw(
            "select room.id "
            +"from room join client_room on room.id=client_room.room_id "
            +"where client_room.date_in>'"+request.POST.get("date_2")+"' OR client_room.date_out<'"
            +request.POST.get("date_1")+"'"
            +" UNION "
            +" select room.id "
            +" from room "
            +" where room.id NOT IN(select client_room.room_id from client_room) "
            )
        
            return render(request, "clientRoom.html", {"clientsRooms": clientsRooms
                                        ,"roomList": roomList ,"clientList": clientList
                                        ,"date1":request.POST.get("date_1")
                                        ,"date2":request.POST.get("date_2")})
    if request.method == "POST":
        if (request.POST.get("date_1")==None):
            clientRoom = ClientRoom()
            clientRoom.client =  Client.objects.get(id=request.POST.get("client.id"))
            clientRoom.room = Room.objects.get(id=request.POST.get("room"))
            clientRoom.date_in=request.POST.get("date_in")
            clientRoom.date_out=request.POST.get("date_out")
            clientRoom.save()
        
    return render(request, "clientRoom.html", {"clientsRooms": clientsRooms
                                        ,"roomList": roomList ,"clientList": clientList})                        

def editClientRoom(request, id):
    roomList = Room.objects.raw(
            "select room.id "
            +"from room") 
    clientList = Client.objects.values_list("id","name").distinct()
    try:
        clientRoom = ClientRoom.objects.get(id=id)

        if request.method == "POST":
            if (request.POST.get("date_1")):

                roomList=Room.objects.raw(
                "select room.id "
                +"from room join client_room on room.id=client_room.room_id "
                +"where client_room.date_in>'"+request.POST.get("date_2")+"' OR client_room.date_out<'"
                +request.POST.get("date_1")+"'"
                +" UNION "
                +" select room.id "
                +" from room "
                +" where room.id NOT IN(select client_room.room_id from client_room) "
                )
            
                return render(request, "editClientRoom.html", {"record": clientRoom
                                            ,"roomList": roomList ,"clientList": clientList
                                            ,"date1":request.POST.get("date_1")
                                            ,"date2":request.POST.get("date_2")})

        if request.method == "POST":
            if (request.POST.get("date_1")==None):
                clientRoom.client =  Client.objects.get(id=request.POST.get("client.id"))
                clientRoom.room = Room.objects.get(id=request.POST.get("room"))
                clientRoom.date_in=request.POST.get("date_in")
                clientRoom.date_out=request.POST.get("date_out")
                clientRoom.save()
                return HttpResponseRedirect("/roomOrder")
        else:
            return render(request, "editClientRoom.html", {"record": clientRoom
                                        ,"roomList": roomList ,"clientList": clientList})
    except ClientRoom.DoesNotExist:
        return HttpResponseNotFound("<h2>Record not found</h2>")

def deleteClient(request, id):
    try:
        client = Client.objects.get(id=id)
        client.delete()
        return HttpResponseRedirect("/clients")
    except Client.DoesNotExist:
        return HttpResponseNotFound("<h2>Client not found</h2>")

def deleteRoom(request, id):
    try:
        room = Room.objects.get(id=id)
        room.delete()
        return HttpResponseRedirect("/rooms")
    except Room.DoesNotExist:
        return HttpResponseNotFound("<h2>Room not found</h2>")

def deleteService(request, id):
    try:
        service = Service.objects.get(id=id)
        service.delete()
        return HttpResponseRedirect("/services")
    except Service.DoesNotExist:
        return HttpResponseNotFound("<h2>Service not found</h2>")

def deleteClientRoom(request, id):
    try:
        clientRoom = ClientRoom.objects.get(id=id)
        clientRoom.delete()
        return HttpResponseRedirect("/roomOrder")
    except clientRoom.DoesNotExist:
        return HttpResponseNotFound("<h2>Record not found</h2>")

def deleteClientService(request, id):
    try:
        clientService = ClientService.objects.get(id=id)
        clientService.delete()
        return HttpResponseRedirect("/serviceOrder")
    except clientService.DoesNotExist:
        return HttpResponseNotFound("<h2>Record not found</h2>")

def report(request):
    if request.method == "POST":
            rooms=ClientRoom.objects.raw("select client_room.id as id,'room' as type, room.price as price"
                +" from client_room join room on client_room.room_id=room.id"
                +" where client_room.date_in>'"+request.POST.get("fstdate")
                +"' AND client_room.date_out<'"+request.POST.get("scddate")+"'")
                
            services=ClientService.objects.raw("select client_service.id as id,'service' as type, service.price as price"
                +" from client_service join service on client_service.service_id=service.id"
                +" where client_service.date>'"+request.POST.get("fstdate")
                +"' AND client_service.date<'"+request.POST.get("scddate")+"'")

            resultPrice=0
            for room in rooms:
                resultPrice+=room.price
            for service in services:
                resultPrice+=service.price

            return render(request, "report.html", {"rooms": rooms, "services": services
            ,"result": resultPrice})

    return render(request, "report.html")