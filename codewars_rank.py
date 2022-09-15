# https://www.codewars.com/kata/51fda2d95d6efda45e00004e/


# TODO: create the User class
# it must support rank, progress, and the inc_progress(rank) method


class User:

    def __init__(self):
        self.rank = -8
        self.progress = 0

    def inc_progress(self, activity):

        correct_rank = list(i for i in range(-8, 9) if i != 0)      # Creates a list with correct ranks from -8 to 8 without 0.
        
        if activity not in correct_rank:                            # Checks correction of the input
            raise ValueError

        if correct_rank.index(activity) > correct_rank.index(self.rank):        # Checks a difference and calculates progress points
            d = correct_rank.index(activity) - correct_rank.index(self.rank)
            self.progress += 10 * d * d
        elif correct_rank.index(activity) == correct_rank.index(self.rank):
            self.progress += 3
        elif correct_rank.index(activity) == correct_rank.index(self.rank) - 1:
            self.progress += 1
        else:
            return
            
        while self.progress >= 100 and self.rank < 8:               # Increases a rank for every 100 progress points
            self.progress -= 100
            self.rank += 1
            if self.rank == 0:                                      # Avoids incorrect rank
                self.rank += 1
            continue
        
        if self.rank == 8:                                          # Keeps progress at 0 when a rank is 8
            self.progress = 0
