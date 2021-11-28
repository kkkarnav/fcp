def pass_note(person):

    if person == 1:
        print("note received!")
        return

    else:
        # passing the note on to the next person
        pass_note(person - 1)


pass_note(13)
