from scrapper import Scrapper

tournament_name = input("Enter Tournament Name:\n")
tournament_link = input("Enter URL of Results page of tournament (e.g. the Prelim Seeds page):\n")

tournament = Scrapper()
tournament.analyze_tournament(tournament_name, tournament_link)

print("Results generated in the \"Results\" subfolder of the program.")
