



from django.http import JsonResponse
from interface.models import Notification

from datetime import datetime
from django.contrib import messages
from django.utils.html import format_html

def fetch_message(request):

    user = request.user
    print(user)
    notifications = Notification.objects.filter(user=user).order_by('-created_at')
    unread_count = notifications.filter(is_read=False)

   
    notification_data = []
    for notification in unread_count:
        notification_data.append({
            'message': notification.message,
            'is_read': notification.is_read
        })

        

    return JsonResponse({'unread_count': unread_count.count(), 'notifications': notification_data})







def read_message(request):
    print("I am Enter For Updating Read Status...")
    user = request.user
    Notification.objects.filter(user=user, is_read=False).update(is_read=True )
    return JsonResponse({'success': True})









def update_consolidation(request):

    user = request.user
    notifications = Notification.objects.filter(user=user , is_read =False).order_by('-created_at')

    unread_count = notifications.filter(is_read=False).count()

    notification_data = []
    for notification in notifications:
        notification_data.append({
            'message': notification,
            'is_read': notification.is_read
        })

        

    return JsonResponse({'unread_count': unread_count, 'notifications': notification_data})
     

def add_package_notification(user ,request):
    link = "<a href='http://127.0.0.1:8000/packages'>http://127.0.0.1:8000/packages</a>"
    message = (
        f"Your Package is Reached at Our Site. You can make a decision to visit {link}"
     )
    notification =Notification(user = user ,message =format_html(message), is_read = False ,created_at = datetime.now() )
    try:
       notification.save()
       messages.success(request , "Notification Added")
    except Exception as e:
       messages.error(request , "Notification Not Added")
       print("Exception At adding Package Notification :", e)   



     

