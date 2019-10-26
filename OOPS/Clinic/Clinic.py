import json


class ClinicManagement:


    def __init__(self):
        pass



    def doctorInformation(self):
        with open('doc.json', 'r+') as f:
            fl = f.read()
            jsonfl = json.loads(fl)
            f.close()
        return jsonfl



    def patientInformation(self):
        with open('patient.json', 'r+') as f:
            fl = f.read()
            jsonfl = json.loads(fl)
            f.close()
        return jsonfl



    def appointment(self):
        with open('appointments.json', 'r') as f:
            fl = f.read()
            jsonfl = json.loads(fl)
            f.close()
        return jsonfl

    def addDoct(self):
        docName = input(" Enter doctor Name: \n")
        dId = input(" Enter Doctor ID: \n")
        dSpcl = input(" Enter specialization: \n")
        dAvil = input(" Enter avilablity in (AM/PM/BOTH): \n")
        with open('doc.json', 'r')as f:
            fl = f.read()
            json_f = json.loads(fl)
        new_dir = {"name": docName, "id": dId, "specialization": dSpcl, "availability": dAvil}
        with open('doc.json', 'w')as f:
            json_f['doctors'].append(new_dir)
            f.write(json.dumps(json_f, indent=2))
            print(" Record Inserted Successfully ")



    def displayDoct(self):
        count = 0
        doct = self.doctorInformation()
        doctors = doct['doctors']
        print("Doctors Details \n Serial No \t\t Name \t\t\t\t\t Specialization ")
        for i in range(len(doctors)):
            name = doctors[i]['name']
            spcl = doctors[i]['specialization']
            count += 1
            print(' ', count, '\t\t', name, '\t\t', spcl)


    def addAppointment(self):
        
        doct = self.doctorInformation()
        doctors = doct['doctors']
        for i in range(len(doctors)):
            name = doctors[i]['name']
            spclzn = doctors[i]['specialization']
            available = doctors[i]['availability']
            print(name, '    ', spclzn, '    ', available, '    ')
        doctName = input("Enter the Doctor Name")
        time = input(" Availability (AM/PM/BOTH)")
        appointmentDict = self.appointment()  # read appointment json.
        appointmentList = appointmentDict[doctName]  # store all patients of 1 doctor in list.
        print("Appointment list is ", appointmentList)
        if len(appointmentList) <=5:
            for i in range(len(doctors)):
                if doctors[i]["name"] == doctName:
                    if time.upper() == doctors[i]["availability"]:
                        print("Doctor is Available..!! Please Enter the patient details:")
                        name = input(" Enter pName:")
                        id = int(input(" Enter patient Id:"))
                        age = int(input(" Enter patient age:"))
                        mob_no = input(" Enter patient's pMobNumber:")
                        with open('appointments.json', 'r')as f:
                            file = f.read()
                            json_f = json.loads(file)
                        new_dict = {"pName": name, "Id": id, "pAge": age, "pMobNumber": mob_no, "Time": time}
                        with open('appointments.json', 'a+') as f:
                            json_f[doctName].append(new_dict)
                            f.write(json.dumps(json_f, indent=2))
                        print("Your appointment is fixed. Thank You !")
                    else:
                        print("Sorry. Doctor is not available at the Moment !! ")



    def doctorSearchById(self):
        doct = self.doctorInformation()
        doctors = doct['doctors']
        id = int(input("Enter doctor Id :"))
        for i in range(len(doct)):
            if doctors[i]["Id"] == id:
                print("Congrats Doctor is available..!!")
                break
            else:
                print("Sorry Doctor is not available..!!")
                break



    def doctorSearchBySpclzn(self):
        doct = self.doctorInformation()
        doctors = doct['doctors']
        Spec = (input("Enter doctor name you want to search:"))
        for i in range(len(doct)):
            if Spec == doctors[i]["specialization"]:
                print("Congratulations Doctor is available..!!")
                break
            else:
                print("Sorry Doctor is not available..!!")
                break



    def doctorSearchByName(self):
        doct = self.doctorInformation()
        doctors = doct['doctors']
        name = (input("Enter the Doctor name that you want to Search:"))
        for i in range(len(doct)):
            if name == doctors[i]["name"]:
                print("Doctor is available..!!")
                break
            else:
                print("Doctor is not available..!!")
                break



    def Users(self):
        print("------------------- Hospital Management -------------------\n")
        yn = input("Do you Want to Continue? (Y/N)")
        while (yn == 'y') or (yn == 'Y') or (yn == 'Yes') or (yn == 'yes'):
            choice = int(input("Press \n 1. Doctor options \n 2. Patient options \n 3. Exit"))
            if choice == 1:
                ch = int(input("Press \n 1. Add doctor \n 2. View doctor \n 3. Go back\n"))
                if ch == 1:
                    self.addDoct()
                    break
                if ch == 2:
                    self.displayDoct()
                    break
                if ch == 3:
                    yn == 3
            if choice == 2:
                ch = int(input("Press \n 1. Add oppintment \n 2. search doctor \n 3. Go back"))
                if ch == 1:
                    self.addAppointment()
                    break
                if ch == 2:
                    op = int(input("Press \n 1. Seach by ID \n 2. Search by Specalization \n 3. Seach by Name\n"))
                    if op == 1:
                        self.doctorSearchById()
                        break
                    if op == 2:
                        self.doctorSearchBySpclzn()
                        break
                    if op == 3:
                        self.doctorSearchByName()
                        break
                if ch == 3:
                    (yn == 'n') or (yn == 'N') or (yn == 'No') or (yn == 'no')

            if choice == 3:
                exit()



# Driver Code

if __name__ == '__main__':

    ClMg = ClinicManagement()
    patient = ClMg.patientInformation()
    appointment = ClMg.appointment()
    ClMg.Users()
