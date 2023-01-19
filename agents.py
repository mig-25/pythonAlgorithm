import random

comp = {}
dep = {}
agents = {}
agent = {}

#kwargs example, kwargs allows a function to take unkonwn number of kewword arguments
def compInfo(**kwargs): #kwargs argument is a dictionary
    for key, value in kwargs.items():
        print(key, value)
        
    company_name = input("Ange företagets namn: ")    
    comp["företag"] = company_name
    depInfo()
    
def depInfo(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
   
    depId = input("Ange avdID: ")
    depName = input("Ange avdNamn: ")

    dep["avdID"] = depId #assign input variable value to dictionary key
    dep["avdNamn"] = depName
    
    comp[depId] = dep #add department to company dictionary
    personInfo()

def personInfo(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
    
    active = True
    while active:    
        fName = input("Ange agents förnamn: ")
        lName = input("Ange agents efternamn: ")
        name = f"{fName} {lName}"
        agentsKilled = int(input(f"Antal agenter som {name} har skjutit ner: "))
        
        emp = random.randint(1, 100)
        empId = str(emp)
        #single agent attributes
        agent = {
            "namn": name,
            "dödadeFiender": agentsKilled,
            "id": empId
        }
        
        agents[empId] = agent
        dep['agents'] = agents #add agents to department dictionary
        
        repeat = input("Vill du lägga till fler kurser? (j/n) ").lower()
        # if user does not want to add another agent, set active flag to False to exit loop
        if repeat == 'n':
            active = False
   
def printKillStatus():
    with open("agentStatus.txt", "w") as f:
        if any(agent['dödadeFiender'] > 5 for agent in agents.values()):
            rank = "There is a 007 among the agents"
        else:
            rank = "Only normal agents"
        
        f.write("\nSäkerhetstjänsten: %s \n\n" % (comp["företag"]))
        f.write("Utfärdat: %s\n" % rank) # visa rätt status som rubrik
        f.write("Avddelnings ID: %s,\tAvdelningsnamn: %s\n\n" % (dep['avdID'], dep['avdNamn']))
        f.write("-----------------Antal lividerade agenter: %s-----------------\n\n" % sum(agent['dödadeFiender'] for agent in agents.values()))
            
        for agent in agents.values():
            f.write("Agents namn: %s,\nAntal dödade fiender: %s,\nAgentens anställningsnr: %s\n\n" % (agent['namn'], agent['dödadeFiender'], agent['id']))
   
    f = open("agentStatus.txt", "r")
    print(f.read())
    


def main():
    compInfo()
    printKillStatus()
    
    """ for key, value in dep.items():
        print(f"{key} = {value}")
    
    for c_id, c_info in agents.items():
        print("\nAnställnings nr:", c_id)
        
        for key in c_info:
            print(key + ':', c_info[key]) """

if __name__ == "__main__":
    main()