from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection

# Create your views here.
def index(request):
    # Control database here
    #---------------------------------------------------------------
    # Cau lenh them thong tin vao bang users
    # INSERT INTO table_name
    # VALUES (value1, value2, value3, ...);
    '''
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO users \
        VALUES (12, 'nga','1234', 'tran_viet_nga', '0867012045', 'haibatrung')")
    '''
    #---------------------------------------------------------------
    # Cau lenh kiem tra thong tin tai khoan
    # SELECT * FROM table_name;

    with connection.cursor() as cursor: # Khoi tao ket noi database
        cursor.execute("SELECT * FROM users")
        # Tao ra 1 tupple chua danh sach thong tin truy van
        result = cursor.fetchall()
        print(result)
    # Tao tu dien keyword va value phuc vu cho HMTL
    context = {
        'data_user': result[0]}

    return render(request, 'home.html', context)

