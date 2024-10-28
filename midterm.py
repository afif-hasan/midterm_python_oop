class Star_cinema:
    hall_list=[]

    def entry_hall(self,hall):
        self.hall_list.append(hall)
    
    @classmethod
    def hall_show_list(self,hall_name):
        for hall in self.hall_list:
            if hall._Hall__name==hall_name:
                hall.view_show_list()
                return
        print("Invalid Hall name")


class Hall(Star_cinema):

    def __init__(self,name,rows,cols,hall_no):
        self.__name=name
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=hall_no
        self.__show_list=[]
        self.__seats={}
        super().entry_hall(self)
    
    def __repr__(self):
        return f"{self.__hall_no}--> {self.__name}"
    
    def entry_show(self,show_id,movie_name,Time):
        show_info=(show_id,movie_name,Time)
        self.__show_list.append(show_info)
        seat_matrix=[]
        for row in range(self.__rows):
            rows=[]
            for col in range(self.__cols):
                rows.append(0) 
            seat_matrix.append(rows)
        self.__seats[show_id]=seat_matrix

                
    def book_ticket(self,show_id,seat_tuple):
        if show_id not in self.__seats:
            print(f"Show unavailable")
            return
        seat_matrix=self.__seats[show_id]
        for row,col in seat_tuple:
            if row>0 and row<=self.__rows and col>0 and col<=self.__cols:
                if seat_matrix[row-1][col-1]==0:
                    seat_matrix[row-1][col-1]='-'
                    print(f"Seat at row: {row} and col: {col} successfully booked ")
                else:
                    print(f"seat is already booked")
            else:
                print(f"Invalid seat range ({row},{col})")
    
    def view_show_list(self):
        print("\n----Shows running----\n")
        if len(self.__show_list)==0:
            print("No show available")
        else:
            for shows_info in self.__show_list:
                print(f"show id: {shows_info[0]} Movie name:----{shows_info[1]}----\n Time: {shows_info[2]}")
        
    
    def view_available_seats(self,show_id):
        if show_id not in self.__seats:
            print("Invalid Show id")
        else:
            for shows in self.__show_list:
                if shows[0]==show_id:
                    print(f"\n----{shows[1]}----")
                    break
            seat_matrix=self.__seats[show_id]
            print("----Available Seats----\n")
            for row in range(self.__rows):
                for col in range(self.__cols):
                    if seat_matrix[row][col]==0:
                        print(f"     Seat({row+1},{col+1})")
            print("\n----layout view----\n")
            for row in seat_matrix:
                print('    ',*row)
                    
                 
            
vip=Hall("vip",5,5,"1")
premium=Hall("premium",6,6,"2")
vip.entry_show("101",'Jawan',"25/11/2024")
vip.entry_show("102","Dunki","27/11/2024")
vip.entry_show("103","Lapataa Ladies","28/11/2024")

counter_open=True
while counter_open:
    print("\n-----Ticket Counter-----")
    print("\nAvailable option -->")
    print("1. View Halls")
    print("2. View running shows in Halls")
    print("3. View available seats")
    print("4. Book Ticket")
    print("5. Exit")

    option=int(input("Choose option: "))
    if option==2:
        hall=str(input("Enter Hall name: "))
        Star_cinema.hall_show_list(hall)
    elif option==1:
        print("\n-----Halls-----\n")
        print(" ",*Star_cinema.hall_list)
    elif option==3:
        show_id=input("Enter show id: ")
        vip.view_available_seats(show_id)
    elif option==4:
        show_id=input("Enter show id: ")
        no_of_tickets=int(input("Enter Ticket Quantity: "))
        seat_list=[]
        for i in range(no_of_tickets):
            row=int(input(f"Enter row of seat {i+1} : "))
            col=int(input(f"Enter coloumn of seat {i+1}: "))
            seat_list.append((row,col))
        currentHall=None
        for Halls in Star_cinema.hall_list:
            for shows in Halls._Hall__show_list:
                if shows[0]==show_id:
                    currentHall=Halls
                    break
        currentHall.book_ticket(show_id,seat_list)
    elif option==5:
        break




        