import subprocess

def main():
    
    show_profiles = subprocess.run(["netsh", "wlan", "show", "profiles"], capture_output=True, text=True).stdout.split("\n")

    profiles = [i.split(":")[1][1:] for i in 
    show_profiles if "All User Profile" in i]

    for profile in profiles:
        try:
            show_passwords = subprocess.run(["netsh", "wlan", "show", "profile", profile, "key=clear"], capture_output=True, text=True, check=True).stdout.split("\n")
            passwords = [j.split(":")[1][1:] for j in show_passwords if "Key Content" in j]

            try:
                print("{:30} | {}".format(profile, passwords[0]))   

            except IndexError:
                print("{:30} | {}".format(profile, "NONE"))   
        except subprocess.CalledProcessError:
                print("{:30} | {}".format(profile, "ENDCODING ERROR"))   


    print("")
    exit()



if __name__ == "__main__":
    main()
