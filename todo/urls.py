from django.urls import path 
from . import views
urlpatterns = [
    # Add Task
    path('addTask/' , views.addTask , name = "addTask"),
    # mark_as_done
    path('mark_as_done/<int:pk>/' , views.mark_as_done  , name='mark_as_done'),

    # mark_as_undone
    path('mark_as_undone/<int:pk>/' , views.mark_as_undone  , name='mark_as_undone'),

    #Edit Task
    path('EditTask/<int:pk>/' , views.EditTask  , name='EditTask'),

    ## Delete Task
    path('Delete_Task/<int:pk>' , views.Delete_Task , name= "Delete_Task")


]