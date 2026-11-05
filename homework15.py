def shutdown(arg):
    if arg == "yes":
        return "Shutting down"
    elif arg == "no":
        return "Shutdown aborted"
    else:
        return "Sorry"

print(shutdown("yes"))
print(shutdown("no"))
print(shutdown("maybe"))