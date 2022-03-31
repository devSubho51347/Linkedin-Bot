import bot.Linkedin_profile


with bot.Linkedin_profile.Linkedin_scraper(teardown=True) as robot:
    robot.sign_in()
    search_ele = input("Enter what you want to search:")
    robot.search(search_ele)
    robot.define_attributes()

    i = 0
    while i < 2:
        robot.search_results()
        i = i + 1
    robot.print_database()
    robot.create_dataframe()
