# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.
from random import randint
class Train:
    @staticmethod
    def greet():
        print("good morning")
    def __init__(self,trainNo,frm,to,fare):
        self.trainNo=trainNo
        self.frm=frm
        self.to=to
        self.fare=fare
    
    def ticket_booking(self):
        print("your ticket has been booked from ",{self.frm} ,"to", {self.to})
    def status(self):
        print("trian with train number", {self.trainNo} ,"is running on time")
        print("available seats are",{randint(1,583)})
    def fares(self):
        print("your fare from ",{self.frm}, "to", {self.to},"is" ,{randint(293,3773)})
    @staticmethod
    def conc():
        print(" thanks\n have a safe journey")

TrainInfo=Train(86349,"delhi","mumbai",222)
TrainInfo.greet()
TrainInfo.ticket_booking()
TrainInfo.status()
TrainInfo.fares()
TrainInfo.conc()

