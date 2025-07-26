def parse_intent(command):
    #it open browser
    if "open browser" in command:
        return "open browser"
    
    #it shutdown the system
    elif "shutdown" in command:
        return "shutdown"
    
    #it open instagram
    elif "Instagram" in command:
        return "Instagram"
    
    #it open code
    elif "open code" in command:
        return "open code"
    
    #it open reddit
    elif "reddit" in command:
        return "reddit"
    
    else:
        return "unknown"