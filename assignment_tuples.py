#1 Tuple Mastery in Python
#task 1
'''
[("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

"Itinerary 1: Alice - From New York to London
 Itinerary 2: Bob - From Tokyo to San Francisco"
 '''

def re_format(customer_info):
    output = ""
    i = 0
    for traveler_name, origin, destination in customer_info:
        i += 1
        output += f"\nItinerary {i}: {traveler_name} - From {origin} to {destination}"
    return output

print(re_format([("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]))

#2 Python Data Structure Challenges in Real-World Scenarios
#task 1

library = [("1984", "George Orwell"), ("Brave New World", "Aldous Huxley")]


def add_book(book, author):

    book_tuple = (book, author,)
    library.append(book_tuple)
    library1 = set(library)
    library2 = list(library1)
    return library2
    
print(add_book("1984", "George Orwell"))

#3. Python Loops and Tuples in Analytical Applications
#task 1

stock_data = [
    ("AAPL", "2021-01-01", 130.0),
    ("AAPL", "2021-01-02", 132.0),
    ("MSFT", "2021-01-01", 220.0)
]

def avg_price(stock_symbol):
    avg = 0
    quantity = 0
    for symbol, date, price in stock_data:
        if symbol == stock_symbol:
            avg += price
            quantity += 1
    if quantity != 0:
        avg = avg / quantity
    return avg

print(avg_price("AAPL"))

#task 2
attendees = [
    ("Alice", "Python Conference"),
    ("Bob", "Python Conference"),
    ("Charlie", "AI Summit")
]

def list_attendees(event):
    attendees = []
    for person, p_event in attendees:
        if p_event == event:
            attendees.append(person)
    print(attendees)

def count_attendees():
    event_attendees = {}
    for person, p_event in attendees:
        event_attendees.update({p_event:0})
    for person, p_event in attendees:
        event_attendees[p_event] += 1
    return event_attendees

print(count_attendees())





        





