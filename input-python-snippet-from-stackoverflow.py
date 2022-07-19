def my_function():
    with open("test.txt", "w+") as f:
        os.chdir("//10.2.30.61/c$\Qlikview_Tropal/apps/ventes")
        for fichiers in glob.glob("*"):
            today = datetime.datetime.today()
            modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(fichiers))
            duration = today - modified_date
            if duration.days < 1:
                f.write(f"{fichiers} = {duration} \n")

my_function()
