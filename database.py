import os

def create_database_files():
    files_to_create = [
        "student_info.txt", 
        "room_info_boys.txt", 
        "room_info_girls.txt", 
        "room_info_others.txt", 
        "inouttime.txt", 
        "visitor_info.txt", 
        "leave_applications.txt"
    ]
    
    for f in files_to_create:
        if not os.path.exists(f):
            open(f, 'w').close()
            print(f"[+] Created new file: {f}")